# Impersonate VCF Automation Service Account Against vCenter

## Component
**VCF Automation**

## MITRE ATT&CK
- **ID:** T1078.004
- **Tactic:** Defense Evasion

## Description
VCF Automation (formerly vRealize Automation / Aria Automation) configures each integrated vCenter as a "Cloud Account" using a dedicated service account with vSphere admin-level privileges. 

In the event of compromise of the VCF Automation service account, an attacker could impersonate the principal to hide their identity and possibly perform privileged actions against vCenter abusing the agent's privileges. This activity would demonstrate characteristics irregular to the agent's standardised behaviour.

## Threat Actors
_None_

## Log Sources
- VPXD Logs (/var/log/vmware/vpxd/vpxd.log)
- SSO Audit Events (/var/log/vmware/sso/audit_events.log)

## References
- https://virtualhobbit.com/2020/01/14/setting-the-vra-software-agent-to-run-as-a-different-user/
- https://blog.kimjohansson.se/2025/11/07/vcf9-create-organization-in-vcf-a/

## Author
Leonidas Tsaousis (@laripping)
