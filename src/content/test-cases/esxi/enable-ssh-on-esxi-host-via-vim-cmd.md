# Enable SSH on ESXi Host via vim-cmd

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1021.004
- **Tactic:** Lateral Movement

## Description
Adversaries with shell access on an ESXi host enable the SSH service directly via vim-cmd, bypassing vCenter entirely. Test (from a privileged ESXi shell session): `vim-cmd hostsvc/enable_ssh; vim-cmd hostsvc/start_ssh`. Disable cleanup: `vim-cmd hostsvc/disable_ssh; vim-cmd hostsvc/stop_ssh`. Distinct from PowerCLI / vCenter variants because no vpxd.log entry is produced - the action is local to the host.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- Abyss Locker

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- Auth Logs (/var/log/auth.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.004/T1021.004.md
- https://www.sygnia.co/blog/abyss-locker-ransomware-targeting-esxi/

## Author
AlbinoGazelle (Atomic Red Team)
