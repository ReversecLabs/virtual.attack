# Persistence via /etc/rc.local.d/ Startup Script on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1037.004
- **Tactic:** Persistence

## Description
Adversaries plant a startup script under /etc/rc.local.d/ (typically /etc/rc.local.d/local.sh, or attacker-named files such as vmware_local.sh / vmware_rhttpio.sh per Mandiant) that re-launches their backdoor on every host reboot. Because ESXi runs an in-memory filesystem and discards on-disk changes at shutdown, rc.local.d is one of the few durable persistence locations on the hypervisor. The attacker script typically: (a) opens a custom firewall ruleset for backdoor traffic, (b) executes the implant binary, and (c) deletes itself from disk to leave only in-memory artefacts. Test (from a privileged ESXi shell session): `echo "/bin/your_test_binary &" >> /etc/rc.local.d/local.sh; chmod +x /etc/rc.local.d/local.sh; auto-backup.sh` (auto-backup.sh persists the rc.local.d change into the bootbank).

## Threat Actors
- UNC3886
- Fire Ant
- UNC5221
- WARP PANDA

## Log Sources
- ESXi Shell Logs (/var/log/shell.log)
- Auth Logs (/var/log/auth.log)
- syslog (/var/log/syslog)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening
- https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b

## Author
Leonidas Tsaousis (@laripping)
