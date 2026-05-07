# Create Hidden Rogue VM on ESXi via Direct vmx Invocation

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1564.006
- **Tactic:** Defense Evasion

## Description
Adversaries with root on an ESXi host create a rogue VM by directly invoking the vmx binary against a hand-crafted .vmx descriptor on a datastore (e.g. `/bin/vmx -x /vmfs/volumes/<datastore>/<vm>/<vm>.vmx &`), rather than registering the VM through `vim-cmd vmsvc/registervm`. Because the VM never enters the host inventory, it is hidden from vCenter UI/API and from `vim-cmd vmsvc/getallvms` output. Persistence is added by appending the same vmx invocation to `/etc/rc.local.d/local.sh`, ensuring the rogue VM restarts on host reboot. Distinct from "Create New VM on ESXi" which uses inventory-visible registration.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- syslog (/var/log/syslog)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.md
- https://vninja.net/2024/05/06/rogue-vms-on-esxi/
- https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b

## Author
Atomic Red Team
