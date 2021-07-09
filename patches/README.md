To generate a new ISRG CP from a patch, follow these instructions:

1. Apply a patch in this directory against a markdown copy of the BRs. Current BR markdown can be found here, for example:

https://github.com/cabforum/servercert/blob/main/docs/BR.md

2. Run the no-stipulation tool against the patched BRs to add required text to empty leaf sections:

https://github.com/letsencrypt/cp-cps/blob/master/tools/no-stipulations/no_stipulation.py

3. Review the updated CP to make sure the changes are correct and appropriate. Make sure to look for added language that is self-referential to the BRs, such as "these Baseline Requirements." That would need to be changed, whereas something like "these Requirements" is fine because "Requirements" has been re-defined to refer to our CP.
