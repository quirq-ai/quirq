# Checker tests

## Owner

sharmasuraj0123

## Worker

organize-quirq-repo/checker-tests

## Status

Done

## Input

Add automated tests for the structure checker in quirq-ai/quirq, so that changes to the rules can't silently break it. Put a standard-library `unittest` file at `.github/scripts/test_check_structure.py` that builds small throwaway repositories in a temporary directory (the checker reads `git ls-files`, so initialize git there) and checks that a valid layout passes and that a few known mistakes fail: a sub-channel README without `## Owner`, an output format outside Slides, One pager, Website, or GitHub URL, a `## Status` other than Open or Done, and a content file name that isn't kebab-case. Run the tests in `.github/workflows/structure.yml` next to the checker. Don't change the checker's rules. `python3 .github/scripts/check_structure.py` must still pass. Open one pull request against main.

## Output format

GitHub URL
