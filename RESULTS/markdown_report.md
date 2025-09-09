# OADP CRD Version Comparison Report

**Comparing versions:** 1.3, 1.4, 1.5
**Common files found:** 18
**Note:** Hiding additions by default. Use --show-additions to see added parameters.

## 📄 File: `oadp-operator.clusterserviceversion.yaml`

### 1.3→1.4

- ❌ **REMOVED**: `metadata.annotations.createdAt`
  - Line 156 in version 1.3
- ❌ **REMOVED**: `metadata.annotations.olm.properties`
  - Line 169 in version 1.3
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[1].value`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[2].value`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[3].value`

### 1.4→1.5

- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].resourceNames`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[1].rules[4].nonResourceURLs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[1].rules[5].resourceNames`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[13].name`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[13].value`

### 1.3→1.5

- ❌ **REMOVED**: `metadata.annotations.olm.properties`
  - Line 169 in version 1.3
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[10].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[11].statusDescriptors[7].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[12].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[13].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[14].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[0].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[1].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[7].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[6].statusDescriptors[8].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[8].statusDescriptors[2].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[3].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[4].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[5].path`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].description`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].displayName`
- ❌ **REMOVED**: `spec.customresourcedefinitions.owned[9].statusDescriptors[6].path`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].resourceNames`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[10].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[11].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[12].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[13].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[14].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[15].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[16].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].apiGroups`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].resources`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[0].rules[17].verbs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[1].rules[4].nonResourceURLs`
- ❌ **REMOVED**: `spec.install.spec.clusterPermissions[1].rules[5].resourceNames`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[1].value`
- ❌ **REMOVED**: `spec.install.spec.deployments[0].spec.template.spec.containers[0].env[2].value`


## 📄 File: `oadp.openshift.io_dataprotectionapplications.yaml`

### 1.3→1.4

- ❌ **REMOVED**: `spec.versions[0].schema.openAPIV3Schema.properties.spec.properties.backupLocations.items.properties.velero.properties.credential.properties.name.default`
- ❌ **REMOVED**: `spec.versions[0].schema.openAPIV3Schema.properties.spec.properties.snapshotLocations.items.properties.velero.properties.credential.properties.name.default`


## 📊 Summary

- **Files analyzed:** 18
- **Files with changes:** 2
- **Parameters removed (shown):** 292
- ❌ **Parameters removed:** 292
- 💡 **Parameters added (hidden):** 2472 - use --show-additions to view

## 📄 File Analysis Breakdown

| File Name | Added | Removed | Total |
|-----------|--------|---------|-------|
| `oadp.openshift.io_dataprotectionapplications.yaml` | 2014 | 2 | 2016 |
| `oadp-operator.clusterserviceversion.yaml` | 438 | 290 | 728 |
| `oadp.openshift.io_cloudstorages.yaml` | 18 | 0 | 18 |
| `openshift-adp-controller-manager-metrics-service_v1_service.yaml` | 2 | 0 | 2 |
| `openshift-adp-metrics-reader_rbac.authorization.k8s.io_v1_clusterrole.yaml` | 0 | 0 | 0 |
| `velero.io_backuprepositories.yaml` | 0 | 0 | 0 |
| `velero.io_backups.yaml` | 0 | 0 | 0 |
| `velero.io_backupstoragelocations.yaml` | 0 | 0 | 0 |
| `velero.io_datadownloads.yaml` | 0 | 0 | 0 |
| `velero.io_datauploads.yaml` | 0 | 0 | 0 |
| `velero.io_deletebackuprequests.yaml` | 0 | 0 | 0 |
| `velero.io_downloadrequests.yaml` | 0 | 0 | 0 |
| `velero.io_podvolumebackups.yaml` | 0 | 0 | 0 |
| `velero.io_podvolumerestores.yaml` | 0 | 0 | 0 |
| `velero.io_restores.yaml` | 0 | 0 | 0 |
| `velero.io_schedules.yaml` | 0 | 0 | 0 |
| `velero.io_serverstatusrequests.yaml` | 0 | 0 | 0 |
| `velero.io_volumesnapshotlocations.yaml` | 0 | 0 | 0 |
| **TOTAL** | **2472** | **292** | **2764** |

## 📈 Change Distribution

- **Files with only additions:** 2
- **Files with only removals:** 0
- **Files with both changes:** 2
- **Files unchanged:** 14