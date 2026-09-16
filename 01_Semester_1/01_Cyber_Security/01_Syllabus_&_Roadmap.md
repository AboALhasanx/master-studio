# 🗺️ 16-Week Syllabus & Progress Roadmap: Cyber Security

> **Course Code:** CS601  
> **Course Title:** Cyber Security / *الأمن السيبراني المتقدم*  
> **Instructor:** Asst. Prof. Dr. Huda Lafta Majeed (*أ.م.د. هدى لفتة مجيد*)  
> **Credit Hours:** 2 Units | Weekly Time: Sunday 08:30 AM – 10:30 AM  
> **Repository Directory:** `01_Semester_1/01_Cyber_Security/`

---

## 1. Course Overview & Master Competency Matrix

This postgraduate course explores modern cybersecurity from an enterprise defense, threat analysis, and risk management perspective. Candidates transition from passive theoretical knowledge to proactive incident triage, architectural defense engineering, and threat intelligence.

```
+=======================================================================================================+
|                                    16-WEEK PROGRESS TRACKER OVERVIEW                                  |
+=======================================================================================================+
| Completed Weeks: [ 0 / 16 ] | Progress: 0.0% | Status: Initializing Semester 1                        |
+=======================================================================================================+
```

---

## 2. Detailed 16-Week Chronological Roadmap

### 🏁 Phase 1: Foundations, Organizational Threat Modeling & Cryptography (Weeks 1–4)

- [ ] **Week 01: Foundations of Modern Cybersecurity & Threat Landscape**
  - **Topics:** Evolution of cyber threats, Confidentiality-Integrity-Availability (CIA) triad vs. Parkerian Hexad, Attack Surface expansion, Threat Actor Taxonomy (Nation-State, Cybercrime syndicates, Hacktivists, Insiders).
  - **Primary Materials:** Lecture Week 01 PDF (`02_Raw_Materials/Week 01 - Introduction to Cybersecurity.pdf`).
  - **Deliverables:** Study Note in `03_Study_Notes/Week_01_Threat_Landscape.md`.
  - **Self-Assessment:** Identify the 5 threat actor tiers and map them to historical attack campaigns.

- [ ] **Week 02: Cybersecurity Risks as Strategic Organizational Threats**
  - **Topics:** Enterprise risk assessment methodologies (NIST SP 800-30), Quantitative vs. Qualitative Risk Analysis, Asset valuation, Vulnerability scoring (CVSS v3.1/v4.0), Business Impact Analysis (BIA).
  - **Primary Materials:** Lecture Week 02 PDF (`02_Raw_Materials/Week 02 - Cybersecurity Risks as Organizational Threats.pdf`).
  - **Deliverables:** Risk Calculation Formula sheet and risk assessment matrix.
  - **Self-Assessment:** Compute Single Loss Expectancy (SLE) and Annualized Loss Expectancy (ALE) for an enterprise database compromise scenario.

- [ ] **Week 03: Cryptographic Engineering & Key Governance**
  - **Topics:** Symmetric vs. Asymmetric cryptographic primitives (AES-GCM, RSA, ECC/Ed25519), Hash functions & HMAC, Public Key Infrastructure (PKI), Certificate Authorities, Key Lifecycle & Hardware Security Modules (HSM).
  - **Primary Materials:** Lecture Week 03 PDF (`02_Raw_Materials/Week 03 - Cryptography Basics.pdf`).
  - **Deliverables:** Cryptographic algorithm trade-off table in `03_Study_Notes/`.
  - **Self-Assessment:** Compare RSA-4096 vs. ECC-256 in terms of computational overhead and quantum vulnerability.

- [ ] **Week 04: Network Security Architecture & Perimeter Defense**
  - **Topics:** Stateful Packet Inspection (SPI) vs. Next-Generation Firewalls (NGFW), IDS/IPS signature vs. anomaly detection, Network Segmentation, DMZ architecture, Micro-segmentation, VPN protocols (IPsec, WireGuard, TLS).
  - **Primary Materials:** Lecture Week 04 PDF (`02_Raw_Materials/Week 04 - Network Security Fundamentals.pdf`).
  - **Deliverables:** Mermaid Network Topology Diagram in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Design a zero-trust network zone layout for an e-commerce platform processing credit cards.

---

### 🛡️ Phase 2: Web Defense, Malware Mechanisms & Practical Case Triage (Weeks 5–8)

- [ ] **Week 05: Web Application Security & OWASP Top 10**
  - **Topics:** Injection attacks (SQLi, Command Injection), Cross-Site Scripting (Stored, Reflected, DOM-based XSS), Broken Object Level Authorization (BOLA), CSRF vs. SameSite cookies, Secure API gateway design.
  - **Primary Materials:** Lecture Week 05 PDF (`02_Raw_Materials/Week 05 - Web Application Security.pdf`) + OWASP Top 10 documentation.
  - **Deliverables:** Web Exploit & Remediation Cheat Sheet in `03_Study_Notes/`.
  - **Self-Assessment:** Write parameterized queries and Content Security Policy (CSP) headers mitigating XSS and SQLi.

- [ ] **Week 06: Malware Typologies, Cyber Kill Chains & Ransomware Triage**
  - **Topics:** Viruses, Worms, Trojans, Rootkits, Ransomware mechanisms (crypto-lockers, double/triple extortion), MITRE ATT&CK Framework, Lockheed Martin Cyber Kill Chain.
  - **Primary Materials:** Lecture Week 06 PDF + `Scenario WK 06 - Ransomware Outbreak.pdf`.
  - **Practical Lab:** Triage Scenario WK 06 (Simulated Ransomware Outbreak in a Financial Institution).
  - **Deliverables:** Incident Triage Report in `03_Study_Notes/Scenario_WK06_Ransomware_Triage.md`.
  - **Self-Assessment:** Trace the step-by-step lateral movement of a ransomware strain exploiting SMB vulnerabilities.

- [ ] **Week 07: Advanced Malware Detection & Data Leak Prevention (DLP)**
  - **Topics:** Static vs. Dynamic malware analysis, Sandboxing, EDR behavioral telemetry, Memory forensics, Data Loss Prevention (DLP) architecture, Covert exfiltration channels (DNS tunneling, ICMP payloads).
  - **Primary Materials:** Lecture Week 07 PDF + `Scenario WK 07 - Data-Leak Attempt.pdf`.
  - **Practical Lab:** Analyze Scenario WK 07 (Data-Leak Attempt at a University IT Center).
  - **Deliverables:** DLP rule configuration guide and covert channel detection analysis.
  - **Self-Assessment:** Explain how dynamic behavioral heuristics detect polymorphic malware that bypasses signature hashes.

- [ ] **Week 08: Midterm Examination & Threat Intelligence Synthesis**
  - **Exam Focus:** Comprehensive evaluation covering Weeks 1–7 (Scenario-based triage, mathematical risk analysis, cryptographic protocols, defense trade-offs).
  - **Weight:** 30% of coursework grade.
  - **Deliverables:** Midterm review bank and corrected diagnostic errors in `LEARNER_MODEL.md`.

---

### ☁️ Phase 3: Cloud, Social Engineering, IoT & Zero Trust (Weeks 9–12)

- [ ] **Week 09: Social Engineering, Phishing & Identity Deception**
  - **Topics:** Spear phishing, Whaling, Business Email Compromise (BEC), Voice phishing (Vishing / AI voice cloning), Human-centric security controls, DMARC/DKIM/SPF email authentication standards.
  - **Primary Materials:** Lecture Week 08/09 PDF (`02_Raw_Materials/Week 08 - Phishing Attacks and Social Engineering.pdf`).
  - **Deliverables:** Email authentication architecture diagram (DMARC/SPF/DKIM).
  - **Self-Assessment:** Analyze raw email headers to detect spoofed domain senders and malicious redirect links.

- [ ] **Week 10: Cloud Security, Shared Responsibility & Multi-Cloud Risk**
  - **Topics:** Cloud Service Models (IaaS, PaaS, SaaS) and security boundaries, Cloud Security Posture Management (CSPM), Cloud Workload Protection (CWPP), IAM misconfigurations, S3 bucket leakage, Serverless security.
  - **Primary Materials:** Lecture Week 09 PDF + `Scenario WK 10 - FinSecure Global Cloud Attack.pdf`.
  - **Practical Lab:** Complete threat analysis of Scenario WK 10 (FinSecure Global Hybrid Cloud Attack).
  - **Deliverables:** Cloud Threat Analysis Brief in `03_Study_Notes/`.
  - **Self-Assessment:** Formulate a least-privilege IAM policy matrix for a multi-tier AWS/Azure microservice architecture.

- [ ] **Week 11: Cyber-Physical Systems, SCADA & IoT Infrastructure Security**
  - **Topics:** Internet of Things (IoT) threat vectors, Constrained device security (MQTT, CoAP, BLE), Industrial Control Systems (ICS) and SCADA vulnerabilities, Firmware extraction and reverse engineering, Purdue Enterprise Reference Architecture (PERA).
  - **Primary Materials:** Lecture Week 11 PDF (`02_Raw_Materials/Week 11 - Cyber Infrastructure & IoT Security.pdf`).
  - **Deliverables:** IoT security hardening checklist in `03_Study_Notes/`.
  - **Self-Assessment:** Contrast IT vs. OT security priorities (Availability vs. Confidentiality priority inversion).

- [ ] **Week 12: Zero Trust Architecture (ZTA) & Identity Governance**
  - **Topics:** NIST SP 800-207 Zero Trust Architecture principles, Continuous verification, Micro-segmentation, Policy Decision Point (PDP) vs. Policy Enforcement Point (PEP), Privileged Access Management (PAM).
  - **Primary Materials:** Lecture Week 12 PDF + NIST SP 800-207 Standard.
  - **Deliverables:** ZTA Architecture Diagram (Mermaid) in `06_Diagrams_&_Mindmaps/`.
  - **Self-Assessment:** Explain how ZTA mitigates blast radius when an internal workstation credentials are stolen.

---

### 🎯 Phase 4: Incident Response, Forensics & Governance (Weeks 13–16)

- [ ] **Week 13: Cyber Conflict, Attribution & Advanced Persistent Threats (APTs)**
  - **Topics:** State-sponsored cyber warfare, APT lifecycle and tactics, Cyber attribution challenges, International cyber law and norms (Tallinn Manual), Defense against sophisticated living-off-the-land (LotL) binaries.
  - **Primary Materials:** Research papers on APT hunting and threat intelligence feeds (STIX/TAXII).
  - **Deliverables:** Academic literature summary on APT detection in `04_Academic_Papers/`.
  - **Self-Assessment:** Map an APT campaign to the MITRE ATT&CK Matrix across Initial Access to Exfiltration.

- [ ] **Week 14: Incident Response Lifecycle & Digital Forensics Engineering**
  - **Topics:** NIST SP 800-61r2 Incident Handling Guide (Preparation, Detection & Analysis, Containment, Eradication & Recovery, Post-Incident Activity), Chain of Custody, Volatile memory acquisition (Volatility), Disk imaging (FTK/dd), Log analysis (SIEM / Splunk / Elastic).
  - **Primary Materials:** Lecture Week 14 PDF (`02_Raw_Materials/Week 14 - Incident Response and Digital Forensics.pdf`).
  - **Deliverables:** Incident Response Runbook in `03_Study_Notes/`.
  - **Self-Assessment:** Outline the forensic chain of custody protocol when seizing a server involved in financial fraud.

- [ ] **Week 15: Enterprise Security Management, Auditing & ISO/IEC 27001**
  - **Topics:** Information Security Management Systems (ISMS), ISO/IEC 27001:2022 Controls, Security compliance, Internal auditing, Security culture and board-level risk reporting.
  - **Primary Materials:** Lecture Week 15 PDF (`02_Raw_Materials/Week 15 - Cyber Management and Infrastructure Issues.pdf`).
  - **Deliverables:** ISO 27001 Statement of Applicability (SoA) sample table.
  - **Self-Assessment:** Map technical security controls to ISO 27001 Annex A clauses.

- [ ] **Week 16: Comprehensive Course Review & Final Examination Preparation**
  - **Activities:** Comprehensive mock exam covering all 15 weeks of scenarios, trade-off matrices, and technical definitions; review of professor exam preferences.
  - **Deliverables:** 100-Question Master Anki deck export in `07_Quizzes_&_Anki/`.
  - **Final Exam Readiness Target:** Score $\ge 85\%$ on full mock exam.

---

## 3. Evaluation & Assessment Weightings

| Component | Weight | Target Score | Description |
|:---|:---:|:---:|:---|
| **Class Attendance & Seminar Participation** | 10% | 10% | Weekly presence, active engagement during scenario discussions |
| **Practical Scenario Reports (WK 06, 07, 10)** | 15% | 14% | Written technical incident triage briefs |
| **Oral Seminar Presentation (Marp)** | 15% | 14% | 10-slide academic research presentation on emerging cyber threat |
| **Midterm Examination (Week 08)** | 20% | 18% | Written exam on Weeks 1–7 |
| **Final Semester Examination (Week 16)** | 40% | 35% | Comprehensive written examination |
| **Total Course Grade** | **100%** | **$\ge 90\%$** | **Grade Target: Distinction (امتياز)** |
