# Retrieve Credentials for Other VCF Components via Shell

## Component
**SDDC Manager**

## MITRE ATT&CK
- **ID:** T1555
- **Tactic:** Credential Access

## Description
SDDC manager's lookup_password utility can be used to retrieve plain text credentials to other VCF systems

## Threat Actors
_None_

## Log Sources
- Auth Logs (/var/log/auth.log)
- Shell History (/home/<user>/.bash_history)
- OperationsManager Logs (/var/log/vmware/vcf/operationsmanager/operationsmanager.log)

## References
- https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/manage-passwords-admin/look-up-account-credentials-using-the-lookup-password-command-admin.html

## Author
Leonidas Tsaousis (@laripping)
