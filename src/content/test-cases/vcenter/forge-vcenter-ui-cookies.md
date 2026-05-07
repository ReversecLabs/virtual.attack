# Forge vCenter UI Cookies

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1606.002
- **Tactic:** Credential Access

## Description
With prior root access on the VCSA, the attacker extracts the vmdir database (/storage/db/vmware-vmdir/data.mdb) and parses out the IdP signing cert, IdP private key and VMCA root cert. Using these (e.g. Horizon3 vcenter_saml_login.py / Sygnia-observed vCenter_GenerateLoginCookie.py / Metasploit auxiliary/admin/vmware/vcenter_forge_saml_token), the attacker mints a self-signed SAML assertion for Administrator@vsphere.local and exchanges it via the SSO websso endpoint for a valid VSPHERE-UI-JSESSIONID cookie. Browsing to https://<vcsa>/ui with the cookie yields full Admin access without password or MFA. Documented in-the-wild by Sygnia for Fire Ant/UNC3886.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)
- WebSSO Logs (/var/log/vmware/sso/websso.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://horizon3.ai/attack-research/attack-blogs/compromising-vcenter-via-saml-certificates/

## Author
Atomic Red Team
