# Install Servlet Filter in vCenter Tomcat

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1556.003
- **Tactic:** Credential Access

## Description
Mandiant documented BRICKSTORM operators installing a malicious Java Servlet Filter (BRICKSTEAL) into the Tomcat instance hosting vCenter's web interface. The filter executes on every HTTP request and harvests HTTP Basic credentials from authentication attempts to vCenter, bypassing MFA. The filter is loaded entirely in-memory via a custom dropper, requiring no on-disk modification or restart.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- vSphere UI Tomcat Logs (/var/log/vmware/vsphere-ui/logs/)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign
- https://cloud.google.com/blog/topics/threat-intelligence/vsphere-brickstorm-defender-guide

## Author
Leonidas Tsaousis (@laripping)
