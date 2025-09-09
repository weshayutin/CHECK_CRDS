#!/usr/bin/env python3
"""
OADP CRD Analysis Enhanced Setup Script

This script automatically sets up the directory structure needed for OADP CRD version comparison.
It prompts for the local oadp-operator repository path, then automatically checks out each
required branch (release-1.3, release-1.4, release-1.5) and copies CRDs from bundle/manifests
to the corresponding versioned directories.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Dict

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

class OADPSetupEnhanced:
    def __init__(self):
        self.base_dir = Path("/var/tmp/OADP")
        # Map of version to potential git branch/tag names (in order of preference)
        self.version_mapping = {
            "1.3": ["oadp-1.3", "release-1.3", "v1.3.0", "v1.3", "1.3"],
            "1.4": ["oadp-1.4", "release-1.4", "v1.4.0", "v1.4", "1.4"], 
            "1.5": ["oadp-1.5", "release-1.5", "v1.5.0", "v1.5", "1.5"]
        }
        
    def print_header(self):
        """Print setup script header."""
        print(f"{Colors.BOLD}{Colors.CYAN}OADP CRD Analysis Enhanced Setup{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print("This script will automatically set up all OADP versions for CRD comparison.")
        print(f"Target directory: {Colors.YELLOW}{self.base_dir}{Colors.END}")
        print(f"Versions to process: {Colors.CYAN}{', '.join(self.version_mapping.keys())}{Colors.END}")
        print(f"Looking for branches: {Colors.YELLOW}oadp-1.3, oadp-1.4, oadp-1.5{Colors.END}")
        print()
        
    def prompt_for_oadp_path(self) -> Path:
        """Prompt user for oadp-operator repository path."""
        while True:
            print(f"{Colors.BOLD}Please provide the path to your local oadp-operator repository:{Colors.END}")
            print(f"Example: {Colors.YELLOW}/home/user/oadp-operator{Colors.END}")
            print(f"{Colors.YELLOW}Note: This should be a clean git repository (uncommitted changes will be stashed){Colors.END}")
            
            user_input = input("Path: ").strip()
            
            if not user_input:
                print(f"{Colors.RED}Error: Please provide a valid path.{Colors.END}")
                continue
                
            # Expand ~ and resolve path
            repo_path = Path(user_input).expanduser().resolve()
            
            if not repo_path.exists():
                print(f"{Colors.RED}Error: Directory does not exist: {repo_path}{Colors.END}")
                continue
                
            # Check if it looks like oadp-operator repo
            if not (repo_path / ".git").exists():
                print(f"{Colors.RED}Error: Not a git repository: {repo_path}{Colors.END}")
                continue
                
            bundle_path = repo_path / "bundle" / "manifests"
            if not bundle_path.exists():
                print(f"{Colors.RED}Error: bundle/manifests directory not found in {repo_path}{Colors.END}")
                print(f"{Colors.YELLOW}Make sure you're pointing to the oadp-operator repository root.{Colors.END}")
                continue
                
            print(f"{Colors.GREEN}✅ Found oadp-operator repository at: {repo_path}{Colors.END}")
            return repo_path
    
    def discover_available_branches(self, repo_path: Path) -> List[str]:
        """Discover all available branches and tags in the repository."""
        try:
            # Get remote branches
            result = subprocess.run(
                ["git", "branch", "-r"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            
            branches = []
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    line = line.strip()
                    if line and not line.startswith('origin/HEAD'):
                        # Remove 'origin/' prefix
                        branch = line.replace('origin/', '')
                        branches.append(branch)
            
            # Get tags
            result = subprocess.run(
                ["git", "tag", "-l"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    line = line.strip()
                    if line:
                        branches.append(line)
            
            return sorted(set(branches))
            
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Warning: Could not discover branches: {e}{Colors.END}")
            return []
    
    def find_best_branch_for_version(self, repo_path: Path, version: str, available_branches: List[str]) -> Optional[str]:
        """Find the best matching branch/tag for a given version."""
        possible_names = self.version_mapping.get(version, [])
        
        # Check each possible name in order of preference
        for candidate in possible_names:
            if candidate in available_branches:
                return candidate
        
        # If no exact match, try partial matching
        for candidate in possible_names:
            for branch in available_branches:
                if candidate.lower() in branch.lower() or branch.lower().endswith(candidate.lower()):
                    return branch
        
        return None

    def check_git_status(self, repo_path: Path) -> bool:
        """Check git repository status and handle uncommitted changes."""
        try:
            # Check for uncommitted changes
            result = subprocess.run(
                ["git", "status", "--porcelain"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            
            if result.returncode != 0:
                print(f"{Colors.RED}Error: Failed to check git status{Colors.END}")
                return False
            
            if result.stdout.strip():
                print(f"{Colors.YELLOW}⚠️  Repository has uncommitted changes.{Colors.END}")
                response = input("Stash changes and continue? (y/N): ").strip().lower()
                
                if response == 'y':
                    stash_result = subprocess.run(
                        ["git", "stash", "push", "-m", "OADP setup script auto-stash"], 
                        cwd=repo_path, 
                        capture_output=True, 
                        text=True
                    )
                    if stash_result.returncode == 0:
                        print(f"{Colors.GREEN}✅ Changes stashed successfully{Colors.END}")
                        return True
                    else:
                        print(f"{Colors.RED}Error: Failed to stash changes{Colors.END}")
                        return False
                else:
                    print(f"{Colors.YELLOW}Setup cancelled. Please commit or stash your changes first.{Colors.END}")
                    return False
            
            return True
            
        except Exception as e:
            print(f"{Colors.RED}Error checking git status: {e}{Colors.END}")
            return False
    
    def checkout_branch(self, repo_path: Path, branch: str) -> bool:
        """Checkout a specific branch or tag."""
        try:
            # Fetch latest changes
            print(f"  📡 Fetching latest changes...")
            fetch_result = subprocess.run(
                ["git", "fetch", "origin"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            
            if fetch_result.returncode != 0:
                print(f"{Colors.YELLOW}⚠️  Warning: Failed to fetch from origin (continuing anyway){Colors.END}")
            
            # Try different checkout strategies
            checkout_attempts = [
                branch,                    # Direct branch/tag name
                f"origin/{branch}",       # Remote branch
                f"tags/{branch}",         # Tag reference
                f"refs/tags/{branch}"     # Full tag reference
            ]
            
            for attempt in checkout_attempts:
                print(f"  🔄 Trying to checkout {attempt}...")
                checkout_result = subprocess.run(
                    ["git", "checkout", attempt], 
                    cwd=repo_path, 
                    capture_output=True, 
                    text=True
                )
                
                if checkout_result.returncode == 0:
                    print(f"  {Colors.GREEN}✅ Successfully checked out {attempt}{Colors.END}")
                    return True
                else:
                    print(f"    ⚠️  {attempt} failed: {checkout_result.stderr.strip()}")
            
            print(f"  {Colors.RED}❌ All checkout attempts failed for {branch}{Colors.END}")
            return False
                    
        except Exception as e:
            print(f"  {Colors.RED}❌ Error checking out {branch}: {e}{Colors.END}")
            return False
    
    def find_crd_files(self, bundle_path: Path) -> List[Path]:
        """Find all CRD files in bundle/manifests."""
        crd_files = []
        
        # Look for YAML files that are likely CRDs
        for file_path in bundle_path.glob("*.yaml"):
            if file_path.is_file():
                # Read first few lines to check if it's a CRD
                try:
                    with open(file_path, 'r') as f:
                        content = f.read(500)  # Read first 500 chars
                        if ('kind: CustomResourceDefinition' in content or 
                            'ClusterRole' in content or 
                            'Service' in content or 
                            'ConfigMap' in content or
                            'ClusterServiceVersion' in content):
                            crd_files.append(file_path)
                except Exception:
                    # If we can't read it, skip it
                    continue
        
        return sorted(crd_files)
    
    def create_version_directory(self, version: str, crd_files: List[Path]) -> bool:
        """Create version directory and copy CRD files."""
        version_dir = self.base_dir / version
        
        # Create base directory structure
        try:
            self.base_dir.mkdir(parents=True, exist_ok=True)
            version_dir.mkdir(parents=True, exist_ok=True)
            print(f"  📁 Created directory: {version_dir}")
        except Exception as e:
            print(f"  {Colors.RED}❌ Error creating directory {version_dir}: {e}{Colors.END}")
            return False
        
        # Clear existing files in version directory
        for existing_file in version_dir.glob("*.yaml"):
            existing_file.unlink()
        
        # Copy CRD files
        copied_count = 0
        for crd_file in crd_files:
            try:
                dest_file = version_dir / crd_file.name
                shutil.copy2(crd_file, dest_file)
                copied_count += 1
                print(f"    📄 {crd_file.name}")
            except Exception as e:
                print(f"    {Colors.RED}❌ Failed to copy {crd_file.name}: {e}{Colors.END}")
        
        print(f"  {Colors.GREEN}✅ Copied {copied_count} files to version {version}{Colors.END}")
        return copied_count > 0
    
    def process_all_versions(self, repo_path: Path) -> Dict[str, bool]:
        """Process all OADP versions automatically."""
        results = {}
        
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}🔄 Processing All OADP Versions{Colors.END}")
        print(f"{Colors.MAGENTA}{'='*50}{Colors.END}")
        
        # Ensure base directory exists
        try:
            self.base_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Ensured base directory exists: {self.base_dir}")
        except Exception as e:
            print(f"{Colors.RED}❌ Error creating base directory {self.base_dir}: {e}{Colors.END}")
            return results
        
        # Discover available branches
        print(f"\n🔍 Discovering available branches and tags...")
        available_branches = self.discover_available_branches(repo_path)
        if available_branches:
            print(f"Found {len(available_branches)} branches/tags: {', '.join(available_branches[:10])}{'...' if len(available_branches) > 10 else ''}")
        else:
            print(f"{Colors.YELLOW}⚠️  Could not discover branches, will try default names{Colors.END}")
        
        for version in self.version_mapping.keys():
            # Find the best branch for this version
            if available_branches:
                best_branch = self.find_best_branch_for_version(repo_path, version, available_branches)
            else:
                # Fallback to first candidate if discovery failed
                best_branch = self.version_mapping[version][0]
            
            if not best_branch:
                print(f"\n{Colors.BOLD}{Colors.RED}📦 Processing OADP {version} - No suitable branch found{Colors.END}")
                print(f"Available branches: {', '.join(available_branches) if available_branches else 'Unknown'}")
                results[version] = False
                continue
            
            print(f"\n{Colors.BOLD}{Colors.CYAN}📦 Processing OADP {version} (branch: {best_branch}){Colors.END}")
            print(f"{Colors.CYAN}{'-'*40}{Colors.END}")
            
            # Checkout the branch
            if not self.checkout_branch(repo_path, best_branch):
                print(f"  {Colors.RED}❌ Skipping version {version} due to checkout failure{Colors.END}")
                results[version] = False
                continue
            
            # Find CRD files
            bundle_path = repo_path / "bundle" / "manifests"
            if not bundle_path.exists():
                print(f"  {Colors.RED}❌ bundle/manifests not found for {version}{Colors.END}")
                results[version] = False
                continue
                
            crd_files = self.find_crd_files(bundle_path)
            print(f"  📄 Found {len(crd_files)} CRD files")
            
            # Create version directory and copy files
            if self.create_version_directory(version, crd_files):
                results[version] = True
                print(f"  {Colors.GREEN}✅ Version {version} completed successfully{Colors.END}")
            else:
                results[version] = False
                print(f"  {Colors.RED}❌ Version {version} failed{Colors.END}")
        
        return results
    
    def verify_setup(self) -> bool:
        """Verify the setup is correct."""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}🔍 Verifying Setup{Colors.END}")
        print(f"{Colors.MAGENTA}{'='*30}{Colors.END}")
        
        if not self.base_dir.exists():
            print(f"{Colors.RED}❌ Base directory doesn't exist: {self.base_dir}{Colors.END}")
            return False
        
        # Check each version directory
        existing_versions = []
        for version in self.version_mapping.keys():
            version_dir = self.base_dir / version
            if version_dir.exists():
                file_count = len(list(version_dir.glob("*.yaml")))
                print(f"{Colors.GREEN}✅ Version {version}: {file_count} files{Colors.END}")
                existing_versions.append(version)
            else:
                print(f"{Colors.YELLOW}⚠️  Version {version}: Not found{Colors.END}")
        
        if len(existing_versions) >= 2:
            print(f"\n{Colors.GREEN}✅ Setup verification passed!{Colors.END}")
            print(f"Found {len(existing_versions)} version directories: {', '.join(existing_versions)}")
            return True
        else:
            print(f"\n{Colors.YELLOW}⚠️  Need at least 2 version directories for comparison.{Colors.END}")
            return False
    
    def show_results_summary(self, results: Dict[str, bool]):
        """Show summary of processing results."""
        print(f"\n{Colors.BOLD}{Colors.GREEN}📋 Processing Summary{Colors.END}")
        print(f"{Colors.GREEN}{'='*40}{Colors.END}")
        
        successful = [v for v, success in results.items() if success]
        failed = [v for v, success in results.items() if not success]
        
        print(f"✅ Successful: {Colors.GREEN}{', '.join(successful) if successful else 'None'}{Colors.END}")
        if failed:
            print(f"❌ Failed: {Colors.RED}{', '.join(failed)}{Colors.END}")
        
        print(f"\nTotal versions processed: {len(successful)}/{len(self.version_mapping)}")
    
    def show_next_steps(self):
        """Show next steps to the user."""
        print(f"\n{Colors.BOLD}{Colors.GREEN}🎉 Setup Complete!{Colors.END}")
        print(f"{Colors.GREEN}{'='*40}{Colors.END}")
        print(f"Your OADP CRD analysis environment is ready!")
        print()
        print(f"{Colors.BOLD}Next Steps:{Colors.END}")
        print(f"1. 📁 Navigate to: {Colors.CYAN}cd ~/OADP/CHECK_CRDS{Colors.END}")
        print(f"2. 🔍 Run comparison: {Colors.CYAN}python3 oadp_crd_comparison.py {self.base_dir}{Colors.END}")
        print(f"3. 📊 View full report: {Colors.CYAN}python3 oadp_crd_comparison.py --show-additions {self.base_dir}{Colors.END}")
        print()
        print(f"{Colors.YELLOW}💡 Tip: Your git repository has been left on the last processed branch.{Colors.END}")
        print(f"{Colors.YELLOW}    You may want to checkout your original branch when done.{Colors.END}")
    
    def show_troubleshooting_info(self, repo_path: Path):
        """Show troubleshooting information for branch issues."""
        print(f"\n{Colors.BOLD}{Colors.YELLOW}🛠️  Troubleshooting Information{Colors.END}")
        print(f"{Colors.YELLOW}{'='*50}{Colors.END}")
        
        print(f"Repository path: {repo_path}")
        
        # Show available branches
        print(f"\n📋 Available branches and tags:")
        available_branches = self.discover_available_branches(repo_path)
        if available_branches:
            for i, branch in enumerate(available_branches, 1):
                print(f"  {i:2d}. {branch}")
        else:
            print(f"  {Colors.RED}❌ Could not discover any branches{Colors.END}")
        
        # Show what we're looking for
        print(f"\n🔍 Looking for these patterns:")
        for version, candidates in self.version_mapping.items():
            best_match = None
            if available_branches:
                best_match = self.find_best_branch_for_version(repo_path, version, available_branches)
            
            status = f"{Colors.GREEN}✅ Found: {best_match}{Colors.END}" if best_match else f"{Colors.RED}❌ Not found{Colors.END}"
            print(f"  OADP {version}: {candidates} -> {status}")
        
        print(f"\n💡 Suggestions:")
        print(f"  1. Check if you have the correct OADP repository")
        print(f"  2. Run 'git fetch --all' in your repository to get latest refs")
        print(f"  3. Check if releases use different naming (v1.3.0, 1.3-release, etc.)")
        print(f"  4. Use the manual setup if automatic detection fails")
    
    def run(self):
        """Run the complete enhanced setup process."""
        self.print_header()
        
        # Get oadp-operator path
        repo_path = self.prompt_for_oadp_path()
        
        # Check git status and handle uncommitted changes
        if not self.check_git_status(repo_path):
            print(f"{Colors.RED}Setup cancelled due to git status issues.{Colors.END}")
            return
        
        # Process all versions
        results = self.process_all_versions(repo_path)
        
        # Show results summary
        self.show_results_summary(results)
        
        # Verify setup
        if self.verify_setup():
            self.show_next_steps()
        else:
            print(f"\n{Colors.YELLOW}Setup completed but verification had issues.{Colors.END}")
            
            # If no versions were successful, show troubleshooting info
            successful_count = sum(1 for success in results.values() if success)
            if successful_count == 0:
                self.show_troubleshooting_info(repo_path)
            else:
                print(f"Check the error messages above for details.")

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Enhanced OADP CRD setup - automatically process all versions",
        epilog="This script will checkout release branches and copy CRDs automatically."
    )
    parser.add_argument(
        "--troubleshoot", 
        action="store_true", 
        help="Show branch troubleshooting info for a repository without running setup"
    )
    parser.add_argument(
        "--repo-path",
        help="Repository path (for troubleshooting mode)"
    )
    
    args = parser.parse_args()
    
    try:
        setup = OADPSetupEnhanced()
        
        if args.troubleshoot:
            if args.repo_path:
                repo_path = Path(args.repo_path).expanduser().resolve()
            else:
                repo_path = setup.prompt_for_oadp_path()
            
            setup.show_troubleshooting_info(repo_path)
        else:
            setup.run()
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Setup cancelled by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()