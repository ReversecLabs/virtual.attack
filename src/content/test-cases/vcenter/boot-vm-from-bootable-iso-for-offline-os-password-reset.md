# Boot VM from Bootable ISO for Offline OS Password Reset

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
The attacker mounts a bootable utility ISO (e.g. PCUnlocker, Lazesoft, Hiren's BootCD) to a powered-off target VM via vCenter, modifies VM boot order to boot from CD-ROM, and uses the live environment to reset the local administrator password on the guest OS, bypassing domain authentication. UNC3944 documented this against domain controllers and admin workstations.

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
