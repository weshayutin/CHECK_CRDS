#!/usr/bin/env python3
"""
Quick validation script to verify the OADP CRD analysis setup is working correctly.
"""

import sys
from pathlib import Path

def main():
    """Validate the setup."""
    base_dir = Path("/var/tmp/OADP")
    check_crds_dir = Path.home() / "OADP" / "CHECK_CRDS"
    
    print("🔍 Validating OADP CRD Analysis Setup...")
    print("=" * 40)
    
    # Check ~/OADP/CHECK_CRDS directory
    if check_crds_dir.exists():
        print("✅ ~/OADP/CHECK_CRDS directory exists")
        
        # Check required files
        required_files = ["oadp_crd_comparison.py", "setup_oadp_analysis.py", "README.md"]
        for file_name in required_files:
            file_path = check_crds_dir / file_name
            if file_path.exists():
                print(f"✅ {file_name} found")
            else:
                print(f"❌ {file_name} missing")
    else:
        print("❌ ~/OADP/CHECK_CRDS directory not found")
        return False
    
    # Check /var/tmp/OADP directory
    if base_dir.exists():
        print(f"✅ {base_dir} directory exists")
        
        # Check for version directories
        versions = ["1.3", "1.4", "1.5"]
        found_versions = []
        
        for version in versions:
            version_dir = base_dir / version
            if version_dir.exists():
                file_count = len(list(version_dir.glob("*.yaml")))
                print(f"✅ Version {version}: {file_count} files")
                found_versions.append(version)
            else:
                print(f"⚠️  Version {version}: Not found")
        
        if len(found_versions) >= 2:
            print(f"\n🎉 Setup is ready for comparison!")
            print(f"Found {len(found_versions)} versions: {', '.join(found_versions)}")
            print("\nNext steps:")
            print(f"  cd ~/OADP/CHECK_CRDS")
            print(f"  python3 oadp_crd_comparison.py {base_dir}")
        else:
            print(f"\n⚠️  Need at least 2 versions for comparison.")
            print(f"Run: python3 setup_oadp_analysis_enhanced.py  (recommended)")
            print(f"  or: python3 setup_oadp_analysis.py --manual")
    else:
        print(f"⚠️  {base_dir} directory not found")
        print("This is normal for first-time setup.")
        print("Run: python3 setup_oadp_analysis_enhanced.py  (recommended)")
        print("  or: python3 setup_oadp_analysis.py --manual")
    
    return True

if __name__ == "__main__":
    main()