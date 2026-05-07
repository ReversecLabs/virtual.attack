# Download VMDK from Datastore via vCenter UI

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1567
- **Tactic:** Exfiltration

## Description
Adversaries with the vCenter privileges "Datastore > Browse datastore" and "Datastore > Low level file operations" can use the vSphere Client's Datastore Browser to download virtual disk files (.vmdk) from a datastore directly to their workstation. The disk can then be mounted offline for e.g. extraction of NTDS.dit, registry hives, password vaults, source code, or other on-disk secrets - bypassing all in-guest controls (EDR, FDE-when-sealed-to-TPM, DLP). In detail, vCenter exposes datastore files over HTTPS at https://<vcenter>/folder/<vm-dir>/<file>?dcPath=<datacenter>&dsName=<datastore> - the Datastore Browser is a UI wrapper around this URL family. Pre-condition: target VM must be powered off (active .vmdk files are locked - a powered-on VM produces a "file is locked" error on download). Two file types matter: the descriptor .vmdk (~1 KB text file pointing to the data) and the -flat.vmdk (the actual disk content, sized to the VM disk). The flat is what attackers actually want; the descriptor alone is useless. Test (lab only): power off a small non-prod test VM, vSphere Client -> Storage -> select datastore -> Files tab -> navigate to the VM directory -> right-click <vm>-flat.vmdk -> Download.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- vCenter rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log)
- ESXi rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log on the ESXi host backing the datastore)
- HOSTD Logs (/var/log/hostd.log on the ESXi host)

## References
- https://knowledge.broadcom.com/external/article/301563/download-files-from-vcenter-datastore-us.html
- https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-182EEDD3-299B-44FA-BFA9-F2732220C37F.html

## Author
Leonidas Tsaousis (@laripping)
