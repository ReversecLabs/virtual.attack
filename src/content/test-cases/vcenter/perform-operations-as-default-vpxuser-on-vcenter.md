# Perform Operations as Default vpxuser on vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1078.001
- **Tactic:** Defense Evasion

## Description
VPXUSER is a default vCenter service account used internally to manage and connect to ESXi hosts. With access to the VCSA filesystem or to vCenter UI, an attacker authenticates as VPXUSER (or harvests its credential from the vPostgreSQL database) and uses it to perform vCenter operations. Per MITRE's NERVE writeup, UNC5221 used VPXUSER to make seven API calls enumerating mounted and unmounted drives, and to deploy rogue VMs onto ESXi hosts. Test (from vCenter UI), authenticating manually using plaintext credentials.  Test (from a privileged shell on the VCSA): use govmomi/PowerCLI Connect-VIServer and run a benign enumeration call (e.g. Get-Datastore, Get-VM); verify the action is logged under the VPXUSER principal rather than the original admin

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)

## References
- https://medium.com/mitre-engenuity/infiltrating-defenses-abusing-vmware-in-mitres-cyber-intrusion-4ea647b83f5b
- https://medium.com/mitre-engenuity/technical-deep-dive-understanding-the-anatomy-of-a-cyber-intrusion-080bddc679f3

## Author
Leonidas Tsaousis (@laripping)
