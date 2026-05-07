# Install Reverse-Tunnel Tool on VCSA

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1219
- **Tactic:** Command and Control

## Description
With root on the VCSA, the attacker installs a remote-access / tunneling tool (Mandiant documented Teleport specifically for UNC3944) configured to dial out to attacker-controlled infrastructure, providing a persistent encrypted reverse-tunnel C2 channel that bypasses inbound firewall rules.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- Auth Logs (/var/log/auth.log)
- systemd Journal (journalctl)
- cron Logs (/var/log/cron)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
