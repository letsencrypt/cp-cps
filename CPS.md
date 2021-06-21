# 1. INTRODUCTION

## 1.1 Overview

This Certification Practice Statement ("CPS") document outlines the certification services practices for Internet Security Research Group ("ISRG") Public Key Infrastructure ("ISRG PKI").

ISRG PKI services include, but are not limited to, issuing, managing, validating, revoking, and renewing Certificates in accordance with the requirements of the ISRG Certificate Policy (CP). It is recommended that readers familiarize themselves with the ISRG CP prior to reading this document.

ISRG PKI services are most commonly, but not necessarily exclusively, provided under the brand/trademark "Let's Encrypt".

The ISRG PKI conforms to the current version of the guidelines adopted by the Certification Authority/Browser Forum (“CAB Forum”) when issuing publicly trusted certificates, including the Baseline Requirements for the Issuance and Management of Publicly Trusted Certificates (“Baseline Requirements”). CAB Forum documents can be found at https://www.cabforum.org. If there is any conflict between this CPS and a relevant CAB Forum requirement or guideline, then the CAB Forum requirement or guideline shall take precedence.

Other documents related to the behavior and control of the ISRG PKI, such as a Subscriber Agreement and Privacy Policy, can be found at https://letsencrypt.org/repository/.

Per IETF PKIX RFC 3647, this CPS is divided into nine components that cover security controls, practices, and procedures for certification services provided by the ISRG PKI.

The following Certification Authorities are covered under this CPS:

| CA Type | Distinguished Name | Key Pair Type and Parameters | Cert SHA-256 Fingerprint | Validity Period |
|---------|--------------------|------------------------------|--------------------------|-----------------|
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X1 | RSA, n has 4096 bits, e=65537 | 96:BC:EC:06:26:49:76:F3:<br>74:60:77:9A:CF:28:C5:A7:<br>CF:E8:A3:C0:AA:E1:1A:8F:<br>FC:EE:05:C0:BD:DF:08:C6 | Not Before: Jun  4 11:04:38 2015 GMT,<br>Not After: Jun  4 11:04:38 2035 GMT |
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X2 | ECDSA, NIST curve P-384 | 69:72:9b:8e:15:a8:6e:fc:<br>17:7a:57:af:b7:17:1d:fc:<br>64:ad:d2:8c:2f:ca:8c:f1:<br>50:7e:34:45:3c:cb:14:70 | Not Before: Sept  4 00:00:00 2020 GMT,<br>Not After: Sept 17 16:00:00 2040 GMT |

This work is licensed under the Creative Commons Attribution 4.0 International License. To
view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative
Commons, PO Box 1866, Mountain View, CA 94042, USA.

## 1.2 Document name and identification

This is the ISRG Certification Practices Statement. This document was approved for publication by the ISRG Policy Management Authority, and is made available at https://letsencrypt.org/repository/.

The following revisions have been made:

| Date              | Changes                                            | Version |
|-------------------|----------------------------------------------------|---------|
| May 5, 2015 | Original. | 1.0 |
| September 9, 2015 | Added/corrected a number of policy URIs, removed LDAP as mechanism for publishing certificate information, removed administrative contact requirement for DV-SSL subscribers, removed mention of web-based revocation option, removed description of customer service center, substantial changes to all of Section 9 regarding legal matters, other minor fixes/improvements. | 1.1 |
| September 22, 2015 | Updated serial number description in Section 10.3.1, DV-SSL Certificate Profiles. | 1.2 |
| March 16, 2016 | Update root CRL issuance periods, disallow issuance to ‘.mil’ TLD, make NameConstraints extension optional for cross- certification profile, clarify optional NameConstraints contents, clarify that OSCP ResponderID is byname, clarify that OCSP nonce extension is not supported. | 1.3 |
| May 5, 2016 | Reference CP v1.2 rather than CP v1.1. Add info about tlsFeature extension, serialNumber in Subject Distinguished Name field. | 1.4 |
| October 18, 2016 | Do not require discontinuing use of a private key due to incorrect information in a certificate. Add information about issuance for Internationalized Domain Names. Add information about CA’s CAA identifying domain. Do not require discontinuing use of a private key due to expiration or revocation of a certificate. | 1.5 |
| April 13, 2017 | Complete rewrite of CPS. | 2.0 |
| February 6, 2018 | Remove restriction on issuing to '.mil' TLD. | 2.1 |
| March 10, 2018 | Remove text stating that wildcard certificates are not supported. Clarify that wildcard validation must use DNS Change method. | 2.2 |
| May 4, 2018 | Add CT fields to certificate profiles. Specify current Baseline Requirements compliance for all validations. Update certificate expiration notice text. Remove reference loops. Minor cleanup. | 2.3 |
| September 20, 2018 | Define Certificate Problem Reports in Section 1.6.1. Add information about submitting Certificate Problem Reports to Section 1.5.2. | 2.4 |
| November 14, 2018 | Remove user notice text from end-entity certificate profile in Section 7.1. | 2.5 |
| July 3, 2019 | Minor grammatical and capitalization changes. | 2.6 |
| January 21, 2020 | Make structure more exactly match RFC 3647 recommendation. Audit use of phrase No Stipulation and eliminate blank sections. Remove restriction on issuance for IP addresses in Section 7.1.5. Update lists of appropriate and prohibited certificate uses in Sections 1.4.1 and 1.4.2. Clarify annual vulnerability assessment requirements in Section 5.4.8. | 2.7 |
| May 28, 2020 | Specify in Section 4.9.3 that revocations for key compromise will result in blocking of the public key for future issuance and revocation of other outstanding certificates with the key. Update description of Certificate Transparency submissions. | 2.8 |
| July 14, 2020 | Clarify revocation request instructions in Section 4.9.3. | 2.9 |
| October 27, 2020 | List ISRG Root X2 in section 1.1. Update Section 3.2.2 to clarify that ISRG never performs domain validation manually. Update Section 9 to eliminate references to third party RAs, as ISRG does not use or allow them. | 3.0 |
| April 2, 2021 | Update CPS for ECDSA hierarchy. Update ISRG physical address. Inclusivity language improvement.  | 3.1 |
| April 20, 2021 | Clarifications regarding revocation process for Section 4.9.3. Clarify OCSP availability for intermediate certificates in Section 4.9.9. | 3.2 |
| June  8, 2021 | Section 7.1 end entity certificate lifetime specification updated to match Section 6.3.2. Update BR references in Section 3.2.2. Add Section 4.2.4 regarding CAA checking. State in Section 6.7 that the CA complies with the CA/Browser Forum’s Network and Certificate System Security Requirements. | 3.3 |

## 1.3 PKI participants

### 1.3.1 Certification authorities

ISRG is a CA that provides services including, but not limited to, issuing, managing, validating, revoking, and renewing publicly-trusted Certificates. These services are performed in accordance with the requirements of the ISRG Certificate Policy (CP) and this CPS. These services are provided to the general public with exceptions as deemed appropriate by ISRG management or in accordance with relevant law.

ISRG PKI services are most commonly, but not necessarily exclusively, provided under the brand/trademark "Let's Encrypt".

### 1.3.2 Registration authorities

ISRG serves as its own RA. RA services are not performed by third parties.

### 1.3.3 Subscribers

See definition of "Subscriber" in Section 1.6.1 Definitions.

### 1.3.4 Relying parties

See definition of "Relying Party" in Section 1.6.1 Definitions.

Relying Parties must verify the validity of certificates via CRL or OCSP prior to relying on certificates. CRL and OCSP location information is provided within certificates.

### 1.3.5 Other participants

Other participants include CAs that cross-sign or issue subordinates to the ISRG PKI.

ISRG PKI vendors and service providers with access to confidential information or privileged systems are required to operate in compliance with the ISRG CP.

## 1.4 Certificate usage

### 1.4.1 Appropriate certificate uses

No stipulation.

### 1.4.2 Prohibited certificate uses

Certificates may not be used:

* For any application requiring fail-safe performance such as a) the operation of nuclear power facilities b) air traffic control systems c) aircraft navigation systems d) weapons control systems e) any other system in which failure could lead to injury, death, or environmental damage.
* For software or hardware architectures that provide facilities for interference with encrypted communications, including but not limited to a) active eavesdropping (e.g., Man-in-the-middle attacks) b) traffic management of domain names or internet protocol (IP) addresses that the organization does not own or control. Note that these restrictions shall apply regardless of whether a relying party communicating through the software or hardware architecture has knowledge of its providing facilities for interference with encrypted communications.

Note that Certificates do not guarantee anything regarding reputation, honesty, or the current state of endpoint security. A Certificate only represents that the information contained in it was verified as reasonably correct when the Certificate was issued.

## 1.5 Policy administration

### 1.5.1 Organization administering the document

This CPS document is maintained by the ISRG PMA.

### 1.5.2 Contact person

The ISRG PMA can be contacted at:

Policy Management Authority<br/>
Internet Security Research Group<br/>
548 Market St., PMB 57274<br/>
San Francisco, CA 94104-5401<br/>
USA<br/>

Certificate revocation requests can be made via the ACME API. Please see Section 4.9.3 for more information.

Certificate Problem Reports can be submitted via email to:

[cert-prob-reports@letsencrypt.org](mailto:cert-prob-reports@letsencrypt.org)

### 1.5.3 Person determining CPS suitability for the policy

The ISRG PMA is responsible for determining the suitability of this CPS. The ISRG PMA is informed by results and recommendations received from an independent auditor.

### 1.5.4 CPS approval procedures

The ISRG PMA approves any revisions to this CPS document after formal review.

## 1.6 Definitions and acronyms

### 1.6.1 Definitions

* ACME Protocol
  * A protocol used for validation, issuance, and management of certificates. The protocol is an open standard managed by the IETF.
* Applicant
  * An entity applying for a certificate.
* Baseline Requirements
  * A document published by the CAB Forum which outlines minimum requirements for publicly trusted Certificate Authorities.
* CAB Forum
  * Certificate Authority / Browser Forum, a group a CAs and browsers which come together to discuss technical and policy issues related to PKI systems. (https://cabforum.org/)
* Certificate Problem Report
  * Complaint of suspected Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, or inappropriate conduct related to Certificates.
* Certificate Repository
  * A repository of information about ISRG certificates. It is located at: https://letsencrypt.org/certificates/
* Cross Certificate
  * A certificate that is used to establish a trust relationship between two Root CAs.
* Policy and Legal Repository
  * A repository of policy and legal documents related to the ISRG PKI. It is located at: https://letsencrypt.org/repository/
* Key Pair
  * A Private Key and its associated Public Key.
* Precertificate
  * A certificate containing a critical poison extension as defined by RFC 6962 Section 3.1.
* Private Key
  * The key in a Key Pair that must be kept secret. Used to create digital signatures that can be verified by the corresponding Public Key or to decrypt messages encrypted by the corresponding Public Key.
* Public Key
  * The only key in a Key Pair that can safely be publicly disclosed. Used by Relying Parties to verify digital signatures from the corresponding private key or to encrypt messages that can only be decrypted by the corresponding private key.
* Relying Party
  * An entity that relies upon information contained within certificates issued by ISRG PKI services.
* Root CA
  * The top-level Certification Authority whose Root Certificate is distributed by Application Software Suppliers and that issues Subordinate CA Certificates.
* Secure PKI Facilities
  * Facilities designed to protect sensitive PKI infrastructure, including CA private keys.
* Subscriber
  * An entity that has agreed to a Subscriber Agreement and is using ISRG PKI services.
* Trusted Contributor
  * A contributor who performs in a Trusted Role. Trusted Contributors may be employees, contractors, or community members. Trusted Contributors must be properly trained and qualified, and have the proper legal obligations in place before performing in a Trusted Role.
* Trusted Role
  * A role which qualifies a person to access or modify ISRG PKI systems, infrastructure, and confidential information.

### 1.6.2 Acronyms

* ACME
  * Automated Certificate Management Environment
* CA
  * Certificate Authority
* CAA
  * Certificate Authority Authorization
* CP
  * Certificate Policy
* CPS
  * Certification Practice Statement
* DV
  * Domain Validation
* FQDN
  * Fully Qualified Domain Name
* HSM
  * Hardware Security Module
* IDN
  * Internationalized Domain Name
* IP
  * Internet Protocol
* ISRG
  * Internet Security Research Group
* PKI
  * Public Key Infrastructure
* PMA
  * Policy Management Authority
* RA
  * Registration Authority
* SAN
  * Subject Alternative Name
* TLD
  * Top Level Domain

### 1.6.3 References

No references defined at this time.

### 1.6.4 Conventions

Terms not otherwise defined in this CPS shall be as defined in applicable agreements, user manuals, Certificate Policies and Certification Practice Statements, of the CA.

The key words “MUST”, “MUST NOT”, "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in these Requirements shall be interpreted in accordance with RFC 2119.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

## 2.1 Repositories

ISRG CP, CPS, Privacy Policy, Subscriber Agreement, and WebTrust audit documents are made publicly available in the Policy and Legal Repository, which can be found at:

https://letsencrypt.org/repository/

## 2.2 Publication of certification information

Records of all ISRG root and intermediate certificates, including those that have been revoked, are available in the Certificate Repository:

https://letsencrypt.org/certificates/

ISRG certificates contain URLs to locations where certificate-related information is published, including revocation information via OCSP and/or CRLs.

## 2.3 Time or frequency of publication

New or updated ISRG CP, CPS, Privacy Policy, Subscriber Agreement, and WebTrust audit documents are made publicly available as soon as possible. This typically means within seven days of receipt or approval.

New or updated ISRG root and intermediate certificates are made publicly available as soon as possible. This typically means within seven days of creation.

## 2.4 Access controls on repositories

Read only access to the Policy and Legal Repository and certificate information is unrestricted. Write access is protected by logical and physical controls.

# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

### 3.1.1 Types of names

Certificate distinguished names and subject alternative names are compliant with the CP.

### 3.1.2 Need for names to be meaningful

ISRG certificates include a "Subject" field which identifies the subject entity (i.e. organization or domain). The subject entity is identified using a distinguished name.

ISRG certificates include an "Issuer" field which identifies the issuing entity. The issuing entity is identified using a distinguished name.

### 3.1.3 Anonymity or pseudonymity of subscribers

Subscribers are not identified in DV certificates, which have subject fields identifying only domain names (not people or organizations). Relying parties should consider DV certificate subscribers to be anonymous.

### 3.1.4 Rules for interpreting various name forms

Distinguished names in certificates are to be interpreted using X.500 standards and ASN.1 syntax.

Certificates do not assert any specific relationship between subscribers and registrants of domain names contained in certificates.

Regarding Internationalized Domain Names, ISRG will have no objection so long as the domain is resolvable via DNS. It is the CA’s position that homoglyph spoofing should be dealt with by registrars, and Web browsers should have sensible policies for when to display the punycode versions of names.

### 3.1.5 Uniqueness of names

No stipulation.

### 3.1.6 Recognition, authentication, and role of trademarks

ISRG reserves the right to make all decisions regarding Subscriber names in certificates. Entities requesting certificates will be required to demonstrate their right to use names (e.g. demonstrate control of a domain name), but trademark rights are not verified.

While ISRG will comply with U.S. law and associated legal orders, it is ISRG's position that trademark enforcement responsibility for domain names should lie primarily with domain registrars and the legal system.

## 3.2 Initial identity validation

ISRG may elect not to issue any certificate at its sole discretion.

### 3.2.1 Method to prove possession of private key

Applicants are required to prove possession of the Private Key corresponding to the Public Key in a Certificate request, which can be done by signing the request with the Private Key.

### 3.2.2 Authentication of organization and domain identity

ISRG only issues Domain Validation (DV) certificates. When a certificate request includes a list of FQDNs in a SAN list, all domains in the list are fully validated prior to issuance.

Validation for DV certificates involves demonstrating proper control over a domain. ISRG validates domain control in an automated fashion via the ACME protocol.

There are three methods used for demonstrating domain control:

1. Agreed-Upon Change to Website - ACME: Confirming the Applicant’s control over the requested FQDN by confirming the presence of agreed-upon content contained in a file or on a web page under the “/.well-known/acme-challenge/” directory on the requested FQDN that is accessible to the CA via HTTP over port 80, following redirects. (BR Section 3.2.2.4.19)

2. DNS Change: Confirming the Applicant’s control over the requested FQDN by confirming the presence of a random value (with at least 128 bits entropy) in a DNS TXT or CAA record for the requested FQDN prefixed with the label '\_acme-challenge'. (BR Section 3.2.2.4.7)

3. TLS Using ALPN: Confirming the Applicant’s control over the requested FQDN by confirming the presence of a random value (with at least 128 bits entropy) within a Certificate on the requested FQDN which is accessible to the CA via TLS over port 443. (BR Section 3.2.2.4.20)

Validation for wildcard domain requests must be completed using the DNS Change method.

All validations are performed in compliance with the current CAB Forum Baseline Requirements at the time of validation.

### 3.2.3 Authentication of individual identity

ISRG does not issue certificates to individuals, and thus does not authenticate individual identities.

### 3.2.4 Non-verified subscriber information

Non-verified Applicant information is not included in ISRG certificates.

### 3.2.5 Validation of authority

ISRG does not issue certificates to organizations, and thus does not validate any natural person's authority to request certificates on behalf of organizations.

Organizations have the option to specify CA issuance authority via CAA records, which ISRG respects.

### 3.2.6 Criteria for interoperation

ISRG discloses Cross Certificates in its Certificate Repository:

https://letsencrypt.org/certificates/

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

See Section 4.7.

### 3.3.2 Identification and authentication for re-key after revocation

See Section 4.7.

## 3.4 Identification and authentication for revocation request

Identification and authentication for revocation requests is performed by ISRG in compliance with Section 4.9 of this document.

Identification and authentication are not required when revocation is being requested by ISRG.

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate application

### 4.1.1 Who can submit a certificate application

Anyone may submit an application for a certificate via the ACME protocol. Issuance will depend on proper validation and compliance with ISRG policies.

### 4.1.2 Enrollment process and responsibilities

The enrollment process involves the following steps, in no particular order:

* Generating a key pair using secure methods
* Submitting a request for a certificate containing all necessary information, including the public key
* Agreeing to the relevant Subscriber Agreement

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions

ISRG performs all identification and authentication functions in accordance with the ISRG CP. This includes validation per CPS Section 3.2.2.

ISRG checks for relevant CAA records prior to issuing certificates. The CA acts in accordance with CAA records if present. The CA’s CAA identifying domain is ‘letsencrypt.org’.

### 4.2.2 Approval or rejection of certificate applications

Approval requires successful completion of validation per Section 3.2.2 as well as compliance with all CA policies.

Certificates containing a new gTLD under consideration by ICANN will not be issued. The CA Server will periodically be updated with the latest version of the Public Suffix List and will consult the ICANN domains section for every requested DNS identifier. CA server will not validate or issue for DNS identifiers that do not have a Public Suffix in the ICANN domains section. The Public Suffix List is updated when new gTLDs are added, and never includes new gTLDs before they are resolvable.

ISRG maintains a list of high-risk domains and blocks issuance of certificates for those domains. Requests for removal from the high-risk domains list will be considered, but will likely require further documentation confirming control of the domain from the Applicant, or other proof as deemed necessary by ISRG management.

### 4.2.3 Time to process certificate applications

No stipulation.

### 4.2.4 CAA Record Checking

As part of the issuance process, ISRG will check for CAA records and follow the processing instructions found, for each dNSName in the subjectAltName extension of the certificate to be issued, as specified in RFC 8659. If the CA issues, the CA will do so within the TTL of the CAA record, or 8 hours, whichever is greater.

See Section 3.2.2.8 of the ISRG CP for more information about CAA checking policy.

## 4.3 Certificate issuance

### 4.3.1 CA actions during certificate issuance

Certificates issued by the Root CA require an individual authorized by ISRG to deliberately issue a direct command in order for the Root CA to perform a certificate signing operation.

The source of a certificate request is confirmed before issuance. CA processes are protected from unauthorized modification during certificate issuance. Issued certificates are stored in a database and then made available to the Subscriber.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate

End-entity certificates are made available to Subscribers via the ACME protocol as soon after issuance as reasonably possible. Typically this happens within a few seconds.

## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance

See ISRG CP Section 4.4.1.

### 4.4.2 Publication of the certificate by the CA

All root and intermediate certificates are made available publicly via the Certificate Repository.

All end-entity certificates are made available to Subscribers via the ACME protocol.

For each end-entity certificate issuance, ISRG signs a Precertificate and
submits it to a selection of Certificate Transparency logs. Upon successful
submission, ISRG will attempt to issue a certificate that matches the
Precertificate (per RFC 6962 Section 3.1) and embeds at least two of the resulting
Signed Certificate Timestamps (SCTs). ISRG submits the resulting final certificate
to a selection of Certificate Transparency logs on a best-effort basis.

ISRG does not guarantee issuance of a final certificate for every Precertificate.

### 4.4.3 Notification of certificate issuance by the CA to other entities

See Section 4.4.2.

## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

Subscribers are obligated to generate Key Pairs using reasonably trustworthy systems.

Subscribers are obligated to take reasonable measures to protect their Private Keys from unauthorized use or disclosure (which constitutes compromise). Subscribers must discontinue use of any Private Keys that are known or suspected to have been compromised.

Certificates must be used in accordance with their intended purpose, which is outlined in this CPS and the associated CP. Subscribers must cease use of certificates being used outside of their intended purpose.

### 4.5.2 Relying party public key and certificate usage

Relying Parties must fully evaluate the context in which they are relying on certificates and the information contained in them, and decide to what extent the risk of reliance is acceptable. If the risk of relying on a certificate is determined to be unacceptable, then Relying Parties should not use the certificate or should obtain additional assurances before using the certificate.

ISRG does not warrant that any software used by Relying Parties to evaluate or otherwise handle certificates does so properly.

Relying Parties ignoring certificate expiration, revocation data provided via OCSP or CRL, or other pertinent information do so at their own risk.

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

Certificate revocation permanently ends the certificate's operational period prior to its stated validity period.

### 4.9.1 Circumstances for revocation

ISRG will follow the ISRG CP and revoke a certificate in accordance with Section 4.9.1.1 and Section 4.9.1.2 of the ISRG CP.

ISRG maintains a continuous (24x7x365) ability to accept and respond to revocation requests and related inquiries.

### 4.9.2 Who can request revocation

Anyone can revoke any certificate via the ACME API if they can sign the revocation request with the private key associated with the certificate. No other information is required in such cases. A number of ACME clients support this functionality.

Anyone can revoke any certificate via the ACME API if they can demonstrate control over all domains covered by the certificate. No other information is required in such cases. A number of ACME clients support this functionality.

Subscribers can revoke certificates belonging to their accounts via the ACME API if they can sign the revocation request with the associated account private key. No other information is required in such cases. A number of ACME clients support this.

Certificates may be administratively revoked by ISRG if it is determined that the Subscriber has failed to meet obligations under the CP, this CPS, the relevant Subscriber Agreement, or any other applicable agreement, regulation, or law. Certificates may also be administratively revoked at the discretion of ISRG management.

### 4.9.3 Procedure for revocation request

Revocation requests may be made by anyone, at any time, via the Certificate Revocation interface of the ACME Protocol defined in RFC 8555 section 7.6. Successful revocation requests with a reason code of `keyCompromise` will result in the affected key being blocked for future issuance and all currently valid certificates with that key will be revoked.

Requests for revocation may also be made by emailing [cert-prob-reports@letsencrypt.org](mailto:cert-prob-reports@letsencrypt.org). ISRG will respond to such requests within 24 hours, though an investigation into the legitimacy of the request may take longer.

An investigation into whether revocation or other appropriate action is warranted will be based on at least the following criteria:

1. The nature of the alleged problem;
2. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
3. The entity making the complaint; and
4. Relevant legislation.

### 4.9.4 Revocation request grace period

There is no grace period for a revocation request. A revocation request must be made as soon as circumstances requiring revocation are confirmed.

### 4.9.5 Time within which CA must process the revocation request

Investigation into a revocation request will begin within 24 hours of receiving the request.

Once a decision has been made to revoke a certificate, revocation will be carried out within 24 hours.

### 4.9.6 Revocation checking requirement for relying parties

Relying Parties who cannot or choose not to check revocation status, but decide to rely on a certificate anyway, do so at their own risk.

See Section 4.5.2.

### 4.9.7 CRL issuance frequency (if applicable)

ISRG will issue updated CRLs for intermediate certificates with a frequency greater than or equal to that required by the ISRG CP.

ISRG does not issue CRLs for end-entity certificates.

### 4.9.8 Maximum latency for CRLs (if applicable)

When a CRL is requested by a Relying Party the time to receive a response will be less than ten seconds under normal operating conditions.

### 4.9.9 On-line revocation/status checking availability

Revocation information will be made available for all end-entity certificates via OCSP. Revocation information may be made available for intermediate certificates via OCSP.

### 4.9.10 On-line revocation checking requirements

See Section 4.9.6.

### 4.9.11 Other forms of revocation advertisements available

ISRG allows for OCSP stapling.

### 4.9.12 Special requirements re key compromise

See Section 4.9.3.

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

CRL entries for intermediate certificates will remain in place until the certificates expire. ISRG does not provide CRLs for end-entity certificates.

OCSP responses will be made available for all unexpired certificates.

### 4.10.2 Service availability

All certificate status services are made available at all times (24x7x365) if possible.

### 4.10.3 Optional features

No stipulation.

## 4.11 End of subscription

A Subscriber's subscription ends once all of Subscriber's ISRG certificates have expired or been revoked.

Prior to expiration of a Subscriber's certificate, ISRG may send Subscriber a notice regarding upcoming Certificate expiration if a contact email address was provided.

## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices

Not applicable.

### 4.12.2 Session key encapsulation and recovery policy and practices

Not applicable.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

## 5.1 Physical controls

### 5.1.1 Site location and construction

ISRG Secure PKI Facilities are located in the United States, as are all copies of CA root and intermediate private keys.

ISRG maintains at least two Secure PKI Facilities at all times for the sake of redundancy.

Secure PKI Facilities are constructed so as to prevent unauthorized entry or interference.

Secure PKI Facilities are monitored at all times (24x7x365) so as to prevent unauthorized entry or interference.

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

ISRG prohibits any media that contains or has contained sensitive data from leaving organizational control in such a state that it may still be operational, or contain recoverable data. Such media may include printed documents or digital storage devices. When media that has contained sensitive information reaches its end of life, the media is physically destroyed such that recovery is reasonably believed to be impossible.

### 5.1.8 Off-site backup

ISRG maintains multiple backups of private keys at multiple Secure PKI Facilities. All backups are stored on devices meeting FIPS 140 Level 3 criteria.

## 5.2 Procedural controls

### 5.2.1 Trusted roles

All persons, employees or otherwise, with the ability to materially impact the operation of ISRG PKI systems and services, or the ability to view CA confidential information, must do so while designated as serving in a Trusted Role.

Trusted Roles include, but are not limited to:

* Management
  * May view confidential information but may not directly impact CA operations. Strong decision-making authority.
* Security Officers
  * May view confidential information but may not directly impact CA operations. Strong decision-making authority.
* Systems Administrators
  * May view confidential information and directly impact CA operations. Decision-making authority is limited.
* Engineering Liaisons
  * May view confidential information but may not directly impact CA operations. No decision-making authority.

Each Trusted Role requires an appropriate level of training and legal obligation.

### 5.2.2 Number of persons required per task

A number of tasks, such as key generation and entering areas physically containing operating ISRG PKI systems, require at least two people in Trusted Roles to be present.

### 5.2.3 Identification and authentication for each role

Anyone performing work in a Trusted Role must identify and authenticate themselves before accessing ISRG PKI systems or confidential information.

### 5.2.4 Roles requiring separation of duties

Nobody with the ability to deploy software to ISRG PKI systems (e.g. Systems Administrators) may have the ability to commit code to core CA software. The reverse is also true.

## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

ISRG management is responsible for making sure that Trusted Contributors are trustworthy and competent, which includes having proper qualifications and experience.

ISRG management ensures this with appropriate interviewing practices, training, background checks, and regular monitoring and review of Trusted Contributor job performance.

### 5.3.2 Background check procedures

Trusted Contributors must undergo a background check prior to performing in a trusted role. ISRG management will review the results of background checks for problematic issues prior to approving performance of a trusted role.

Background checks include, but are not limited to, criminal background and employment history.

### 5.3.3 Training requirements

Trusted Contributors must be trained on topics relevant to the role in which they will perform.

Training programs are developed for each role by ISRG management and Security Officers.

### 5.3.4 Retraining frequency and requirements

Training is repeated for each Trusted Contributor on an annual basis and re-covers all topics relevant to their trusted role.

Training is also offered whenever changes in the industry or operations require it in order for contributors to competently perform in their trusted roles.

### 5.3.5 Job rotation frequency and sequence

No stipulation.

### 5.3.6 Sanctions for unauthorized actions

Action will be taken to safeguard ISRG and its subscribers whenever ISRG Trusted Contributors, whether through negligence or malicious intent, fail to comply with ISRG policies including this CPS.

Actions taken in response to non-compliance may include termination, removal from trusted roles, or reporting to legal authorities.

Once management becomes aware of non-compliance the Trusted Contributor(s) in question will be removed from trusted roles until a review of their actions is complete.

### 5.3.7 Independent contractor requirements

Independent contractors who are assigned to perform Trusted Roles are subject to the duties and requirements specified for such roles in this CPS and the accompanying CP. This includes those described in Section 5.3. Potential sanctions for unauthorized activities by independent contractors are described in Section 5.3.6.

### 5.3.8 Documentation supplied to personnel

Trusted Contributors are provided with all documentation necessary to perform their duties. This always includes, at a minimum, a copy of the ISRG CP, CPS, and Information Security Policy.

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

Audit logs are retained for at least seven years and will be made available to compliance auditors upon request.

### 5.4.4 Protection of audit log

Audit logs, whether in production or archived, are protected using both physical and logical access controls.

### 5.4.5 Audit log backup procedures

ISRG makes regular backup copies of audit logs. Audit log backup copies are sent for secure offsite storage at least once per month.

### 5.4.6 Audit collection system (internal vs. external)

Audit data is automatically generated and reported/recorded by operating systems, CA software applications, and network devices. Systems are in place to ensure proper reporting and recording of audit data, and the failure of such systems may lead to suspension of CA services until proper audit log reporting is restored.

### 5.4.7 Notification to event-causing subject

No stipulation.

### 5.4.8 Vulnerability assessments

Audit logs are monitored by Trusted Contributors, including operations and engineering staff. Anomalies indicating attempted breaches of CA security are reported and investigated.

Automated internal and external vulnerability scans occur at least every two weeks, though more typically every week.

Extensive vulnerability assessments for ISRG infrastructure are conducted at least annually by qualified third parties.

ISRG Security Officers perform a risk assessment at least annually. This risk assessment:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;

2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and

3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

## 5.5 Records archival

### 5.5.1 Types of records archived

ISRG archives all audit logs, the contents of which are described in Section 5.4.1. ISRG may also archive any other information deemed critical to understanding the historical performance of the CA's duties.

### 5.5.2 Retention period for archive

ISRG retains all documentation relating to certificate requests and the verification thereof, and all Certificates and revocation thereof, for at least seven years after any Certificate based on that documentation ceases to be valid.

### 5.5.3 Protection of archive

Archives are protected from unauthorized modification or destruction by strong security and environmental controls at primary and offsite storage facilities.

### 5.5.4 Archive backup procedures

Archives are backed up at primary CA facilities as well as at secure off-site facilities.

### 5.5.5 Requirements for time-stamping of records

Records are time-stamped as they are created.

Machine-created records use system time, which is synchronized automatically with third-party time sources. Machines without network access have the time set manually.

Manual records use a manually entered date and time, complete with time zone in use.

### 5.5.6 Archive collection system (internal or external)

No stipulation.

### 5.5.7 Procedures to obtain and verify archive information

No stipulation.

## 5.6 Key changeover

When a CA certificate is nearing expiration, a key changeover procedure is used to transition to a new CA certificate. The following steps constitute a key changeover procedure:

1. Some time prior to CA certificate expiration, the private key associated with the expiring certificate is no longer used to sign new certificates. It is only used to sign CRLs and OCSP responses.

2. A new key pair is generated and a new CA certificate is created containing the new key pair's public key. This new key pair is used to sign new certificates.

3. If necessary or desired, the old private key associated with the expiring certificate may be used to cross-sign the new certificate.

## 5.7 Compromise and disaster recovery

### 5.7.1 Incident and compromise handling procedures

ISRG has created and maintains incident response procedures for a range of potential compromise and disaster situations. Such situations include, but are not limited to, natural disasters, security incidents, and equipment failure. Incident response plans are reviewed, potentially updated, and tested on at least an annual basis.

### 5.7.2 Computing resources, software, and/or data are corrupted

In the event that computing resources, software, and/or data are corrupted or otherwise damaged, ISRG will assess the situation, including its impact on CA integrity and security, and take appropriate action. CA operations may be suspended until mitigation is complete. Subscribers may be notified if corruption or damage has a material impact on the service provided to them.

### 5.7.3 Entity private key compromise procedures

In the event that a CA Private Key is compromised, or suspected to be compromised, ISRG will immediately launch a thorough investigation. Forensic evidence will be collected and secured as quickly as possible. If it cannot be determined with a high degree of certainty that the private key in question was not compromised, then the following steps may be taken in whatever order is deemed most appropriate by ISRG Security Officers:

* Certificates relying on the private key in question will be revoked.
* ISRG will notify root programs relying on the integrity of the key in question.
* ISRG will notify Subscribers relying on the integrity of the key in question.

### 5.7.4 Business continuity capabilities after a disaster

ISRG maintains multiple geographically diverse facilities, each of which is capable of operating ISRG CA systems independently. In the event that a disaster entirely disables one facility, ISRG CA operations will fail over to another facility.

## 5.8 CA or RA termination

In the event that ISRG CA services are to be terminated:

* All affected parties, including root programs and Subscribers, will be provided with notice as far in advance as reasonably possible.
* A termination plan will be created and review by the ISRG PMA.

If a suitable successor entity exists, the following steps will be taken:

* CA Private Keys, records, logs, and other critical documentation will be transferred to the successor organization in a secure and compliant manner.
* Arrangements will be made for compliant continuation of CA responsibilities.

If a suitable successor entity does not exist, the following steps will be taken:

* All certificates issued will be revoked and final CRLs will be published.
* CA Private Keys will be destroyed.
* CA records, logs, and other critical documentation will be transferred to a third party or government entity with appropriate legal controls in place to protect information while allowing its use in compliance with relevant policies and the law.

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

CA private keys are generated by HSMs meeting the requirements of Section 6.2.1. This occurs during a ceremony meeting the requirements of this CPS and the accompanying CP.

Subscriber key pairs are generated and managed by Subscribers. Generation and management of Subscriber key pairs must be done in compliance with the terms of the CA Subscriber Agreement and ISRG CPS Section 9.6.3.

### 6.1.2 Private key delivery to subscriber

ISRG never generates or has access to Subscriber Private Keys.

### 6.1.3 Public key delivery to certificate issuer

Subscriber Public Keys are communicated to ISRG electronically via the ACME protocol.

### 6.1.4 CA public key delivery to relying parties

ISRG Public Keys are provided to Relying Parties as part of browser, operating system, or other software trusted root certificate lists.

ISRG Public Keys are also available on ISRG websites such as [letsencrypt.org](https://letsencrypt.org/).

### 6.1.5 Key sizes

ISRG CA root RSA Private Keys are at least 4096 bits in length.

ISRG CA root ECDSA Private Keys are at least 384 bits in length.

ISRG CA intermediate RSA Private Keys are at least 2048 bits in length.

ISRG CA intermediate ECDSA Private Keys are at least 384 bits in length.

### 6.1.6 Public key parameters generation and quality checking

ISRG uses HSMs conforming to FIPS 186-4, capable of providing random number generation and on-board creation of at least 2048-bit RSA keys and at least 384-bit ECDSA keys.

Per Section 5.3.3, NIST SP 800‐89, the CA ensures that the public exponent of the RSA Keys for a DV-SSL Certificates is in the range between 2<sup>16</sup>+1 and 2<sup>256</sup>-1. The moduli are an odd number, not the power of a prime, and have no factors smaller than 752.

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

See Section 7, Certificate Profiles.

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

### 6.2.1 Cryptographic module standards and controls

ISRG uses HSMs meeting FIPS 140-2 Level 3 (or higher) requirements.

### 6.2.2 Private key (n out of m) multi-person control

ISRG has put into place security mechanisms which require multiple people performing in Trusted Roles in order to access CA Private Keys, both physically and logically. This is true for all copies of Private Keys, in production or backups, on-site or off-site.

### 6.2.3 Private key escrow

ISRG does not escrow CA Private Keys and does not provide such a service for Subscribers.

### 6.2.4 Private key backup

Critical ISRG Private Keys are backed up both on-site and off-site, in multiple geographic locations, under multi-person control.

### 6.2.5 Private key archival

ISRG does not archive private keys.

### 6.2.6 Private key transfer into or from a cryptographic module

ISRG CA Private Keys are generated inside HSMs and are only transferred between HSMs for redundancy or backup purposes. When transferred, keys are encrypted prior to leaving HSMs and unwrapped only inside destination HSMs. Keys never exist in plain text form outside of HSMs.

### 6.2.7 Private key storage on cryptographic module

ISRG CA Private Keys are stored on HSMs meeting the requirements stated in Section 6.2.1.

### 6.2.8 Method of activating private key

ISRG CA Private Keys are always stored on HSMs and activated using the mechanisms provided by the HSM manufacturer. Activation data and devices are protected.

### 6.2.9 Method of deactivating private key

ISRG CA Private Keys are always stored on HSMs and deactivated using the mechanisms provided by the HSM manufacturer.

### 6.2.10 Method of destroying private key

ISRG CA Private Keys are destroyed by Trusted Contributors using a FIPS 140-2 (or higher) validated zeroize method provided by the HSMs storing the keys. Physical destruction of the HSM is not required.

Subscribers are obligated to securely destroy private keys when they should no longer be used, in most cases by securely deleting all copies of private key files from storage media.

### 6.2.11 Cryptographic Module Rating

See Section 6.2.1.

## 6.3 Other aspects of key pair management

### 6.3.1 Public key archival

See Section 5.5.

### 6.3.2 Certificate operational periods and key pair usage periods

The lifetimes of ISRG Root CA certificates are specified in Section 1.1. Corresponding key pairs have the same lifetimes.

End-entity certificates issued by ISRG to Subscribers shall have a validity period less than 100 days. Subscriber key pairs may be re-used indefinitely provided that there is no suspicion or confirmation of Private Key compromise.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

Activation data used to activate CA Private Keys is generated during a key ceremony. Activation data is transferred to the person who will use it, or place it will be stored, in a secure fashion.

### 6.4.2 Activation data protection

Activation data is protected from unauthorized disclosure via a combination of physical and logical means.

### 6.4.3 Other aspects of activation data

No stipulation.

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

ISRG CA infrastructure and systems are appropriately secured in order to protect CA software and data from unauthorized access or modification. Access to systems is secured via multi-factor authentication whenever possible. Security updates are applied in a timely fashion. Vulnerability scans are run regularly.

### 6.5.2 Computer security rating

No stipulation.

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

ISRG has developed policies and procedures to effectively manage the acquisition and development of its CA systems.

ISRG CA hardware and software is dedicated solely to performing CA functions.

Vendor selection includes an evaluation of reputation in the market, ability to deliver a quality product, vulnerability history, and the likelihood of remaining viable in the future. Purchases are made in such a way that as little information about the future use of products as possible is disclosed. Physical product deliveries are received by Trusted Contributors and inspected for evidence of tampering. HSMs are shipped in tamper-evident packaging and tamper bag serial numbers are confirmed with the vendor upon reception.

ISRG maintains a CA testing environment separate from the production environment. The testing environment matches the production environment as closely as reasonably possible but does not have access to CA Private Keys used in trusted certificates. The purpose of this testing platform is to allow extensive but safe testing of software and systems that are or will be deployed to the CA production environment.

ISRG has developed and maintains appropriate change control policies and procedures to be followed any time CA systems are modified. Changes to ISRG CA systems require review by qualified Trusted Personnel who are different from the person requesting the change. Change requests are documented, as are any subsequent required reviews or approvals.

When ISRG develops software to be used in CA operations, software development policies are put into place and methodologies are followed in order to ensure software quality and integrity. This always includes a requirement for peer review of code changes. Unit testing is strongly encouraged. Code commit privileges are granted only to qualified and trusted contributors. Nobody with the ability to deploy software to ISRG PKI systems (e.g. Systems Administrators) may have the ability to commit code to core CA software. The reverse is also true.

### 6.6.2 Security management controls

ISRG has mechanisms in place to control and monitor security-related configuration of CA systems. Equipment and software is installed and configured using a documented change control process. Software integrity is verified upon deployment using checksums.

### 6.6.3 Life cycle security controls

No stipulation.

## 6.7 Network security controls

ISRG implements reasonable network security safeguards and controls to prevent unauthorized access to CA systems and infrastructure. ISRG complies with the CA/Browser Forum’s Network and Certificate System Security Requirements.

ISRG's network is multi-tiered and utilizes the principle of defense in depth.

Firewalls and other critical CA systems are configured based on a necessary-traffic-only allowlisting policy whenever possible.

ISRG root CA Private Keys are stored offline in a secure manner.

## 6.8 Time-stamping

See Section 5.5.5.

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

All fields are as specified in RFC 5280, including fields and extensions not specifically mentioned.
Extensions are not marked critical unless specifically described here as critical.

### Root CA Certificate

| Field or extension             | Value                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Serial Number                  | Must be unique, with 64 bits of output from a CSPRNG                               |
| Issuer Distinguished Name      | C=US, O=Internet Security Research Group, CN=ISRG Root X&lt;n&gt;<br/> where n is an integer representing the instance of the Root<br/> CA Certificate. For example, ISRG Root X1, ISRG Root X2, etc. |
| Subject Distinguished Name     | Same as Issuer DN                                                                  |
| Validity Period                | Up to 25 years                                                                     |
| Basic Constraints              | Critical.<br/> cA=True, pathLength constraint absent                               |
| Key Usage                      | Critical.<br/> keyCertSign, cRLSign                                                |

### Intermediate CA Certificate

| Field or extension             | Value                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Serial Number                  | Must be unique, with 64 bits of output from a CSPRNG                               |
| Issuer Distinguished Name      | Derived from Issuer certificate                                                    |
| Subject Distinguished Name     | C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X&lt;n&gt;; or<br/> C=US, O=Let's Encrypt, CN=[ER]&lt;n&gt;<br/> where n is an integer representing the instance of the Subordinate CA Certificate.|
| Validity Period                | Up to 8 years                                                                      |
| Basic Constraints              | Critical.<br/> cA=True, pathLength constraint 0                                    |
| Key Usage                      | Critical.<br/> keyCertSign, cRLSign, digitalSignature                              |
| Extended Key Usage             | TLS Server Authentication, TLS Client Authentication                               |
| Certificate Policies           | CAB Forum Domain Validated (2.23.140.1.2.1)<br/>ISRG Domain Validated (1.3.6.1.4.1.44947.1.1.1)<br/>Policy Qualifier Id=CPS<br/>Qualifier: Pointer to this CPS |
| Authority Information Access   | Contains CA Issuers URL (and optionally an OCSP URL). URLs vary based on Issuer.   |
| CRL Distribution Points        | Contains a CRL URL. URL varies based on Issuer.                                    |

### DV-SSL End Entity Certificate

| Field or extension             | Value                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Serial Number                  | Must be unique, with 64 bits of output from a CSPRNG                               |
| Issuer Distinguished Name      | Derived from Issuer certificate                                                    |
| Subject Distinguished Name     | CN=one of the values from the Subject Alternative Name extension                   |
| Validity Period                | Less than 100 days                                                                 |
| Basic Constraints              | Critical.<br/> cA=False                                                            |
| Key Usage                      | Critical.<br/> digitalSignature, keyEncipherment                                   |
| Extended Key Usage             | TLS Server Authentication, TLS Client Authentication                               |
| Certificate Policies           | CAB Forum Domain Validated (2.23.140.1.2.1)<br/>ISRG Domain Validated (1.3.6.1.4.1.44947.1.1.1)<br/>CPS Qualifier: Pointer to this CPS |
| Authority Information Access   | Contains CA Issuers URL and OCSP URL. URLs vary based on Issuer.                   |
| Subject Public Key             | RSA with modulus between 2048 and 4096, inclusive; or namedCurve P-256; or namedCurve P-384 |
| Subject Alternative Name       | A sequence of 1 to 100 dNSNames                                                    |
| TLS Feature                    | Contains status_request if requested by the subscriber in the CSR                  |
| Precertificate poison          | Per RFC 6962. In Precertificates only.                                             |
| Signed Certificate Timestamp List | Per RFC 6962. In final certificates only.                                       |

### Root OCSP Signing Certificate

Signed by a Root CA Certificate, these Certificates sign OCSP responses for Intermediate CA Certificates.

| Field or extension             | Value                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| Serial Number                  | Must be unique, with 64 bits of output from a CSPRNG                               |
| Issuer Distinguished Name      | C=US, O=Internet Security Research Group, CN=ISRG Root X1                          |
| Subject Distinguished Name     | C=US, O=Internet Security Research Group, CN=ISRG Root OCSP X1                     |
| Validity Period                | 5 years                                                                            |
| Basic Constraints              | Critical.<br/> cA=False                                                            |
| Key Usage                      | Critical.<br/> digitalSignature                                                    |
| Extended Key Usage             | Critical.<br/> OCSPSigning                                                         |
| No Check                       | Present

### 7.1.1 Version number(s)

All certificates use X.509 version 3.

### 7.1.2 Certificate extensions

See section 7.1.

### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

No stipulation.

#### 7.1.3.2 Signature AlgorithmIdentifier

| Name                    | Object identifier                    |
| ----------------------- | ------------------------------------ |
| sha256WithRSAEncryption | 1.2.840.113549.1.1.11                |
| ecdsa-with-SHA384       | 1.2.840.10045.4.3.3                  |

### 7.1.4 Name forms

See ISRG Certificate Policy.

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

| Field or Extension        | Value                                                                          |
| ------------------------- | ------------------------------------------------------------------------------ |
| Version                   | V2                                                                             |
| Signature Algorithm       | sha256WithRSAEncryption or ecdsa-with-SHA384                                   |
| ThisUpdate                | The date and time when the Certificate revocation list was issued.             |
| NextUpdate                | ThisUpdate + 30 days                                                           |
| RevokedCertificates       | Contains: userCertificate, revocationDate, reasonCode                          |
| CRLnumber                 | The serial number of this CRL in an incrementally increasing sequence of CRLs. |

### 7.2.1 Version number(s)

See section 7.2.

### 7.2.2 CRL and CRL entry extensions

No stipulation.

## 7.3 OCSP profile

ISRG OCSP responders implement the RFC 5019 profile of RFC 6960.

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

ISRG's WebTrust compliance audits are performed by a qualified auditor. A qualified auditor means a natural person, legal entity, or group of natural persons or legal entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit (which is ISRG);
2. The ability to conduct an audit that addresses the relevant criteria
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403;
5. (For audits conducted in accordance with the WebTrust standard) licensed by WebTrust;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors & Omissions insurance with policy limits of at least one million US dollars in coverage

## 8.3 Assessor's relationship to assessed entity

ISRG's WebTrust auditors shall have no financial interest in, or other type of relationship with, ISRG, which might cause the auditors to have a bias for or against ISRG.

## 8.4 Topics covered by assessment

Compliance audits cover ISRG's compliance with the ISRG CP and this CPS, as well as the following WebTrust principles and criteria:

* Principles and Criteria for Certification Authorities
* WebTrust Principles and Criteria for Certification Authorities – SSL Baseline with Network Security

## 8.5 Actions taken as a result of deficiency

Noncompliance with relevant requirements will be documented by auditors (internal or external), the ISRG PMA will be informed, and the ISRG PMA will ensure that steps are taken to address the issues as quickly as reasonably possible.

## 8.6 Communication of results

Audit results are reported to the ISRG PMA and any other entity entitled to the results by law, regulation, or agreement. This includes a number of Web user agent (i.e. browser) root programs.

ISRG is not required to publicly disclose any audit finding that does not impact the overall audit opinion.

## 8.7 Self-Audits

ISRG performs a quarterly internal audit of at least 3% of issuance since the last WebTrust audit period.
The sample is randomly selected. Results are saved and provided to auditors upon request.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

ISRG does not charge any fees for certificate issuance or renewal.

### 9.1.2 Certificate access fees

No stipulation.

### 9.1.3 Revocation or status information access fees

ISRG does not charge any fees for certificate revocation or for checking the validity status of an issued certificate using a CRL or OSCP.

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

ISRG employees, agents, and contractors are responsible for protecting confidential information and are bound by ISRG’s policies with respect to the treatment of confidential information or are contractually obligated to do so. Employees receive training on how to handle confidential information.

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

ISRG follows the privacy policy posted on its website (https://letsencrypt.org/repository/) when handling personal information.

### 9.4.2 Information treated as private

The privacy policy posted on ISRG’s website (https://letsencrypt.org/repository/) identifies information that ISRG treats as private.

### 9.4.3 Information not deemed private

The privacy policy posted on ISRG’s website (https://letsencrypt.org/repository/) identifies information that ISRG does not treat as private.

### 9.4.4 Responsibility to protect private information

ISRG employees and contractors are subject to policies or contractual obligations requiring them to comply with ISRG’s privacy policy (https://letsencrypt.org/repository/) or contractual obligations at least as protective of private information as ISRG’s privacy policy.

### 9.4.5 Notice and consent to use private information

ISRG follows the privacy policy posted on its website (https://letsencrypt.org/repository/) when using personal information.

### 9.4.6 Disclosure pursuant to judicial or administrative process

ISRG may disclose personal information if compelled to do so by court order or other compulsory legal process, provided that ISRG will oppose such disclosure with all legal and technical tools reasonably available to ISRG.

### 9.4.7 Other information disclosure circumstances

ISRG may disclose personal information under other circumstances that are described in the privacy policy posted on its website (https://letsencrypt.org/repository/).

## 9.5 Intellectual property rights

ISRG and/or its business partners own the intellectual property rights in ISRG’s services, including the certificates, trademarks used in providing the services, and this CPS. Certificate and revocation information are the property of ISRG. ISRG grants permission to reproduce and distribute certificates on a non-exclusive and royalty-free basis, provided that they are reproduced and distributed in full. Private Keys and Public Keys remain the property of the Subscribers who rightfully hold them.

Notwithstanding the foregoing, third party software (including open source software) used by ISRG to provide its services is licensed, not owned, by ISRG.

## 9.6 Representations and warranties

### 9.6.1 CA representations and warranties

Except as expressly stated in this CPS or in a separate agreement with a Subscriber, ISRG does not make any representations or warranties regarding its products or services. ISRG represents and warrants, to the extent specified in this CPS, that:

1. ISRG complies, in all material aspects, with the CP and this CPS,
2. ISRG publishes and updates CRLs and OCSP responses on a regular basis,
3. All certificates issued under this CPS will be verified in accordance with this CPS and meet the minimum requirements found herein and in the CAB Forum Baseline Requirements, and
4. ISRG will maintain a repository of public information on its website.

### 9.6.2 RA representations and warranties

ISRG does not use RA services from third parties.

### 9.6.3 Subscriber representations and warranties

1. Each Subscriber warrants to ISRG and the public-at-large that Subscriber is the legitimate registrant of the Internet domain name that is, or is going to be, the subject of the ISRG certificate issued to Subscriber, or that Subscriber is the duly authorized agent of such registrant.
2. Each Subscriber warrants to ISRG and the public-at-large that either (a) Subscriber did not obtain control of such domain name as the result of a seizure of such domain name, or (b) such domain name had no ongoing lawful uses at the time of such seizure.
3. Each Subscriber warrants that all information in the ISRG certificate issued to Subscriber regarding Subscriber or its domain name is accurate, current, reliable, complete, and not misleading.
4. Each Subscriber warrants that all information provided by Subscriber to ISRG is accurate, current, complete, reliable, complete, and not misleading.
5. Each Subscriber warrants that Subscriber rightfully holds the Private Key corresponding to the Public Key listed in the ISRG certificate issued to Subscriber.
6. Each Subscriber warrants that Subscriber has taken all appropriate, reasonable, and necessary steps to secure and keep Subscriber’s Private Key secret.
7. Each Subscriber acknowledges and accepts that ISRG is entitled to revoke Subscriber’s ISRG certificates immediately if the Subscriber violates the terms of the Subscriber Agreement or if ISRG discovers that any of Subscriber’s ISRG certificates are being used to enable criminal activities such as phishing attacks, fraud, or the distribution of malware.

### 9.6.4 Relying party representations and warranties

Each Relying Party represents and warrants that, prior to relying on an ISRG certificate, it:

1. Obtained sufficient knowledge on the use of digital certificates and PKI,
2. Studied the applicable limitations on the usage of certificates and agrees to ISRG’s limitations on its liability related to the use of certificates,
3. Has read, understands, and agrees to this CPS,
4. Verified both the ISRG certificate and the certificates in the certificate chain using the relevant CRL or OCSP,
5. Will not use an ISRG certificate if the certificate has expired or been revoked, and
6. Will take all reasonable steps to minimize the risk associated with relying on a digital signature, including only relying on an ISRG certificate after considering:
  * Applicable law and the legal requirements for identification of a party, protection of the confidentiality or privacy of information, and enforceability of the transaction;
  * The intended use of the certificate as listed in the certificate or this CPS,
  * The data listed in the certificate,
  * The economic value of the transaction or communication,
  * The potential loss or damage that would be caused by an erroneous identification or a loss of confidentiality or privacy of information in the application, transaction, or communication,
  * The Relying Party’s previous course of dealing with the Subscriber,
  * The Relying Party’s understanding of trade, including experience with computer-based methods of trade, and
  * Any other indicia of reliability or unreliability pertaining to the Subscriber and/or the application, communication, or transaction.

Any unauthorized reliance on a certificate is at a party’s own risk.

### 9.6.5 Representations and warranties of other participants

No stipulation.

## 9.7 Disclaimers of warranties

ISRG certificates and services are provided “as-is.” ISRG disclaims any and all warranties of any type, whether express or implied, including and without limitation any implied warranty of title, non-infringement, merchantability, or fitness for a particular purpose, in connection with any ISRG service or ISRG certificate.

## 9.8 Limitations of liability

ISRG does not accept any liability for any loss, harm, claim, or attorney’s fees in connection with any certificates. ISRG will not be liable for any damages, attorney’s fees, or recovery, regardless of whether such damages are direct, consequential, indirect, incidental, special, exemplary, punitive, or compensatory, even if ISRG has been advised of the possibility of such damages. This limitation on liability applies irrespective of the theory of liability, i.e., whether the theory of liability is based upon contract, warranty, indemnification, contribution, tort, equity, statute or regulation, common law, or any other source of law, standard of care, category of claim, notion of fault or responsibility, or theory of recovery. This disclaimer is intended to be construed to the fullest extent allowed by applicable law.

Without waiving or limiting the foregoing in any way, ISRG does not make, and ISRG expressly disclaims, any warranty regarding its right to use any technology, invention, technical design, process, or business method used in either issuing certificates or providing any of ISRG’s services. Each subscriber affirmatively and expressly waives the right to hold ISRG responsible in any way, or seek indemnification against ISRG, for any infringement of intellectual property rights, including patent, trademark, trade secret, or copyright.

## 9.9 Indemnities

### 9.9.1 Indemnification by ISRG

The CA does not provide any indemnification except as described in Section 9.9.1 of the Certificate Policy.

### 9.9.2 Indemnification by Subscribers

Each Subscriber will indemnify and hold harmless ISRG and its directors, officers, employees, agents, and affiliates from any and all liabilities, claims, demands, damages, losses, costs, and expenses, including attorneys’ fees, arising out of or related to: (i) any misrepresentation or omission of material fact by Subscriber to ISRG, irrespective of whether such misrepresentation or omission was intentional, (ii) Subscriber’s violation of the Subscriber Agreement, (iii) any compromise or unauthorized use of an ISRG certificate or corresponding Private Key, or (iv) Subscriber’s misuse of an ISRG certificate. If applicable law prohibits Subscriber from providing indemnification for another party’s negligence or acts, such restriction, or any other restriction required by law for this indemnification provision to be enforceable, shall be deemed to be part of this indemnification provision.

### 9.9.3 Indemnification by Relying Parties

To the extent permitted by law, each Relying Party shall indemnify ISRG, its partners, and any cross-signed entities, and their respective directors, officers, employees, agents, and contractors against any loss, damage, or expense, including reasonable attorney’s fees, related to the Relying Party’s (i) breach of any service terms applicable to the services provided by ISRG or its affiliates and used by the Relying Party, this CPS, or applicable law; (ii) unreasonable reliance on a certificate; or (iii) failure to check the certificate’s status prior to use.

## 9.10 Term and termination

### 9.10.1 Term

This CPS and any amendments to this CPS are effective when published to the ISRG online repository and remain in effect until replaced with a newer version.

### 9.10.2 Termination

This CPS and any amendments remain in effect until replaced with a newer version.

### 9.10.3 Effect of termination and survival

ISRG will communicate the conditions and effect of this CPS’s termination via the ISRG Repository. The communication will specify which provisions survive termination. At a minimum, all responsibilities related to protecting confidential information will survive termination. All Subscriber Agreements remain effective until the certificate is revoked or expired, even if this CPS terminates.

## 9.11 Individual notices and communications with participants

ISRG accepts notices related to this CPS at the locations specified in Section 1.5.2 of this CPS. Notices are deemed effective after the sender receives a valid and digitally signed acknowledgment of receipt from ISRG. If an acknowledgement of receipt is not received within five days, the sender must resend the notice in paper form to the street address specified in Section 1.5.2 of this CPS using either a courier service that confirms delivery or via certified or registered mail with postage prepaid and return receipt requested. ISRG may allow other forms of notice in its Subscriber Agreements.

## 9.12 Amendments

### 9.12.1 Procedure for amendment

This CPS is reviewed at least annually and may be reviewed more frequently. Amendments are made by posting an updated version of the CPS to the online repository. Controls are in place that are designed to reasonably ensure that this CPS is not amended and published without the prior authorization of the ISRG PMA.

### 9.12.2 Notification mechanism and period

ISRG posts CPS revisions to its Repository. ISRG does not guarantee or set a notice-and-comment period and may make changes to this CPS without notice.

### 9.12.3 Circumstances under which OID must be changed

The ISRG PMA is solely responsible for determining whether an amendment to the CPS requires an OID change.

## 9.13 Dispute resolution provisions

Any claim, suit or proceeding arising out of this CPS or any ISRG product or service must be brought in a state or federal court located in San Jose, California. ISRG may seek injunctive or other relief in any state, federal, or national court of competent jurisdiction for any actual or alleged infringement of its, its affiliates, or any third party’s intellectual property or other proprietary rights.

## 9.14 Governing law

The laws of the state of California, United States of America, govern the interpretation, construction, and enforcement of this CPS and all proceedings related to ISRG products and services, including tort claims, without regard to any conflicts of law principles. The United Nations Convention for the International Sale of Goods does not apply to this CPS.

## 9.15 Compliance with applicable law

This CPS is subject to all applicable laws and regulations, including United States restrictions on the export of software and cryptography products.

## 9.16 Miscellaneous provisions

### 9.16.1 Entire agreement

ISRG requires each party using its products and services to enter into an agreement that delineates the terms associated with the product or service. If an agreement has provisions that differ from this CPS, then the agreement with that party controls, but solely with respect to that party. Third parties may not rely on or bring action to enforce such agreement.

### 9.16.2 Assignment

Any entities operating under this CPS may not assign their rights or obligations without the prior written consent of ISRG. Unless specified otherwise in a contract with a party, ISRG does not provide notice of assignment.

### 9.16.3 Severability

If any provision of this CPS is held invalid or unenforceable by a competent court or tribunal, the remainder of the CPS will remain valid and enforceable. Each provision of this CPS that provides for a limitation of liability, disclaimer of a warranty, or an exclusion of damages is severable and independent of any other provision.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

ISRG may seek indemnification and attorneys’ fees from a party for damages, losses, and expenses related to that party’s conduct. ISRG’s failure to enforce a provision of this CPS does not waive ISRG’s right to enforce the same provision later or right to enforce any other provision of this CPS. To be effective, waivers must be in writing and signed by ISRG.

### 9.16.5 Force Majeure

ISRG is not liable for any delay or failure to perform an obligation under this CPS to the extent that the delay or failure is caused by an occurrence beyond ISRG’s reasonable control. The operation of the Internet is beyond ISRG’s reasonable control.

## 9.17 Other provisions

No stipulation.
