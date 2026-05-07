# Create New VM on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1564.006
- **Tactic:** Defense Evasion

## Description
Rogue VMs can be created from VMX definition files directly on ESXi hosts using native utilities such as /bin/vmx and vim-cmd

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/

## Author
Leonidas Tsaousis (@laripping)
