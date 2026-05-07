# Execute Guest Commands via vmtoolsd Channel

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1059.003
- **Tactic:** Execution

## Description
Adversaries with shell access on an ESXi host abuse the legitimate VMware Tools guest-operations channel to run commands inside guest VMs without valid in-guest credentials. Commands appear inside the guest as child processes of vmtoolsd.exe (Windows) or vmtoolsd (Linux), bypassing in-guest EDR attribution and authentication. Per Mandiant, UNC3886 used a Python wrapper (e.g. `python e.py 127.0.0.1 vpxuser <password> <target_vm> "cmd.exe /c <command>"`) called from their hypervisor-resident backdoor to dispatch commands via this channel. Test (lab only): from a privileged ESXi shell, use the VIX/govmomi guest-ops API or PowerCLI Invoke-VMScript to execute a benign command in a guest VM and confirm the resulting process tree shows vmtoolsd as the parent. Distinct from "Exploit CVE-2023-20867" because this technique works against fully-patched VMware Tools when the operator already has host root.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- Per-VM Logs (/vmfs/volumes/<datastore>/<vm>/vmware.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening

## Author
Leonidas Tsaousis (@laripping)
