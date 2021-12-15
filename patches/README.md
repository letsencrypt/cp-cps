The latest version of the BRs can be found at <https://github.com/cabforum/servercert/blob/main/docs/BR.md>.

To generate a new ISRG CP from the BRs and this patch, follow these instructions. All commands assume that you have both this repository and the servercert repository checked out side-by-side.

1. Manually edit the first "hunk" of this patch:
   a. Update the removed lines to match the new version of the base document: correct version number, date, and new entries in the Revisions section; and
   b. Update the added lines to include one for our own new revision of the CP.

2. Apply this patch against the latest version of the BRs, for example:
   ```sh
   $ rm cp-cps/CP.md
   $ patch servercert/docs/BR.md cp-cps/patches/isrg-cp-from-brs.patch -o cp-cps/CP.md`
   ```

3. Regenerate the patch file to prevent drift in the hunk offsets:
   ```sh
   $ rm cp-cps/patches/isrg-cp-from-brs.patch
   $ git diff servercert/docs/BR.md cp-cps/CP.md > cp-cps/patches/isrg-cp-from-brs.patch
   ```

4. Run the no-stipulation tool against the patched BRs to add required text to empty leaf sections:
   ```sh
   $ ./cp-cps/tools/no-stipulations/no_stipulation.py -d cp-cps/CP.md -o cp-cps/CP.md.stips
   $ mv cp-cps/CP.md.stips cp-cps/CP.md
   ```
5. Review the updated CP and patchfile to make sure the changes are correct and appropriate. Make sure to look for added language that is self-referential to the BRs, such as "these Baseline Requirements." That would need to be changed, whereas something like "these Requirements" is fine because "Requirements" has been re-defined to refer to our CP. If any changes are necessary, make sure that they are reflected in the patchfile so that they don't get lost the next time this process is followed.
