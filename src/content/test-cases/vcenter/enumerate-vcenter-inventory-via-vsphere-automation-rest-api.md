# Enumerate vCenter Inventory via vSphere Automation REST API

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1018
- **Tactic:** Discovery

## Description
An adversary with valid vCenter credentials can use the vSphere Automation API's legacy `/rest` routes to rapidly inventory the managed environment. This can be achieved with the following steps: 
1. Create a session with `POST https://<VCENTER>/rest/com/vmware/cis/session` using HTTP Basic authentication
2. Then, appending the returned session identifier in the `vmware-api-session-id` HTTP header, issue GET requests to the following endpoints `/rest/appliance/system/version`, `/rest/vcenter/datacenter`, `/rest/vcenter/cluster`, `/rest/vcenter/host`, `/rest/vcenter/vm`, `/rest/vcenter/datastore`, `/rest/vcenter/network` etc. 

QUIRSO observed this sequence using the unusual `GoodMoodle-VCFleet/1.0` user agent after suspected exploitation of CVE-2026-59309. 

Note: While the threat actor was unnamed in the original research and was refered simply as a "Chinese-Nexus APT", the GitHub username `pikpak0066` is attached below for test case identification purposes, which was the creator of a repository linked to the incident. More details cen be found in the QUIRSO investigation linked in the References. 

## Threat Actors
- pikpak0066

## Log Sources
- vAPI Endpoint Access Logs (/var/log/vmware/vapi/endpoint/endpoint-access.log)
- vCenter rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log)
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)

## References
- https://medium.com/@quirso_de/global-exploitation-of-cve-2026-59310-by-suspected-chinese-nexus-apt-related-cve-2026-59309-443a79e1466d
- https://developer.broadcom.com/xapis/vsphere-automation-api/latest/vcenter/


## Author
Leonidas Tsaousis (@laripping)