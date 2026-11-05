# Grant Perfcharts Passwordless Sudo

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1548.003
- **Tactic:** Privilege Escalation

## Description
With root access on the VCSA, an attacker can grant an existing user unrestricted passwordless sudo by adding the appropriate rules under `/etc/sudoers.d/`. 

QUIRSO observed a suspected Chinese-nexus APT creating a new sudoers rule file via cron command execution, which granted the `perfcharts` service account related to the Tomcat web application, the ability to execute arbitrary commands as sudo without providing password. This was subsequently used to launch JSP web shell with highest privileges.

This technique can be implemented with the following commands, executed from a root shell: 
```bash
echo 'perfcharts ALL=(root) NOPASSWD: ALL' > /etc/sudoers.d/vmware-perf
echo 'Defaults:perfcharts !requiretty' >> /etc/sudoers.d/vmware-perf
chmod 440 /etc/sudoers.d/vmware-perf
```

Note: While the threat actor was unnamed in the original research and was refered simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details cen be found in the QUIRSO investigation linked in the References. 

## Threat Actors
- pikpak0066

## Log Sources
- Auth Logs (/var/log/auth.log)
- Audit Logs (/var/log/audit/audit.log)
- systemd Journal (journalctl)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d

## Author
Leonidas Tsaousis (@laripping)
