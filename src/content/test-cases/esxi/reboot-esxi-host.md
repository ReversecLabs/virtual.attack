# Reboot ESXi Host

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1529
- **Tactic:** Impact

## Description
Rebooting an ESXi host disrupts all running VMs, clears in-memory logs, and installs any persistence applied. Without a remote syslog target configured, all ESXi logs are lost on reboot, eliminating evidence of prior activity. Attackers could perform this with two methods:

1. **ESXi Shell (SSH):**
   ```bash
   esxcli system shutdown reboot --reason "Maintenance"
   ```
   Or using the native shell command:
   ```bash
   reboot
   ```

2. **PowerCLI (remote):**
   ```powershell
   Connect-VIServer -Server <esxi_ip>
   Restart-VMHost -VMHost "<esxi_host>" -Force -Confirm:$false
   ```


## Threat Actors
_None_

## Log Sources
- vmksummary Logs (/var/run/log/vmksummary.log)
- HOSTD Logs (/var/run/log/hostd.log)

## References
- https://attack.mitre.org/techniques/T1529/
- https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/esxcli-concepts-and-examples-8-0/managing-hosts/stopping-and-rebooting-hosts-with-esxcli.html
- https://knowledge.broadcom.com/external/article/317245/determining-why-an-esxi-host-was-powered.html
- https://knowledge.broadcom.com/external/article/306962/location-of-esxi-log-files.html


## Author
Leonidas Tsaousis (@laripping)
