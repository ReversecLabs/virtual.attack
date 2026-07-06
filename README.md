# Virtual//Attack

*Attack techniques for Threat Emulation in VMware environments*

> Browse them live at https://virtualatt.ac


<!-- TODO CHANGE SHIELDS BELOW -->
<p align="center">
  <img src="project-logo.png"><br /><br />
  <img alt="Techniques" src="https://img.shields.io/badge/Techniques-86-flat.svg?style=flat-square">
  <img alt="Components" src="https://img.shields.io/badge/Components-7-flat.svg?style=flat-square">
  <img alt="GitHub License" src="https://img.shields.io/github/license/reverseclabs/leonidas?style=flat">
  <a href="https://astro.build"><img src="https://astro.badg.es/v2/built-with-astro/tiny.svg" alt="Built with Astro" width="120" height="20"></a>
</p>




## Overview

A comprehensive collection of 80+ individual atacker actions that can be simulated against VCF environments in Purple Team exercises. Grounded in threat intelligence and accompanied by log sources for defenders.  

## The problem

> [!IMPORTANT] 
> Detection capability in VMware/VCF/vSphere estates remains low or inexistent.  

Despite the criticality of the virtualisation environment, organisations do not proactively invest in the resilience against threats 

## How to use this project

**🟣VMware Threat Emulations**

To empower security teams to build detections and hunt threats, this repo provides reproducible attack test cases mapped to the MITRE ATT&CK framework. These can be used in adversary emulation drills, to ultimately drive:
- assessment of preventative controls
- discovery of blind spots
- development of detections
- identification of any design or architectural issues

By cloning this repo and maintaining internally for their own environment, purple teams can continuously stress the defences of their own VMware/VCF defences.


## The Techniques


<!-- ## Repository structure -->

Test cases can be found in `src/content`, organised per VCF component. Each test case is a separate `.md` file in `src/content/test-cases/[component]/`, with only one technique allowed in every `.md` file.



**📦 What Is Covered & What Not**


- **Beyond vSphere**: This collection includes not only the usual vCenter and ESXi attacks, but covers also VMware components of security significance in the [VCF](https://www.vmware.com/products/cloud-infrastructure/vmware-cloud-foundation) ecosystem such as the [SDDC Manager](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-operations-design/sddc-manager.html), as well as crucial integrations like Active Directory.  

- **Reproducible**: For the offensive practitioner, each technique comes with detailed insructions and links to origin sources to ensure each test case can be carried out reproducibly.  

- **Defender-friendly**: For the blue teamer, each test case also comes with the Log Sources where evidence is expected to be recorded, aiding the triage process.  

A design decision was made during compilation of the collection to leave out: 

- **CVE exploits** - Various CVEs are actively discovered in VMware products across the different versions. Even where publicly available PoCs exist, these do not represent attack techniques in the Adversary Emulation sense, and can simply be addressed by patching. 

- **Known-malware samples** - For safety purposes, purpose-built malware recovered from past incidents such as BEEFLUSH and VIRTUALPITA are also not included in this library. Instead of focusing on static artifacts that can be trivially signatured, this project focuses on building resilience at higher levels of the [Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html).


**💻 Browse The Collection** 

Visit https://virtualatt.ac for an HTML UI powered by [Astro](astro.build), featuring dynamic test case/VMware component filtering, a responsive design, and even a dark theme!


**🤝Contributing**

As the VCF threat landscape evolves, contributions by the community are welcome and encouraged. 

To add new test cases, simply:

1. Fork the repo
1. Add new `.md` files following the [`template.md`](template.md)
1. Make sure it looks as expected with `npm install && npm run dev`
1. Open a Merge Request 


- 🔬**Real-world Threats**: The majority of test cases has been extracted from threat intelligence reports detailing real-world vSphere incidents. *Additionally, a few more test cases have been added that have not yet been documented, but can be executed practively to assess controls and tailor detections.* 
 









## Inspiration

This project is inspired by:

- [Atomic Red Team](https://atomicredteam.io/) - The de facto threat emulation framework
- [Leonidas](https://github.com/reverseclabs/leonidas) - Cloud Attack Simulation framework, complete with attack definitions 
- [Detection in the Cloud](https://detectioninthe.cloud/) - Rendered Leonidas attack definitions 
- [Kubenomicon](https://kubenomicon.com/) - A similar resource for Kubernetes 
- [Wiz Cloud Threat Landscape](threats.wiz.io) - Browsable UI tracking cloud incidents  

