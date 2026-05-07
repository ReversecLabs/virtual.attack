# Disable ESXi Syslog Forwarding (vmsyslogd)

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1562.006
- **Tactic:** Defense Evasion

## Description
With root on an ESXi host, the attacker terminates the vmsyslogd process or empties `Syslog.global.logHost` to halt remote SIEM ingestion. Achieved via `esxcli system syslog config set --loghost=` or `kill -9 $(pidof vmsyslogd)`. Sygnia explicitly documents unexpected vmsyslogd termination as a Fire Ant indicator.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- Auth Logs (/var/log/auth.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://www.sygnia.co/blog/fire-ant-a-deep-dive-into-hypervisor-level-espionage/
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening

## Author
Leonidas Tsaousis (@laripping)
