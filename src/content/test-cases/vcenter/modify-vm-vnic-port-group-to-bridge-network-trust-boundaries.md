# Modify VM vNIC Port Group to Bridge Network Trust Boundaries

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1599.001
- **Tactic:** Lateral Movement

## Description
Adversaries with the vCenter privilege "Virtual Machine > Configuration > Modify device settings" (granted by VM Admin or any custom role with disk/NIC edit rights) reconfigure a VM's virtual NIC to attach to a port group on a different VLAN, effectively performing a hypervisor-mediated VLAN hop that bypasses physical network segmentation and any north-south firewall sitting between segments. Common abuse patterns include: (a) attaching a compromised DMZ VM's vNIC to the management VLAN to reach vCenter/ESXi from "outside," (b) attaching an attacker-staged VM to a Tier 0 segment (e.g. AD DC subnet) to scrape credentials or attack DCs at Layer 2, and (c) bridging a single rogue VM across two trust zones via dual vNICs (echoing UNC5221/NERVE rogue-VM dual-NIC pattern). Because the change is a routine vSphere operation, it generates only a benign-looking VmReconfiguredEvent in vpxd.log unless detection is specifically tuned to network-label changes. Test (from a privileged vSphere Client session): right-click a non-production test VM, Edit Settings, change the Network adapter port group from its current VLAN to a different one (use a non-sensitive lab port group, e.g. an isolated test VLAN), apply, verify reachability changed, then revert. Distinct from "Create Rogue VM via vCenter UI" because here the VM already exists - the attacker is repurposing connectivity, not provisioning a new asset.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- HOSTD Logs (/var/log/hostd.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/vsphere-active-directory-integration-risks

## Author
Leonidas Tsaousis (@laripping)
