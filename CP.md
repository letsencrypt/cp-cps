# 1. INTRODUCTION

## 1.1 Overview

This Certificate Policy ("CP") document outlines the certificate policies for Internet Security Research Group ("ISRG") Public Key Infrastructure ("ISRG PKI").

ISRG PKI services include, but are not limited to, issuing, managing, validating, revoking, and renewing Certificates in accordance with the requirements of this CP.

ISRG PKI services are most commonly, but not necessarily exclusively, provided under the brand/trademark "Let's Encrypt".

The ISRG PKI conforms to the current version of the guidelines adopted by the Certification Authority/Browser Forum (“CAB Forum”) when issuing publicly trusted certificates, including the Baseline Requirements for the Issuance and Management of Publicly Trusted Certificates (“Baseline Requirements”). CAB Forum documents can be found at https://www.cabforum.org. If there is any conflict between this CP and a relevant CAB Forum requirement or guideline, then the CAB Forum requirement or guideline shall take precedence.

Other documents related to the behavior and control of the ISRG PKI, such as a Subscriber Agreement and Privacy Policy, can be found at https://letsencrypt.org/repository/.

Per IETF PKIX RFC 3647, this CP is divided into nine components that cover security controls, practices, and procedures for certification services provided by the ISRG PKI.

The following Certification Authorities are covered under this CP:

| CA Type | Distinguished Name | Key Pair Type and Parameters | Cert SHA-256 Fingerprint | Validity Period |
|---------|--------------------|------------------------------|--------------------------|-----------------|
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X1 | RSA, n has 4096 bits, e=65537 | 96:BC:EC:06:26:49:76:F3:<br>74:60:77:9A:CF:28:C5:A7:<br>CF:E8:A3:C0:AA:E1:1A:8F:<br>FC:EE:05:C0:BD:DF:08:C6 | Not Before: Jun  4 11:04:38 2015 GMT,<br>Not After: Jun  4 11:04:38 2035 GMT |
| Root CA | C=US,<br>O=Internet Security Research Group,<br>CN=ISRG Root X2 | ECDSA, NIST curve P-384 | 69:72:9b:8e:15:a8:6e:fc:<br>17:7a:57:af:b7:17:1d:fc:<br>64:ad:d2:8c:2f:ca:8c:f1:<br>50:7e:34:45:3c:cb:14:70 | Not Before: Sept  4 00:00:00 2020 GMT,<br>Not After: Sept 17 16:00:00 2040 GMT |

This work is licensed under the Creative Commons Attribution 4.0 International License. To
view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative
Commons, PO Box 1866, Mountain View, CA 94042, USA.

## 1.2 Document name and identification

This is the ISRG Certificate Policy. This document was approved for publication by the ISRG Policy Management Authority, and is made available at https://letsencrypt.org/repository/.

The following revisions have been made:

| Date              | Changes                                            | Version |
|-------------------|----------------------------------------------------|---------|
| May 5, 2015 | Original | 1.0 |
| September 9, 2015 | Added DV SSL OID, added/corrected a number of policy URIs, clarifications to Procedure for Revocation Request, substantial changes to all of Section 9 regarding legal matters, other minor fixes/improvements | 1.1 |
| May 5, 2016 | Add info about tlsFeature extension, serialNumber in Subject Distinguished Name field. | 1.2 |
| April 13, 2017 | Simplify Section 1.2, "Document Name and Identification. Simplify Section 3.2.2.2, "Performance of Electronic Identification." Validation methods in use are detailed in CPS. Update CPS section numbers for CRL and OCSP profiles. Remove Section 10, “Certificate Profiles.” Profiles are now in our CPS. | 1.3 |
| May 22, 2017 | Complete rewrite. | 2.0 |
| February 6, 2018 | Update text of Section 6.1.7 to match Baseline Requirements v1.5.1. | 2.1 |
| September 20, 2018 | Define Certificate Problem Report in Section 1.6.1. Update Section 3.2.2.4 "Validation of Domain Authorization or Control" to match latest BRs but omit methods we do not use. Add additional revocation reason to Section 4.9.1.1 for compliance with upcoming BR revision. Minor updates to Sections 4.9.3 and 4.9.5. | 2.2 |
| July 3, 2019 | Remove IP address validation information which is not applicable. Update sections 4.9.1.1, 4.9.1.2, and 4.9.5 to match current BRs. Other minor updates (e.g. capitalization). | 2.3 |
| January 21, 2020 | Make structure more exactly match RFC 3647 recommendation. Audit use of phrase No Stipulation and eliminate blank sections. Add policy information for IP address validation. | 2.4 |
| October 27, 2020 | List ISRG Root X2 in section 1.1. Update sections 3.2.2.4, 3.2.2.5, 3.2.2.6, 3.2.2.8, 4.2.1, 4.9.10, 7.1.2, and 7.1.3 regarding validation methods, OCSP, certificate profiles, and cryptographic algorithms, to match Baseline Requirements. | 2.5 |
| April 2, 2021 | Update ISRG physical address. | 2.6 |

## 1.3 PKI participants

### 1.3.1 Certification authorities

ISRG is a CA that provides services including, but not limited to, issuing, managing, validating, revoking, and renewing publicly-trusted Certificates. These services are performed in accordance with the requirements of this Certificate Policy (CP) and the ISRG Certification Practice Statement (CPS). These services are provided to the general public with exceptions as deemed appropriate by ISRG management or in accordance with relevant law.

ISRG PKI services are most commonly, but not necessarily exclusively, provided under the brand/trademark "Let's Encrypt".

### 1.3.2 Registration authorities

ISRG does not delegate any validation tasks to third party registration authorities.

### 1.3.3 Subscribers

See definition of "Subscriber" in Section 1.6.1 Definitions.

### 1.3.4 Relying parties

See definition of "Relying Party" in Section 1.6.1 Definitions.

Relying Parties must verify the validity of certificates via CRL or OCSP prior to relying on certificates. CRL and OCSP location information is provided within certificates.

### 1.3.5 Other participants

Other participants include CAs that cross-sign or issue subordinates to the ISRG PKI.

ISRG PKI vendors and service providers with access to confidential information or privileged systems are required to operate in compliance with this CP.

## 1.4 Certificate usage

### 1.4.1 Appropriate certificate uses

No stipulation.

### 1.4.2 Prohibited certificate uses

No stipulation.

## 1.5 Policy administration

### 1.5.1 Organization administering the document

This CP document is maintained by the ISRG PMA.

### 1.5.2 Contact person

The ISRG PMA can be contacted at:

Policy Management Authority<br/>
Internet Security Research Group<br/>
548 Market St., PMB 57274<br/>
San Francisco, CA 94104-5401<br/>
USA<br/>

Issues can be filed via the GitHub repository where this document is maintained:

https://github.com/letsencrypt/cp-cps

### 1.5.3 Person determining CPS suitability for the policy

The ISRG PMA is responsible for determining the suitability of this CP. The ISRG PMA is informed by results and recommendations received from an independent auditor.

### 1.5.4 CP approval procedures

The ISRG PMA approves any revisions to this CP document after formal review.

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
* Private Key
  * The key in a Key Pair that must be kept secret. Used to create digital signatures that can be verified by the corresponding Public Key or to decrypt messages encrypted by the corresponding Public Key.
* Public Key
  * The only key in a Key Pair that can safely be publicly disclosed. Used by Relying Parties to verify digital signatures from the corresponding private key or to encrypt messages that can only be decrypted by the corresponding private key.
* Relying Party
  * An entity that relies upon information contained within certificates issued by ISRG PKI services.
* Root CA
  * The top-level Certification Authority whose Root Certificate is distributed by Application Software Suppliers and that issues Subordinate CA Certificates.
* Subscriber
  * An entity that has agreed to a Subscriber Agreement and is using ISRG PKI services.
* Trusted Contributor
  * A contributor who performs in a Trusted Role. Trusted Contributors may be employees, contractors, or community members. Trusted Contributors must be properly trained and qualified, and have the proper legal obligations in place before performing in a Trusted Role.
* Trusted Role
  * A role which qualifies a person to access or modify ISRG PKI systems, infrastructure, and confidential information.

### 1.6.2 Acronyms

* ACME
  * Automated Certificate Management Environment
* BRs
  * Baseline Requirements
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

Terms not otherwise defined in this CP shall be as defined in applicable agreements, user manuals, Certificate Policies and Certification Practice Statements, of the CA.

The key words “MUST”, “MUST NOT”, "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this CP shall be interpreted in accordance with RFC 2119.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of the BRs.

## 2.1 Repositories

The CA SHALL make revocation information for Subordinate Certificates and Subscriber Certificates available in accordance with this Policy.

## 2.2 Publication of certification information

The CA SHALL publicly disclose its Certificate Policy and/or Certification Practice Statement through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA’s selected audit scheme (see Section 8.1). The disclosures MUST include all the material required by RFC 2527 or RFC 3647, and MUST be structured in accordance with either RFC 2527 or RFC 3647.

Effective as of 8 September 2017, section 4.2 of a CA's Certificate Policy and/or Certification Practice Statement (section 4.1 for CAs still conforming to RFC 2527) SHALL state the CA’s policy or practice on processing CAA Records for Fully Qualified Domain Names; that policy shall be consistent with these Requirements. It shall clearly specify the set of Issuer Domain Names that the CA recognizes in CAA "issue" or "issuewild" records as permitting it to issue. The CA SHALL log all actions taken, if any, consistent with its processing practice.

The CA SHALL publicly give effect to these Requirements and represent that it will adhere to the latest published version. The CA MAY fulfill this requirement by incorporating these Requirements directly into its Certificate Policy and/or Certification Practice Statements or by incorporating them by reference using a clause such as the following (which MUST include a link to the official version of these Requirements):

> [Name of CA] conforms to the current version of the Baseline
> Requirements for the Issuance and Management of Publicly-Trusted
> Certificates published at http://www.cabforum.org. In the event of any
> inconsistency between this document and those Requirements, those
> Requirements take precedence over this document.

The CA SHALL host test Web pages that allow Application Software Suppliers to test their software with Subscriber Certificates that chain up to each publicly trusted Root Certificate. At a minimum, the CA SHALL host separate Web pages using Subscriber Certificates that are (i) valid, (ii) revoked, and (iii) expired.

## 2.3 Time or frequency of publication

The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of the BRs.

## 2.4 Access controls on repositories

The CA shall make its Repository public available in a read-only manner.

# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

### 3.1.1 Types of names

No stipulation.

### 3.1.2 Need for names to be meaningful

No stipulation.

### 3.1.3 Anonymity or pseudonymity of subscribers

No stipulation.

### 3.1.4 Rules for interpreting various name forms

No stipulation.

### 3.1.5 Uniqueness of names

No stipulation.

### 3.1.6 Recognition, authentication, and role of trademarks

No stipulation.

## 3.2 Initial identity validation

### 3.2.1 Method to prove possession of private key

No stipulation.

### 3.2.2 Authentication of organization and domain identity

If the Applicant requests a Certificate that will contain Subject Identity Information comprised only of the countryName field, then the CA SHALL verify the country associated with the Subject using a verification process meeting the requirements of Section 3.2.2.3 and that is described in the CA’s Certificate Policy and/or Certification Practice Statement. If the Applicant requests a Certificate that will contain the countryName field and other Subject Identity Information, then the CA SHALL verify the identity of the Applicant, and the authenticity of the Applicant Representative’s certificate request using a verification process meeting the requirements of this Section 3.2.2.1 and that is described in the CA’s Certificate Policy and/or Certification Practice Statement. The CA SHALL inspect any document relied upon under this Section for alteration or falsification.

#### 3.2.2.1 Identity

If the Subject Identity Information is to include the name or address of an organization, the CA SHALL verify the identity and address of the organization and that the address is the Applicant’s address of existence or operation. The CA SHALL verify the identity and address of the Applicant using documentation provided by, or through communication with, at least one of the following:

1. A government agency in the jurisdiction of the Applicant’s legal creation, existence, or recognition;
2. A third party database that is periodically updated and considered a Reliable Data Source;
3. A site visit by the CA or a third party who is acting as an agent for the CA; or
4. An Attestation Letter.

The CA MAY use the same documentation or communication described in 1 through 4 above to verify both the Applicant’s identity and address.

Alternatively, the CA MAY verify the address of the Applicant (but not the identity of the Applicant) using a utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.2 DBA/Tradename

If the Subject Identity Information is to include a DBA or tradename, the CA SHALL verify the Applicant’s right to use the DBA/tradename using at least one of the following:

1. Documentation provided by, or communication with, a government agency in the jurisdiction of the Applicant’s legal creation, existence, or recognition;

2. A Reliable Data Source;

3. Communication with a government agency responsible for the management of such DBAs or tradenames;

4. An Attestation Letter accompanied by documentary support; or

5. A utility bill, bank statement, credit card statement, government-issued tax document, or other form of identification that the CA determines to be reliable.

#### 3.2.2.3 Verification of country

If the subject:countryName field is present, then the CA SHALL verify the country associated with the Subject using one of the following: (a) the IP Address range assignment by country for either (i) the web site’s IP address, as indicated by the DNS record for the web site or (ii) the Applicant’s IP address; (b) the ccTLD of the requested Domain Name; (c) information provided by the Domain Name Registrar; or (d) a method identified in Section 3.2.2.1. The CA SHOULD implement a process to screen proxy servers in order to prevent reliance upon IP addresses assigned in countries other than where the Applicant is actually located.

#### 3.2.2.4 Validation of domain authorization or control

This section defines the permitted processes and procedures for validating the Applicant's ownership or control of the domain.

The CA SHALL confirm that prior to issuance, the CA has validated each Fully-Qualified Domain Name (FQDN) listed in the Certificate as follows:

1.  When the FQDN does not contain "onion" as the rightmost label, the CA SHALL validate the FQDN using at least one of the methods listed below; and
1.  When the FQDN contains "onion" as the rightmost label, the CA SHALL validate the FQDN in accordance with Appendix B of the Baseline Requirements v1.7.3.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation must have been initiated within the time period specified in the relevant requirement (such as Section 4.2.1 of this document) prior to Certificate issuance. For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

CAs SHALL maintain a record of which domain validation method, including relevant BR version number, they used to validate every domain.

**Note:** FQDNs may be listed in Subscriber Certificates using dNSNames in the subjectAltName extension or in Subordinate CA Certificates via dNSNames in permittedSubtrees within the Name Constraints extension.

##### 3.2.2.4.7 DNS change

Confirming the Applicant's control over the FQDN by confirming the presence of a Random Value or Request Token for either in a DNS CNAME, TXT or CAA record for either 1) an Authorization Domain Name; or 2) an Authorization Domain Name that is prefixed with a label that begins with an underscore character.

If a Random Value is used, the CA SHALL provide a Random Value unique to the Certificate request and SHALL not use the Random Value after (i) 30 days or (ii) if the Applicant submitted the Certificate request, the timeframe permitted for reuse of validated information relevant to the Certificate (such as in Section 3.3.1 of these Guidelines or Section 11.14.3 of the EV Guidelines).

Note: Once the FQDN has been validated using this method, the CA MAY also issue Certificates for other FQDNs that end with all the labels of the validated FQDN. This method is suitable for validating Wildcard Domain Names.

#### 3.2.2.4.19 Agreed-Upon Change to Website - ACME

Confirming the Applicant's control over a FQDN by validating domain control of the FQDN using the ACME HTTP Challenge method defined in section 8.3 of RFC 8555. The following are additive requirements to RFC 8555.

The CA MUST receive a successful HTTP response from the request (meaning a 2xx HTTP status code must be received).

The token (as defined in RFC 8555, section 8.3) MUST NOT be used for more than 30 days from its creation. The CPS MAY specify a shorter validity period for Random Values, in which case the CA MUST follow its CPS.

If the CA follows redirects:
1.	Redirects MUST be initiated at the HTTP protocol layer (e.g. using a 3xx status code).
2.	Redirects MUST be the result of an HTTP status code result within the 3xx Redirection class of status codes, as defined in RFC 7231, Section 6.4.
3.	Redirects MUST be to resource URLs with either via the "http" or "https" scheme.
4.	Redirects MUST be to resource URLs accessed via Authorized Ports.

**Note:** Once the FQDN has been validated using this method, the CA MAY also issue Certificates for other FQDNs that end with all the labels of the validated FQDN. This method is suitable for validating Wildcard Domain Names.

##### 3.2.2.4.20 TLS Using ALPN

Confirming the Applicant's control over a FQDN by validating domain control of the FQDN by negotiating a new application layer protocol using the TLS Application-Layer Protocol Negotiation (ALPN) Extension [RFC7301] as defined in RFC 8737. The following are additive requirements to RFC 8737.

The token (as defined in RFC 8737, section 3) MUST NOT be used for more than 30 days from its creation. The CPS MAY specify a shorter validity period for the token, in which case the CA MUST follow its CPS.

**Note:** Once the FQDN has been validated using this method, the CA MAY NOT also issue Certificates for other FQDNs that end with all the labels of the validated FQDN unless the CA performs a separate validation for that FQDN using an authorized method. This method is NOT suitable for validating Wildcard Domain Names.

#### 3.2.2.5 Authentication for an IP address

This section defines the permitted processes and procedures for validating the Applicant’s ownership or control of an IP Address listed in a Certificate.

The CA SHALL confirm that prior to issuance, the CA has validated each IP Address listed in the Certificate using at least one of the methods specified in this section.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation must have been initiated within the time period specified in the relevant requirement (such as Section 4.2.1 of this document) prior to Certificate issuance. For purposes of IP Address validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

After July 31, 2019, CAs SHALL maintain a record of which IP validation method, including the relevant BR version number, was used to validate every IP Address.

**Note:** IP Addresses verified in accordance with this section 3.2.5 may be listed in Subscriber Certificates as defined in section 7.1.4.2 or in Subordinate CA Certificates via iPAddress in permittedSubtrees within the Name Constraints extension. CAs are not required to verify IP Addresses listed in Subordinate CA Certificates via iPAddress in excludedSubtrees in the Name Constraints extension prior to inclusion in the Subordinate CA Certificate.

##### 3.2.2.5.6 ACME “http-01” method for IP addresses

Confirming the Applicant's control over the IP Address by performing the procedure documented for an “http-01” challenge in draft 04 of “ACME IP Identifier Validation Extension,” available at https://tools.ietf.org/html/draft-ietf-acme-ip-04#section-4.

##### 3.2.2.5.7 ACME “tls-alpn-01” method for IP Addresses

Confirming the Applicant's control over the IP Address by performing the procedure documented for a “tls-alpn-01” challenge in draft 04 of “ACME IP Identifier Validation Extension,” available at https://tools.ietf.org/html/draft-ietf-acme-ip-04#section-4.

#### 3.2.2.6 Wildcard Domain Validation
Before issuing a certificate with a wildcard character (\*) in a CN or subjectAltName of type DNS-ID, the CA MUST establish and follow a documented procedure that determines if the wildcard character occurs in the first label position to the left of a "registry-controlled" label or "public suffix" (e.g. "\*.com", "\*.co.uk", see RFC 6454 Section 8.2 for further explanation).

If a wildcard would fall within the label immediately to the left of a registry-controlled /1 or public suffix, CAs MUST refuse issuance unless the applicant proves its rightful control of the entire Domain Namespace. (e.g. CAs MUST NOT issue "\*.co.uk" or "\*.local", but MAY issue "\*.example.com" to Example Co.).

Determination of what is "registry-controlled" versus the registerable portion of a Country Code Top-Level Domain Namespace is not standardized at the time of writing and is not a property of the DNS itself. Current best practice is to consult a "public suffix list" such as the [Public Suffix List (PSL)](<http://publicsuffix.org/>), and to retrieve a fresh copy regularly.

If using the PSL, a CA SHOULD consult the "ICANN DOMAINS" section only, not the "PRIVATE DOMAINS" section. The PSL is updated regularly to contain new gTLDs delegated by ICANN, which are listed in the "ICANN DOMAINS" section. A CA is not prohibited from issuing a Wildcard Certificate to the Registrant of an entire gTLD, provided that control of the entire namespace is demonstrated in an appropriate way.

#### 3.2.2.7 Data source accuracy

Prior to using any data source as a Reliable Data Source, the CA SHALL evaluate the source for its reliability, accuracy, and resistance to alteration or falsification. The CA SHOULD consider the following during its evaluation:

1. The age of the information provided,
2. The frequency of updates to the information source,
3. The data provider and purpose of the data collection,
4. The public accessibility of the data availability, and
5. The relative difficulty in falsifying or altering the data.

Databases maintained by the CA, its owner, or its affiliated companies do not qualify as a Reliable Data Source if the primary purpose of the database is to collect information for the purpose of fulfilling the validation requirements under this Section 3.2.

#### 3.2.2.8 CAA Records

As part of the issuance process, the CA MUST check for CAA records and follow the processing instructions found, for each dNSName in the subjectAltName extension of the certificate to be issued, as specified in RFC 8659. If the CA issues, they MUST do so within the TTL of the CAA record, or 8 hours, whichever is greater.

This stipulation does not prevent the CA from checking CAA records at any other time.

When processing CAA records, CAs MUST process the issue, issuewild, and iodef property tags as specified in RFC 8659, although they are not required to act on the contents of the iodef property tag. Additional property tags MAY be supported, but MUST NOT conflict with or supersede the mandatory property tags set out in this document. CAs MUST respect the critical flag and not issue a certificate if they encounter an unrecognized property tag with this flag set.

RFC 8659 requires that CAs "MUST NOT issue a certificate unless the CA determines that either (1) the certificate request is consistent with the applicable CAA RRset or (2) an exception specified in the relevant CP or CPS applies." For issuances conforming to the Baseline Requirements, CAs MUST NOT rely on any exceptions specified in their CP or CPS unless they are one of the following:

* CAA checking is optional for certificates for which a Certificate Transparency pre-certificate was created and logged in at least two public logs, and for which CAA was checked.
* CAA checking is optional for certificates issued by a Technically Constrained Subordinate CA Certificate as set out in Baseline Requirements section 7.1.5, where the lack of CAA checking is an explicit contractual provision in the contract with the Applicant.
* CAA checking is optional if the CA or an Affiliate of the CA is the DNS Operator (as defined in RFC 7719) of the domain's DNS.

CAs are permitted to treat a record lookup failure as permission to issue if:

* the failure is outside the CA's infrastructure; and
* the lookup has been retried at least once; and
* the domain's zone does not have a DNSSEC validation chain to the ICANN root.

CAs MUST document potential issuances that were prevented by a CAA record in sufficient detail to provide feedback to the CAB Forum on the circumstances, and SHOULD dispatch reports of such issuance requests to the contact(s) stipulated in the CAA iodef record(s), if present. CAs are not expected to support URL schemes in the iodef record other than mailto: or https:.

### 3.2.3 Authentication of individual identity

If an Applicant subject to this Section 3.2.3 is a natural person, then the CA SHALL verify the Applicant’s name, Applicant’s address, and the authenticity of the certificate request.

The CA SHALL verify the Applicant’s name using a legible copy, which discernibly shows the Applicant’s face, of at least one currently valid government-issued photo ID (passport, drivers license, military ID, national ID, or equivalent document type). The CA SHALL inspect the copy for any indication of alteration or falsification.

The CA SHALL verify the Applicant’s address using a form of identification that the CA determines to be reliable, such as a government ID, utility bill, or bank or credit card statement. The CA MAY rely on the same government-issued ID that was used to verify the Applicant’s name.

The CA SHALL verify the certificate request with the Applicant using a Reliable Method of Communication.

### 3.2.4 Non-verified subscriber information

No stipulation.

### 3.2.5 Validation of authority

If the Applicant for a Certificate containing Subject Identity Information is an organization, the CA SHALL use a Reliable Method of Communication to verify the authenticity of the Applicant Representative’s certificate request.

The CA MAY use the sources listed in section 3.2.2.1 to verify the Reliable Method of Communication. Provided that the CA uses a Reliable Method of Communication, the CA MAY establish the authenticity of the certificate request directly with the Applicant Representative or with an authoritative source within the Applicant’s organization, such as the Applicant’s main business offices, corporate offices, human resource offices, information technology offices, or other department that the CA deems appropriate.

In addition, the CA SHALL establish a process that allows an Applicant to specify the individuals who may request Certificates. If an Applicant specifies, in writing, the individuals who may request a Certificate, then the CA SHALL NOT accept any certificate requests that are outside this specification. The CA SHALL provide an Applicant with a list of its authorized certificate requesters upon the Applicant’s verified written request.

### 3.2.6 Criteria for interoperation

The CA SHALL disclose all Cross Certificates that identify the CA as the Subject, provided that the CA arranged for or accepted the establishment of the trust relationship (i.e. the Cross Certificate at issue).

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

No stipulation.

### 3.3.2 Identification and authentication for re-key after revocation

No stipulation.

## 3.4 Identification and authentication for revocation request

No stipulation.

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate application

### 4.1.1 Who can submit a certificate application

In accordance with Section 5.5.2, the CA SHALL maintain an internal database of all previously revoked Certificates and previously rejected certificate requests due to suspected phishing or other fraudulent usage or concerns. The CA SHALL use this information to identify subsequent suspicious certificate requests.

### 4.1.2 Enrollment process and responsibilities

Prior to the issuance of a Certificate, the CA SHALL obtain the following documentation from the Applicant:

1. A certificate request, which may be electronic; and

2. An executed Subscriber Agreement or Terms of Use, which may be electronic.

The CA SHOULD obtain any additional documentation the CA determines necessary to meet these Requirements.

Prior to the issuance of a Certificate, the CA SHALL obtain from the Applicant a certificate request in a form prescribed by the CA and that complies with these Requirements. One certificate request MAY suffice for multiple Certificates to be issued to the same Applicant, subject to the aging and updating requirement in Section 3.3.1, provided that each Certificate is supported by a valid, current certificate request signed by the appropriate Applicant Representative on behalf of the Applicant. The certificate request MAY be made, submitted and/or signed electronically.

The certificate request MUST contain a request from, or on behalf of, the Applicant for the issuance of a Certificate, and a certification by, or on behalf of, the Applicant that all of the information contained therein is correct.

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions

The certificate request MAY include all factual information about the Applicant to be included in the Certificate, and such additional information as is necessary for the CA to obtain from the Applicant in order to comply with these Requirements and the CA's Certificate Policy and/or Certification Practice Statement. In cases where the certificate request does not contain all the necessary information about the Applicant, the CA SHALL obtain the remaining information from the Applicant or, having obtained it from a reliable, independent, third-party data source, confirm it with the Applicant. The CA SHALL establish and follow a documented procedure for verifying all data requested for inclusion in the Certificate by the Applicant.

Applicant information MUST include, but not be limited to, at least one Fully-Qualified Domain Name or IP address to be included in the Certificate's SubjectAltName extension.

Section 6.3.2 limits the validity period of Subscriber Certificates. The CA MAY use the documents and data provided in Section 3.2 to verify certificate information, or may reuse previous validations themselves, provided that the CA obtained the data or document from a source specified under Section 3.2 or completed the validation itself no more than 825 days prior to issuing the Certificate.

In no case may a prior validation be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

The CA SHALL develop, maintain, and implement documented procedures that identify and require additional verification activity for High Risk Certificate Requests prior to the Certificate's approval, as reasonably necessary to ensure that such requests are properly verified under these Requirements.

If a Delegated Third Party fulfills any of the CA's obligations under this section , the CA SHALL verify that the process used by the Delegated Third Party to identify and further verify High Risk Certificate Requests provides at least the same level of assurance as the CA's own processes.

### 4.2.2 Approval or rejection of certificate applications

CAs SHOULD NOT issue Certificates containing a new gTLD under consideration by ICANN. Prior to issuing a Certificate containing an Internal Name with a gTLD that ICANN has announced as under consideration to make operational, the CA MUST provide a warning to the applicant that the gTLD may soon become resolvable and that, at that time, the CA will revoke the Certificate unless the applicant promptly registers the domain name. When a gTLD is delegated by inclusion in the IANA Root Zone Database, the Internal Name becomes a Domain Name, and at such time, a Certificate with such gTLD, which may have complied with these Requirements at the time it was issued, will be in a violation of these Requirements, unless the CA has verified the Subscriber’s rights in the Domain Name. The provisions below are intended to prevent such violation from happening.

Within 30 days after ICANN has approved a new gTLD for operation, as evidenced by publication of a contract with the gTLD operator on [www.ICANN.org](https://www.ICANN.org) each CA MUST (1) compare the new gTLD against the CA’s records of valid certificates and (2) cease issuing Certificates containing a Domain Name that includes the new gTLD until after the CA has first verified the Subscriber's control over or exclusive right to use the Domain Name in accordance with Section 3.2.2.4.

Within 120 days after the publication of a contract for a new gTLD is published on [www.icann.org](https://www.ICANN.org), CAs MUST revoke each Certificate containing a Domain Name that includes the new gTLD unless the Subscriber is either the Domain Name Registrant or can demonstrate control over the Domain Name.

### 4.2.3 Time to process certificate applications

No stipulation.

## 4.3 Certificate issuance

### 4.3.1 CA actions during certificate issuance

Certificate issuance by the Root CA SHALL require an individual authorized by the CA (i.e. the CA system operator, system officer, or PKI administrator) to deliberately issue a direct command in order for the Root CA to perform a certificate signing operation.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate

No stipulation.

## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance

No stipulation.

### 4.4.2 Publication of the certificate by the CA

No stipulation.

### 4.4.3 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

See Section 9.6.3, provisions 2 and 4.

### 4.5.2 Relying party public key and certificate usage

No stipulation.

## 4.6 Certificate renewal

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

#### 4.9.1.1	Reasons for revoking a subscriber certificate

The CA SHALL revoke a Certificate within 24 hours if one or more of the following occurs:

1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise; or
4. The CA obtains evidence that the validation of domain authorization or control for any Fully-Qualified Domain Name or IP address in the Certificate should not be relied upon.

The CA SHOULD revoke a certificate within 24 hours and MUST revoke a Certificate within 5 days if one or more of the following occurs:

1. The Certificate no longer complies with the requirements of Sections 6.1.5 and 6.1.6;
2. The CA obtains evidence that the Certificate was misused;
3. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use;
4. The CA is made aware of any circumstance indicating that use of a Fully-Qualified Domain Name or IP address in the Certificate is no longer legally permitted (e.g. a court or arbitrator has revoked a Domain Name Registrant's right to use the Domain Name, a relevant licensing or services agreement between the Domain Name Registrant and the Applicant has terminated, or the Domain Name Registrant has failed to renew the Domain Name);
5. The CA is made aware that a Wildcard Certificate has been used to authenticate a fraudulently misleading subordinate Fully-Qualified Domain Name;
6. The CA is made aware of a material change in the information contained in the Certificate;
7. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's Certificate Policy or Certification Practice Statement;
8. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate;
9. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository;
10. Revocation is required by the CA's Certificate Policy and/or Certification Practice Statement; or
11. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise, methods have been developed that can easily calculate it based on the Public Key (such as a Debian weak key, see http://wiki.debian.org/SSLkeys), or if there is clear evidence that the specific method used to generate the Private Key was flawed.

#### 4.9.1.2 Reasons for revoking a subordinate CA certificate

The Issuing CA SHALL revoke a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:

1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of Sections 6.1.5 and 6.1.6;
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with or that Subordinate CA has not complied with this document or the applicable Certificate Policy or Certification Practice Statement;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository; or
9. Revocation is required by the Issuing CA's Certificate Policy and/or Certification Practice Statement.

### 4.9.2 Who can request revocation

The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties may submit Certificate Problem Reports informing the issuing CA of reasonable cause to revoke the certificate.

### 4.9.3 Procedure for revocation request

The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process MUST be described in the CA's Certificate Policy or Certification Practice Statement. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide Subscribers, Relying Parties, Application Software Suppliers, and other third parties with clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in section 1.5.2 of their CPS.

### 4.9.4 Revocation request grace period

No stipulation.

### 4.9.5 Time within which CA must process the revocation request

Within 24 hours after receiving a Certificate Problem Report, the CA SHALL investigate the facts and circumstances related to a Certificate Problem Report and provide a preliminary report on its findings to both the Subscriber and the entity who filed the Certificate Problem Report.

After reviewing the facts and circumstances, the CA SHALL work with the Subscriber and any entity reporting the Certificate Problem Report or other revocation-related notice to establish whether or not the certificate will be revoked, and if so, a date which the CA will revoke the certificate. The period from receipt of the Certificate Problem Report or revocation-related notice to published revocation MUST NOT exceed the time frame set forth in Section 4.9.1.1. The date selected by the CA SHOULD consider the following criteria:

1. The nature of the alleged problem (scope, context, severity, magnitude, risk of harm);
2. The consequences of revocation (direct and collateral impacts to Subscribers and Relying Parties);
3. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
4. The entity making the complaint (for example, a complaint from a law enforcement official that a Web site is engaged in illegal activities should carry more weight than a complaint from a consumer alleging that she didn't receive the goods she ordered); and
5. Relevant legislation.

### 4.9.6 Revocation checking requirement for relying parties

No stipulation.

(Note: Following certificate issuance, a certificate may be revoked for reasons stated in Section 4.9.1. Therefore, relying parties should check the revocation status of all certificates that contain a CDP or OCSP pointer.)

### 4.9.7 CRL issuance frequency (if applicable)

For the status of Subscriber Certificates:

> If the CA publishes a CRL, then the CA SHALL update and reissue CRLs at least once every seven days, and the value of the nextUpdate field MUST NOT be more than ten days beyond the value of the thisUpdate field.

For the status of Subordinate CA Certificates:

> The CA SHALL update and reissue CRLs at least (i) once every twelve months and (ii) within 24 hours after revoking a Subordinate CA Certificate, and the value of the nextUpdate field MUST NOT be more than twelve months beyond the value of the thisUpdate field.

### 4.9.8 Maximum latency for CRLs (if applicable)

No stipulation.

### 4.9.9 On-line revocation/status checking availability

OCSP responses MUST conform to RFC6960 and/or RFC5019. OCSP responses MUST either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or

2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose
revocation status is being checked.

In the latter case, the OCSP signing Certificate MUST contain an extension of type id-pkix-ocsp-nocheck, as
defined by RFC6960.

### 4.9.10 On-line revocation checking requirements

OCSP responders operated by the CA SHALL support the HTTP GET method, as described in RFC 6960 and/or RFC 5019.

The validity interval of an OCSP response is the difference in time between the thisUpdate and nextUpdate field, inclusive. For purposes of computing differences, a difference of 3,600 seconds shall be equal to one hour, and a difference of 86,400 seconds shall be equal to one day, ignoring leap-seconds.

For the status of Subscriber Certificates:

Prior to 2020-09-30:
The CA SHALL update information provided via an Online Certificate Status Protocol at least every four days. OCSP responses from this service MUST have a maximum expiration time of ten days.

Effective 2020-09-30:

1. OCSP responses MUST have a validity interval greater than or equal to eight hours;
2. OCSP responses MUST have a validity interval less than or equal to ten days;
3. For OCSP responses with validity intervals less than sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol prior to one-half of the validity period before the nextUpdate.
4. For OCSP responses with validity intervals greater than or equal to sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol at least eight hours prior to the nextUpdate, and no later than four days after the thisUpdate.

For the status of Subordinate CA Certificates:

* The CA SHALL update information provided via an Online Certificate Status Protocol (i) at least every twelve months; and (ii) within 24 hours after revoking a Subordinate CA Certificate.

If the OCSP responder receives a request for the status of a certificate serial number that is "unused", then the responder SHOULD NOT respond with a "good" status. If the OCSP responder is for a CA that is not Technically Constrained in line with Section 7.1.5, the responder MUST NOT respond with a "good" status for such requests.

The CA SHOULD monitor the OCSP responder for requests for "unused" serial numbers as part of its security response procedures.

The OCSP responder MAY provide definitive responses about "reserved" certificate serial numbers, as if there was a corresponding Certificate that matches the Precertificate [RFC6962].

A certificate serial number within an OCSP request is one of the following three options:

1.	"assigned" if a Certificate with that serial number has been issued by the Issuing CA, using any current or previous key associated with that CA subject; or
2.	"reserved" if a Precertificate [RFC6962] with that serial number has been issued by (a) the Issuing CA; or (b) a Precertificate Signing Certificate [RFC6962] associated with the Issuing CA; or
3.	"unused" if neither of the previous conditions are met.

### 4.9.11 Other forms of revocation advertisements available

If the Subscriber Certificate is for a high-traffic FQDN, the CA MAY rely on stapling, in accordance with [RFC4366], to distribute its OCSP responses. In this case, the CA SHALL ensure that the Subscriber “staples” the OCSP response for the Certificate in its TLS handshake. The CA SHALL enforce this requirement on the Subscriber either contractually, through the Subscriber Agreement or Terms of Use, or by technical review measures implemented by the CA.

### 4.9.12 Special requirements re key compromise

See Section 4.9.1.

### 4.9.13 Circumstances for suspension

The Repository MUST NOT include entries that indicate that a Certificate is suspended.

### 4.9.14 Who can request suspension

Not applicable.

### 4.9.15 Procedure for suspension request

Not applicable.

### 4.9.16 Limits on suspension period

Not applicable.

## 4.10 Certificate status services

### 4.10.1 Operational characteristics

Revocation entries on a CRL or OCSP Response MUST NOT be removed until after the Expiry Date of the revoked Certificate.

### 4.10.2 Service availability

The CA SHALL operate and maintain its CRL and OCSP capability with resources sufficient to provide a response time of ten seconds or less under normal operating conditions.

The CA SHALL maintain an online 24x7 Repository that application software can use to automatically check the current status of all unexpired Certificates issued by the CA.

The CA SHALL maintain a continuous 24x7 ability to respond internally to a high-priority Certificate Problem Report, and where appropriate, forward such a complaint to law enforcement authorities, and/or revoke a Certificate that is the subject of such a complaint.

### 4.10.3 Optional features

No stipulation.

## 4.11 End of subscription

No stipulation.

## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices

No stipulation.

### 4.12.2 Session key encapsulation and recovery policy and practices

No stipulation.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

The CA/Browser Forum’s Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

The CA SHALL develop, implement, and maintain a comprehensive security program designed to:

1. Protect the confidentiality, integrity, and availability of Certificate Data and Certificate Management Processes;
2. Protect against anticipated threats or hazards to the confidentiality, integrity, and availability of the Certificate Data and Certificate Management Processes;
3. Protect against unauthorized or unlawful access, use, disclosure, alteration, or destruction of any Certificate Data or Certificate Management Processes;
4. Protect against accidental loss or destruction of, or damage to, any Certificate Data or Certificate Management Processes; and
5. Comply with all other security requirements applicable to the CA by law.

The Certificate Management Process MUST include:

1. physical security and environmental controls;
2. system integrity controls, including configuration management, integrity maintenance of trusted code, and malware detection/prevention;
3. network security and firewall management, including port restrictions and IP address filtering;
4. user management, separate trusted-role assignments, education, awareness, and training; and
5. logical access controls, activity logging, and inactivity time-outs to provide individual accountability.

The CA’s security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

Based on the Risk Assessment, the CA SHALL develop, implement, and maintain a security plan consisting of security procedures, measures, and products designed to achieve the objectives set forth above and to manage and control the risks identified during the Risk Assessment, commensurate with the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST include administrative, organizational, technical, and physical safeguards appropriate to the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST also take into account then-available technology and the cost of implementing the specific measures, and SHALL implement a reasonable level of security appropriate to the harm that might result from a breach of security and the nature of the data to be protected.

## 5.1 Physical controls

### 5.1.1 Site location and construction

No stipulation.

### 5.1.2 Physical access

No stipulation.

### 5.1.3 Power and air conditioning

No stipulation.

### 5.1.4 Water exposures

No stipulation.

### 5.1.5 Fire prevention and protection

No stipulation.

### 5.1.6 Media storage

No stipulation.

### 5.1.7 Waste disposal

No stipulation.

### 5.1.8 Off-site backup

No stipulation.

## 5.2 Procedural controls

### 5.2.1 Trusted roles

No stipulation.

### 5.2.2 Number of persons required per task

The CA Private Key SHALL be backed up, stored, and recovered only by personnel in trusted roles using, at least, dual control in a physically secured environment.

### 5.2.3 Identification and authentication for each role

No stipulation.

### 5.2.4 Roles requiring separation of duties

No stipulation.

## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

Prior to the engagement of any person in the Certificate Management Process, whether as an employee, agent, or an independent contractor of the CA, the CA SHALL verify the identity and trustworthiness of such person.

### 5.3.2 Background check procedures

No stipulation.

### 5.3.3 Training requirements

The CA SHALL provide all personnel performing information verification duties with skills-training that covers basic Public Key Infrastructure knowledge, authentication and vetting policies and procedures (including the CA’s Certificate Policy and/or Certification Practice Statement), common threats to the information verification process (including phishing and other social engineering tactics), and these Requirements.

The CA SHALL maintain records of such training and ensure that personnel entrusted with Validation Specialist duties maintain a skill level that enables them to perform such duties satisfactorily.

The CA SHALL document that each Validation Specialist possesses the skills required by a task before allowing the Validation Specialist to perform that task.

The CA SHALL require all Validation Specialists to pass an examination provided by the CA on the information verification requirements outlined in these Requirements.

### 5.3.4 Retraining frequency and requirements

All personnel in Trusted Roles SHALL maintain skill levels consistent with the CA’s training and performance programs.

### 5.3.5 Job rotation frequency and sequence

No stipulation.

### 5.3.6 Sanctions for unauthorized actions

No stipulation.

### 5.3.7 Independent contractor requirements

The CA SHALL verify that the Delegated Third Party’s personnel involved in the issuance of a Certificate meet the training and skills requirements of Section 5.3.3 and the document retention and event logging requirements of Section 5.4.1.

### 5.3.8 Documentation supplied to personnel

No stipulation.

## 5.4 Audit logging procedures

### 5.4.1 Types of events recorded

The CA and each Delegated Third Party SHALL record details of the actions taken to process a certificate request and to issue a Certificate, including all information generated and documentation received in connection with the certificate request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:

1. CA key lifecycle management events, including:
  * Key generation, backup, storage, recovery, archival, and destruction; and
  * Cryptographic device lifecycle management events.
2. CA and Subscriber Certificate lifecycle management events, including:
  * Certificate requests, renewal, and re-key requests, and revocation;
  * All verification activities stipulated in these Requirements and the CA’s Certification Practice Statement;
  * Date, time, phone number used, persons spoken to, and end results of verification telephone calls;
  * Acceptance and rejection of certificate requests;
  * Issuance of Certificates; and
  * Generation of Certificate Revocation Lists and OCSP entries.
3. Security events, including:
  * Successful and unsuccessful PKI system access attempts;
  * PKI and security system actions performed;
  * Security profile changes;
  * System crashes, hardware failures, and other anomalies;
  * Firewall and router activities; and
  * Entries to and exits from the CA facility.

Log entries MUST include the following elements:

1. Date and time of entry;
2. Identity of the person making the journal entry; and
3. Description of the entry.

### 5.4.2 Frequency of processing log

No stipulation.

### 5.4.3 Retention period for audit log

The CA SHALL retain any audit logs generated for at least seven years. The CA SHALL make these audit logs available to its Qualified Auditor upon request.

### 5.4.4 Protection of audit log

No stipulation.

### 5.4.5 Audit log backup procedures

No stipulation.

### 5.4.6 Audit collection system (internal vs. external)

No stipulation.

### 5.4.7 Notification to event-causing subject

No stipulation.

### 5.4.8 Vulnerability assessments

Additionally, the CA’s security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;

2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and

3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

## 5.5 Records archival

### 5.5.1 Types of records archived

No stipulation.

### 5.5.2 Retention period for archive

The CA SHALL retain all documentation relating to certificate requests and the verification thereof, and all Certificates and revocation thereof, for at least seven years after any Certificate based on that documentation ceases to be valid.

### 5.5.3 Protection of archive

No stipulation.

### 5.5.4 Archive backup procedures

No stipulation.

### 5.5.5 Requirements for time-stamping of records

No stipulation.

### 5.5.6 Archive collection system (internal or external)

No stipulation.

### 5.5.7 Procedures to obtain and verify archive information

No stipulation.

## 5.6 Key changeover

No stipulation.

## 5.7 Compromise and disaster recovery

### 5.7.1 Incident and compromise handling procedures

CA organizations shall have an Incident Response Plan and a Disaster Recovery Plan.

The CA SHALL document a business continuity and disaster recovery procedures designed to notify and reasonably protect Application Software Suppliers, Subscribers, and Relying Parties in the event of a disaster, security compromise, or business failure. The CA is not required to publicly disclose its business continuity plans but SHALL make its business continuity plan and security plans available to the CA’s auditors upon request. The CA SHALL annually test, review, and update these procedures.

The business continuity plan MUST include:

1. The conditions for activating the plan,
2. Emergency procedures,
3. Fallback procedures,
4. Resumption procedures,
5. A maintenance schedule for the plan;
6. Awareness and education requirements;
7. The responsibilities of the individuals;
8. Recovery time objective (RTO);
9. Regular testing of contingency plans.
10. The CA’s plan to maintain or restore the CA’s business operations in a timely manner following interruption to or failure of critical business processes
11. A requirement to store critical cryptographic materials (i.e., secure cryptographic device and activation materials) at an alternate location;
12. What constitutes an acceptable system outage and recovery time
13. How frequently backup copies of essential business information and software are taken;
14. The distance of recovery facilities to the CA’s main site; and
15. Procedures for securing its facility to the extent possible during the period of time following a disaster and prior to restoring a secure environment either at the original or a remote site.

### 5.7.2 Computing resources, software, and/or data are corrupted

No stipulation.

### 5.7.3 Entity private key compromise procedures

No stipulation.

### 5.7.4 Business continuity capabilities after a disaster

No stipulation.

## 5.8 CA or RA termination

No stipulation.

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

#### 6.1.1.1 CA key pair generation

For Root CA Key Pairs created after the Effective Date that are either (i) used as Root CA Key Pairs or (ii) Key Pairs generated for a subordinate CA that is not the operator of the Root CA or an Affiliate of the Root CA, the CA SHALL:

1. prepare and follow a Key Generation Script,
2. have a Qualified Auditor witness the Root CA Key Pair generation process or record a video of the entire Root CA Key Pair generation process, and
3. have a Qualified Auditor issue a report opining that the CA followed its key ceremony during its Key and Certificate generation process and the controls used to ensure the integrity and confidentiality of the Key Pair.

For other CA Key Pairs created after the Effective Date that are for the operator of the Root CA or an Affiliate of the Root CA, the CA SHOULD:

1. prepare and follow a Key Generation Script and
2. have a Qualified Auditor witness the Root CA Key Pair generation process or record a video of the entire Root CA Key Pair generation process.

In all cases, the CA SHALL:

1. generate the keys in a physically secured environment as described in the CA’s Certificate Policy and/or Certification Practice Statement;
2. generate the CA keys using personnel in trusted roles under the principles of multiple person control and split knowledge;
3. generate the CA keys within cryptographic modules meeting the applicable technical and business requirements as disclosed in the CA’s Certificate Policy and/or Certification Practice Statement;
4. log its CA key generation activities; and
5. maintain effective controls to provide reasonable assurance that the Private Key was generated and protected in conformance with the procedures described in its Certificate Policy and/or Certification Practice Statement and (if applicable) its Key Generation Script.

#### 6.1.1.2 RA key pair generation

No stipulation.

#### 6.1.1.3 Subscriber key pair generation

The CA SHALL reject a certificate request if the requested Public Key does not meet the requirements set forth in Sections 6.1.5 and 6.1.6 or if it has a known weak Private Key (such as a Debian weak key, see [http://wiki.debian.org/SSLkeys](http://wiki.debian.org/SSLkeys)).

### 6.1.2 Private key delivery to subscriber

Parties other than the Subscriber SHALL NOT archive the Subscriber Private Key without authorization by the Subscriber.

If the CA or any of its designated RAs generated the Private Key on behalf of the Subscriber, then the CA SHALL encrypt the Private Key for transport to the Subscriber.

If the CA or any of its designated RAs become aware that a Subscriber’s Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subscriber, then the CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.1.3 Public key delivery to certificate issuer

No stipulation.

### 6.1.4 CA public key delivery to relying parties

No stipulation.

### 6.1.5 Key sizes

Certificates MUST meet the following requirements for algorithm type and key size.

(1)	Root CA Certificates

* Digest algorithm
  * SHA-1\*, SHA-256, SHA-384 or SHA-512
* Minimum RSA modulus size (bits)
  * 2048
* ECC curve
  * NIST P-256, P-384, or P-521
* Minimum DSA modulus and divisor size (bits) \*\*\*
  * L= 2048, N= 224 or L= 2048, N= 256

(2)	Subordinate CA Certificates

* Digest algorithm
  * SHA-1\*, SHA-256, SHA-384 or SHA-512
* Minimum RSA modulus size (bits)
  * 2048
* ECC curve
  * NIST P-256, P-384, or P-521
* Minimum DSA modulus and divisor size (bits)\*\*\*
  * L= 2048, N= 224 Or L= 2048, N= 256


(3)	Subscriber Certificates

* Digest algorithm
  * SHA1\*, SHA-256, SHA-384 or SHA-512
* Minimum RSA modulus size (bits)
  * 2048
* ECC curve
  * NIST P-256, P-384, or P-521
* Minimum DSA modulus and divisor size (bits)\*\*\*
  * L= 2048, N= 224 Or L= 2048, N= 256

\* SHA-1 MAY be used with RSA keys in accordance with the criteria defined in Section 7.1.3.

\*\*\* L and N (the bit lengths of modulus p and divisor q, respectively) are described in the Digital Signature Standard, FIPS 186-4 ([http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf](http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)).

### 6.1.6 Public key parameters generation and quality checking

RSA: The CA SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2<sup>16</sup>+1 and 2<sup>256</sup>-1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. [Source: Section 5.3.3, NIST SP 800-89].

DSA: Although FIPS 800-57 says that domain parameters may be made available at some accessible site, compliant DSA certificates MUST include all domain parameters. This is to insure maximum interoperability among relying party software. The CA MUST confirm that the value of the public key has the unique correct representation and range in the field, and that the key has the correct order in the subgroup. [Source: Section 5.3.1, NIST SP 800-89].

ECC: The CA SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. [Source: Sections 5.6.2.3.2 and 5.6.2.3.3, respectively, of NIST SP 56A: Revision 2].

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

Private Keys corresponding to Root Certificates MUST NOT be used to sign Certificates except in the following cases:

1. Self-signed Certificates to represent the Root CA itself;
2. Certificates for Subordinate CAs and Cross Certificates;
3. Certificates for infrastructure purposes (administrative role certificates, internal CA operational device
certificates); and
4. Certificates for OCSP Response verification.

## 6.2 Private Key Protection and Cryptographic Module Engineering Controls

The CA SHALL implement physical and logical safeguards to prevent unauthorized certificate issuance. Protection of the CA Private Key outside the validated system or device specified above MUST consist of physical security, encryption, or a combination of both, implemented in a manner that prevents disclosure of the CA Private Key. The CA SHALL encrypt its Private Key with an algorithm and key-length that, according to the state of the art, are capable of withstanding cryptanalytic attacks for the residual life of the encrypted key or key part.

### 6.2.1 Cryptographic module standards and controls

No stipulation.

### 6.2.2 Private key (n out of m) multi-person control

No stipulation.

### 6.2.3 Private key escrow

No stipulation.

### 6.2.4 Private key backup

See Section 5.2.2.

### 6.2.5 Private key archival

Parties other than the Subordinate CA SHALL NOT archive the Subordinate CA Private Keys without authorization by the Subordinate CA.

### 6.2.6 Private key transfer into or from a cryptographic module

If the Issuing CA generated the Private Key on behalf of the Subordinate CA, then the Issuing CA SHALL encrypt the Private Key for transport to the Subordinate CA. If the Issuing CA becomes aware that a Subordinate CA’s Private Key has been communicated to an unauthorized person or an organization not affiliated with the Subordinate CA, then the Issuing CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.2.7 Private key storage on cryptographic module

The CA SHALL protect its Private Key in a system or device that has been validated as meeting at least FIPS 140 level 3 or an appropriate Common Criteria Protection Profile or Security Target, EAL 4 (or higher), which includes requirements to protect the Private Key and other assets against known threats.

### 6.2.8 Method of activating private key

No stipulation.

### 6.2.9 Method of deactivating private key

No stipulation.

### 6.2.10 Method of destroying private key

No stipulation.

### 6.2.11 Cryptographic Module Rating

No stipulation.

## 6.3 Other aspects of key pair management

### 6.3.1 Public key archival

No stipulation.

### 6.3.2 Certificate operational periods and key pair usage periods

Subscriber Certificates issued after 1 March 2018 MUST have a Validity Period no greater than 825 days.

Subscriber Certificates issued after 1 July 2016 but prior to 1 March 2018 MUST have a Validity Period no greater than 39 months.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

No stipulation.

### 6.4.2 Activation data protection

No stipulation.

### 6.4.3 Other aspects of activation data

No stipulation.

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

The CA SHALL enforce multi-factor authentication for all accounts capable of directly causing certificate issuance.

### 6.5.2 Computer security rating

No stipulation.

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

No stipulation.

### 6.6.2 Security management controls

No stipulation.

### 6.6.3 Life cycle security controls

No stipulation.

## 6.7 Network security controls

No stipulation.

## 6.8 Time-stamping

No stipulation.

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

The CA SHALL meet the technical requirements set forth in Section 2.2 - Publication of Information, Section 6.1.5 - Key Sizes, and Section 6.1.6 - Public Key Parameters Generation and Quality Checking.

CAs SHALL generate non-sequential Certificate serial numbers greater than zero (0) containing at least 64 bits of output from a CSPRNG.

### 7.1.1 Version number(s)

Certificates MUST be of type X.509 v3.

### 7.1.2 Certificate extensions

This section specifies the additional requirements for Certificate content and extensions for Certificates.

#### 7.1.2.1 Root CA certificate

a. `basicConstraints`

   This extension MUST appear as a critical extension. The cA field MUST be set true. The pathLenConstraint field SHOULD NOT be present.

b. `keyUsage`

   This extension MUST be present and MUST be marked critical. Bit positions for keyCertSign and cRLSign MUST be set. If the Root CA Private Key is used for signing OCSP responses, then the digitalSignature bit MUST be set.

c. `certificatePolicies`

   This extension SHOULD NOT be present.

d. `extendedKeyUsage`

   This extension MUST NOT be present.

#### 7.1.2.2 Subordinate CA certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   `certificatePolicies:policyIdentifier` (Required)

   The following fields MAY be present if the Subordinate CA is not an Affiliate of the entity that controls the Root CA.

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Optional)

     id-qt 1 [RFC5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

   HTTP URL for the Root CA's Certificate Policies, Certification Practice Statement, Relying Party Agreement, or other pointer to online policy information provided by the CA.

b. `cRLDistributionPoints`

   This extension MUST be present and MUST NOT be marked critical. It MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension SHOULD be present. It MUST NOT be marked critical.

   It SHOULD contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   It MAY contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).

d. `basicConstraints`

   This extension MUST be present and MUST be marked critical. The cA field MUST be set true. The pathLenConstraint field MAY be present.

e. `keyUsage`

   This extension MUST be present and MUST be marked critical. Bit positions for `keyCertSign` and `cRLSign` MUST be set. If the Subordinate CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit MUST be set.

f. `nameConstraints` (optional)

   If present, this extension SHOULD be marked critical[^*].

[^*]: Non-critical Name Constraints are an exception to RFC 5280 (4.2.1.10), however, they MAY be used until the Name Constraints extension is supported by Application Software Suppliers whose software is used by a substantial portion of Relying Parties worldwide.

g. `extkeyUsage` (optional/required)

   For Cross Certificates that share a Subject Distinguished Name and Subject Public Key with a Root Certificate operated in accordance with these Requirements, this extension MAY be present. If present, this extension SHOULD NOT be marked critical. This extension MUST only contain usages for which the issuing CA has verified the Cross Certificate is authorized to assert. This extension MAY contain the `anyExtendedKeyUsage` [RFC5280] usage, if the Root Certificate(s) associated with this Cross Certificate are operated by the same organization as the issuing Root Certificate.

   For all other Subordinate CA Certificates, including Technically Constrained Subordinate CA Certificates:

   This extension MUST be present and SHOULD NOT be marked critical[^**].

   For Subordinate CA Certificates that will be used to issue TLS certificates, the value `id-kp-serverAuth` [RFC5280] MUST be present. The value `id-kp-clientAuth` [RFC5280] MAY be present. The values `id-kp-emailProtection` [RFC5280], `id-kp-codeSigning` [RFC5280], `id-kp-timeStamping` [RFC5280], and `anyExtendedKeyUsage` [RFC5280] MUST NOT be present. Other values SHOULD NOT be present.

   For Subordinate CA Certificates that are not used to issue TLS certificates, then the value `id-kp-serverAuth` [RFC5280] MUST NOT be present. Other values MAY be present, but SHOULD NOT combine multiple independent usages (e.g. including `id-kp-timeStamping` [RFC5280] with `id-kp-codeSigning` [RFC5280]).

[^**]: While RFC 5280, Section 4.2.1.12, notes that this extension will generally only appear within end-entity certificates, these Requirements make use of this extension to further protect relying parties by limiting the scope of subordinate certificates, as implemented by a number of Application Software Suppliers.

h. `authorityKeyIdentifier` (required)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain a keyIdentifier field and it MUST NOT contain a authorityCertIssuer or authorityCertSerialNumber field.

#### 7.1.2.3 Subscriber certificate

a. `certificatePolicies`

   This extension MUST be present and SHOULD NOT be marked critical.

   * `certificatePolicies:policyIdentifier` (Required)

      A Policy Identifier, defined by the issuing CA, that indicates a Certificate Policy asserting the issuing CA's adherence to and compliance with these Requirements.

   The following extensions MAY be present:

   * `certificatePolicies:policyQualifiers:policyQualifierId` (Recommended)

      id-qt 1 [RFC 5280].

   * `certificatePolicies:policyQualifiers:qualifier:cPSuri` (Optional)

      HTTP URL for the Subordinate CA's Certification Practice Statement, Relying Party Agreement or other pointer to online information provided by the CA.

b. `cRLDistributionPoints`

   This extension MAY be present. If present, it MUST NOT be marked critical, and it MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess`

   This extension MUST be present. It MUST NOT be marked critical, and it MUST contain the HTTP URL of the Issuing CA's OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1). It SHOULD also contain the HTTP URL of the Issuing CA's certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).

d. `basicConstraints` (optional)

   The cA field MUST NOT be true.

e. `keyUsage` (optional)

   If present, bit positions for keyCertSign and cRLSign MUST NOT be set.

f. `extKeyUsage` (required)

   Either the value `id-kp-serverAuth` [RFC5280] or `id-kp-clientAuth` [RFC5280] or both values MUST be present. `id-kp-emailProtection` [RFC5280] MAY be present. Other values SHOULD NOT be present. The value `anyExtendedKeyUsage` MUST NOT be present.

g. `authorityKeyIdentifier` (required)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain a `keyIdentifier` field and it MUST NOT contain a `authorityCertIssuer` or `authorityCertSerialNumber` field.

#### 7.1.2.4 All certificates

All other fields and extensions MUST be set in accordance with RFC 5280. The CA SHALL NOT issue a Certificate that contains a `keyUsage` flag, `extendedKeyUsage` value, Certificate extension, or other data not specified in section 7.1.2.1, 7.1.2.2, or 7.1.2.3  unless the CA is aware of a reason for including the data in the Certificate.

CAs SHALL NOT issue a Certificate with:

a. Extensions that do not apply in the context of the public Internet (such as an extendedKeyUsage value for a service that is only valid in the context of a privately managed network), unless:

   i. such value falls within an OID arc for which the Applicant demonstrates ownership, or
   ii. the Applicant can otherwise demonstrate the right to assert the data in a public context; or

b. semantics that, if included, will mislead a Relying Party about the certificate information verified by the CA (such as including extendedKeyUsage value for a smart card, where the CA is not able to verify that the corresponding Private Key is confined to such hardware due to remote issuance).

#### 7.1.2.5 Application of RFC 5280

For purposes of clarification, a Precertificate, as described in RFC 6962 - Certificate Transparency, shall not be considered to be a "certificate" subject to the requirements of RFC 5280 - Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile under these Requirements.

### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

The following requirements apply to the `subjectPublicKeyInfo` field within a Certificate or Precertificate. No other encodings are permitted.

##### 7.1.3.1.1 RSA

The CA SHALL indicate an RSA key using the rsaEncryption (OID: 1.2.840.113549.1.1.1) algorithm identifier. The parameters MUST be present, and MUST be an explicit NULL.
The CA SHALL NOT use a different algorithm, such as the id-RSASSA-PSS (OID: 1.2.840.113549.1.1.10) algorithm identifier, to indicate an RSA key.

When encoded, the `AlgorithmIdentifier` for RSA keys MUST be byte-for-byte identical with the following hex-encoded bytes: `300d06092a864886f70d0101010500`

##### 7.1.3.1.2 ECDSA

The CA SHALL indicate an ECDSA key using the id-ecPublicKey (OID: 1.2.840.10045.2.1) algorithm identifier. The parameters MUST use the `namedCurve` encoding.

* For P-256 keys, the `namedCurve` MUST be secp256r1 (OID: 1.2.840.10045.3.1.7).
* For P-384 keys, the `namedCurve` MUST be secp384r1 (OID: 1.3.132.0.34).
* For P-521 keys, the `namedCurve` MUST be secp521r1 (OID: 1.3.132.0.35).

When encoded, the `AlgorithmIdentifier` for ECDSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:

* For P-256 keys, `301306072a8648ce3d020106082a8648ce3d030107`.
* For P-384 keys, `301006072a8648ce3d020106052b81040022`.
* For P-521 keys, `301006072a8648ce3d020106052b81040023`.

#### 7.1.3.2 Signature AlgorithmIdentifier

All objects signed by a CA Private Key MUST conform to these requirements on the use of the `AlgorithmIdentifier` or `AlgorithmIdentifier`-derived type in the context of signatures.

In particular, it applies to all of the following objects and fields:

* The `signatureAlgorithm` field of a Certificate or Precertificate.
* The `signature` field of a TBSCertificate (for example, as used by either a Certificate or Precertificate).
* The `signatureAlgorithm` field of a CertificateList
* The `signature` field of a TBSCertList
* The `signatureAlgorithm` field of a BasicOCSPResponse.

No other encodings are permitted for these fields.

##### 7.1.3.2.1 RSA

The CA SHALL use one of the following signature algorithms and encodings. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the specified hex-encoded bytes.

* RSASSA-PKCS1-v1_5 with SHA-256:

  Encoding:
  `300d06092a864886f70d01010b0500`.

* RSASSA-PKCS1-v1_5 with SHA-384:

  Encoding:
  `300d06092a864886f70d01010c0500`.

* RSASSA-PKCS1-v1_5 with SHA-512:

  Encoding:
  `300d06092a864886f70d01010d0500`.

* RSASSA-PSS with SHA-256, MGF-1 with SHA-256, and a salt length of 32 bytes:

  Encoding:
  ```
  304106092a864886f70d01010a3034a00f300d0609608648016503040201
  0500a11c301a06092a864886f70d010108300d0609608648016503040201
  0500a203020120
  ```

* RSASSA-PSS with SHA-384, MGF-1 with SHA-384, and a salt length of 48 bytes:

  Encoding:
  ```
  304106092a864886f70d01010a3034a00f300d0609608648016503040202
  0500a11c301a06092a864886f70d010108300d0609608648016503040202
  0500a203020130
  ```

* RSASSA-PSS with SHA-512, MGF-1 with SHA-512, and a salt length of 64 bytes:

  Encoding:
  ```
  304106092a864886f70d01010a3034a00f300d0609608648016503040203
  0500a11c301a06092a864886f70d010108300d0609608648016503040203
  0500a203020140
  ```

In addition, the CA MAY use the following signature algorithm and encoding if all of the following conditions are met:

* If used within a Certificate, such as the `signatureAlgorithm` field of a Certificate or the `signature` field of a TBSCertificate:
  * The new Certificate is a Root CA Certificate or Subordinate CA Certificate that is a Cross-Certificate; and,
  * There is an existing Certificate, issued by the same issuing CA Certificate, using the following encoding for the signature algorithm; and,
  * The existing Certificate has a `serialNumber` that is at least 64-bits long; and,
  * The only differences between the new Certificate and existing Certificate are one of the following:
    * A new `subjectPublicKey` within the `subjectPublicKeyInfo`, using the same algorithm and key size; and/or,
    * A new `serialNumber`, of the same encoded length as the existing Certificate; and/or
    * The new Certificate's `extendedKeyUsage` extension is present, has at least one key usage specified, and none of the key usages specified are the id-kp-serverAuth (OID: 1.3.6.1.5.5.7.3.1) or the anyExtendedKeyUsage (OID: 2.5.2937.0) key usages; and/or
    * The new Certificate's `basicConstraints` extension has a pathLenConstraint that is zero.
* If used within an OCSP response, such as the `signatureAlgorithm` of a BasicOCSPResponse:
  * All unexpired, un-revoked Certificates that contain the Public Key of the CA Key Pair and that have the same Subject Name MUST also contain an `extendedKeyUsage` extension with the only key usage present being the id-kp-ocspSigning (OID: 1.3.6.1.5.5.7.3.9) key usage.
* If used within a CRL, such as the `signatureAlgorithm` field of a CertificateList or the `signature` field of a TBSCertList:
  * The CRL is referenced by one or more Root CA or Subordinate CA Certificates; and,
  * The Root CA or Subordinate CA Certificate has issued one or more Certificates using the following encoding for the signature algorithm.

**Note:** The above requirements do not permit a CA to sign a Precertificate with this encoding.

* RSASSA-PKCS1-v1_5 with SHA-1:

  Encoding:
  `300d06092a864886f70d0101050500`

##### 7.1.3.2.2 ECDSA
The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is P-256, the signature MUST use ECDSA with SHA-256. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040302`.

If the signing key is P-384, the signature MUST use ECDSA with SHA-384. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040303`.

If the signing key is P-521, the signature MUST use ECDSA with SHA-512. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040304`.

### 7.1.4 Name forms

#### 7.1.4.1 Issuer information

The content of the Certificate Issuer Distinguished Name field MUST match the Subject DN of the Issuing CA to support Name chaining as specified in RFC 5280, section 4.1.2.4.

#### 7.1.4.2 Subject information

By issuing the Certificate, the CA represents that it followed the procedure set forth in its Certificate Policy and/or Certification Practice Statement to verify that, as of the Certificate’s issuance date, all of the Subject Information was accurate. CAs SHALL NOT include a Domain Name or IP Address in a Subject attribute except as specified in Sections 3.2.2.4 or 3.2.2.5.

##### 7.1.4.2.1 Subject alternative name extension

| Certificate Field         | Req\Opt  | Contents                       |
|---------------------------|----------|--------------------------------|
| extensions:subjectAltName | Required | This extension MUST contain at least one entry. Each entry MUST be either a dNSName containing the Fully-Qualified Domain Name or an iPAddress containing the IP address of a server. The CA MUST confirm that the Applicant controls the Fully-Qualified Domain Name or IP address or has been granted the right to use it by the Domain Name Registrant or IP address assignee, as appropriate. Wildcard FQDNs are permitted. |

As of the Effective Date of these Requirements, prior to the issuance of a Certificate with a subjectAlternativeName extension or Subject commonName field containing a Reserved IP Address or Internal Name, the CA SHALL notify the Applicant that the use of such Certificates has been deprecated by the CA / Browser Forum and that the practice will be eliminated by October 2016. Also as of the Effective Date, the CA SHALL NOT issue a certificate with an Expiry Date later than 1 November 2015 with a subjectAlternativeName extension or Subject commonName field containing a Reserved IP Address or Internal Name. Effective 1 October 2016, CAs SHALL revoke all unexpired Certificates whose subjectAlternativeName extension or Subject commonName field contains a Reserved IP Address or Internal Name. Effective May 1, 2015, each CA SHALL revoke all unexpired Certificates with an Internal Name using onion as the right-most label in an entry in the subjectAltName Extension or commonName field unless such Certificate was issued in accordance with Appendix F of the EV Guidelines.

##### 7.1.4.2.2 Subject distinguished name fields

| Certificate Field         | Req\Opt  | Contents                       |
|---------------------------|----------|--------------------------------|
| subject:commonName (OID 2.5.4.3) | Deprecated | If present, this field MUST contain a single IP address or Fully-Qualified Domain Name that is one of the values contained in the Certificate’s subjectAltName extension (see Section 7.1.4.2.1). |
| subject:organizationName (OID 2.5.4.10) | Optional | If present, the subject:organizationName field MUST contain either the Subject’s name or DBA as verified under Section 3.2.2.2. The CA may include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows “Company Name Incorporated”, the CA MAY use “Company Name Inc.” or “Company Name”. Because Subject name attributes for individuals (e.g. givenName (2.5.4.42) and surname (2.5.4.4)) are not broadly supported by application software, the CA MAY use the subject:organizationName field to convey a natural person Subject’s name or DBA. |
| subject:givenName (2.5.4.42) and subject:surname (2.5.4.4) | Optional | If present, the subject:givenName field and subject:surname field MUST contain an natural person Subject’s name as verified under Section 3.2.3. A Certificate containing a subject:givenName field or subject:surname field MUST contain the (2.23.140.1.2.3) Certificate Policy OID. |
| subject:streetAddress (OID: 2.5.4.9) | Optional if the subject:organizationName field, subject:givenName field, or subject:surname field are present. Prohibited if the subject:organizationName field, subject:givenName, and subject:surname field are absent. | If present, the subject:streetAddress field MUST contain the Subject’s street address information as verified under Section 3.2.2.1. |
| subject:localityName (OID: 2.5.4.7) | Required if the subject:organizationName field, subject:givenName field, or subject:surname field are present and the subject:stateOrProvinceName field is absent. Optional if the subject:stateOrProvinceName field and the subject:organizationName field, subject:givenName field, or subject:surname field are present. Prohibited if the subject:organizationName field, subject:givenName, and subject:surname field are absent. | If present, the subject:localityName field MUST contain the Subject’s locality information as verified under Section 3.2.2.1. If the subject:countryName field specifies the ISO 3166-1 user-assigned code of XX in accordance with Section 7.1.4.2.2(g), the localityName field MAY contain the Subject’s locality and/or state or province information as verified under Section 3.2.2.1. |
| subject:stateOrProvinceName (OID: 2.5.4.8) | Required if the subject:organizationName field, subject:givenName field, or subject:surname field are present and subject:localityName field is absent. Optional if the subject:localityName field and the subject:organizationName field, and subject:givenName field , or subject:surname field are present. Prohibited if the subject:organizationName field, subject:givenName field , or subject:surname field are absent. | If present, the subject:stateOrProvinceName field MUST contain the Subject’s state or province information as verified under Section 3.2.2.1. If the subject:countryName field specifies the ISO 3166-1 user-assigned code of XX in accordance with Section 7.1.4.2.2(g), the subject:stateOrProvinceName field MAY contain the full name of the Subject’s country information as verified under Section 3.2.2.1. |
| subject:postalCode (OID: 2.5.4.17) | Optional if the subject:organizationName, subject:givenName field, or subject:surname fields are present. Prohibited if the subject:organizationName field, subject:givenName field, or subject:surname field are absent. | If present, the subject:postalCode field MUST contain the Subject’s zip or postal information as verified under Section 3.2.2.1. |
| subject:countryName (OID: 2.5.4.6) ) | Required if the subject:organizationName field, subject:givenName, or subject:surname field are present. Optional if the subject:organizationName field, subject:givenName field, and subject:surname field are absent. | If the subject:organizationName field is present, the subject:countryName MUST contain the two-letter ISO 3166-1 country code associated with the location of the Subject verified under Section 3.2.2.1. If the subject:organizationName field is absent, the subject:countryName field MAY contain the two-letter ISO 3166-1 country code associated with the Subject as verified in accordance with Section 3.2.2.3. If a Country is not represented by an official ISO 3166-1 country code, the CA MAY specify the ISO 3166-1 user-assigned code of XX indicating that an official ISO 3166-1 alpha-2 code has not been assigned. |
| subject:organizationalUnitName | Optional | The CA SHALL implement a process that prevents an OU attribute from including a name, DBA, tradename, trademark, address, location, or other text that refers to a specific natural person or Legal Entity unless the CA has verified this information in accordance with Section 3.2 and the Certificate also contains subject:organizationName, subject:givenName, subject:surname, subject:localityName, and subject:countryName attributes, also verified in accordance with Section 3.2.2.1. |

All other optional attributes, when present within the subject field, MUST contain information that has been verified by the CA. Optional attributes MUST NOT contain metadata such as ‘.’, ‘-‘, and ‘ ‘ (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable.

#### 7.1.4.3 Subject information – subordinate CA certificates

By issuing a Subordinate CA Certificate, the CA represents that it followed the procedure set forth in its Certificate Policy and/or Certification Practice Statement to verify that, as of the Certificate’s issuance date, all of the Subject Information was accurate.

### 7.1.5 Name constraints

For a Subordinate CA Certificate to be considered Technically Constrained, the certificate MUST include an Extended Key Usage (EKU) extension specifying all extended key usages that the Subordinate CA Certificate is authorized to issue certificates for. The anyExtendedKeyUsage KeyPurposeId MUST NOT appear within this extension.

If the Subordinate CA Certificate includes the id-kp-serverAuth extended key usage, then the Subordinate CA Certificate MUST include the Name Constraints X.509v3 extension with constraints on dNSName, iPAddress and DirectoryName as follows:

* For each dNSName in permittedSubtrees, the CA MUST confirm that the Applicant has registered the dNSName or has been authorized by the domain registrant to act on the registrant's behalf in line with the verification practices of section 3.2.2.4.
* For each iPAddress range in permittedSubtrees, the CA MUST confirm that the Applicant has been assigned the iPAddress range or has been authorized by the assigner to act on the assignee's behalf.
* For each DirectoryName in permittedSubtrees the CA MUST confirm the Applicants and/or Subsidiary’s Organizational name and location such that end entity certificates issued from the subordinate CA Certificate will be in compliancy with section 7.1.2.4 and 7.1.2.5.

If the Subordinate CA Certificate is not allowed to issue certificates with an iPAddress, then the Subordinate CA Certificate MUST specify the entire IPv4 and IPv6 address ranges in excludedSubtrees. The Subordinate CA Certificate MUST include within excludedSubtrees an iPAddress GeneralName of 8 zero octets (covering the IPv4 address range of 0.0.0.0/0). The Subordinate CA Certificate MUST also include within excludedSubtrees an iPAddress GeneralName of 32 zero octets (covering the IPv6 address range of ::0/0). Otherwise, the Subordinate CA Certificate MUST include at least one iPAddress in permittedSubtrees.

A decoded example for issuance to the domain and sub domains of example.com by organization Example LLC, Boston, Massachusetts, US would be:

```markdown
    X509v3 Name Constraints:
          Permitted:
               DNS:example.com
               DirName: C=US, ST=MA, L=Boston, O=Example LLC
          Excluded:
               IP:0.0.0.0/0.0.0.0
               IP:0:0:0:0:0:0:0:0/0:0:0:0:0:0:0:0
```

If the Subordinate CA is not allowed to issue certificates with dNSNames, then the Subordinate CA Certificate MUST include a zero-length dNSName in excludedSubtrees. Otherwise, the Subordinate CA Certificate MUST include at least one dNSName in permittedSubtrees.

### 7.1.6 Certificate policy object identifier

#### 7.1.6.1 Reserved certificate policy identifiers

This section describes the content requirements for the Root CA, Subordinate CA, and Subscriber Certificates, as they relate to the identification of Certificate Policy.

The following Certificate Policy identifiers are reserved for use by CAs as an optional means of asserting compliance with these Requirements as follows:

> {joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) domain-validated(1)} (2.23.140.1.2.1), if the Certificate complies with these Requirements but lacks Subject Identity Information that is verified in accordance with Section 3.2.2.1 or Section 3.2.3.

If the Certificate asserts the policy identifier of 2.23.140.1.2.1, then it MUST NOT include organizationName, givenName, surname, streetAddress, localityName, stateOrProvinceName, or postalCode in the Subject field.

> {joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) baseline-requirements(2) organization-validated(2)} (2.23.140.1.2.2), if the Certificate complies with these Requirements and includes Subject Identity Information that is verified in accordance with Section 3.2.2.1.

> {joint‐iso‐itu‐t(2) international‐organizations(23) ca‐browser‐forum(140) certificate‐policies(1) baseline‐requirements(2) individual-validated(3)} (2.23.140.1.2.3), if the Certificate complies with these Requirements and includes Subject Identity Information that is verified in accordance with Section 3.2.3.

If the Certificate asserts the policy identifier of 2.23.140.1.2.2, then it MUST also include organizationName, localityName (to the extent such field is required under Section 7.1.4.2.2), stateOrProvinceName (to the extent such field is required under Section 7.1.4.2.2), and countryName in the Subject field. If the Certificate asserts the policy identifier of 2.23.140.1.2.3, then it MUST also include (i) either organizationName or givenName and surname, (ii) localityName (to the extent such field is required under Section 7.1.4.2.2), (iii) stateOrProvinceName (to the extent required under Section 7.1.4.2.2), and (iv) countryName in the Subject field.

#### 7.1.6.2 Root CA certificates

A Root CA Certificate SHOULD NOT contain the certificatePolicies extension.

#### 7.1.6.3 Subordinate CA certificates

A Certificate issued after the Effective Date to a Subordinate CA that is not an Affiliate of the Issuing CA:

1.	MUST include one or more explicit policy identifiers that indicates the Subordinate CA’s adherence to and compliance with these Requirements (i.e. either the CA/Browser Forum reserved identifiers or identifiers defined by the CA in its Certificate Policy and/or Certification Practice Statement) and
2.	MUST NOT contain the “anyPolicy” identifier (2.5.29.32.0).

A Certificate issued after the Effective Date to a Subordinate CA that is an affiliate of the Issuing CA:

1.	MAY include the CA/Browser Forum reserved identifiers or an identifier defined by the CA in its Certificate Policy and/or Certification Practice Statement to indicate the Subordinate CA’s compliance with these Requirements and
2.	MAY contain the “anyPolicy” identifier (2.5.29.32.0) in place of an explicit policy identifier.

A Subordinate CA SHALL represent, in its Certificate Policy and/or Certification Practice Statement, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

#### 7.1.6.4 Subscriber certificates

A Certificate issued to a Subscriber MUST contain one or more policy identifier(s), defined by the Issuing CA, in the Certificate’s certificatePolicies extension that indicates adherence to and compliance with these Requirements. CAs complying with these Requirements MAY also assert one of the reserved policy OIDs in such Certificates.

The issuing CA SHALL document in its Certificate Policy or Certification Practice Statement that the Certificates it issues containing the specified policy identifier(s) are managed in accordance with these Requirements.

### 7.1.7 Usage of Policy Constraints extension

No stipulation.

### 7.1.8 Policy qualifiers syntax and semantics

No stipulation.

### 7.1.9 Processing semantics for the critical Certificate Policies extension

No stipulation.

## 7.2 CRL profile

### 7.2.1 Version number(s)

No stipulation.

### 7.2.2 CRL and CRL entry extensions

No stipulation.

## 7.3 OCSP profile

### 7.3.1 Version number(s)

No stipulation.

### 7.3.2 OCSP extensions

No stipulation.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

The CA SHALL at all times:

1.	Issue Certificates and operate its PKI in accordance with all law applicable to its business and the Certificates it issues in every jurisdiction in which it operates;
2.	Comply with these Requirements;
3.	Comply with the audit requirements set forth in this section; and
4.	Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

## 8.1 Frequency or circumstances of assessment

Certificates that are capable of being used to issue new certificates MUST either be Technically Constrained in line with section 7.1.5 and audited in line with section 8.7 only, or Unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new certificates if it contains an X.509v3 basicConstraints extension, with the cA boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period MUST NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in Section 8.1, then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in
Section 8.1, then, before issuing Publicly-Trusted Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in Section 8.1. The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted Certificate.

## 8.2 Identity/qualifications of assessor

The CA’s audit SHALL be performed by a Qualified Auditor. A Qualified Auditor means a natural person, Legal Entity, or group of natural persons or Legal Entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit;
2. The ability to conduct an audit that addresses the criteria specified in an Eligible Audit Scheme (see Section 8.1);
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403;
5. (For audits conducted in accordance with the WebTrust standard) licensed by WebTrust;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors &

Omissions insurance with policy limits of at least one million US dollars in coverage.

## 8.3 Assessor's relationship to assessed entity

No stipulation.

## 8.4 Topics covered by assessment

The CA SHALL undergo an audit in accordance with one of the following schemes:

1. WebTrust for Certification Authorities v2.0;
2. A national scheme that audits conformance to ETSI TS 102 042/ ETSI EN 319 411-1;
3. A scheme that audits conformance to ISO 21188:2006; or
4. If a Government CA is required by its Certificate Policy to use a different internal audit scheme, it MAY use such scheme provided that the audit either (a) encompasses all requirements of one of the above schemes or (b) consists of comparable criteria that are available for public review.

Whichever scheme is chosen, it MUST incorporate periodic monitoring and/or accountability procedures to ensure that its audits continue to be conducted in accordance with the requirements of the scheme.

The audit MUST be conducted by a Qualified Auditor, as specified in Section 8.3.

If a Delegated Third Party is not currently audited in accordance with Section 8 and is not an Enterprise RA, then prior to certificate issuance the CA SHALL ensure that the domain control validation process required under Section 3.2.2.4 or IP address verification under 3.2.2.5 has been properly performed by the Delegated Third Party by either (1) using an out-of-band mechanism involving at least one human who is acting either on behalf of the CA or on behalf of the Delegated Third Party to confirm the authenticity of the certificate request or the information supporting the certificate request or (2) performing the domain control validation process itself.

If the CA is not using one of the above procedures and the Delegated Third Party is not an Enterprise RA, then the CA SHALL obtain an audit report, issued under the auditing standards that underlie the accepted audit schemes found in Section 8.1, that provides an opinion whether the Delegated Third Party’s performance complies with either the Delegated Third Party’s practice statement or the CA’s Certificate Policy and/or Certification Practice Statement. If the opinion is that the Delegated Third Party does not comply, then the CA SHALL not allow the Delegated Third Party to continue performing delegated functions.

The audit period for the Delegated Third Party SHALL NOT exceed one year (ideally aligned with the CA’s audit). However, if the CA or Delegated Third Party is under the operation, control, or supervision of a Government Entity and the audit scheme is completed over multiple years, then the annual audit MUST cover at least the core controls that are required to be audited annually by such scheme plus that portion of all non-core controls that are allowed to be conducted less frequently, but in no case may any non-core control be audited less often than once every three years.

## 8.5 Actions taken as a result of deficiency

No stipulation.

## 8.6 Communication of results

The Audit Report SHALL state explicitly that it covers the relevant systems and processes used in the issuance of all Certificates that assert one or more of the policy identifiers listed in Section 7.1.6.1. The CA SHALL make the Audit Report publicly available. The CA is not required to make publicly available any general audit findings that do not impact the overall audit opinion. For both government and commercial CAs, the CA SHOULD make its Audit Report publicly available no later than three months after the end of the audit period. In the event of a delay greater than three months, and if so requested by an Application Software Supplier, the CA SHALL provide an explanatory letter signed by the Qualified Auditor.

## 8.7 Self-Audits

During the period in which the CA issues Certificates, the CA SHALL monitor adherence to its Certificate Policy, Certification Practice Statement and these Requirements and strictly control its service quality by performing self audits on at least a quarterly basis against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by it during the period commencing immediately after the previous self-audit sample was taken. Except for Delegated Third Parties that undergo an annual audit that meets the criteria specified in Section 8.1, the CA SHALL strictly control the service quality of Certificates issued or containing information verified by a Delegated Third Party by having a Validation Specialist employed by the CA perform ongoing quarterly audits against a randomly selected sample of at least the greater of one certificate or three percent of the Certificates verified by the Delegated Third Party in the period beginning immediately after the last sample was taken. The CA SHALL review each Delegated Third Party’s practices and procedures to ensure that the Delegated Third Party is in compliance with these Requirements and the relevant Certificate Policy and/or Certification Practice Statement.

The CA SHALL internally audit each Delegated Third Party’s compliance with these Requirements on an annual basis.

During the period in which a Technically Constrained Subordinate CA issues Certificates, the CA which signed the Subordinate CA SHALL monitor adherence to the CA’s Certificate Policy and the Subordinate CA’s Certification Practice Statement. On at least a quarterly basis, against a randomly selected sample of the greater of one certificate or at least three percent of the Certificates issued by the Subordinate CA, during the period commencing immediately after the previous audit sample was taken, the CA shall ensure all applicable CP are met.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

No stipulation.

### 9.1.2 Certificate access fees

No stipulation.

### 9.1.3 Revocation or status information access fees

No stipulation.

### 9.1.4 Fees for other services

No stipulation.

### 9.1.5 Refund policy

No stipulation.

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

No stipulation.

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

No stipulation.

### 9.4.2 Information treated as private

No stipulation.

### 9.4.3 Information not deemed private

No stipulation.

### 9.4.4 Responsibility to protect private information

No stipulation.

### 9.4.5 Notice and consent to use private information

No stipulation.

### 9.4.6 Disclosure pursuant to judicial or administrative process

No stipulation.

### 9.4.7 Other information disclosure circumstances

No stipulation.

## 9.5 Intellectual property rights

No stipulation.

## 9.6 Representations and warranties

### 9.6.1 CA representations and warranties

By issuing a Certificate, the CA makes the certificate warranties listed herein to the following Certificate Beneficiaries:

* The Subscriber that is a party to the Subscriber or Terms of Use Agreement for the Certificate;
* All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root Certificate in software distributed by such Application Software Supplier; and
* All Relying Parties who reasonably rely on a Valid Certificate.

The CA represents and warrants to the Certificate Beneficiaries that, during the period when the Certificate is valid, the CA has complied with these Requirements and its Certificate Policy and/or Certification Practice Statement in issuing and managing the Certificate.

The Certificate Warranties specifically include, but are not limited to, the following:

1. Right to Use Domain Name or IP Address. That, at the time of issuance, the CA: (i) implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Domain Name(s) and IP address(es) listed in the Certificate’s subject field and subjectAltName extension (or, only in the case of Domain Names, was delegated such right or control by someone who had such right to use or control); (ii) followed the procedure when issuing the Certificate; and (iii) accurately described the procedure in this Certificate Policy and/or the corresponding Certification Practice Statement.

2. Authorization for Certificate. That, at the time of issuance, the CA: (i) implemented a procedure for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative is authorized to request the Certificate on behalf of the Subject; (ii) followed the procedure when issuing the Certificate; and (iii) accurately described the procedure in this Certificate Policy and/or the corresponding Certification Practice Statement.

3. Accuracy of Information. That, at the time of issuance, the CA: (i) implemented a procedure for verifying the accuracy of all of the information contained in the Certificate (with the exception of the subject:organizationalUnitName attribute); (ii) followed the procedure when issuing the Certificate; and (iii) accurately described the procedure in this Certificate Policy and/or the corresponding Certification Practice Statement.

4. No Misleading Information. That, at the time of issuance, the CA: (i) implemented a procedure for reducing the likelihood that the information contained in the Certificate’s subject:organizationalUnitName attribute would be misleading; (ii) followed the procedure when issuing the Certificate; and (iii) accurately described the procedure in this Certificate Policy and/or the corresponding Certification Practice Statement.

5. Identity of Applicant. That, if the Certificate contains Subject Identity Information, the CA: (i) implemented a procedure to verify the identity of the Applicant in accordance with Section 3.2; (ii) followed the procedure when issuing the Certificate; and (iii) accurately described the procedure in this Certificate Policy and/or the corresponding Certification Practice Statement.

6. Subscriber Agreement. That, if the CA and Subscriber are not Affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies the CA/B Forum Baseline Requirements, or, if the CA and Subscriber are Affiliated, the Applicant Representative acknowledged and accepted the Terms of Use.

7. Status. That the CA maintains a 24 x 7 publicly-accessible Repository with current information regarding the status (valid or revoked) of all unexpired Certificates; and

8. Revocation. That the CA will revoke the Certificate for any of the reasons specified in the CA/B Forum Baseline Requirements.

The Root CA SHALL be responsible for the performance and warranties of the Subordinate CA, for the Subordinate CA’s compliance with these Requirements, and for all liabilities and indemnification obligations of the Subordinate CA under these Requirements, as if the Root CA were the Subordinate CA issuing the Certificates.

By issuing a Certificate, the CA represents that it followed the procedure set forth this Policy and its Certification Practice Statement to verify that, as of the Certificate’s issuance date, all of the Subject Information was accurate.

By issuing a Subordinate CA Certificate, the CA represents that it followed the procedure set forth in this Policy and/or its Certification Practice Statement to verify that, as of the Subordinate CA Certificate’s issuance date, all of the Subject Information was accurate.

The CA represents that all Certificates containing a policy identifier indicating compliance with the CA/B Forum Baseline Requirements are issued and managed in accordance with the CA/B Forum Baseline Requirements.

Every Subordinate CA shall represent, in its Certificate Policy and/or Certification Practice Statement, that all Certificates containing a policy identifier indicating compliance with the CA/B Forum Baseline Requirements are issued and managed in accordance with the CA/B Forum Baseline Requirements.

### 9.6.2 RA representations and warranties

No stipulation.

### 9.6.3 Subscriber representations and warranties

The CA SHALL require, as part of the Subscriber or Terms of Use Agreement, that the Applicant make the commitments and warranties in this section for the benefit of the CA and the Certificate Beneficiaries.

Prior to the issuance of a Certificate, the CA SHALL obtain, for the express benefit of the CA and the Certificate Beneficiaries, either:

1. The Applicant’s agreement to the Subscriber Agreement with the CA, or

2. The Applicant’s agreement to the Terms of Use agreement.

The CA SHALL implement a process to ensure that each Subscriber or Terms of Use Agreement is legally enforceable against the Applicant. In either case, the Agreement MUST apply to the Certificate to be issued pursuant to the certificate request. The CA MAY use an electronic or "click-through" Agreement provided that the CA has determined that such agreements are legally enforceable. A separate Agreement MAY be used for each certificate request, or a single Agreement MAY be used to cover multiple future certificate requests and the resulting Certificates, so long as each Certificate that the CA issues to the Applicant is clearly covered by that Subscriber or Terms of Use Agreement.

The Subscriber or Terms of Use Agreement MUST contain provisions imposing on the Applicant itself (or made by the Applicant on behalf of its principal or agent under a subcontractor or hosting service relationship) the following obligations and warranties:

1. Accuracy of Information: An obligation and warranty to provide accurate and complete information at all times to the CA, both in the certificate request and as otherwise requested by the CA in connection with the issuance of the Certificate(s) to be supplied by the CA;

2. Protection of Private Key: An obligation and warranty by the Applicant to take all reasonable measures to maintain sole control of, keep confidential, and properly protect at all times the Private Key that corresponds to the Public Key to be included in the requested Certificate(s) (and any associated activation data or device, e.g. password or token);

3. Acceptance of Certificate: An obligation and warranty that the Subscriber will review and verify the Certificate contents for accuracy;

4. Use of Certificate: An obligation and warranty to install the Certificate only on servers that are accessible at the subjectAltName(s) listed in the Certificate, and to use the Certificate solely in compliance with all applicable laws and solely in accordance with the Subscriber or Terms of Use Agreement;

5. Reporting and Revocation: An obligation and warranty to promptly cease using a Certificate and its associated Private Key, and promptly request the CA to revoke the Certificate, in the event that: (a) any information in the Certificate is, or becomes, incorrect or inaccurate, or (b) there is any actual or suspected misuse or compromise of the Subscriber’s Private Key associated with the Public Key included in the Certificate;

6. Termination of Use of Certificate: An obligation and warranty to promptly cease all use of the Private Key corresponding to the Public Key included in the Certificate upon revocation of that Certificate for reasons of Key Compromise.

7. Responsiveness: An obligation to respond to the CA’s instructions concerning Key Compromise or Certificate misuse within a specified time period.

8. Acknowledgment and Acceptance: An acknowledgment and acceptance that the CA is entitled to revoke the certificate immediately if the Applicant were to violate the terms of the Subscriber or Terms of Use Agreement or if the CA discovers that the Certificate is being used to enable criminal activities such as phishing attacks, fraud, or the distribution of malware.

### 9.6.4 Relying party representations and warranties

No stipulation.

### 9.6.5 Representations and warranties of other participants

No stipulation.

## 9.7 Disclaimers of warranties

No stipulation.

## 9.8 Limitations of liability

For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and this Policy and/or corresponding Certification Practice Statement, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA’s Certificate Policy and/or Certification Practice Statement. If the CA has not issued or managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its Certificate Policy and/or Certification Practice Statement, then the CA SHALL include the limitations on liability in the CA’s Certificate Policy and/or Certification Practice Statement.

## 9.9 Indemnities

### 9.9.1 Indemnification by ISRG

Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have a Root Certificate distribution agreement in place with the Root CA do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier’s software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).

## 9.10 Term and termination

### 9.10.1 Term

No stipulation.

### 9.10.2 Termination

No stipulation.

### 9.10.3 Effect of termination and survival

No stipulation.

## 9.11 Individual notices and communications with participants

No stipulation.

## 9.12 Amendments

### 9.12.1 Procedure for amendment

No stipulation.

### 9.12.2 Notification mechanism and period

No stipulation.

### 9.12.3 Circumstances under which OID must be changed

No stipulation.

## 9.13 Dispute resolution provisions

No stipulation.

## 9.14 Governing law

No stipulation.

## 9.15 Compliance with applicable law

No stipulation.

## 9.16 Miscellaneous provisions

### 9.16.1 Entire agreement

No stipulation.

### 9.16.2 Assignment

No stipulation.

### 9.16.3 Severability

If a court or government body with jurisdiction over the activities covered by the CA/B Forum Baseline Requirements determines that the performance of any mandatory requirement is illegal, then such requirement is considered reformed to the minimum extent necessary to make the requirement valid and legal. This applies only to operations or certificate issuances that are subject to the laws of that jurisdiction. The parties involved SHALL notify the CA/Browser Forum of the facts, circumstances, and law(s) involved, so that the CA/Browser Forum may revise these Requirements accordingly.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

No stipulation.

### 9.16.5 Force Majeure

No stipulation.

## 9.17 Other provisions

No stipulation.
