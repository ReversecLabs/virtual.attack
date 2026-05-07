# Add User to BashShellAdministrators SSO Group

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
Adding a user to the SystemConfiguration.BashShellAdministrators SSO group grants the ability to obtain a Bash shell on the VCSA via SSH, even without any vSphere admin role. Mandiant documented BRICKSTORM operators using this technique to elevate from SSO-level access to root-equivalent shell access on the VCSA, then deleting the group membership after implant install.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign
- https://www.cisa.gov/news-events/analysis-reports/ar25-338a

## Author
Leonidas Tsaousis (@laripping)
