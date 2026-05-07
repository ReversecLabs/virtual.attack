# Retrieve Credentials for Other VCF Components via the API

## Component
**SDDC Manager**

## MITRE ATT&CK
- **ID:** T1555
- **Tactic:** Credential Access

## Description
SDDC manager's API can be used to retrieve plain text credentials to other VCF systems
GET /v1/system/credentials/service

## Threat Actors
_None_

## Log Sources
- OperationsManager Logs (/var/log/vmware/vcf/operationsmanager/operationsmanager.log)
- SDDC Manager UI Logs (/var/log/vmware/vcf/sddc-manager-ui-app/sddc-manager-ui-app.log)
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)

## References
- https://knowledge.broadcom.com/external/article/327195/retrieve-the-service-accounts-credential.html

## Author
Leonidas Tsaousis (@laripping)
