# B-017: ISJAVA wrongly documented as "NOT in DDF"
**Status:** FIXED (Pass 362, 2026-06-26)
**Date:** 2026-06-26
**Keywords:** ISJAVA, DDF, FIELD.DDF, parse_ddf.py, IS_JAVA_PARAM, brackets, field name parsing, tier1-tables.md

## Symptom
Multiple passes (Pass 293/297/345/348) stated ISJAVA was "TAS runtime-only, not registered in Pervasive schema." tier1-tables.md had a bold warning "Virtual table — NOT registered in Pervasive/Btrieve DDF."

## Root Cause
parse_ddf.py's `parse_field_ddf` function rejects field names containing brackets (`[`, `]`). ISJAVA's PARAM field is stored in DDF as 25 sub-fields named `IS_JAVA_PARAM[  1]` through `IS_JAVA_PARAM[ 25]`. The parser filtered all 25 out, leaving only IS_JAVA_UID and IS_JAVA_DATE. Since only 2 of 3 known TAS vars were found, and prior assumptions concluded "not in DDF," the error persisted across 6 passes.

## Attempts
**Fix (worked):** Raw binary scan of FIELD.DDF for target field IDs 17588–17612 confirmed all 25 IS_JAVA_PARAM sub-fields exist in DDF with file_id=437. ISJAVA.B file header confirms 2054-byte record size (40+2000+4+overhead). Corrected in tier1-tables.md and EVO-DECOMPILE-TODO.md.

## Resolution / Lesson
When the DDF parser finds fewer fields than TAS named_vars suggest, always do a raw binary scan — the parser's character filter can silently drop valid fields with non-standard name characters.
