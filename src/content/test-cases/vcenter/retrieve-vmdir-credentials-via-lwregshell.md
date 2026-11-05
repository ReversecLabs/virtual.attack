# Retrieve vmdir Credentials via lwregshell

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1552.001
- **Tactic:** Credential Access

## Description
VMware Directory Service (VMDir) is the built-in LDAP directory service included in the VMware vCenter Server Appliance (VCSA). With root access on the VCSA, an attacker can retrieve the distinguished name and password of the `vmdir` machine account from the Likewise registry.

QUIRSO observed a suspected Chinese-nexus APT querying the `HKEY_THIS_MACHINE\\services\\vmdir` registry location using the `/opt/likewise/bin/lwregshell` utility, with a command such as the following:

```bash
/opt/likewise/bin/lwregshell ls "[HKEY_THIS_MACHINE\Services\vmdir]"
```

The recovered credentials were then used to bind to the local `vmdir` LDAP service and create SSO administrators.

Note: While the threat actor was unnamed in the original research and was referred to simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details can be found in the QUIRSO investigation linked in the References.

## Threat Actors
- pikpak0066

## Log Sources
- Audit Logs (/var/log/audit/audit.log)
- Auth Logs (/var/log/auth.log)
- systemd Journal (journalctl)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d
- https://knowledge.broadcom.com/external/article/312479/vcenter-server-patchupgrade-fails-due-to.html

## Author
Leonidas Tsaousis (@laripping)
