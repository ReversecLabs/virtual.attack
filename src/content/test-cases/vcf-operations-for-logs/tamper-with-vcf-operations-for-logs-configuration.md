# Tamper with VCF Operations for Logs Configuration

## Component
**VCF Operations for Logs**

## MITRE ATT&CK
- **ID:** T1562.006
- **Tactic:** Defense Evasion

## Description
Stealthier alternative to stopping the loginsight service. Rather than dropping ingestion entirely , the adversary edits the appliance configuration to selectively break logging while leaving the service running and reporting healthy. The appliance keeps ingesting at expected volumes from most sources, so SOC dashboards show no anomaly - but specific event types, sources, or alerts that would have flagged the attacker\'s other TTPs are quietly dropped, redirected, or de-indexed. Edit paths: (a) Direct file edit at /usr/lib/loginsight/application/conf/loginsight-config.xml (also referenced as loginsight-config.xml#<seq>) (b) Internal API at https://<log_insight_fqdn>/internal/config - browser-accessible to admin users, applies live without restart, no on-disk change visible until next config dump.

## Threat Actors
_None_

## Log Sources
- loginsight-config.xml file modification time
- Appliance Auth Logs (/var/log/auth.log) for SSH session correlation
- Appliance audit Logs (/var/log/audit/audit.log)

## References
- https://knowledge.broadcom.com/external/article/315959/aria-operations-for-logs-formerly-vreali.html

## Author
Leonidas Tsaousis (@laripping)
