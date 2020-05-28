# This document contains some guidelines for editing ISRG CP and CPS documents.

## CP

Our CP is a copy of the Baseline Requirements (BRs) with the following changes:

1. Change anything that is obviously necessary, including much of the content in Sections 1.1 and 1.2.

2. Stucture should follow the structure suggested in RFC 3647 Section 6. Casing of section labels should match RFC 3647 casing. Where there is a difference between the BR structure and RFC 3647 suggested structures, use RFC 3647.

Note that any RFC 3647 section is allowed to contain sub-sections that are not defined in RFC 3647, so additional sub-sections in the BRs should be copied.

An example of a conflict between RFC 3647 and the BR structure is the title of Section 3.2.2. The BRs call it "Authentication of Organization and Domain Identity" but RFC 3647 calls it "Authentication of organization identity". We must use the RFC 3647 section name.

3. Section names for any validation methods we don't use under Sections 3.2.2.4 and 3.2.2.5 should be [Reserved] with "No stipulation." as the content. We do not include information for validation methods we don't use so as to not introduce confusion.

4. No sections can be left blank. If there is a blank section in the BRs say "No stipulation." to indicate that our CP will not impose additional requirements.

5. Section 9, legal, is designed and reviewed by ISRG attorneys.

## CPS

The CPS should have the same structure at the CP, but contain more detailed information.

Section 9, legal, is designed and reviewed by ISRG attorneys.
