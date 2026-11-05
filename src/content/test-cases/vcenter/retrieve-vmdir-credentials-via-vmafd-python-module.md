# Retrieve vmdir Credentials via vmafd Python Module

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1552.001
- **Tactic:** Credential Access

## Description
VMware Directory Service (VMDir) is the built-in LDAP directory service included in the VMware vCenter Server Appliance (VCSA). With root access on the VCSA, an attacker can retrieve the distinguished name and password of the `vmdir` machine account using the vmafd Python module.

VMware Authentication Framework Daemon (vmafd) provides a Python module that can expose the VCSA machine name, machine password, and SSO domain. By locating the VMware `vmafd` Python module and calling `GetMachineName()`, `GetDomainName()` an attacker can reconstruct the `vmdir` machine account distinguished name (DN). The module also exposes an API to retrieve the machine account password `GetMachinePassword()`.
The recovered credentials were then used to bind to the local `vmdir` LDAP service and create SSO administrators.

QUIRSO observed this method as a fallback when the actor could not recover the `vmdir` registry values with `lwregshell`. The recovered script operated as follows: 

```python
import sys; sys.path.insert(0,'$VP')    #vmafd located previously in the filesystem
try:
    import vmafd; c=vmafd.client('localhost')
    print(c.GetMachineName()); print(c.GetMachinePassword()); print(c.GetDomainName())
except Exception:
    sys.exit(1)
```

NOTE: While the threat actor was unnamed in the original research and was referred to simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details can be found in the QUIRSO investigation linked in the References.

## Threat Actors
- pikpak0066

## Log Sources
- Audit Logs (/var/log/audit/audit.log)
- Auth Logs (/var/log/auth.log)
- systemd Journal (journalctl)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d
- https://github.com/QUIRSO/QTR/blob/main/2026-08/Global%20Exploitation%20of%20CVE-2026-59310%20by%20Suspected%20Chinese-Nexus%20APT%20and%20Related%20CVE-2026-59309%20Activity/scripts/vmware-perf-upd.sh

## Author
Leonidas Tsaousis (@laripping)
