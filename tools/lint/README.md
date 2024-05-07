# CP/CPS Linter

This tool performs a variety of simple checks on the CP/CPS to ensure that it
is in compliance with the Baseline Requirements. It is superficial: a clean
lint check is a necessary but not sufficient condition for full compliance.

Usage:

```sh
$ go run . /path/to/cps.md
heading "### 3.1.3 Anonymity or pseudonymity of subscribers" found out-of-order on line 199
heading "### 4.4.2 Publication of the certificate by the CA" not found
empty section found at line 71
empty section found at line 272
exit status 1
```

This tool is used by GitHub Actions to check every PR against this repo.

## Checks

The linter looks for compliance with Ballot SC-074, which added the following
text to the Baseline Requirements, Section 2.2:

> the Certificate Policy and/or Certification Practice Statement MUST be structured in accordance with section 6 of RFC 3647 and MUST:
>
> * include at least every section and subsection defined in section 6 of RFC 3647;
> * only use the words "No Stipulation" to mean that the particular document imposes no requirements related to that section; and
> * contain no sections that are blank and have no subsections.

### RFC 3647 Outline

A significant portion of this linter's work is confirming that the structure of
the CP/CPS matches the outline laid out in [RFC 3647, Section
6](https://datatracker.ietf.org/doc/html/rfc3647#section-6). This outline is
reproduced in [outline.txt](outline.txt), which was produced using the following
procedure:

1. Copy-paste the whole of Section 6 into a plaintext document.
2. Remove the leading text, and the page headers and footers.
3. Unwrap all section titles which were broken onto multiple lines.
4. Replace all sequences of more than one space (`  `) with a single space.
5. Remove the `(11)` footnote indicator which follows some entries.
6. Prepend each line with a number of `#` equal to its section depth.

The lint tool then ensures that every line in this file appears in the CP/CPS,
exactly as written, in order.

## No Empty Sections

The linter also looks for any places where two section header lines separated
only by whitespace have the same or decreasing section depth (e.g. "1.2.3"
followed by "1.3"), indicating that the first of the two sections has no
content.

## Use of "No Stipulation"

This linter does **not** check whether the phrase "No Stipulation" has been used
to mean anything other than that "that the particular document imposes no
requirements related to that section", since doing so is a semantic (not
syntactic) matter.
