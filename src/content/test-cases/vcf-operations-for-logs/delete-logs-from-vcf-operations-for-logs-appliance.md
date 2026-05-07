# Delete Logs from VCF Operations for Logs Appliance

## Component
**VCF Operations for Logs**

## MITRE ATT&CK
- **ID:** T1070.002
- **Tactic:** Defense Evasion

## Description
VCF Operations for Logs (formerly vRealize Log Insight / Aria Operations for Logs) is the centralized log aggregation appliance in the VCF stack, ingesting syslog and CFAPI events from vCenter, ESXi, SDDC Manager, NSX, and other components. The appliance itself is Photon OS-based and writes its own operational logs - admin authentication, config changes, query history, ingestion errors, internal service activity - to /storage/var/loginsight/*.log (and additional locations under /var/log/loginsight/, including upgrade.log). Adversaries with root SSH/console access on the appliance delete these logs to remove evidence of their activity on the appliance itself or other cmponents, by tampering/removing files under /storage/var/loginsight/ and /storage/core/loginsight/cidata/store/ respectively.

## Threat Actors
_None_

## Log Sources
- Appliance Auth Logs (/var/log/auth.log on the appliance)
- Appliance audit Logs (/var/log/audit/audit.log if auditd configured)
- systemd Journal (journalctl on the appliance)
- Bash History (/root/.bash_history if not also cleared)
- SIEM copies

## References
- https://knowledge.broadcom.com/external/article/315959/aria-operations-for-logs-formerly-vreali.html

## Author
Leonidas Tsaousis (@laripping)
