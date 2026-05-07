# Extract vpxuser Service Account Credentials from vCenter

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1555
- **Tactic:** Credential Access

## Description
vpxuser is the service account vCenter creates on each managed ESXi host with full root rights, exempt from lockdown mode. With root on the VCSA, an attacker decrypts vpxuser passwords stored in the vCenter database (e.g. via vCenter_dumpVPXUserPasswords.py), granting direct admin access to every connected ESXi host while bypassing vCenter logging.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- Auth Logs (/var/log/auth.log)
- Shell History (/home/<user>/.bash_history)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/

## Author
Leonidas Tsaousis (@laripping)
