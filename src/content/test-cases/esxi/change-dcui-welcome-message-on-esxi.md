# Change DCUI Welcome Message on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1491.001
- **Tactic:** Impact

## Description
Adversaries modify the welcome message shown on the ESXi Direct Console User Interface (DCUI) - the screen visible at the host's physical/iLO/iDRAC console. Used as a "calling card" by ransomware operators or to display a defacement notice on hypervisor consoles. Test (from a privileged ESXi shell session): `esxcli system welcomemsg set --message="<defacement text>"`. Verify with `esxcli system welcomemsg get`.

## Threat Actors
_None_

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.md

## Author
AlbinoGazelle (Atomic Red Team)
