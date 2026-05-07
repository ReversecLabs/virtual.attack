# Modify ESXi System Clock to Defeat Forensic Timelines

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1070.006
- **Tactic:** Defense Evasion

## Description
Adversaries with root on an ESXi host modify the system clock immediately before and after malicious actions (e.g. VIB installation, backdoor execution) so that the resulting log entries carry deceptive timestamps - in Mandiant's case study, attacker logs were backdated to 2013, far outside the actual incident timeline. The clock modification itself, however, is recorded in /var/log/vmkwarning.log as a system-time-change event, providing the anchor that exposes the technique. Test (from a privileged ESXi shell session): `esxcli system time set --hour=10 --year=2013 --day=9 --month=10`, perform a benign action, then restore: `esxcli system time set --year=$(date +%Y) --month=$(date +%m) --day=$(date +%d) --hour=$(date +%H)`.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- VMkernel Warning Logs (/var/log/vmkwarning.log)
- VMKernel Logs (/var/log/vmkernel.log)
- syslog (/var/log/syslog)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence

## Author
Leonidas Tsaousis (@laripping)
