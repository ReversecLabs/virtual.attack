# Mass Power Off VMs via ESXi Direct Commands

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1529
- **Tactic:** Impact

## Description
Once root is obtained on an ESXi host, attackers rapidly power off all running VMs as a precursor to ransomware encryption or VMDK detachment. Three primary methods are observed: (a) `for i in $(vim-cmd vmsvc/getallvms | awk 'NR>1 {print $1}'); do vim-cmd vmsvc/power.off $i & done` - iterates the inventory and powers off each VM; (b) per-VM `esxcli vm process kill --type=force --world-id=<id>` after enumerating with `esxcli vm process list`; (c) `pkill -f vmx-vthread` to terminate the VMX worker processes for all running VMs (Avoslocker pattern). Distinct from vCenter-mediated power-off because vCenter VPXD logs do not capture this activity.

## Threat Actors
- UNC3944
- Scattered Spider
- Octo Tempest
- 0ktapus
- Muddled Libra
- Avoslocker
- SPRITE SPIDER
- FERAL SPIDER
- CYBORG SPIDER
- PINCHY SPIDER
- VIKING SPIDER

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)
- VMKernel Logs (/var/log/vmkernel.log)

## References
- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1529/T1529.md
- https://lolesxi-project.github.io/LOLESXi/lolesxi/Binaries/vim-cmd/
- https://blogs.vmware.com/security/2022/02/avoslocker-modern-linux-ransomware-threats.html
- https://www.crowdstrike.com/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/
- https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/

## Author
Atomic Red Team
