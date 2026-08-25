# Boot VM from Bootable ISO for Offline OS Password Reset

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
Under certain conditions (no secure boot, no disk encryption at rest) an attacker can mount a bootable utility ISO (e.g. PCUnlocker, Lazesoft, Hiren's BootCD) to a powered-off target VM via vCenter, and modify VM boot order to boot from CD-ROM. Then using the live environment, they could reset the local administrator password on the guest OS, bypassing domain authentication. 

## Threat Actors


## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)

## References

## Author
Leonidas Tsaousis (@laripping)
