# OADP CRD Analysis - Quick Usage Guide

## 🎯 For New Users

### Step 1: Initial Setup

#### Option A: Enhanced Setup (Recommended)
```bash
cd ~/OADP/CHECK_CRDS
python3 setup_oadp_analysis_enhanced.py
```

When prompted:
- **Path**: Point to your local oadp-operator repository (e.g., `/home/user/oadp-operator`)

The script will automatically process all versions (1.3, 1.4, 1.5) by checking out the appropriate branches.

#### Option B: Manual Setup
```bash
cd ~/OADP/CHECK_CRDS
python3 setup_oadp_analysis.py --manual
```

When prompted:
- **Path**: Point to your local oadp-operator repository (e.g., `/home/user/oadp-operator`)
- **Version**: Choose which OADP version this represents (1.3, 1.4, or 1.5)

Repeat this for each OADP version you want to compare.

### Step 2: Validate Setup
```bash
python3 validate_setup.py
```

### Step 3: Run Analysis
```bash
# Show only removals (focus on breaking changes)
python3 oadp_crd_comparison.py /var/tmp/OADP

# Show both additions and removals  
python3 oadp_crd_comparison.py --show-additions /var/tmp/OADP
```

## 📊 Example Output

```
OADP CRD Version Comparison Report
============================================================
Comparing versions: 1.3, 1.4, 1.5
Common files found: 18

📄 File Analysis Breakdown
File Name                                          Added    Removed  Total   
-------------------------------------------------- -------- -------- --------
oadp.openshift.io_dataprotectionapplications.yaml  2014     2        2016    
oadp-operator.clusterserviceversion.yaml           438      290      728     
oadp.openshift.io_cloudstorages.yaml               18       0        18      
...

📈 Change Distribution:
  Files with only additions: 2
  Files with only removals: 0
  Files with both changes: 2
  Files unchanged: 14
```

## 🔧 Advanced Usage

### Compare Custom Directory
```bash
python3 oadp_crd_comparison.py /path/to/your/oadp/versions
```

### Export Results
```bash
python3 oadp_crd_comparison.py /var/tmp/OADP > oadp_analysis_report.txt
```

## 🆘 Quick Troubleshooting

**"No parameter differences found"**
- Run `python3 validate_setup.py` to check your setup
- Ensure you have multiple version directories

**"bundle/manifests not found"**  
- Point to the root of oadp-operator repository, not a subdirectory

**Need to add more versions?**
- Run `python3 setup_oadp_analysis.py` again with different oadp-operator checkouts