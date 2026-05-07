# Virtual//Attack

*Attack techniques for Threat Emulation in VMware environments*


<p align="center">
  <img src="project-logo.png"><br /><br />
  <!-- <img alt="GitHub License" src="https://img.shields.io/github/license/nickvourd/SugarFree?style=social&logo=GitHub&logoColor=purple">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/nickvourd/SugarFree?logoColor=yellow"><br />
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/nickvourd/SugarFree?logoColor=red">
  <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/nickvourd/SugarFree?logoColor=blue">
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/nickvourd/SugarFree?style=social&logo=GitHub&logoColor=green"> -->
</p>




## Overview

A comprehensive collection of 70+ individual atacker actions that can be simulated against VCF environments in Purple Team exercises.

- 🔬**Real-world Threats**: The majority of test cases has been extracted from threat intelligence reports detailing real-world vSphere incidents. *Additionally, a few more test cases have been added that have not yet been documented, but can be executed practively to assess controls and tailor detections.* 

- 🗺️**Beyond vSphere**: This collection includes not only the usual vCenter and ESXi attacks, but also components of security significance in the [VCF](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) ecosystem such as the [SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/sddc-manager.html), as well as crucial integrations like Active Directory.  

- 🔴**Reproducible**: For the red teamer, detailed insructions and links to useful origin sources to ensure each test case can be carried out reproducibly.  

- 🔵**Defender-friendly**: For the blue teamer, each test case also comes with the Log Sources where evidence is expected to be recorded, aiding the triage process.  

## 💻 Browse Them Live

Visit https://thedomain....  for a web UI rendered using Astro, featuring dynamic filtering and a responsive design.

Alternatively, Develop Locally with `npm install && npm run dev`


## How to Use This Project

**🟣VMware Threat Emulations**

This project aims to empower security teams to perform proactive attack emulation exercises against the VMware / VCF / vSphere environments, and build resilience to threats. 

Starting from this repository, purple teams can adjust the test cases to their environment and eventually execute them in threat emulation plans that will drive:
- assessment of preventative controls
- discovery of blind spots
- development of detections
- identification of any design or architectural issues



**🤝Contributing**

As the VCF threat landscape evolves, contributions by the community are welcome and encouraged. 

To add new test cases, simply:

1. Fork the repo
2. Add new `.md` files following the [Test Case file format](#Test-Case-file-format) 
3. Run the verifier script, to ensure new contributions match the expected format 
4. Open a Merge Request


## What Isn't Included

Various CVEs are actively discovered in VMware products across the different versions. Even where publicly available PoCs exist, this project will not include CVE exploits, as these can be addressed via patching. 

Known-malware samples such as BEEFLUSH, VIRTUALPITA are also not included for safety. Instead, the focus is on the techniques, with aim aim to build resilience at higher levels of the [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html). 




## Repository structure
- Test cases can be found in `src/content`, organised per VCF component
- Each test case is a separate `.md` file in `src/content/test-cases/[component]/`. One test case per `.md` file
- Test case `.md` files look like: 

### Test Case file format

```markdown
# Create New VM on ESXi

## Component
**ESXi**

## MITRE ATT&CK
- **ID:** T1564.006
- **Tactic:** Defense Evasion

## Description
Rogue VMs can be created from VMX definition files...

## Threat Actors
- UNC3886
- Fire Ant

## Log Sources
- HOSTD Logs (/var/log/hostd.log)
- ESXi Shell Logs (/var/log/shell.log)

## References
- https://...

## Author
Leonidas Tsaousis (@laripping)
```



## Inspiration

This project is inspired by:

- [Atomic Red Team](https://atomicredteam.io/) - The de facto threat emulation framework
- [Leonidas](https://github.com/reverseclabs/leonidas) - Cloud Attack Simulation framework, complete with attack definitions 
- [Detection in the Cloud](https://detectioninthe.cloud/) - Rendered Leonidas attack definitions 
- [Kubenomicon](https://kubenomicon.com/) - A similar resource for Kubernetes 



## License

MIT License
