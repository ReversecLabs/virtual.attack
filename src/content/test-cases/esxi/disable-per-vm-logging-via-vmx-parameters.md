# Disable Per-VM Logging via .vmx Parameters

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562.006
- **Tactic:** Defense Evasion

## Description
With reconfigure-VM rights on vCenter or direct .vmx access on ESXi, the attacker sets `logging = "FALSE"` in the VM's .vmx file to disable per-VM vmware.log generation, eliminating that forensic artefact. Frequently observed alongside `isolation.tools.copy.disable = "FALSE"` to enable clipboard exfiltration.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
