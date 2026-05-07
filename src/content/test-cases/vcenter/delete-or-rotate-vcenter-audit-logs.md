# Delete or Rotate vCenter Audit Logs

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1070.002
- **Tactic:** Defense Evasion

## Description
With root on the VCSA, the attacker manually rotates or deletes vCenter log files in /var/log/vmware/vpxd/ and /var/log/vmware/sso/ to remove forensic evidence. Often combined with stopping/restarting vmware-vpxd or vmware-stsd to flush log buffers.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra

## Log Sources
- Auth Logs (/var/log/auth.log)
- Shell History (/home/<user>/.bash_history)
- systemd Journal (journalctl)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944

## Author
Leonidas Tsaousis (@laripping)
