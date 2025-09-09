# OADP CRD Version Comparison Tool

This tool compares OADP Custom Resource Definition files across versions 1.3, 1.4, and 1.5 to identify parameter additions and removals between versions.

## 🚀 Quick Start

### 1. Setup Your Environment

#### Option A: Enhanced Setup (Recommended)

Process all OADP versions automatically:

```bash
cd ~/OADP/CHECK_CRDS
python3 setup_oadp_analysis_enhanced.py
```

The enhanced setup script will:
- Prompt you for your local oadp-operator repository path
- Automatically checkout oadp-1.3, oadp-1.4, and oadp-1.5 branches
- Copy CRDs from `bundle/manifests` for each version
- Create all version directories in one go
- Handle git stashing if you have uncommitted changes

#### Option B: Manual Setup

Process one version at a time:

```bash
cd ~/OADP/CHECK_CRDS
python3 setup_oadp_analysis.py --manual
```

**Repeat this process for each OADP version you want to compare.**

### 2. Run the Comparison

Once you have at least 2 versions set up:

```bash
# Show only removals (default - focuses on potential breaking changes)
python3 oadp_crd_comparison.py /var/tmp/OADP

# Show both additions and removals
python3 oadp_crd_comparison.py --show-additions /var/tmp/OADP
```

## 📊 Understanding the Output

### Default Mode (Removals Only)
- **Red ❌**: Parameters removed in newer versions
- **Line numbers**: Exact location in the source file
- **Version transitions**: Shows which version removed the parameter

### Full Mode (--show-additions)
- **Green ✅**: Parameters added in newer versions  
- **Red ❌**: Parameters removed in newer versions
- **Both**: Complete picture of API evolution

### Summary Report
The tool provides a comprehensive summary including:

```
📄 File Analysis Breakdown
File Name                                          Added    Removed  Total   
-------------------------------------------------- -------- -------- --------
oadp.openshift.io_dataprotectionapplications.yaml  2014     2        2016    
oadp-operator.clusterserviceversion.yaml           438      290      728     
...

📈 Change Distribution:
  Files with only additions: 2
  Files with only removals: 0  
  Files with both changes: 2
  Files unchanged: 14
```

## 📁 Directory Structure

After setup, your directory structure will look like:

```
~/OADP/CHECK_CRDS/
├── setup_oadp_analysis.py      # Setup script
├── oadp_crd_comparison.py      # Comparison tool
└── README.md                   # This file

/var/tmp/OADP/
├── 1.3/                        # OADP 1.3 CRDs
│   ├── oadp.openshift.io_dataprotectionapplications.yaml
│   ├── oadp-operator.clusterserviceversion.yaml
│   └── ...
├── 1.4/                        # OADP 1.4 CRDs
│   └── ...
└── 1.5/                        # OADP 1.5 CRDs
    └── ...
```

## 🔧 Advanced Usage

### Compare Custom Directory
```bash
python3 oadp_crd_comparison.py /path/to/your/oadp/versions
```

### Help and Options
```bash
python3 oadp_crd_comparison.py --help
```

## 🛠️ Prerequisites

- Python 3.6+
- PyYAML library (`pip install pyyaml`)
- Local checkout(s) of [oadp-operator](https://github.com/openshift/oadp-operator)

## 📋 Example Workflows

### Enhanced Workflow (Recommended)

1. **Clone OADP operator repository:**
   ```bash
   git clone https://github.com/openshift/oadp-operator.git
   ```

2. **Run enhanced setup:**
   ```bash
   cd ~/OADP/CHECK_CRDS
   python3 setup_oadp_analysis_enhanced.py
   # When prompted, point to your oadp-operator directory
   ```

3. **Run comparison:**
   ```bash
   python3 oadp_crd_comparison.py /var/tmp/OADP
   ```

### Manual Workflow

1. **Clone OADP operator repositories for different versions:**
   ```bash
   git clone https://github.com/openshift/oadp-operator.git oadp-1.3
   cd oadp-1.3 && git checkout oadp-1.3
   
   git clone https://github.com/openshift/oadp-operator.git oadp-1.4  
   cd oadp-1.4 && git checkout oadp-1.4
   
   git clone https://github.com/openshift/oadp-operator.git oadp-1.5
   cd oadp-1.5 && git checkout oadp-1.5
   ```

2. **Run setup for each version:**
   ```bash
   cd ~/OADP/CHECK_CRDS
   python3 setup_oadp_analysis.py --manual  # Point to oadp-1.3, select version 1.3
   python3 setup_oadp_analysis.py --manual  # Point to oadp-1.4, select version 1.4  
   python3 setup_oadp_analysis.py --manual  # Point to oadp-1.5, select version 1.5
   ```

3. **Run comparison:**
   ```bash
   python3 oadp_crd_comparison.py /var/tmp/OADP
   ```

## 🎯 Use Cases

- **API Evolution Analysis**: Track how OADP APIs change between versions
- **Breaking Change Detection**: Identify removed parameters that could break upgrades
- **Feature Addition Tracking**: See what new capabilities are added
- **Documentation**: Generate change logs for version releases
- **Testing**: Ensure backward compatibility in upgrades

## 🐛 Troubleshooting

**"bundle/manifests directory not found"**
- Ensure you're pointing to the root of the oadp-operator repository
- Check that the repository has the `bundle/manifests` directory

**"No parameter differences found"**
- Verify you have multiple version directories in `/var/tmp/OADP`
- Check that the CRD files were copied correctly
- Try running with `--show-additions` to see if there are only additions

**"Files with changes: 0"**
- This might indicate identical files across versions
- Verify you're comparing different versions of OADP

**"pathspec 'oadp-1.x' did not match any file(s)"**
- The repository might use different branch names
- Run: `python3 setup_oadp_analysis_enhanced.py --troubleshoot --repo-path /path/to/oadp-operator`
- This will show available branches and what the script is looking for
- Make sure you're using the correct OADP repository with oadp-1.3, oadp-1.4, oadp-1.5 branches

## 🔧 Troubleshooting Commands

```bash
# Check what branches are available in your repository
python3 setup_oadp_analysis_enhanced.py --troubleshoot --repo-path /path/to/oadp-operator

# Get help with enhanced setup
python3 setup_oadp_analysis_enhanced.py --help
```