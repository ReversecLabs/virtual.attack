# Interact with ESXi over vSphere Web Services (SOAP) API

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1106
- **Tactic:** Execution

## Description
Attacker interacts directly with the vSphere Web Services API at https://<esxi>/sdk - bypassing vCenter and the ESXi Host Client UI - typically via PowerCLI, pyvmomi or govmomi using local ESXi credentials (often root or vpxuser harvested from a compromised vCenter). Direct SOAP calls allow VM enumeration, snapshot, disk attach/detach, rogue VM registration and guest operations while leaving fewer artifacts in vCenter logs. Sygnia documents Fire Ant/UNC3886 extracting vpxuser creds and using PowerCLI to interact with guest VMs (CVE-2023-20867).

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- vObserver Logs (/var/log/vobd.log)
- Auth Logs (/var/log/auth.log)
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)

## References
- https://detect.fyi/vmware-esxi-logging-detection-opportunities-4fb56411ec21
- https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/

## Author
Leonidas Tsaousis (@laripping)
