# Add user to Lockdown Exception Users from vCenter UI

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Defense Evasion

## Description
Stealthier variant of "Disable ESXi Lockdown Mode." 

Rather than turning Lockdown off, the attacker leaves Lockdown enabled and adds their own principal to the per-host Exception Users list. Users on this list retain whatever privileges they have on the host even when Lockdown is in force - so direct SSH/Host Client/DCUI access continues to work for that one principal, while the host still reports "Lockdown: Enabled" to compliance tooling. 

Important precondition: the user must already have admin privileges on the host (locally provisioned or via host-level AD permissions). 

From vCenter UI: select host -> Configure -> System -> Security Profile -> Edit Lockdown Mode -> Exception Users -> Add.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)
- rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log)
- vObserver Logs (/var/log/vobd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://knowledge.broadcom.com/external/article/425190/managing-exception-users-in-esxi-lockdow.html
- https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security/securing-esxi-hosts/customizing-hosts-with-the-security-profile/lockdown-mode.html

## Author
Leonidas Tsaousis (@laripping)
