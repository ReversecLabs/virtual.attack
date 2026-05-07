# Falsify VIB XML Descriptor Acceptance Level

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1036.005
- **Tactic:** Defense Evasion

## Description
Distinct from changing the host-wide acceptance level (T1562.010), this technique tampers with an individual VIB's XML descriptor file - editing the <acceptance-level> field from "community" to "partner" - so that subsequent listings via `esxcli software vib list` report the higher (false) acceptance level. The signature file is left empty/unmatched, which means `esxcli software vib signature verify` still flags the discrepancy ("Signature Not Available: Host may have been upgraded from an older ESXi version"), but operators rely on defenders not running this verification check. Test (lab only): take a benign CommunitySupported VIB, edit its descriptor.xml to claim "partner" acceptance, repackage, install with --force, and verify (a) `vib list` reports "Partner" and (b) `vib signature verify` reports unsigned.

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- ESXi Profile XML (/var/db/esximg/profile)
- esxupdate Logs (/var/log/esxupdate.log)
- Auth Logs (/var/log/auth.log)

## References
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence
- https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-detection-hardening

## Author
Leonidas Tsaousis (@laripping)
