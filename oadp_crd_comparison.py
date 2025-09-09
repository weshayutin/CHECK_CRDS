#!/usr/bin/env python3
"""
OADP CRD Version Comparison Tool

This tool compares OADP Custom Resource Definition files across versions 1.3, 1.4, and 1.5
and identifies parameter additions (green check) and removals (red X) between versions.
"""

import os
import sys
import yaml
import json
import argparse
from typing import Dict, List, Set, Tuple, Any
from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict

# ANSI color codes for output formatting
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

@dataclass
class ParameterChange:
    path: str
    line_number: int
    change_type: str  # 'added' or 'removed'
    version_from: str
    version_to: str
    parameter_name: str
    full_path: str

class CRDComparator:
    def __init__(self, base_dir: str = ".", show_additions: bool = False):
        self.base_dir = Path(base_dir)
        self.versions = ["1.3", "1.4", "1.5"]
        self.show_additions = show_additions
        self.common_files = self._find_common_files()
        
    def _find_common_files(self) -> List[str]:
        """Find files that exist in all three version directories."""
        version_files = {}
        for version in self.versions:
            version_dir = self.base_dir / version
            if version_dir.exists():
                version_files[version] = set(f.name for f in version_dir.iterdir() if f.is_file())
        
        if len(version_files) < 3:
            raise ValueError("Not all version directories (1.3, 1.4, 1.5) found")
        
        # Find intersection of all sets
        common = version_files[self.versions[0]]
        for version in self.versions[1:]:
            common = common.intersection(version_files[version])
        
        return sorted(list(common))
    
    def _load_yaml_with_line_numbers(self, file_path: Path) -> Tuple[Dict, Dict[str, int]]:
        """Load YAML file and create a mapping of parameter paths to line numbers."""
        with open(file_path, 'r') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Parse YAML
        try:
            data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML {file_path}: {e}")
            return {}, {}
        
        # Create line number mapping
        line_map = {}
        current_path = []
        
        for i, line in enumerate(lines, 1):
            line_stripped = line.strip()
            if not line_stripped or line_stripped.startswith('#'):
                continue
                
            # Calculate indentation level
            indent_level = (len(line) - len(line.lstrip())) // 2
            
            # Adjust current path based on indentation
            if indent_level < len(current_path):
                current_path = current_path[:indent_level]
            
            # Extract key from line
            if ':' in line_stripped:
                key = line_stripped.split(':')[0].strip().strip('"\'')
                if key and not key.startswith('-'):
                    # Add to current path
                    if indent_level == len(current_path):
                        current_path.append(key)
                    elif indent_level < len(current_path):
                        current_path = current_path[:indent_level] + [key]
                    else:
                        current_path.append(key)
                    
                    # Store line number for this path
                    path_str = '.'.join(current_path)
                    line_map[path_str] = i
        
        return data, line_map
    
    def _extract_parameters(self, data: Dict, prefix: str = "", line_map: Dict[str, int] = None) -> Dict[str, int]:
        """Recursively extract all parameters and their line numbers from CRD data."""
        params = {}
        if line_map is None:
            line_map = {}
            
        if not isinstance(data, dict):
            return params
            
        for key, value in data.items():
            current_path = f"{prefix}.{key}" if prefix else key
            
            # Store this parameter
            if current_path in line_map:
                params[current_path] = line_map[current_path]
            else:
                params[current_path] = 0  # Fallback if line number not found
            
            # Recursively process nested dictionaries
            if isinstance(value, dict):
                nested_params = self._extract_parameters(value, current_path, line_map)
                params.update(nested_params)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        list_path = f"{current_path}[{i}]"
                        nested_params = self._extract_parameters(item, list_path, line_map)
                        params.update(nested_params)
        
        return params
    
    def compare_versions(self, filename: str) -> List[ParameterChange]:
        """Compare a specific file across all versions and return changes."""
        changes = []
        file_data = {}
        file_params = {}
        
        # Load data for all versions
        for version in self.versions:
            file_path = self.base_dir / version / filename
            if file_path.exists():
                data, line_map = self._load_yaml_with_line_numbers(file_path)
                file_data[version] = data
                file_params[version] = self._extract_parameters(data, "", line_map)
        
        # Compare versions pairwise (1.3->1.4, 1.4->1.5, 1.3->1.5)
        version_pairs = [("1.3", "1.4"), ("1.4", "1.5"), ("1.3", "1.5")]
        
        for old_version, new_version in version_pairs:
            if old_version not in file_params or new_version not in file_params:
                continue
                
            old_params = set(file_params[old_version].keys())
            new_params = set(file_params[new_version].keys())
            
            # Find added parameters (in new version but not in old)
            added = new_params - old_params
            for param in added:
                changes.append(ParameterChange(
                    path=filename,
                    line_number=file_params[new_version][param],
                    change_type="added",
                    version_from=old_version,
                    version_to=new_version,
                    parameter_name=param.split('.')[-1],
                    full_path=param
                ))
            
            # Find removed parameters (in old version but not in new)
            removed = old_params - new_params
            for param in removed:
                changes.append(ParameterChange(
                    path=filename,
                    line_number=file_params[old_version][param],
                    change_type="removed",
                    version_from=old_version,
                    version_to=new_version,
                    parameter_name=param.split('.')[-1],
                    full_path=param
                ))
        
        return changes
    
    def generate_report(self) -> None:
        """Generate a comprehensive comparison report."""
        print(f"{Colors.BOLD}{Colors.CYAN}OADP CRD Version Comparison Report{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"Comparing versions: {', '.join(self.versions)}")
        print(f"Common files found: {len(self.common_files)}")
        if not self.show_additions:
            print(f"{Colors.YELLOW}Note: Hiding additions by default. Use --show-additions to see added parameters.{Colors.END}")
        print()
        
        total_changes = 0
        files_with_changes = 0
        
        for filename in self.common_files:
            changes = self.compare_versions(filename)
            
            # Filter changes based on show_additions flag
            if not self.show_additions:
                changes = [c for c in changes if c.change_type == "removed"]
            
            if changes:
                files_with_changes += 1
                total_changes += len(changes)
                
                print(f"{Colors.BOLD}{Colors.YELLOW}📄 File: {filename}{Colors.END}")
                print(f"{Colors.YELLOW}{'-'*50}{Colors.END}")
                
                # Group changes by type and version pair
                grouped_changes = defaultdict(list)
                for change in changes:
                    key = f"{change.version_from}→{change.version_to}"
                    grouped_changes[key].append(change)
                
                for version_pair, version_changes in grouped_changes.items():
                    print(f"{Colors.BOLD}  {version_pair}:{Colors.END}")
                    
                    # Sort by change type (removed first, then added)
                    version_changes.sort(key=lambda x: (x.change_type == "added", x.full_path))
                    
                    for change in version_changes:
                        if change.change_type == "removed":
                            icon = f"{Colors.RED}❌{Colors.END}"
                            color = Colors.RED
                            action = "REMOVED"
                        else:
                            icon = f"{Colors.GREEN}✅{Colors.END}"
                            color = Colors.GREEN
                            action = "ADDED"
                        
                        print(f"    {icon} {color}{action}{Colors.END}: {change.full_path}")
                        if change.line_number > 0:
                            print(f"      {Colors.BLUE}Line {change.line_number}{Colors.END} in version {change.version_to if change.change_type == 'added' else change.version_from}")
                    print()
                
                print()
        
        # Summary
        print(f"{Colors.BOLD}{Colors.MAGENTA}📊 Summary{Colors.END}")
        print(f"{Colors.MAGENTA}{'='*60}{Colors.END}")
        print(f"Files analyzed: {len(self.common_files)}")
        print(f"Files with changes: {files_with_changes}")
        
        # Calculate actual counts from all changes (not filtered)
        all_changes = []
        file_stats = {}
        
        for filename in self.common_files:
            file_changes = self.compare_versions(filename)
            all_changes.extend(file_changes)
            
            # Count additions and removals per file
            file_added = sum(1 for c in file_changes if c.change_type == "added")
            file_removed = sum(1 for c in file_changes if c.change_type == "removed")
            file_stats[filename] = {
                'added': file_added,
                'removed': file_removed,
                'total': file_added + file_removed
            }
        
        added_count = sum(1 for c in all_changes if c.change_type == "added")
        removed_count = sum(1 for c in all_changes if c.change_type == "removed")
        
        if self.show_additions:
            print(f"Total parameter changes: {total_changes}")
            if total_changes == 0:
                print(f"{Colors.GREEN}✅ No parameter differences found across versions!{Colors.END}")
            else:
                print(f"{Colors.GREEN}✅ Parameters added: {added_count}{Colors.END}")
                print(f"{Colors.RED}❌ Parameters removed: {removed_count}{Colors.END}")
        else:
            print(f"Parameters removed (shown): {total_changes}")
            print(f"{Colors.RED}❌ Parameters removed: {removed_count}{Colors.END}")
            if added_count > 0:
                print(f"{Colors.YELLOW}💡 Parameters added (hidden): {added_count} - use --show-additions to view{Colors.END}")
        
        print()
        
        # Detailed file breakdown
        print(f"{Colors.BOLD}{Colors.CYAN}📄 File Analysis Breakdown{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print(f"{'File Name':<50} {'Added':<8} {'Removed':<8} {'Total':<8}")
        print(f"{'-'*50} {'-'*8} {'-'*8} {'-'*8}")
        
        # Sort files by total changes (descending), then by name
        sorted_files = sorted(file_stats.items(), key=lambda x: (-x[1]['total'], x[0]))
        
        for filename, stats in sorted_files:
            # Truncate filename if too long
            display_name = filename if len(filename) <= 50 else filename[:47] + "..."
            
            added_color = Colors.GREEN if stats['added'] > 0 else Colors.WHITE
            removed_color = Colors.RED if stats['removed'] > 0 else Colors.WHITE
            total_color = Colors.YELLOW if stats['total'] > 0 else Colors.WHITE
            
            print(f"{display_name:<50} "
                  f"{added_color}{stats['added']:<8}{Colors.END} "
                  f"{removed_color}{stats['removed']:<8}{Colors.END} "
                  f"{total_color}{stats['total']:<8}{Colors.END}")
        
        print(f"{'-'*50} {'-'*8} {'-'*8} {'-'*8}")
        print(f"{'TOTAL':<50} "
              f"{Colors.GREEN}{added_count:<8}{Colors.END} "
              f"{Colors.RED}{removed_count:<8}{Colors.END} "
              f"{Colors.YELLOW}{added_count + removed_count:<8}{Colors.END}")
        
        # Additional insights
        print()
        files_with_only_additions = sum(1 for stats in file_stats.values() if stats['added'] > 0 and stats['removed'] == 0)
        files_with_only_removals = sum(1 for stats in file_stats.values() if stats['removed'] > 0 and stats['added'] == 0)
        files_with_both = sum(1 for stats in file_stats.values() if stats['added'] > 0 and stats['removed'] > 0)
        files_unchanged = sum(1 for stats in file_stats.values() if stats['total'] == 0)
        
        print(f"{Colors.BOLD}📈 Change Distribution:{Colors.END}")
        print(f"  Files with only additions: {Colors.GREEN}{files_with_only_additions}{Colors.END}")
        print(f"  Files with only removals: {Colors.RED}{files_with_only_removals}{Colors.END}")
        print(f"  Files with both changes: {Colors.YELLOW}{files_with_both}{Colors.END}")
        print(f"  Files unchanged: {Colors.WHITE}{files_unchanged}{Colors.END}")

def main():
    """Main function to run the CRD comparison tool."""
    parser = argparse.ArgumentParser(
        description="Compare OADP CRD files across versions 1.3, 1.4, and 1.5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 oadp_crd_comparison.py                    # Prompt for directory (default: /var/tmp/OADP)
  python3 oadp_crd_comparison.py --show-additions   # Show both additions and removals
  python3 oadp_crd_comparison.py /path/to/oadp      # Use specific directory
  python3 oadp_crd_comparison.py --non-interactive  # Use default directory without prompting
        """
    )
    
    parser.add_argument(
        "directory", 
        nargs="?", 
        help="Directory containing version subdirectories (1.3, 1.4, 1.5). If not provided, will prompt user."
    )
    
    parser.add_argument(
        "--show-additions", 
        action="store_true", 
        help="Show parameter additions (green checks) in addition to removals (red X). By default, only removals are shown."
    )
    
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Use default directory (/var/tmp/OADP) without prompting when no directory is specified."
    )
    
    args = parser.parse_args()
    
    # Determine the directory to use
    if args.directory:
        directory = args.directory
    elif args.non_interactive:
        directory = "/var/tmp/OADP"
    else:
        # Interactive mode - prompt for directory
        print(f"{Colors.BOLD}{Colors.CYAN}OADP CRD Comparison Tool{Colors.END}")
        print(f"{Colors.CYAN}{'='*40}{Colors.END}")
        print()
        
        default_dir = "/var/tmp/OADP"
        prompt = f"Enter directory path (default: {Colors.YELLOW}{default_dir}{Colors.END}): "
        
        try:
            user_input = input(prompt).strip()
            directory = user_input if user_input else default_dir
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Colors.YELLOW}Operation cancelled.{Colors.END}")
            sys.exit(0)
        
        print()
    
    try:
        comparator = CRDComparator(directory, args.show_additions)
        comparator.generate_report()
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()