# VM Encryption using openssl

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1486
- **Tactic:** Impact

## Description
Low-effort / low-sophistication ransomware variants utilised the native openssl utility to encrypt VMDKs using AES

## Threat Actors
- fcker

## Log Sources
- HOSTD Logs (/var/log/hostd.log)

## References
- https://news.sophos.com/en-us/2021/10/05/python-ransomware-script-targets-esxi-server-for-encryption/

## Author
Leonidas Tsaousis (@laripping)
