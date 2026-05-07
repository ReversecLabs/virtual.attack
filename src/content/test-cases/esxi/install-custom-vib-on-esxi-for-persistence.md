# Install Custom VIB on ESXi for Persistence

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1554
- **Tactic:** Persistence

## Description
With root on an ESXi host, the attacker installs a custom VMware Installation Bundle (VIB) to deploy persistent backdoors (e.g. VIRTUALPITA, autobackup.bin). Using `esxcli software vib install --no-sig-check --force` and modified VIB acceptance levels, even unsigned VIBs persist across reboots. Test: build a benign VIB with a PartnerSupported acceptance level and install with --force; confirm the implant survives a reboot.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- esxupdate Logs (/var/log/esxupdate.log)
- ESXi Profile XML (/var/db/esximg/profile)
- Auth Logs (/var/log/auth.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening
- https://win64.li/posts/ESXi-Hypervisor-level-Attacks-and-Techniques/
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1129/T1129.md

## Author
Atomic Red Team
