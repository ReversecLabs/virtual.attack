# Disable execInstalledOnly on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562.001
- **Tactic:** Defense Evasion

## Description
`execInstalledOnly` is an ESXi kernel security parameter that restricts execution to binaries installed via signed VIB packages. Disabling it allows attackers to execute arbitrary code, such as ransomware, on the ESXi host.

1. Connect to the ESXi host via SSH or ESXi Shell with root privileges
2. Check the current value: `esxcli system settings advanced list -o /User/execInstalledOnly`
3. Disable at runtime (no reboot required): `esxcli system settings advanced set -o /User/execInstalledOnly -i 0`
4. Alternatively, to persist across reboots: `esxcli system settings kernel set -s execInstalledOnly -v FALSE`

## Threat Actors
- UNC3944
- Fire Ant

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)
- VMkernel Logs (/var/log/vmkernel.log)
- vCenter Server Event Logs (warning alert triggered when execInstalledOnly is disabled)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.truesec.com/hub/blog/esxi-8-0-and-execinstalledonly-the-good-the-bad-and-the-ugly
- https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security/securing-esxi-hosts/deactivate-the-execinstalledonly-advanced-configuration-runtime-option.html

## Author
Leonidas Tsaousis (@laripping)
