# Uninstall VMware vSphere HA Fault Domain Manager (FDM)

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1562.001
- **Tactic:** Defense Evasion

## Description
Adversaries preparing for ESXi-level encryption proactively disable or uninstall the VMware vSphere High-Availability Fault Domain Manager (FDM) agent on managed ESXi hosts. FDM normally restarts failed VMs automatically, which would interrupt encryption by re-locking VM files. Disabling vSphere HA at the cluster level via vCenter, or uninstalling the FDM VIB on each host (`esxcli software vib remove --vibname=vmware-fdm`), removes this defense. Test (lab only): from a privileged ESXi shell session, `esxcli software vib list | grep fdm` to confirm FDM presence, then `esxcli software vib remove --vibname=vmware-fdm`; verify VM auto-restart no longer occurs. Documented as a SPRITE SPIDER pre-encryption action.

## Threat Actors
- SPRITE SPIDER

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- Auth Logs (/var/log/auth.log)
- esxupdate Logs (/var/log/esxupdate.log)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/

## Author
Leonidas Tsaousis (@laripping)
