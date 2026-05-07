# Modify SDDC Manager user privileges

## Component
**SDDC Manager**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Privilege Escalation

## Description
A user can be granted SDDC ADMIN privileges on the SDDC Manager UI, allowing vCenter admin access

## Threat Actors
_None_

## Log Sources
- SDDC Manager UI Logs (/var/log/vmware/vcf/sddc-manager-ui-app/sddc-manager-ui-app.log)
- OperationsManager Logs (/var/log/vmware/vcf/operationsmanager/operationsmanager.log)
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)

## References
- https://vxworld.co.uk/2025/11/11/vcf-9-deploying-vcf-identity-broker-part-2-role-assignment-validation-and-troubleshooting/#assign-the-service-roles-in-sddc-manager

## Author
Leonidas Tsaousis (@laripping)
