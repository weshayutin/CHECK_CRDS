#!/usr/bin/env python3
"""
OADP CRD Analysis Setup Script

This script helps users set up the directory structure needed for OADP CRD version comparison.
It prompts for the local oadp-operator repository path and creates the versioned directory
structure with CRDs from bundle/manifests.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional

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

class OADPSetup:
    def __init__(self):
        self.base_dir = Path("/var/tmp/OADP")
        self.target_versions = ["1.3", "1.4", "1.5"]
        
    def print_header(self):
        """Print setup script header."""
        print(f"{Colors.BOLD}{Colors.CYAN}OADP CRD Analysis Setup{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        print("This script will set up the directory structure for OADP CRD version comparison.")
        print(f"Target directory: {Colors.YELLOW}{self.base_dir}{Colors.END}")
        print()
        
    def prompt_for_oadp_path(self) -> Path:
        """Prompt user for oadp-operator repository path."""
        while True:
            print(f"{Colors.BOLD}Please provide the path to your local oadp-operator repository:{Colors.END}")
            print(f"Example: {Colors.YELLOW}/home/user/oadp-operator{Colors.END}")
            
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
            bundle_path = repo_path / "bundle" / "manifests"
            if not bundle_path.exists():
                print(f"{Colors.RED}Error: bundle/manifests directory not found in {repo_path}{Colors.END}")
                print(f"{Colors.YELLOW}Make sure you're pointing to the oadp-operator repository root.{Colors.END}")
                continue
                
            print(f"{Colors.GREEN}✅ Found oadp-operator repository at: {repo_path}{Colors.END}")
            return repo_path
    
    def get_git_version_info(self, repo_path: Path) -> Optional[str]:
        """Get current git branch/tag information."""
        try:
            # Try to get current branch/tag
            result = subprocess.run(
                ["git", "describe", "--tags", "--exact-match"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                return f"tag: {result.stdout.strip()}"
            
            # If no exact tag, get branch name
            result = subprocess.run(
                ["git", "branch", "--show-current"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                branch = result.stdout.strip()
                if branch:
                    return f"branch: {branch}"
            
            # Fallback to commit hash
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"], 
                cwd=repo_path, 
                capture_output=True, 
                text=True
            )
            if result.returncode == 0:
                return f"commit: {result.stdout.strip()}"
                
        except Exception:
            pass
        
        return None
    
    def prompt_for_version(self, repo_path: Path) -> str:
        """Prompt user to specify which version this represents."""
        git_info = self.get_git_version_info(repo_path)
        
        print(f"\n{Colors.BOLD}Which OADP version does this repository represent?{Colors.END}")
        if git_info:
            print(f"Current git state: {Colors.YELLOW}{git_info}{Colors.END}")
        
        print(f"Available options: {Colors.CYAN}{', '.join(self.target_versions)}{Colors.END}")
        
        while True:
            version = input("Version: ").strip()
            
            if version in self.target_versions:
                return version
            else:
                print(f"{Colors.RED}Error: Please enter one of: {', '.join(self.target_versions)}{Colors.END}")
    
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
                        if 'kind: CustomResourceDefinition' in content or 'ClusterRole' in content or 'Service' in content or 'ConfigMap' in content:
                            crd_files.append(file_path)
                except Exception:
                    # If we can't read it, skip it
                    continue
        
        return sorted(crd_files)
    
    def create_version_directory(self, version: str, crd_files: List[Path]) -> bool:
        """Create version directory and copy CRD files."""
        version_dir = self.base_dir / version
        
        # Create directory structure
        try:
            self.base_dir.mkdir(parents=True, exist_ok=True)
            version_dir.mkdir(parents=True, exist_ok=True)
            print(f"{Colors.GREEN}✅ Created directory: {version_dir}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}Error creating directory {version_dir}: {e}{Colors.END}")
            return False
        
        # Copy CRD files
        copied_count = 0
        for crd_file in crd_files:
            try:
                dest_file = version_dir / crd_file.name
                shutil.copy2(crd_file, dest_file)
                copied_count += 1
                print(f"  📄 Copied: {crd_file.name}")
            except Exception as e:
                print(f"  {Colors.RED}❌ Failed to copy {crd_file.name}: {e}{Colors.END}")
        
        print(f"{Colors.GREEN}✅ Copied {copied_count} files to version {version}{Colors.END}")
        return copied_count > 0
    
    def verify_setup(self) -> bool:
        """Verify the setup is correct."""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}🔍 Verifying Setup{Colors.END}")
        print(f"{Colors.MAGENTA}{'='*30}{Colors.END}")
        
        all_good = True
        
        # Check if base directory exists
        if not self.base_dir.exists():
            print(f"{Colors.RED}❌ Base directory doesn't exist: {self.base_dir}{Colors.END}")
            return False
        
        # Check each version directory
        existing_versions = []
        for version in self.target_versions:
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
        print(f"{Colors.YELLOW}💡 Tip: To add more versions, run this setup script again with different oadp-operator checkouts.{Colors.END}")
    
    def run(self):
        """Run the complete setup process."""
        print(f"{Colors.BOLD}{Colors.CYAN}OADP CRD Analysis Setup{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        print()
        print(f"{Colors.BOLD}{Colors.YELLOW}🚀 Enhanced Setup Available!{Colors.END}")
        print(f"{Colors.YELLOW}{'='*30}{Colors.END}")
        print(f"We now have an enhanced setup script that automatically processes")
        print(f"all OADP versions (1.3, 1.4, 1.5) in one go!")
        print()
        print(f"{Colors.BOLD}Options:{Colors.END}")
        print(f"1. {Colors.GREEN}Enhanced Setup{Colors.END} (Recommended): Automatically checkout and process all versions")
        print(f"   Command: {Colors.CYAN}python3 setup_oadp_analysis_enhanced.py{Colors.END}")
        print()
        print(f"2. {Colors.YELLOW}Manual Setup{Colors.END}: Process one version at a time (this script)")
        print(f"   Command: {Colors.CYAN}python3 setup_oadp_analysis.py --manual{Colors.END}")
        print()
        
        # Check if user wants enhanced setup
        if len(sys.argv) == 1 or "--manual" not in sys.argv:
            response = input(f"Use enhanced setup? ({Colors.GREEN}Y{Colors.END}/n): ").strip().lower()
            if response != 'n':
                print(f"\n{Colors.GREEN}Starting enhanced setup...{Colors.END}")
                try:
                    os.execvp("python3", ["python3", "setup_oadp_analysis_enhanced.py"])
                except Exception as e:
                    print(f"{Colors.RED}Error launching enhanced setup: {e}{Colors.END}")
                    print(f"Falling back to manual setup...")
                    print()
        
        # Continue with manual setup
        self.print_header()
        
        # Get oadp-operator path
        repo_path = self.prompt_for_oadp_path()
        
        # Get version
        version = self.prompt_for_version(repo_path)
        
        # Find CRD files
        bundle_path = repo_path / "bundle" / "manifests"
        crd_files = self.find_crd_files(bundle_path)
        
        print(f"\n{Colors.BOLD}📄 Found {len(crd_files)} CRD files in bundle/manifests{Colors.END}")
        
        # Create version directory and copy files
        if self.create_version_directory(version, crd_files):
            # Verify setup
            if self.verify_setup():
                self.show_next_steps()
            else:
                print(f"\n{Colors.YELLOW}Setup completed but verification had warnings.{Colors.END}")
                print(f"You may need to add more OADP versions for meaningful comparison.")
        else:
            print(f"\n{Colors.RED}Setup failed. Please check the errors above.{Colors.END}")

def main():
    """Main function."""
    try:
        setup = OADPSetup()
        setup.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Setup cancelled by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()