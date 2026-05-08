# Change vCenter SSO Administrator Password

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1098
- **Tactic:** Persistence

## Description
With sufficient vCenter access, an attacker can change the `administrator@vsphere.local` SSO domain password to lock out legitimate administrators and maintain exclusive control. Scattered Spider was documented changing vCenter credentials as part of ransomware operations.

1. Connect to the VCSA via SSH with root privileges
2. Start the SSO admin shell: `shell`
3. Change the SSO administrator password using the directory CLI:
   `/usr/lib/vmware-vmafd/bin/dir-cli password change --account administrator --old-password <old> --new-password <new>`
4. Alternatively, change it via the vSphere Web Client: **Administration > Single Sign On > Users and Groups > Users**, select `administrator`, then **Edit**

## Threat Actors
- UNC3944
- Scattered Spider

## Log Sources
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944
- https://www.securityweek.com/scattered-spider-targeting-vmware-vsphere-environments/
- https://knowledge.broadcom.com/external/article/326186/resetting-forgotten-vcenter-sso-password.html

## Author
Leonidas Tsaousis (@laripping)
