# Enabling VCSA SSH via VAMI

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1021.004
- **Tactic:** Lateral Movement

## Description
Attacker authenticates to the VCSA Appliance Management Interface (VAMI) on TCP/5480 with root or a privileged local account, then under Access settings toggles 'SSH login' and 'bash shell' to enabled. This grants interactive shell access via SSH/22 - the foothold BRICKSTORM operators use to install the implant at /opt/vmware/sbin/vami-httpd and read /storage/db/vmware-vmdir/data.mdb.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- VAMI Application Management Logs (/var/log/vmware/applmgmt/applmgmt.log)
- VAMI Logs (/var/log/vmware/applmgmt/vami.log)
- Auth Logs (/var/log/auth.log)
- systemd Journal (journalctl)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

## Author
Leonidas Tsaousis (@laripping)
