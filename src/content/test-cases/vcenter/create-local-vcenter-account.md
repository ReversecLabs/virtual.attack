# Create Local vCenter Account

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1136.001
- **Tactic:** Persistence

## Description
With privileged SSO access (typically VSPHERE.LOCAL\Administrator), the attacker creates a new local account in the vsphere.local SSO domain and adds it to SystemConfiguration.BashShellAdministrators - granting the ability to obtain a Bash shell on the VCSA via SSH. Per Mandiant, BRICKSTORM operators delete the account after the implant is installed, leaving the binary on disk for persistence. Test: create bs-test@vsphere.local, add to BashShellAdministrators, SSH to VCSA, drop a benign marker file, then delete the account.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign

## Author
Leonidas Tsaousis (@laripping)
