# 1. INTRODUCTION

## 1.1 Overview

This combined Certificate Policy ("CP") and Certification Practice Statement ("CPS") document ("CP/CPS") outlines the certification services practices for Internet Security Research Group ("ISRG") Public Key Infrastructure ("ISRG PKI").

ISRG PKI services include, but are not limited to, issuing, managing, validating, and revoking publicly-trusted Certificates in a manner consistent with this CP/CPS.

These services are provided to the general public with exceptions as ISRG management deems appropriate or in accordance with relevant law.

ISRG PKI services are most commonly, but not necessarily exclusively, provided under the brand/trademark "Let's Encrypt".

The ISRG PKI conforms to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates published at <https://www.cabforum.org>. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

Other documents related to the behavior and control of the ISRG PKI, such as a Subscriber Agreement and Privacy Policy, can be found at <https://letsencrypt.org/repository/>.

Per IETF PKIX RFC 3647, this CP/CPS is divided into nine components that cover security controls, practices, and procedures for certification services provided by the ISRG PKI.

The following Certification Authorities are covered under this document:

| CA Type | Distinguished Name | Key Pair Type and Parameters | Cert SHA-256 Fingerprint | Validity Period |
|---------|--------------------|------------------------------|--------------------------|-----------------|
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X1 | RSA, n has 4096 bits, e=65537 | 96:BC:EC:06:26:49:76:F3:<br>74:60:77:9A:CF:28:C5:A7:<br>CF:E8:A3:C0:AA:E1:1A:8F:<br>FC:EE:05:C0:BD:DF:08:C6 | Not Before: Jun  4 11:04:38 2015 GMT,<br>Not After: Jun  4 11:04:38 2035 GMT |
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X2 | ECDSA, NIST curve P-384 | 69:72:9B:8E:15:A8:6E:FC:<br>17:7A:57:AF:B7:17:1D:FC:<br>64:AD:D2:8C:2F:CA:8C:F1:<br>50:7E:34:45:3C:CB:14:70 | Not Before: Sept  4 00:00:00 2020 GMT,<br>Not After: Sept 17 16:00:00 2040 GMT |

This work is licensed under the Creative Commons Attribution 4.0 International License. To
view a copy of this license, visit <https://creativecommons.org/licenses/by/4.0/> or send a letter to Creative
Commons, PO Box 1866, Mountain View, CA 94042, USA.

## 1.2 Document name and identification

This is the ISRG CP/CPS. This document was approved for publication by the ISRG Policy Management Authority, and is made available at <https://letsencrypt.org/repository/>.

The following revisions have been made:

| Date              | Changes                                            | Version |
|-------------------|----------------------------------------------------|---------|
| May 5, 2023 | CP and CPS documents are combined. See past documents for prior version history. | 5.0 |
| May 16, 2023 | Make CPS OID and URL in Subscriber Certificates optional. | 5.1 |
| Feb 7, 2024 | Add CRL Distribution Point to subscriber certificate profile. Add IssuingDistributionPoint to subordinate CRL profile. Remove id-qt-cps from subscriber certificate profile, make it optional for subordinate certificate profile. Clarify waste disposal procedure. | 5.2 |
| Mar 22, 2024 | Improve accuracy of information regarding subscriber key compromise in sections 4.9.3 and 4.9.12. | 5.3 |
| Sep 27, 2024 | Remove statements regarding meaningful names. Format section headers to match RFC 3647. | 5.4 |
| Oct 25, 2024 | Consolidate statements about certificate contents into Section 7.1. Replace normative language with descriptive language. | 5.5 |
| Dec 12, 2024 | Make OCSP service optional. | 5.6 |
| Jan 15, 2025 | Update trusted roles, make TLS Client Auth optional, document IP Address validation. | 5.7 |

## 1.3 PKI participants

### 1.3.1 Certification authorities

This CP/CPS applies to the ISRG PKI.

### 1.3.2 Registration authorities

ISRG does not delegate any of the Section 3.2 requirements to a Delegated Third Party. ISRG serves as its own RA.

### 1.3.3 Subscribers

See definition of "Subscriber" in Section 1.6.1 Definitions.

### 1.3.4 Relying parties

See definition of "Relying Party" in Section 1.6.1 Definitions.

### 1.3.5 Other participants

Other participants include CAs that cross-sign or issue subordinates to the ISRG PKI.

ISRG PKI vendors and service providers with access to confidential information or privileged systems are required to operate in compliance with this ISRG CP/CPS.

## 1.4 Certificate usage

### 1.4.1 Appropriate certificate uses

No stipulation.

### 1.4.2 Prohibited certificate uses

Prohibited certificate usage is governed by the Let's Encrypt Subscriber Agreement.

## 1.5 Policy administration

### 1.5.1 Organization administering the document

The ISRG PMA maintains this document.

### 1.5.2 Contact person

The ISRG PMA can be contacted at:

Policy Management Authority<br>
Internet Security Research Group<br>
P.O. Box 18666<br>
Minneapolis, MN 55418-0666<br>
USA<br>

Certificate revocation requests can be made via the ACME API. Please see Section 4.9.3 for more information.

Certificate Problem Reports can be submitted via email to:

[cert-prob-reports@letsencrypt.org](mailto:cert-prob-reports@letsencrypt.org)

Issues can be filed via the GitHub repository where this document is maintained:

<https://github.com/letsencrypt/cp-cps>

### 1.5.3 Person determining CPS suitability for the policy

The ISRG PMA is responsible for determining the suitability of this CP/CPS. ISRG policy is informed by results and recommendations received from an independent auditor.

### 1.5.4 CPS approval procedures

The ISRG PMA approves any revisions to this CP/CPS after formal review.

## 1.6 Definitions and acronyms

### 1.6.1 Definitions

**ACME Protocol**: A protocol used for validation, issuance, and management of certificates. The protocol is an open standard managed by the IETF.

**CAB Forum**: Certificate Authority / Browser Forum, a group of CAs and browsers which come together to discuss technical and policy issues related to PKI systems. (<https://cabforum.org/>)

**Certificate Repository**: A repository of information about ISRG certificates. It is located at: <https://letsencrypt.org/certificates/>

**Identifier**: A value included, or requested to be included, in a Subscriber Certificate's Subject Common Name field or Subject Alternative Name extension, such as a Fully-Qualified Domain Name (FQDN) or an Internet Protocol (IP) address.

**Policy and Legal Repository**: A repository of policy and legal documents related to the ISRG PKI. It is located at: <https://letsencrypt.org/repository/>

**Precertificate**: As defined by RFC 6962 Section 3.1.

**Secure PKI Facilities**: Facilities designed to protect sensitive PKI infrastructure, including CA private keys.

**Trusted Contributor**: A contributor who performs in a Trusted Role. Trusted Contributors may be employees, contractors, or community members. Trusted Contributors must be properly trained and qualified, and have the proper legal obligations in place before performing in a Trusted Role.

See the Baseline Requirements and NetSec Requirements for additional definitions.

### 1.6.2 Acronyms

| **Acronym** | **Meaning** |
| --- | --- |
| ACME | Automated Certificate Management Environment |
| DV | Domain Validation |
| HSM | Hardware Security Module |
| IP | Internet Protocol |
| ISRG | Internet Security Research Group |
| PMA | Policy Management Authority |
| SAN | Subject Alternative Name |
| TLD | Top Level Domain |

See the Baseline Requirements and NetSec Requirements for additional acronyms.

### 1.6.3 References

The "Baseline Requirements": [CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates](https://cabforum.org/baseline-requirements-documents/)

The "NetSec Requirements": [CA/Browser Forum Network and Certificate System Security Requirements](https://cabforum.org/network-security-requirements/)

### 1.6.4 Conventions

Terms not otherwise defined in this CP/CPS shall be as defined in applicable agreements, user manuals, Certificate Policies, and Certification Practice Statements of the CA.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

## 2.1 Repositories

See Sections 4.9.7 and 4.9.10 for details on revocation information.

## 2.2 Publication of certification information

ISRG Combined CP/CPS, Privacy Policy, Subscriber Agreement, and WebTrust audit documents are made publicly available in the Policy and Legal Repository at <https://letsencrypt.org/repository/>.

Records of all ISRG Root and Subordinate CA certificates, including valid/expired/revoked test pages, are available in the Certificate Repository at <https://letsencrypt.org/certificates/>.

## 2.3 Time or frequency of publication

New or updated ISRG Combined CP/CPS, Privacy Policy, Subscriber Agreement, and WebTrust audit documents are made publicly available as soon as possible. This typically means within seven days of receipt or approval. The ISRG PMA approves and publishes updated CP/CPS documents at least annually.

New or updated ISRG Root and Subordinate CA certificates are made publicly available as soon as possible. This typically means within seven days of creation.

## 2.4 Access controls on repositories

Read only access to the Policy and Legal Repository and certificate information is unrestricted. Write access is protected by logical and physical controls.

# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

### 3.1.1 Types of names

See Section 7.1 for the types of names which may appear in Let's Encrypt certificates.

### 3.1.2 Need for names to be meaningful

No stipulation.

### 3.1.3 Anonymity or pseudonymity of subscribers

Subscribers are not identified in DV certificates. Certificates do not assert any specific relationship between Subscribers and owners of Identifiers contained in certificates. Relying Parties should consider DV certificate Subscribers to be anonymous.

### 3.1.4 Rules for interpreting various name forms

It is the CA's position that homoglyph spoofing should be dealt with by registrars, and Web browsers should have sensible policies for when to display the punycode versions of names.

### 3.1.5 Uniqueness of names

No stipulation.

### 3.1.6 Recognition, authentication, and role of trademarks

ISRG reserves the right to make all decisions regarding Subscriber names in certificates. Entities requesting certificates are required to demonstrate their right to use names (e.g. demonstrate control of an FQDN), but trademark rights are not verified.

While ISRG complies with U.S. law and associated legal orders, it is ISRG's position that trademark enforcement responsibility for domain names should lie primarily with domain registrars and the legal system.

## 3.2 Initial identity validation

ISRG may elect not to issue any certificate at its sole discretion.

### 3.2.1 Method to prove possession of private key

No stipulation.

### 3.2.2 Authentication of organization identity

Prior to issuance of a Subscriber Certificate, ISRG uses at least one of the following methods to validate the Applicant's control of each requested DNS name:

1. DNS Change (Baseline Requirements Section 3.2.2.4.7)
2. Agreed-Upon Change to Website - ACME (Baseline Requirements Section 3.2.2.4.19)
3. TLS Using ALPN (Baseline Requirements Section 3.2.2.4.20)

Similarly, ISRG uses at least one of the following methods to validate the Applicant's control of each requested IP address:

1. ACME "http-01" method for IP Addresses (Baseline Requirements Section 3.2.2.5.6)
2. ACME "tls-alpn-01" method for IP Addresses (Baseline Requirements Section 3.2.2.5.7)

Validation for Wildcard Domain Names is only performed using the DNS Change method.

All successful validations and CAA checks performed by our Primary Network Perspectives are corroborated by multiple remote Network Perspectives located in at least two distinct Regional Internet Registries. Each remote Network Perspective has an independent DNS resolver and cache.

All validations are performed in compliance with the current CAB Forum Baseline Requirements at the time of validation.

### 3.2.3 Authentication of individual identity

Not applicable.

### 3.2.4 Non-verified subscriber information

Not applicable.

### 3.2.5 Validation of authority

Not applicable.

### 3.2.6 Criteria for interoperation

ISRG discloses Cross-Certified Subordinate CA Certificates in its Certificate Repository.

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

See Section 4.7.

### 3.3.2 Identification and authentication for re-key after revocation

See Section 4.7.

## 3.4 Identification and authentication for revocation request

Identification and authentication for revocation requests is performed by ISRG as described by Section 4.9 of this document.

Identification and authentication are not required when ISRG is requesting revocation.

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate Application

### 4.1.1 Who can submit a certificate application

Anyone may submit an application for a certificate via the ACME protocol. Issuance depends on proper validation and compliance with ISRG policies.

### 4.1.2 Enrollment process and responsibilities

The enrollment process involves the following steps, in no particular order:

* Generating a key pair using secure methods
* Submitting a request for a certificate containing all necessary information, including the public key
* Agreeing to the relevant Subscriber Agreement

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions

ISRG performs all identification and authentication functions in accordance with this CP/CPS. This includes validation per Section 3.2.2.

Certificate information is verified using data and documents obtained no more than 90 days prior to issuance of the Certificate.

As part of the validation process, ISRG checks for CAA records for each requested DNS name and follows the processing instructions found as specified in RFC 8659 and Section 3.2.2.8 of the Baseline Requirements. The CA acts in accordance with CAA records if present. If the CA issues, it does so within the TTL of the CAA record, or 8 hours, whichever is greater. The CA's CAA identifying domain is `letsencrypt.org`.

ISRG maintains a list of high-risk domains and blocks issuance of certificates for those domains.

### 4.2.2 Approval or rejection of certificate applications

Approval requires successful completion of validation per Section 3.2.2 as well as compliance with all CA policies.

The CA Server is periodically updated with the latest version of the Public Suffix List and consults the ICANN domains section for every requested DNS identifier. The CA server rejects issuance requests for DNS identifiers that do not have a Public Suffix in the ICANN domains section.

### 4.2.3 Time to process certificate applications

No stipulation.

## 4.3 Certificate issuance

### 4.3.1 CA actions during certificate issuance

At a high level, the following steps are taken during issuance of a Subscriber Certificate. ISRG's automated processes confirm that all requested names have been properly validated to be controlled by the Subscriber requesting the certificate. The to-be-signed certificate is linted, then signed by a Subordinate CA in an HSM. After issuance is complete, the certificate is stored in a database and made available to the Subscriber.

All issuance from ISRG Root CAs requires direct action from a person acting in an appropriate Trusted Role as described in Section 5.2.1.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate

Subscriber Certificates are made available to Subscribers via the ACME protocol as soon after issuance as reasonably possible. Typically this happens within a few seconds.

## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance

No stipulation.

### 4.4.2 Publication of the certificate by the CA

See Section 2.2 of this document for Root and Subordinate CA certificate publication information.

All Subscriber Certificates are made available to Subscribers via the ACME protocol. They are also submitted to Certificate Transparency logs on a best-effort basis.

ISRG does not guarantee issuance of a final certificate for every Precertificate.

### 4.4.3 Notification of certificate issuance by the CA to other entities

See Section 4.4.2.

## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

Subscriber usage of Private Keys and Certificates is governed by the Let's Encrypt Subscriber Agreement.

### 4.5.2 Relying party public key and certificate usage

Relying Parties should fully evaluate the context in which they are relying on certificates and the information contained in them, and decide to what extent the risk of reliance is acceptable. If the risk of relying on a certificate is determined to be unacceptable, then Relying Parties should not use the certificate or should obtain additional assurances before using the certificate.

ISRG does not warrant that any software used by Relying Parties to evaluate or otherwise handle certificates does so properly.

## 4.6 Certificate renewal

Certificate renewal requests are treated as applications for new certificates.

### 4.6.1 Circumstance for certificate renewal

No stipulation.

### 4.6.2 Who may request renewal

No stipulation.

### 4.6.3 Processing certificate renewal requests

No stipulation.

### 4.6.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.6.5 Conduct constituting acceptance of a renewal certificate

No stipulation.

### 4.6.6 Publication of the renewal certificate by the CA

No stipulation.

### 4.6.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.7 Certificate re-key

Certificate re-key requests are treated as applications for new certificates.

### 4.7.1 Circumstance for certificate re-key

No stipulation.

### 4.7.2 Who may request certification of a new public key

No stipulation.

### 4.7.3 Processing certificate re-keying requests

No stipulation.

### 4.7.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.7.5 Conduct constituting acceptance of a re-keyed certificate

No stipulation.

### 4.7.6 Publication of the re-keyed certificate by the CA

No stipulation.

### 4.7.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.8 Certificate modification

Certificate modification requests are treated as applications for new certificates.

### 4.8.1 Circumstance for certificate modification

No stipulation.

### 4.8.2 Who may request certificate modification

No stipulation.

### 4.8.3 Processing certificate modification requests

No stipulation.

### 4.8.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.8.5 Conduct constituting acceptance of modified certificate

No stipulation.

### 4.8.6 Publication of the modified certificate by the CA

No stipulation.

### 4.8.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.9 Certificate revocation and suspension

### 4.9.1 Circumstances for revocation

ISRG revokes certificates in accordance with Section 4.9.1.1 and Section 4.9.1.2 of the Baseline Requirements.

Depending on the circumstances, revocation timelines can be as short as 24 hours or even less. Therefore, ISRG strongly recommends against using publicly-trusted TLS server certificates on systems that cannot tolerate timely revocation.

### 4.9.2 Who can request revocation

Anyone can request revocation at any time via the Certificate Revocation interface of the ACME Protocol, as defined in Section 7.6 of RFC 8555.

Requests for revocation may also be made by emailing [cert-prob-reports@letsencrypt.org](mailto:cert-prob-reports@letsencrypt.org).

ISRG may administratively revoke certificates if it determines that the Subscriber has failed to meet obligations under this CP/CPS, the relevant Subscriber Agreement, or any other applicable agreement, regulation, or law. Certificates may also be administratively revoked at ISRG management's discretion.

### 4.9.3 Procedure for revocation request

Revocation requests made via the ACME API are processed automatically. The certificate identified in the revocation request is revoked if:

* the request is signed with the private key associated with the certificate;
* the request is signed with the account key of the Subscriber which originally requested issuance of the certificate; or
* the request is signed with the account key of a Subscriber who has demonstrated control over all Subject Alternative Names in the certificate.

ISRG maintains a continuous (24x7) ability to accept and respond to revocation requests and Certificate Problem Reports. ISRG responds to such requests within 24 hours, though an investigation into the legitimacy of the request may take longer.

An investigation into whether revocation or other appropriate action is warranted is based on at least the following criteria:

1. The nature of the alleged problem;
2. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
3. The entity making the complaint; and
4. Relevant legislation.

In all cases, requests to revoke Short-Lived Subscriber Certificates may be ignored.

### 4.9.4 Revocation request grace period

There is no grace period for a revocation request. A revocation request must be made as soon as circumstances requiring revocation are confirmed.

### 4.9.5 Time within which CA must process the revocation request

Investigation into a revocation request begins within 24 hours of receiving the request. Revocation, if necessary, is carried out within the timeframes set by Baseline Requirements Sections 4.9.1.1 and 4.9.1.2.

### 4.9.6 Revocation checking requirement for relying parties

It is recommended, but not required, that Relying Parties verify the revocation status of ISRG certificates when revocation information is provided by ISRG. Relying Parties who cannot or choose not to check certificate revocation status, but decide to rely on a certificate anyway, do so at their own risk.

See Section 4.5.2.

### 4.9.7 CRL issuance frequency (if applicable)

ISRG issues updated CRLs with the frequency required by the Baseline Requirements.

### 4.9.8 Maximum latency for CRLs (if applicable)

When a Relying Party requests a CRL, the time to receive a response is less than ten seconds under normal operating conditions.

### 4.9.9 On-line revocation/status checking availability

ISRG may provide revocation information via OCSP for Subscriber Certificates and/or Subordinate CA certificates, though ISRG makes no commitment to doing so.

### 4.9.10 On-line revocation checking requirements

No stipulation.

### 4.9.11 Other forms of revocation advertisements available

No stipulation.

### 4.9.12 Special requirements re key compromise

ISRG considers key compromise demonstrated when revocation is successfully requested via the ACME Protocol and the request was signed by the private key of the certificate. Key compromise can be demonstrated via ACME even for certificates that have previously been revoked without demonstrating key compromise.

ISRG may also consider key compromise demonstrated by non-ACME methods.

When key compromise is demonstrated, ISRG blocks the key from use in future issuance and revokes all unexpired non-Short-Lived Subscriber Certificates that used that key.

ISRG does not consider a key compromised unless key compromise is demonstrated, but may revoke a certificate with reason code `keyCompromise` for other reasons. In these cases ISRG may not block the key from future use or revoke certificates using that key, even if the stated reason code is `keyCompromise`.

### 4.9.13 Circumstances for suspension

ISRG does not suspend certificates.

### 4.9.14 Who can request suspension

Not applicable.

### 4.9.15 Procedure for suspension request

Not applicable.

### 4.9.16 Limits on suspension period

Not applicable.

## 4.10 Certificate status services

### 4.10.1 Operational characteristics

Revocation entries on a CRL are not removed until they have appeared in at least one CRL issued after the NotAfter date of the revoked Certificate.

### 4.10.2 Service availability

All certificate status services are made available at all times (24x7) if possible.

### 4.10.3 Optional features

No stipulation.

## 4.11 End of subscription

A Subscriber's subscription ends once all of Subscriber's ISRG certificates have expired or been revoked.

## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices

Not applicable.

### 4.12.2 Session key encapsulation and recovery policy and practices

Not applicable.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

## 5.1 Physical controls

### 5.1.1 Site location and construction

ISRG Secure PKI Facilities are located in the United States, as are all copies of ISRG CA Private Keys.

ISRG maintains at least two Secure PKI Facilities for the sake of redundancy.

Secure PKI Facilities are constructed so as to prevent unauthorized entry or interference.

Secure PKI Facilities are monitored at all times so as to prevent unauthorized entry or interference.

### 5.1.2 Physical access

Physical access to ISRG Secure PKI Facilities is restricted to authorized ISRG employees, vendors, and contractors, for whom access is required in order to execute their jobs. Access restrictions are strongly enforced via multi-factor authentication mechanisms.

### 5.1.3 Power and air conditioning

Redundant power sources are readily available at each Secure PKI Facility, and are designed to meet ISRG's operating requirements.

Air conditioning systems at each Secure PKI Facility are designed to meet ISRG's operating requirements.

### 5.1.4 Water exposures

ISRG Secure PKI Facilities are designed to protect ISRG infrastructure from water exposure/damage.

### 5.1.5 Fire prevention and protection

ISRG Secure PKI Facilities are designed to prevent fire and provide suppression if necessary.

### 5.1.6 Media storage

ISRG Secure PKI Facilities are designed to prevent accidental damage or unauthorized access to media.

### 5.1.7 Waste disposal

ISRG prohibits any media that contains or has contained sensitive data from leaving organizational control unless action has been taken to render any data practically unrecoverable. Such media may include printed documents or digital storage devices. When media that has contained sensitive information reaches its end of life, the media is securely erased or physically destroyed such that recovery is reasonably believed to be impossible.

### 5.1.8 Off-site backup

ISRG maintains multiple backups of ISRG CA Private Keys at multiple Secure PKI Facilities. All backups are stored on devices validated as meeting FIPS 140-2 Level 3 (or higher) criteria.

## 5.2 Procedural controls

### 5.2.1 Trusted roles

All persons, employees or otherwise, with the ability to materially impact the operation of ISRG PKI systems and services can only do so while designated as serving in a Trusted Role.

Trusted Roles include:

* PKI Administrators, whose responsibilities include but are not limited to designing, implementing, and operating CA Infrastructure and Network Equipment.
* PKI Software Engineers, whose responsibilities include but are not limited to designing and implementing CA Infrastructure. Per the principle of least privilege, PKI Software Engineers have less access to CA Infrastructure and Network Equipment than PKI Administrators.
* PKI Managers, whose responsibilities include decision-making authority over CA operations.

Each Trusted Role requires an appropriate level of training and legal obligation.

### 5.2.2 Number of persons required per task

A number of tasks, such as key generation and entering areas physically containing operating ISRG PKI systems, require at least two people in Trusted Roles to be present.

### 5.2.3 Identification and authentication for each role

Anyone performing work in a Trusted Role must identify and authenticate themselves before accessing ISRG PKI systems or confidential information.

### 5.2.4 Roles requiring separation of duties

See Section 6.6.1.

## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

ISRG management is responsible for making sure that Trusted Contributors are trustworthy and competent, which includes having proper qualifications and experience.

ISRG management ensures this with appropriate interviewing practices, training, background checks, and regular monitoring and review of Trusted Contributor job performance.

### 5.3.2 Background check procedures

Trusted Contributors undergo a background check prior to performing in a trusted role. ISRG management reviews the results of background checks for problematic issues prior to approving performance of a trusted role.

Background checks include, without limitation, criminal background and employment history.

### 5.3.3 Training requirements

Trusted Contributors are trained on topics relevant to the role in which they will perform.

Training programs are developed for each role by ISRG management and Security Officers.

### 5.3.4 Retraining frequency and requirements

Training is repeated annually for each Trusted Contributor, and covers topics necessary to maintain skill level requirements.

Training is also offered whenever changes in the industry or operations require it in order for contributors to competently perform in their trusted roles.

### 5.3.5 Job rotation frequency and sequence

No stipulation.

### 5.3.6 Sanctions for unauthorized actions

Action is taken to safeguard ISRG and its Subscribers whenever ISRG Trusted Contributors, whether through negligence or malicious intent, fail to comply with ISRG policies including this CP/CPS.

Actions taken in response to non-compliance may include termination, removal from trusted roles, or reporting to legal authorities.

Once management becomes aware of non-compliance the Trusted Contributor(s) in question will be removed from trusted roles until a review of their actions is complete.

### 5.3.7 Independent contractor requirements

Independent contractors who are assigned to perform Trusted Roles are subject to the duties and requirements specified for such roles in this CP/CPS. This includes those described in Section 5.3. Potential sanctions for unauthorized activities by independent contractors are described in Section 5.3.6.

### 5.3.8 Documentation supplied to personnel

Trusted Contributors are provided with all documentation necessary to perform their duties. This always includes, at a minimum, a copy of the ISRG CP/CPS and Information Security Policy.

## 5.4 Audit logging procedures

### 5.4.1 Types of events recorded

Audit logs are generated for all events related to CA security (physical and logical) and certificate issuance. Logs are automatically generated whenever possible. When it is necessary to manually log information, logs are kept on paper with written confirmation from a witness and securely stored. All audit logs, electronic or otherwise, shall be retained and made available to compliance auditors upon request.

At a minimum, each audit record includes:

* Date and time of entry;
* Identity of the person (or machine) making the entry; and
* Description of the entry.

### 5.4.2 Frequency of processing log

No stipulation.

### 5.4.3 Retention period for audit log

Audit logs are retained for at least the period required by Section 5.4.3 of the Baseline Requirements.

### 5.4.4 Protection of audit log

Audit logs, whether in production or archived, are protected using both physical and logical access controls.

### 5.4.5 Audit log backup procedures

ISRG makes regular backup copies of audit logs.

### 5.4.6 Audit collection system (internal vs. external)

Audit data is automatically generated and reported/recorded by operating systems, CA software applications, and network devices. Systems are in place to ensure proper reporting and recording of audit data, and the failure of such systems may lead to suspension of CA services until proper audit log reporting is restored.

### 5.4.7 Notification to event-causing subject

No stipulation.

### 5.4.8 Vulnerability assessments

Audit logs are monitored by Trusted Contributors, including operations and engineering staff. Anomalies indicating attempted breaches of CA security are reported and investigated.

Internal and external vulnerability scans occur at least every three months.

Extensive vulnerability assessments for ISRG infrastructure are conducted at least annually by qualified third parties.

ISRG Security Officers perform a risk assessment at least annually. This risk assessment:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;

2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and

3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

## 5.5 Records archival

### 5.5.1 Types of records archived

ISRG archives all audit logs, the contents of which are described in Section 5.4.1. ISRG also archives other documents and information critical to understanding the historical security and performance of the CA's duties.

### 5.5.2 Retention period for archive

Archived records are retained for at least the period required by Section 5.5.2 of the Baseline Requirements.

### 5.5.3 Protection of archive

Archives are protected from unauthorized modification or destruction by strong security and environmental controls.

### 5.5.4 Archive backup procedures

Archives are backed up regularly.

### 5.5.5 Requirements for time-stamping of records

Records are time-stamped as they are created.

Machine-created records use system time, which is synchronized automatically with third-party time sources. Machines without network access have the time set manually.

Manual records use a manually entered date and time, complete with time zone in use.

### 5.5.6 Archive collection system (internal or external)

No stipulation.

### 5.5.7 Procedures to obtain and verify archive information

No stipulation.

## 5.6 Key changeover

See Section 6.1.

## 5.7 Compromise and disaster recovery

### 5.7.1 Incident and compromise handling procedures

ISRG has created and maintains incident response procedures for a range of potential compromise and disaster situations. Such situations include, but are not limited to, natural disasters, security incidents, and equipment failure. Incident response plans are reviewed, potentially updated, and tested on at least an annual basis.

### 5.7.2 Computing resources, software, and/or data are corrupted

In the event that computing resources, software, and/or data are corrupted or otherwise damaged, ISRG will assess the situation, including its impact on CA integrity and security, and take appropriate action. CA operations may be suspended until mitigation is complete. Subscribers may be notified if corruption or damage has a material impact on the service provided to them.

### 5.7.3 Entity private key compromise procedures

In the event that an ISRG CA Private Key is compromised, or suspected to be compromised, ISRG will immediately launch a thorough investigation. Forensic evidence will be collected and secured as quickly as possible. If it cannot be determined with a high degree of certainty that the private key in question was not compromised, then the following steps may be taken in whatever order ISRG Security Officers deem most appropriate:

* Certificates relying on the private key in question will be revoked.
* ISRG will notify root programs relying on the integrity of the key in question.
* ISRG will notify Subscribers relying on the integrity of the key in question.

### 5.7.4 Business continuity capabilities after a disaster

ISRG maintains multiple geographically diverse facilities, each of which is capable of operating ISRG PKI systems independently. In the event that a disaster entirely disables one facility, ISRG PKI operations will fail over to another facility.

## 5.8 CA or RA termination

In the event that ISRG PKI services are to be terminated:

* All affected parties, including root programs and Subscribers, will be provided with notice as far in advance as reasonably possible.
* The ISRG PMA will create and review a termination plan.

If a suitable successor entity exists, the following steps will be taken:

* ISRG CA Private Keys, records, logs, and other critical documentation will be transferred to the successor organization in a secure and compliant manner.
* Arrangements will be made for compliant continuation of CA responsibilities.

If a suitable successor entity does not exist, the following steps will be taken:

* All unexpired Subordinate CA Certificates and non-Short-Lived Subscriber Certificates will be revoked and final CRLs will be published.
* ISRG CA Private Keys will be destroyed.
* CA records, logs, and other critical documentation will be transferred to a third party or government entity with appropriate legal controls in place to protect information while allowing its use in compliance with relevant policies and the law.

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

ISRG CA Private Keys are generated by HSMs meeting the requirements of Section 6.2.1. This occurs during a ceremony meeting the requirements of this CP/CPS.

See the Let's Encrypt Subscriber Agreement for information regarding Subscriber key pair generation. Once submitted as part of a certificate request, Subscriber Public Keys are rejected if they do not meet our size requirements (see Section 6.1.5), can be easily compromised by certain attacks (e.g. ROCA, Fermat factorization), or appear in our database of known-weak and known-compromised keys.

### 6.1.2 Private key delivery to subscriber

ISRG never generates or has access to Subscriber Private Keys.

### 6.1.3 Public key delivery to certificate issuer

Subscriber Public Keys are communicated to ISRG electronically via the ACME protocol.

### 6.1.4 CA public key delivery to relying parties

ISRG Root CA Public Keys are generally provided to Relying Parties as part of browser, operating system, or other software trusted root certificate lists. ISRG Subordinate CA Public Keys are generally provided to Relying Parties by Subscribers as part of a TLS handshake.

ISRG Public Keys are also available in the Certificate Repository.

### 6.1.5 Key sizes

ISRG Root CA key pairs are either RSA keys whose encoded modulus size is 4096 bits, or ECDSA keys which are a valid point on the NIST P-384 elliptic curve.

ISRG Subordinate CA key pairs are either RSA keys whose encoded modulus size is 2048 bits, or ECDSA keys which are a valid point on the NIST P-384 elliptic curve.

Public keys in Subscriber Certificates issued by ISRG are either RSA keys whose encoded modulus size is 2048, 3072, or 4096 bits; or ECDSA keys which are a valid point on the NIST P-256, P-384, or P-521 elliptic curves.

### 6.1.6 Public key parameters generation and quality checking

ISRG uses HSMs conforming to FIPS 186-4, capable of providing random number generation and on-board creation of at least 2048-bit RSA keys and at least 384-bit ECDSA keys.

Per [NIST SP 800‐89](https://doi.org/10.6028/NIST.SP.800-89), section 5.3.3, the CA ensures that all RSA keys in ISRG CA and Subscriber certificates have a public exponent of 65537 and an odd modulus which has no factors smaller than 752.

Per [NIST SP 800-56A (Revision 2)](https://doi.org/10.6028/NIST.SP.800-56Ar2), Section 5.6.2.3.2, the CA ensures that all ECDSA keys in ISRG CA and Subscriber certificates comply with the ECC Full Public Key Validation Routine.

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

See Section 7, Certificate Profiles.

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

### 6.2.1 Cryptographic module standards and controls

ISRG uses HSMs validated as meeting FIPS 140-2 Level 3 (or higher) requirements.

### 6.2.2 Private key (n out of m) multi-person control

ISRG has put into place security mechanisms which require multiple people performing in Trusted Roles in order to access ISRG CA Private Keys, both physically and logically. This is true for all copies of Private Keys, in production or backups, on-site or off-site.

### 6.2.3 Private key escrow

ISRG does not escrow CA Private Keys and does not provide such a service for Subscribers.

### 6.2.4 Private key backup

Critical ISRG CA Private Keys are backed up both on-site and off-site, in multiple geographic locations, under multi-person control.

### 6.2.5 Private key archival

ISRG does not archive private keys.

### 6.2.6 Private key transfer into or from a cryptographic module

ISRG CA Private Keys are generated inside HSMs and are only transferred between HSMs for redundancy or backup purposes. When transferred, keys are encrypted prior to leaving HSMs and unwrapped only inside destination HSMs. Keys never exist in plain text form outside of HSMs.

### 6.2.7 Private key storage on cryptographic module

ISRG CA Private Keys are stored on HSMs meeting the requirements stated in Section 6.2.1.

### 6.2.8 Method of activating private key

ISRG CA Private Keys are always stored on HSMs and activated using the mechanisms provided by the HSM manufacturer.

### 6.2.9 Method of deactivating private key

ISRG CA Private Keys are always stored on HSMs and deactivated using the mechanisms provided by the HSM manufacturer.

### 6.2.10 Method of destroying private key

ISRG CA Private Keys are destroyed by Trusted Contributors using a FIPS 140-2 (or higher) validated zeroize method provided by the HSMs storing the keys. Physical destruction of the HSM is not required.

### 6.2.11 Cryptographic Module Rating

See Section 6.2.1.

## 6.3 Other aspects of key pair management

### 6.3.1 Public key archival

See Section 5.5.

### 6.3.2 Certificate operational periods and key pair usage periods

See Section 7.1 for Certificate validity periods.

ISRG Root and Subordinate CA key pairs have lifetimes corresponding to their certificates. Subscriber key pairs may be re-used indefinitely provided that there is no suspicion or confirmation of Private Key compromise.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

Activation data used to activate ISRG CA Private Keys is generated during a key ceremony. Activation data is then transferred to the person who will use it or the place it will be stored.

### 6.4.2 Activation data protection

Activation data is protected from unauthorized disclosure via both physical and logical means.

### 6.4.3 Other aspects of activation data

No stipulation.

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

ISRG PKI infrastructure and systems are appropriately secured in order to protect CA software and data from unauthorized access or modification. Access to systems is secured via multi-factor authentication whenever possible. Security updates are applied in a timely fashion. Vulnerability scans are run regularly.

### 6.5.2 Computer security rating

No stipulation.

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

ISRG has developed policies and procedures to effectively manage the acquisition and development of its CA systems.

ISRG PKI hardware and software is dedicated solely to performing CA functions.

Vendor selection includes an evaluation of reputation in the market, ability to deliver a quality product, vulnerability history, and the likelihood of remaining viable in the future. Physical product deliveries are received by Trusted Contributors and inspected for evidence of tampering. HSMs are shipped in tamper-evident packaging and tamper bag serial numbers are confirmed with the vendor upon receipt.

ISRG maintains a CA testing environment separate from the production environment. The testing environment reasonably emulates the production environment but does not have access to ISRG CA Private Keys used in trusted certificates. The purpose of this testing environment is to allow extensive but safe testing of software and systems that are or will be deployed to the CA production environment.

ISRG has developed and maintains appropriate change control policies and procedures to be followed any time CA systems are modified. Changes to ISRG PKI systems require review by qualified Trusted Personnel who are different from the person requesting the change. Change requests are documented, as are any subsequent required reviews or approvals.

When ISRG develops software to be used in CA operations, software development policies are put into place and methodologies are followed in order to ensure software quality and integrity. This always includes a requirement for peer review of code changes. Code commit privileges are granted only to qualified and trusted contributors. Nobody with the ability to deploy software to ISRG PKI systems may have the ability to unilaterally commit code to core CA software. The reverse is also true.

### 6.6.2 Security management controls

ISRG has mechanisms in place to control and monitor security-related configuration of CA systems. Equipment and software is installed and configured using a documented change control process. Software integrity is verified upon deployment using checksums.

### 6.6.3 Life cycle security controls

No stipulation.

## 6.7 Network security controls

ISRG implements reasonable network security safeguards and controls to prevent unauthorized access to CA systems and infrastructure. ISRG complies with the CA/Browser Forum's Network and Certificate System Security Requirements.

ISRG's network is multi-tiered and utilizes the principle of defense in depth.

Firewalls and other critical CA systems are configured based on a necessary-traffic-only allowlisting policy whenever possible.

ISRG Root CA Private Keys are stored offline in a secure manner.

## 6.8 Time-stamping

See Section 5.5.5.

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

All fields are as specified in RFC 5280 and the Baseline Requirements, including fields and extensions not specifically mentioned.

### Root CA Certificate

| Field or extension             | Value                                                         |
| ------------------------------ | --------------------------------------------------------------|
| Serial Number                  | Unique, with 64 bits of output from a CSPRNG                  |
| Issuer Distinguished Name      | C=US, O=Internet Security Research Group, and a meaningful CN |
| Subject Distinguished Name     | Same as Issuer DN                                             |
| Validity Period                | Up to 25 years                                                |
| Basic Constraints              | cA=True, pathLength constraint absent (critical)              |
| Subject Public Key             | See Sections 6.1.5, 6.1.6, and 7.1.3.1                        |
| Key Usage                      | keyCertSign, cRLSign (critical)                               |

### Subordinate CA Certificate

| Field or extension             | Value                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Serial Number                  | Unique, with 64 bits of output from a CSPRNG                                  |
| Issuer Distinguished Name      | Derived from Issuer certificate                                               |
| Subject Distinguished Name     | C=US, O=Let's Encrypt, and a meaningful CN                                    |
| Validity Period                | Up to 8 years                                                                 |
| Basic Constraints              | cA=True, pathLength constraint 0 (critical)                                   |
| Key Usage                      | keyCertSign, cRLSign, digitalSignature (critical)                             |
| Extended Key Usage             | TLS Server Authentication and optionally TLS Client Authentication            |
| Certificate Policies           | CAB Forum Domain Validated (2.23.140.1.2.1)                                   |
| Authority Information Access   | Contains CA Issuers URL and optionally an OCSP URL; URLs vary based on Issuer |
| Subject Public Key             | See Sections 6.1.5, 6.1.6, and 7.1.3.1                                        |
| CRL Distribution Points        | Contains a CRL URL; URL varies based on Issuer                                |

### DV-SSL Subscriber Certificate

| Field or extension                | Value                                                                             |
| --------------------------------- | --------------------------------------------------------------------------------- |
| Serial Number                     | Unique, with 64 bits of output from a CSPRNG                                      |
| Issuer Distinguished Name         | Derived from Issuer certificate                                                   |
| Subject Distinguished Name        | CN=none, or one of the values from the Subject Alternative Name extension         |
| Validity Period                   | Up to 100 days                                                                    |
| Basic Constraints                 | cA=False (critical)                                                               |
| Key Usage                         | digitalSignature, and optionally keyEncipherment (critical)                       |
| Extended Key Usage                | TLS Server Authentication and optionally TLS Client Authentication                |
| Certificate Policies              | CAB Forum Domain Validated (2.23.140.1.2.1)                                       |
| Authority Information Access      | Contains CA Issuers URL and optionally an OCSP URL; URLs vary based on Issuer     |
| Subject Public Key                | See Sections 6.1.5, 6.1.6, and 7.1.3.1                                            |
| Subject Alternative Name          | A sequence of 1 to 100 dNSNames or ipAddresses (critical if no CN)                |
| TLS Feature                       | Contains status_request if requested by the Subscriber in the CSR                 |
| Precertificate poison             | Per RFC 6962 (precertificates only, critical)                                     |
| Signed Certificate Timestamp List | Per RFC 6962 (final certificates only)                                            |
| CRL Distribution Point            | If present, contains a URI to the CRL shard whose scope includes this certificate |

### 7.1.1 Version number(s)

All certificates use X.509 version 3.

### 7.1.2 Certificate extensions

See section 7.1.

### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

The `AlgorithmIdentifier` field of the `SubjectPublicKeyInfo` field of ISRG Certificates is byte-for-byte identical with one of the hexadecimal encodings specified by Section 7.1.3.1 of the Baseline Requirements.

#### 7.1.3.2 Signature AlgorithmIdentifier

When used in the context of a signature, fields of type `AlgorithmIdentifier` of all objects signed by ISRG CAs are byte-for-byte identical with one of the hexadecimal encodings specified by Section 7.1.3.2 of the Baseline Requirements.

### 7.1.4 Name forms

ISRG does not issue Subscriber Certificates containing the subject:organizationName, subject:givenName, subject:surname, subject:streetAddress, subject:localityName, subject:stateOrProvinceName, subject:postalCode, subject:countryName, or subject:organizationalUnitName fields. The subject:organizationName and subject:countryName fields may be present in our Root CA, Subordinate CA, and other operational certificates.

### 7.1.5 Name constraints

No stipulation.

### 7.1.6 Certificate policy object identifier

See section 7.1.

### 7.1.7 Usage of Policy Constraints extension

Not applicable.

### 7.1.8 Policy qualifiers syntax and semantics

See section 7.1.

### 7.1.9 Processing semantics for the critical Certificate Policies extension

Not applicable.

## 7.2 CRL profile

For the status of Subordinate CA Certificates:

| Field or Extension        | Value                                                                          |
| ------------------------- | ------------------------------------------------------------------------------ |
| Version                   | V2                                                                             |
| Signature Algorithm       | sha256WithRSAEncryption or ecdsa-with-SHA384                                   |
| ThisUpdate                | The date and time when the Certificate revocation list validity begins         |
| NextUpdate                | Up to ThisUpdate + 1 year                                                      |
| RevokedCertificates       | Contains: userCertificate, revocationDate, reasonCode                          |
| CRLnumber                 | The serial number of this CRL in an incrementally increasing sequence of CRLs  |
| IssuingDistributionPoint  | If present, asserts onlyContainsCACerts                                        |

For the status of Subscriber Certificates:

| Field or Extension        | Value                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| Version                   | V2                                                                                           |
| Signature Algorithm       | sha256WithRSAEncryption or ecdsa-with-SHA384                                                 |
| ThisUpdate                | The date and time when the Certificate revocation list validity begins                       |
| NextUpdate                | Up to ThisUpdate + 10 days                                                                   |
| RevokedCertificates       | Contains: userCertificate, revocationDate, reasonCode                                        |
| CRLnumber                 | The serial number of this CRL in an incrementally increasing sequence of CRLs                |
| IssuingDistributionPoint  | Contains a distributionPoint pointing to the CRL's unique URL, asserts onlyContainsUserCerts |

### 7.2.1 Version number(s)

See section 7.2.

### 7.2.2 CRL and CRL entry extensions

No stipulation.

## 7.3 OCSP profile

ISRG OCSP responders, if made available, implement the RFC 5019 profile of RFC 6960.

### 7.3.1 Version number(s)

No stipulation.

### 7.3.2 OCSP extensions

No stipulation.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

WebTrust compliance audits are intended to ensure a CA's compliance with its CP and CPS and relevant WebTrust audit criteria.

## 8.1 Frequency or circumstances of assessment

WebTrust compliance audit periods cover no more than one year and are scheduled by ISRG annually, every year with no gaps.

See Section 8.7 for information about the frequency of self-audits.

## 8.2 Identity/qualifications of assessor

ISRG's WebTrust compliance audits are performed by a licensed WebTrust auditor who is independent from ISRG and qualified per the criteria in Section 8.2 of the Baseline Requirements. 

## 8.3 Assessor's relationship to assessed entity

ISRG's WebTrust auditors shall have no financial interest in, or other type of relationship with, ISRG, which might cause the auditors to have a bias for or against ISRG.

## 8.4 Topics covered by assessment

WebTrust compliance audits cover ISRG's compliance with the ISRG CP/CPS, as well as one of the following two sets of WebTrust principles and criteria:

* Principles and Criteria for Certification Authorities
* WebTrust Principles and Criteria for Certification Authorities – SSL Baseline with Network Security

or

* Principles and Criteria for Certification Authorities
* WebTrust Principles and Criteria for Certification Authorities – SSL Baseline
* WebTrust Principles and Criteria for Certification Authorities – Network Security

## 8.5 Actions taken as a result of deficiency

Noncompliance with relevant requirements will be documented by auditors (internal or external), the ISRG PMA will be informed, and the ISRG PMA will ensure that steps are taken to address the issues as quickly as reasonably possible.

## 8.6 Communication of results

Audit results are reported to the ISRG PMA and any other entity entitled to the results by law, regulation, or agreement. This includes a number of Web user agent (i.e. browser) root programs.

ISRG is not required to publicly disclose any audit finding that does not impact the overall audit opinion.

## 8.7 Self-Audits

ISRG performs a quarterly internal audit of at least a random 3% of issuance since the last WebTrust audit period. This audit includes linting of the selected certificates. Results are saved and provided to auditors upon request.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

ISRG does not charge any fees for certificate issuance or renewal.

### 9.1.2 Certificate access fees

No stipulation.

### 9.1.3 Revocation or status information access fees

ISRG does not charge fees for certificate revocation or status information.

### 9.1.4 Fees for other services

No stipulation.

### 9.1.5 Refund policy

ISRG collects no fees, and so provides no refunds.

## 9.2 Financial responsibility

### 9.2.1 Insurance coverage

No stipulation.

### 9.2.2 Other assets

No stipulation.

### 9.2.3 Insurance or warranty coverage for end-entities

No stipulation.

## 9.3 Confidentiality of business information

### 9.3.1 Scope of confidential information

No stipulation.

### 9.3.2 Information not within the scope of confidential information

No stipulation.

### 9.3.3 Responsibility to protect confidential information

ISRG employees, agents, and contractors are responsible for protecting confidential information and are bound by ISRG's policies with respect to the treatment of confidential information or are contractually obligated to do so. Employees receive training on how to handle confidential information.

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

ISRG follows the privacy policy posted on its website (<https://letsencrypt.org/repository/>) when handling personal information.

### 9.4.2 Information treated as private

The privacy policy posted on ISRG's website (<https://letsencrypt.org/repository/>) identifies information that ISRG treats as private.

### 9.4.3 Information not deemed private

The privacy policy posted on ISRG's website (<https://letsencrypt.org/repository/>) identifies information that ISRG does not treat as private.

### 9.4.4 Responsibility to protect private information

ISRG employees and contractors are subject to policies or contractual obligations requiring them to comply with ISRG's privacy policy (<https://letsencrypt.org/repository/>) or contractual obligations at least as protective of private information as ISRG's privacy policy.

### 9.4.5 Notice and consent to use private information

ISRG follows the privacy policy posted on its website (<https://letsencrypt.org/repository/>) when using personal information.

### 9.4.6 Disclosure pursuant to judicial or administrative process

ISRG may disclose personal information if compelled to do so by court order or other compulsory legal process, provided that if ISRG determines that such court order or legal process is invalid or unconstitutional, ISRG will make reasonable legal efforts to oppose disclosure.

### 9.4.7 Other information disclosure circumstances

ISRG may disclose personal information under other circumstances that are described in the privacy policy posted on its website (<https://letsencrypt.org/repository/>).

## 9.5 Intellectual property rights

ISRG and/or its business partners own the intellectual property rights in ISRG's services, including the certificates, trademarks used in providing the services, and this CP/CPS. Certificate and revocation information are the property of ISRG. ISRG grants permission to reproduce and distribute certificates on a non-exclusive and royalty-free basis, provided that they are reproduced and distributed in full. Private Keys and Public Keys remain the property of the Subscribers who rightfully hold them.

Notwithstanding the foregoing, third party software (including open source software) used by ISRG to provide its services is licensed, not owned, by ISRG.

## 9.6 Representations and warranties

### 9.6.1 CA representations and warranties

Except as expressly stated in this CP/CPS or in a separate agreement with a Subscriber, ISRG does not make any representations or warranties regarding its products or services. ISRG represents and warrants, to the extent specified in this CP/CPS, that:

1. ISRG complies, in all material aspects, with the ISRG CP/CPS,
2. All certificates issued under this CP/CPS will be verified in accordance with this CP/CPS and meet the minimum requirements found herein and in the CAB Forum Baseline Requirements, and
3. ISRG will maintain the Policy and Legal Repository on its website.

### 9.6.2 RA representations and warranties

ISRG does not use RA services from third parties.

### 9.6.3 Subscriber representations and warranties

1. Each Subscriber warrants to ISRG and the public-at-large that Subscriber is the legitimate registrant or assignee of the Identifier that is, or is going to be, the subject of the ISRG certificate issued to Subscriber, or that Subscriber is the duly authorized agent of such entity.
2. Each Subscriber warrants to ISRG and the public-at-large that either (a) Subscriber did not obtain control of such Identifier as the result of a seizure of such Identifier, or (b) such Identifier had no ongoing lawful uses at the time of such seizure.
3. Each Subscriber warrants that all information in the ISRG certificate issued to Subscriber regarding Subscriber or its Identifier is accurate, current, reliable, complete, and not misleading.
4. Each Subscriber warrants that all information provided by Subscriber to ISRG is accurate, current, complete, reliable, complete, and not misleading.
5. Each Subscriber warrants that Subscriber rightfully holds the Private Key corresponding to the Public Key listed in the ISRG certificate issued to Subscriber.
6. Each Subscriber warrants that Subscriber has taken all appropriate, reasonable, and necessary steps to secure and keep Subscriber's Private Key secret.
7. Each Subscriber acknowledges and accepts that ISRG is entitled to revoke Subscriber's ISRG certificates immediately if the Subscriber violates the terms of the Subscriber Agreement or if ISRG discovers that any of Subscriber's ISRG certificates are being used to enable criminal activities such as phishing attacks, fraud, or the distribution of malware.

### 9.6.4 Relying party representations and warranties

Each Relying Party represents and warrants that, prior to relying on an ISRG certificate, it:

1. Obtained sufficient knowledge on the use of digital certificates and PKI,
2. Studied the applicable limitations on the usage of certificates and agrees to ISRG's limitations on its liability related to the use of certificates,
3. Has read, understands, and agrees to this CP/CPS,
4. Will not use an ISRG certificate if the certificate has expired or been revoked, and
5. Will take all reasonable steps to minimize the risk associated with relying on a digital signature, including only relying on an ISRG certificate after considering:
   * Applicable law and the legal requirements for identification of a party, protection of the confidentiality or privacy of information, and enforceability of the transaction;
   * The intended use of the certificate as listed in the certificate or this CP/CPS,
   * The data listed in the certificate,
   * The economic value of the transaction or communication,
   * The potential loss or damage that would be caused by an erroneous identification or a loss of confidentiality or privacy of information in the application, transaction, or communication,
   * The Relying Party's previous course of dealing with the Subscriber,
   * The Relying Party's understanding of trade, including experience with computer-based methods of trade, and
   * Any other indicia of reliability or unreliability pertaining to the Subscriber and/or the application, communication, or transaction.

Any unauthorized reliance on a certificate is at a party's own risk.

### 9.6.5 Representations and warranties of other participants

No stipulation.

## 9.7 Disclaimers of warranties

The use of Services is voluntary and at the Subscriber's own risk. ISRG provides Services "as is" and "as available" without warranties of any kind, except as expressly required by the Baseline Requirements.

## 9.8 Limitations of liability

ISRG does not accept any liability for any loss, harm, claim, or attorney's fees in connection with any certificates. ISRG will not be liable for any damages, attorney's fees, or recovery, regardless of whether such damages are direct, consequential, indirect, incidental, special, exemplary, punitive, or compensatory, even if ISRG has been advised of the possibility of such damages. This limitation on liability applies irrespective of the theory of liability, i.e., whether the theory of liability is based upon contract, warranty, indemnification, contribution, tort, equity, statute or regulation, common law, or any other source of law, standard of care, category of claim, notion of fault or responsibility, or theory of recovery. This disclaimer is intended to be construed to the fullest extent allowed by applicable law.

Without waiving or limiting the foregoing in any way, ISRG does not make, and ISRG expressly disclaims, any warranty regarding its right to use any technology, invention, technical design, process, or business method used in either issuing certificates or providing any of ISRG's services. Each Subscriber affirmatively and expressly waives the right to hold ISRG responsible in any way, or seek indemnification against ISRG, for any infringement of intellectual property rights, including patent, trademark, trade secret, or copyright.

## 9.9 Indemnities

### 9.9.1 Indemnification by ISRG

#### 9.9.1.1 Indemnification of Application Software Suppliers

ISRG shall indemnify each Application Software Supplier that has a Root Certificate distribution agreement in place with the Root CA against any damage or loss suffered by such an Application Software Supplier related to or arising out of any third-party allegation, claim, lawsuit, or proceeding (a "Claim") to the extent such Claim is based on a Certificate issued by ISRG except where the claim, damage, or loss suffered by the Application Software Supplier was directly caused by the Application Software Supplier's software or service displaying either:

(a) a valid and trustworthy Certificate as not valid or trustworthy, or  
(b) displaying as trustworthy either (i) a Certificate that has expired, or (ii) a revoked Certificate, where the revocation status is available online but the Application Software Supplier's software or service failed to check or ignored the status.

#### 9.9.1.2 Indemnification Process

In connection with any Claim described in the foregoing paragraph 9.9.1.1, the indemnified party will:

(a) give ISRG prompt written notice of the Claim (provided that any delay in notification will not relieve ISRG of its indemnity obligations except to the extent that the delay impairs its ability to defend);  
(b) cooperate reasonably with ISRG (at ISRG's expense) in connection with the defense and settlement of the Claim; and  
(c) permit ISRG to control the defense and settlement of the Claim, provided that ISRG may not settle the Claim without the indemnified party's prior written consent (which will not be unreasonably withheld or delayed), and provided further that the indemnified party (at its cost) may participate in the defense and settlement of the Claim with counsel of its own choosing. ISRG's duty to indemnify under this Section 9.9.1 is independent from its other obligations under this CP/CPS.

### 9.9.2 Indemnification by Subscribers

To the extent permitted by law, each Subscriber shall indemnify ISRG, its partners, and any cross-signed entities, and their respective directors, officers, employees, agents, and contractors against any loss, damage, or expense, including reasonable attorney's fees, arising out of or related to:

(a) any misrepresentation or omission by Subscriber, regardless of whether the misrepresentation or omission was intentional or unintentional;  
(b) Subscriber's breach of its Subscriber Agreement, this CP/CPS, or applicable law;  
(c) the compromise or unauthorized use of a certificate or Private Key caused by the Subscriber's negligence or intentional acts; or  
(d) Subscriber's misuse of a certificate or Private Key.

### 9.9.3	Indemnification by Relying Parties

To the extent permitted by law, each Relying Party shall indemnify ISRG, its partners, and any cross-signed entities, and their respective directors, officers, employees, agents, and contractors against any loss, damage, or expense, including reasonable attorney's fees, arising out of or related to: 

(a) breach of any service terms applicable to the services provided by ISRG or its affiliates and used by the Relying Party, this CP/CPS, or applicable law;  
(b) unreasonable reliance on a Certificate; or  
(c) failure to check the Certificate's status prior to use.

## 9.10 Term and termination

### 9.10.1 Term

This CP/CPS and any amendments to this CP/CPS are effective when published to the ISRG online repository and remain in effect until replaced with a newer version.

### 9.10.2 Termination

This CP/CPS and any amendments remain in effect until replaced with a newer version.

### 9.10.3 Effect of termination and survival

ISRG will communicate the conditions and effect of this CP/CPS's termination via the ISRG Repository. The communication will specify which provisions survive termination. At a minimum, all responsibilities related to protecting confidential information will survive termination. All Subscriber Agreements remain effective at least until the certificate is revoked or expired, even if this CP/CPS terminates.

## 9.11 Individual notices and communications with participants

ISRG accepts notices related to this CP/CPS at the locations specified in Section 1.5.2 of this CP/CPS. Notices are deemed effective after the sender receives a valid and digitally signed acknowledgment of receipt from ISRG. If an acknowledgement of receipt is not received within five days, the sender must resend the notice in paper form to the street address specified in Section 1.5.2 of this CP/CPS using either a courier service that confirms delivery or via certified or registered mail with postage prepaid and return receipt requested. ISRG may allow other forms of notice in its Subscriber Agreements.

## 9.12 Amendments

### 9.12.1 Procedure for amendment

This CP/CPS is reviewed at least annually and may be reviewed more frequently. Amendments are made by posting an updated version of this CP/CPS to the online repository. Controls are in place that are designed to reasonably ensure that this CP/CPS is not amended and published without the prior authorization of the ISRG PMA.

### 9.12.2 Notification mechanism and period

ISRG posts CP/CPS revisions to its Repository. ISRG does not guarantee or set a notice-and-comment period and may make changes to this CP/CPS without notice.

### 9.12.3 Circumstances under which OID must be changed

The ISRG PMA is solely responsible for determining whether an amendment to this CP/CPS requires an OID change.

## 9.13 Dispute resolution provisions

Any claim, suit or proceeding arising out of this CP/CPS or any ISRG product or service must be brought in a state or federal court located in San Jose, California. ISRG may seek injunctive or other relief in any state, federal, or national court of competent jurisdiction for any actual or alleged infringement of its, its affiliates, or any third party's intellectual property or other proprietary rights.

## 9.14 Governing law

The laws of the state of California, United States of America, govern the interpretation, construction, and enforcement of this CP/CPS and all proceedings related to ISRG products and services, including tort claims, without regard to any conflicts of law principles. The United Nations Convention for the International Sale of Goods does not apply to this CP/CPS.

## 9.15 Compliance with applicable law

This CP/CPS is subject to all applicable laws and regulations, including United States restrictions on the export of software and cryptography products.

## 9.16 Miscellaneous provisions

### 9.16.1 Entire agreement

ISRG requires each party using its products and services to enter into an agreement that delineates the terms associated with the product or service. If an agreement has provisions that differ from this CP/CPS, then the agreement with that party controls, but solely with respect to that party. Third parties may not rely on or bring action to enforce such agreement.

### 9.16.2 Assignment

Any entities operating under this CP/CPS may not assign their rights or obligations without the prior written consent of ISRG. Unless specified otherwise in a contract with a party, ISRG does not provide notice of assignment.

### 9.16.3 Severability

If any provision of this CP/CPS is held invalid or unenforceable by a competent court or tribunal, the remainder of this CP/CPS will remain valid and enforceable. Each provision of this CP/CPS that provides for a limitation of liability, disclaimer of a warranty, or an exclusion of damages is severable and independent of any other provision.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

ISRG may seek indemnification and attorneys' fees from a party for damages, losses, and expenses related to that party's conduct. ISRG's failure to enforce a provision of this CP/CPS does not waive ISRG's right to enforce the same provision later or right to enforce any other provision of this CP/CPS. To be effective, waivers must be in writing and signed by ISRG.

### 9.16.5 Force Majeure

ISRG is not liable for any delay or failure to perform an obligation under this CP/CPS to the extent that the delay or failure is caused by an occurrence beyond ISRG's reasonable control. The operation of the Internet is beyond ISRG's reasonable control.

## 9.17 Other provisions

No stipulation.
