# Create VCSA Cron Job for Persistence

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1053.003
- **Tactic:** Persistence

## Description
With root access to the vCenter Server Appliance (VCSA), an attacker creates a cron definition that runs a command at a chosen interval. QUIRSO observed a suspected Chinese-nexus intrusion set use cron files impersonating VMware services, including `vmware-vpxd-stats-*` and `vmware-perf-sync-*`, to re-establish access and execute payloads as root. 

Simulate this by creating `/etc/cron.d/vmware-perf-sync-test` with a root-owned job that appends a timestamp to `/var/tmp/vcsa-cron-test.log` every five minutes, for demonstration. 

Note: While the threat actor was unnamed in the original research and was refered simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details cen be found in the QUIRSO investigation linked in the References. 

## Threat Actors
- pikpak0066

## Log Sources
- cron Logs (/var/log/cron)
- systemd Journal (journalctl)
- Auth Logs (/var/log/auth.log)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d

## Author
Leonidas Tsaousis (@laripping)
