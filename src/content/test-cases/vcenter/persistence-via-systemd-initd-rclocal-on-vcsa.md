# Persistence via systemd / init.d / rc.local on VCSA

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1543.002
- **Tactic:** Persistence

## Description
With root on the VCSA, the attacker plants a persistent service by creating a systemd unit (/etc/systemd/system/<svc>.service), modifying init scripts under /etc/init.d/ or /etc/rc.d/, or appending to /etc/rc.local. Mandiant observed BRICKSTORM persistence in directories such as /etc/sysconfig/ and as /opt/vmware/sbin/vami-httpd masquerading as a legitimate VAMI process.

Safe simulation 
(1) From a privileged shell on the VCSA, build a benign filter class that logs only the request URI and timestamp (no credentials, no network egress) to /tmp/test-filter.log, package as a JAR, and drop into /usr/lib/vmware-vsphere-ui/server/webapps/ui/WEB-INF/lib/. 
(2) Add a corresponding <filter> and <filter-mapping url-pattern="/*"> entry to /usr/lib/vmware-vsphere-ui/server/webapps/ui/WEB-INF/web.xml (back up first).
(3) Reload the vsphere-ui service: `vmon-cli -r vsphere-ui`. 
(4) Browse to https://<vcsa>/ui and verify /tmp/test-filter.log records the request. 
(5) Cleanup: restore original web.xml, remove the JAR, restart vsphere-ui. 
For the in-memory variant (closer to BRICKSTEAL's actual TTP), a Java agent could be used, attached via `jcmd <pid> JVMTI.agent_load` against the vsphere-ui JVM rather than touching disk - this exercises the same detection surface (anomalous JVM thread, no file change) without persistence. Do NOT replicate credential-harvesting logic; the goal is to prove the injection mechanism, not the implant.

## Threat Actors
- UNC5221
- WARP PANDA

## Log Sources
- systemd Journal (journalctl)
- Auth Logs (/var/log/auth.log)
- cron Logs (/var/log/cron)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign
- https://www.cisa.gov/news-events/analysis-reports/ar25-338a

## Author
Leonidas Tsaousis (@laripping)
