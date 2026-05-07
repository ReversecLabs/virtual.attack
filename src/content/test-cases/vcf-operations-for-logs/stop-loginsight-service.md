# Stop loginsight Service

## Component
**VCF Operations for Logs**

## MITRE ATT&CK
- **ID:** T1562.001
- **Tactic:** Defense Evasion

## Description
Adversaries with root access on the VCF Operations for Logs appliance can stop the core loginsight service to halt log ingestion, query, and alerting across the entire VCF estate for the duration of their operations. Test (lab only, on the appliance): SSH as root, /etc/init.d/loginsight stop(or service loginsight stop, or systemctl stop loginsight on newer Photon-based versions)

## Threat Actors
_None_

## Log Sources
- Appliance Auth Logs (/var/log/auth.log on the appliance)
- systemd Journal (journalctl -u loginsight on the appliance)

## References
- https://knowledge.broadcom.com/external/article/418753/vrealize-log-insight-node-failed-to-star.html

## Author
Leonidas Tsaousis (@laripping)
