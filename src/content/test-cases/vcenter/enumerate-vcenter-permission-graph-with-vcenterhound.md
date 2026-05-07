# Enumerate vCenter Permission Graph with vCenterHound

## Component
**vCenter**

## MITRE ATT&CK
- **ID:** T1069
- **Tactic:** Discovery

## Description
vCenterHound (https://github.com/MorDavid/vCenterHound, by MorDavid) is the vSphere analogue of BloodHound/SharpHound for Active Directory. It connects to vCenter via the pyVmomi SOAP SDK using any account with broad read access, enumerates the entire infrastructure object graph (Datacenters, Clusters, ESXi Hosts, Resource Pools, VMs, Datastores, Networks, Folders) and the full permission model (Roles, Privileges, Users, Groups, Permission Assignments with role bindings, Group Memberships), and exports the result as a BloodHound OpenGraph JSON file. Read-only operation - no destructive actions, no configuration changes.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- vCenter rhttpproxy Logs (/var/log/vmware/rhttpproxy/rhttpproxy.log)
- vpxd Profiler Logs (/var/log/vmware/vpxd/vpxd-profiler.log)

## References
- https://github.com/MorDavid/vCenterHound
- https://specterops.io/blog/2025/06/24/bloodhound-opengraph/

## Author
Leonidas Tsaousis (@laripping)
