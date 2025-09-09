[1m[96mOADP CRD Version Comparison Report[0m
[96m============================================================[0m
Comparing versions: 1.3, 1.4, 1.5
Common files found: 18
[93mNote: Hiding additions by default. Use --show-additions to see added parameters.[0m

[1m[93m📄 File: oadp-operator.clusterserviceversion.yaml[0m
[93m--------------------------------------------------[0m
[1m  1.3→1.4:[0m
    [91m❌[0m [91mREMOVED[0m: metadata.annotations.createdAt
      [94mLine 156[0m in version 1.3
    [91m❌[0m [91mREMOVED[0m: metadata.annotations.olm.properties
      [94mLine 169[0m in version 1.3
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[1].value
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[2].value
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[3].value

[1m  1.4→1.5:[0m
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].resourceNames
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[1].rules[4].nonResourceURLs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[1].rules[5].resourceNames
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[13].name
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[13].value

[1m  1.3→1.5:[0m
    [91m❌[0m [91mREMOVED[0m: metadata.annotations.olm.properties
      [94mLine 169[0m in version 1.3
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[10].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[11].statusDescriptors[7].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[12].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[13].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[14].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[0].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[1].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[7].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[6].statusDescriptors[8].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[8].statusDescriptors[2].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[3].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[4].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[5].path
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].description
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].displayName
    [91m❌[0m [91mREMOVED[0m: spec.customresourcedefinitions.owned[9].statusDescriptors[6].path
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].resourceNames
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[10].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[11].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[12].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[13].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[14].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[15].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[16].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].apiGroups
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].resources
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[0].rules[17].verbs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[1].rules[4].nonResourceURLs
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.clusterPermissions[1].rules[5].resourceNames
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[1].value
    [91m❌[0m [91mREMOVED[0m: spec.install.spec.deployments[0].spec.template.spec.containers[0].env[2].value


[1m[93m📄 File: oadp.openshift.io_dataprotectionapplications.yaml[0m
[93m--------------------------------------------------[0m
[1m  1.3→1.4:[0m
    [91m❌[0m [91mREMOVED[0m: spec.versions[0].schema.openAPIV3Schema.properties.spec.properties.backupLocations.items.properties.velero.properties.credential.properties.name.default
    [91m❌[0m [91mREMOVED[0m: spec.versions[0].schema.openAPIV3Schema.properties.spec.properties.snapshotLocations.items.properties.velero.properties.credential.properties.name.default


[1m[95m📊 Summary[0m
[95m============================================================[0m
Files analyzed: 18
Files with changes: 2
Parameters removed (shown): 292
[91m❌ Parameters removed: 292[0m
[93m💡 Parameters added (hidden): 2472 - use --show-additions to view[0m

[1m[96m📄 File Analysis Breakdown[0m
[96m============================================================[0m
File Name                                          Added    Removed  Total   
-------------------------------------------------- -------- -------- --------
oadp.openshift.io_dataprotectionapplications.yaml  [92m2014    [0m [91m2       [0m [93m2016    [0m
oadp-operator.clusterserviceversion.yaml           [92m438     [0m [91m290     [0m [93m728     [0m
oadp.openshift.io_cloudstorages.yaml               [92m18      [0m [97m0       [0m [93m18      [0m
openshift-adp-controller-manager-metrics-servic... [92m2       [0m [97m0       [0m [93m2       [0m
openshift-adp-metrics-reader_rbac.authorization... [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_backuprepositories.yaml                  [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_backups.yaml                             [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_backupstoragelocations.yaml              [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_datadownloads.yaml                       [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_datauploads.yaml                         [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_deletebackuprequests.yaml                [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_downloadrequests.yaml                    [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_podvolumebackups.yaml                    [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_podvolumerestores.yaml                   [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_restores.yaml                            [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_schedules.yaml                           [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_serverstatusrequests.yaml                [97m0       [0m [97m0       [0m [97m0       [0m
velero.io_volumesnapshotlocations.yaml             [97m0       [0m [97m0       [0m [97m0       [0m
-------------------------------------------------- -------- -------- --------
TOTAL                                              [92m2472    [0m [91m292     [0m [93m2764    [0m

[1m📈 Change Distribution:[0m
  Files with only additions: [92m2[0m
  Files with only removals: [91m0[0m
  Files with both changes: [93m2[0m
  Files unchanged: [97m14[0m
