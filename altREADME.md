# Virtual//Attack

*Attack techniques for Threat Emulation in VMware environments*

> Browse them at https://...

## The problem

Detection capability in VMware/VCF/vSphere estates remains low or inexistent.  

Despite the criticality of the virtualisation environment, organisations do not proactively invest in the resilience against threats 

## How this project helps

To empower security teams to emulate threats and build detections, this repo provides 70+ reproducible attack test cases covering vCenter, ESXi, and beyond. Including log sources expected, mapped to the MITRE ATT&CK framework.  

## The techniques



A comprehensive collection of 70+ individual atacker actions that can be simulated against VCF environments in Purple Team exercises.

- 🔬**Real-world Threats**: The majority of test cases has been extracted from threat intelligence reports detailing real-world vSphere incidents. *Additionally, a few more test cases have been added that have not yet been documented, but can be executed practively to assess controls and tailor detections.* 

- 🗺️**Beyond vSphere**: This collection includes not only the usual vCenter and ESXi attacks, but also components of security significance in the [VCF](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) ecosystem such as the [SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/sddc-manager.html), as well as crucial integrations like Active Directory.  

- 🔴**Reproducible**: For the red teamer, detailed insructions and links to useful origin sources to ensure each test case can be carried out reproducibly.  

- 🔵**Defender-friendly**: For the blue teamer, each test case also comes with the Log Sources where evidence is expected to be recorded, aiding the triage process.  


**What Isn't Included**

Various CVEs are actively discovered in VMware products across the different versions. Even where publicly available PoCs exist, this project will not include CVE exploits, as these can be addressed via patching. 

Known-malware samples such as BEEFLUSH, VIRTUALPITA are also not included for safety. Instead, the focus is on the techniques, with aim aim to build resilience at higher levels of the [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html). 



Live at ...
Or develop locally 

# Contribute new techniques 