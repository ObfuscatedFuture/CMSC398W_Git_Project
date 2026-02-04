# Role C Instructions

This role focuses on the square root operation feature and fixing error handling.

## Starting Point

Your starter branch: `starter/role-C`

This branch has 3 commits with various changes and some intentional problems to fix.

## Workflow

Make sure you have cloned your group's fork of this repository (not the original upstream repo).

1. Checkout your starter branch (`starter/role-C`).
2. Create your feature branch from it, named `feature/<your-id>` (replace `<your-id>` with your UMD Directory ID).
3. Push your branch to the remote fork:
   ```
   git push -u origin feature/<your-id>
   ```
4. Open a pull request on GitHub: `feature/<your-id>` → `main`

   See [GitHub's pull request documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) for instructions.

Push your branch regularly as you complete each checkpoint.

---

## What You'll Submit

At the end, submit:

1. A pull request (`feature/<your-id>` → `main`) with:
   - All completed checkpoint work
   - Clean commit history
   - Passing tests

2. A final deliverable: create `LEARNINGS-<your-id>.md` in the root of the repository with:
   - The Git commands you used for each checkpoint
   - 1-2 sentences per checkpoint describing what you learned
   - Commit this file to your feature branch

3. Code review participation:
   - Feedback on a teammate's PR
   - Responses to all comments on your own PR
   - At least one approval before merging

---

## Environment Setup

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate it

macOS/Linux:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest tests/
```

Some tests will fail. That is expected. You will fix them in Checkpoint 1.

---

## Checkpoint 1: Staging Is Not Committing

In this checkpoint, make two unrelated changes and commit them separately. The goal is to practice using the staging area to control exactly what goes into each commit.

Run the tests and look at the failures.

Task 1: Fix the failing tests (`src/calculator.py`)

Look at the test output and the `divide` function in `src/calculator.py`. Figure out what is missing and fix it.

Task 2: Add a docstring (`src/validator.py`)

Add a module-level docstring at the top of the file describing what the module does. Write it yourself.

### How to commit

Make these as two separate commits with intentionally poor commit messages. You will fix these in Checkpoint 6:

1. First commit: only the fix to `src/calculator.py`
   - Message: `"fix"`
2. Second commit: only the docstring addition
   - Message: `"update"`

Then push your branch:
```
git push origin feature/<your-id>
```

### Success check

Two new commits on your branch ("fix" and "update"), tests pass.

---

## Checkpoint 2: Undo Without Erasing History

Run `git log --oneline` to browse your history and find the commit with the message starting with `BAD:`.

That commit added excessive debug logging throughout the calculator module. It clutters output and does not belong in production.

Undo the effect of that commit without removing it from history.

### Hints

- Your new commit should clearly describe what it's doing

### Success check

The bad commit still exists in history, and a new commit undoes its changes.

---

## Checkpoint 3: Moving a Commit to the Right Branch

In this checkpoint, you will intentionally commit to the wrong branch and then use `git cherry-pick` to move it.

### Steps

1. Switch to `main` and add this function to `src/validator.py`:

   ```python
   def is_positive(n):
       """Check if a number is positive."""
       return n > 0
   ```

   Commit it with message: `"Add is_positive helper function"`

2. Move it to your feature branch:
   - Note the commit hash you just created
   - Reset `main` back to before that commit
   - Switch to `feature/<your-id>`
   - Use `git cherry-pick` with the commit hash to apply the commit
   - Switch back to `main` and confirm the commit is gone

### Handling conflicts

`git cherry-pick` may produce merge conflicts if both branches modified the same file. Conflict markers look like:

```
<<<<<<< HEAD
(your feature branch's version)
=======
(the cherry-picked commit's version)
>>>>>>> <commit-hash>
```

Edit the file to resolve the conflict, stage it, then run `git cherry-pick --continue`. For this checkpoint, keep both the `abs_value` function already on your feature branch and the new `is_positive` function.

### Success check

The commit exists on your feature branch but not on `main`, with all conflicts resolved.

---

## Checkpoint 4: Recovering Lost Work with Reflog

Simulate accidentally deleting a branch before merging it, then recover the lost commits using `git reflog`.

### Steps

1. Create a branch `experiment/<your-id>` from your current feature branch
2. Make at least one commit on it (for example, add a comment to any source file)
3. Switch back to your feature branch
4. Delete the experimental branch: `git branch -D experiment/<your-id>`
5. Use `git reflog` to find the lost commit
6. Create a branch `recovered/<your-id>` pointing to that commit
7. Merge `recovered/<your-id>` into your feature branch

### Success check

Your feature branch includes the recovered work via a merge from `recovered/<your-id>`.

---

## Checkpoint 5: Syncing with Upstream

Incorporate changes from the upstream repository's `main` branch into your feature branch.

### Steps

1. Add the original (upstream) repository as a remote named `upstream`:
   ```bash
   git remote add upstream <upstream-repo-url>
   ```

2. Fetch from upstream
3. Update your local `main` to match `upstream/main` (a fast-forward merge or reset works here)
4. Rebase your feature branch onto the updated `main`
5. Resolve any conflicts that come up
6. Force-push your branch:
   ```
   git push --force-with-lease origin feature/<your-id>
   ```

### Hints

- `git remote -v` shows all configured remotes
- You can have two remotes: `origin` (your fork) and `upstream` (the original repo)
- `--force-with-lease` is safer than `--force`. It aborts if someone else has pushed to the branch since you last fetched.

### Success check

Your feature branch is rebased onto the latest upstream `main`, with all conflicts resolved.

---

## Checkpoint 6: Interactive Rebase to Clean Up History

Your branch has accumulated several commits. Before submitting for review, organize and clean up the history.

### Steps

1. Count the commits on your branch since it diverged from `main`. Run `git log main..HEAD --oneline` to list them.
2. Run an interactive rebase: `git rebase -i HEAD~<number>` or `git rebase -i main`
3. In the editor:
   - `reword` (`r`): change a commit message
   - `squash` (`s`): combine with the previous commit
   - `edit` (`e`): pause to amend
   - Reorder lines to reorder commits
4. Save, follow the prompts, and edit messages as needed
5. Force-push: `git push --force-with-lease`

### What to fix

- Reword the "fix" and "update" commits from Checkpoint 1 to be descriptive
- Squash related commits where it makes sense
- The final history should tell a clear story of your work

### Success check

Feature branch has a clean, logical commit history with meaningful messages.

---

## Checkpoint 7: Code Review

1. Review one teammate's PR and leave at least one meaningful comment requesting a change
2. Respond to all comments on your own PR
3. Get at least one approval before merging

### Success check

You have reviewed a teammate's PR and received an approval on your own.

---

## Gradescope Submission

Submit both of the following on Gradescope:

1. Your `LEARNINGS-<your-id>.md` file, upload it directly
2. The URL of your pull request (`feature/<your-id>` to `main`)

---

## Grading

**Total: 100 points**

### LEARNINGS File — 60 points

Each checkpoint entry (CP1–CP6) is worth 10 points:

- **Commands (5 pts):** List the exact git commands you ran for that checkpoint, in order.
- **Reflection (5 pts):** 1–2 sentences explaining what you learned and why it matters.

### Code Review — 20 points

| | Points |
|---|---|
| Left at least one meaningful comment requesting a change on a teammate's PR | 7 |
| Responded to all comments on your own PR | 7 |
| PR approved and merged with passing tests | 6 |

### Group Integration — 20 points

Graded as a group based on the final state of `main`:

| | Points |
|---|---|
| All role branches merged into `main` | 5 |
| All tests pass on `main` | 10 |
| `main` has a clean commit history | 5 |

---

## Final Checklist

- [ ] Checkpoint 1: Two commits ("fix" and "update"), tests pass
- [ ] Checkpoint 2: Bad commit reverted (not erased)
- [ ] Checkpoint 3: `is_positive` cherry-picked to feature branch, conflicts resolved
- [ ] Checkpoint 4: Lost work recovered via reflog
- [ ] Checkpoint 5: Rebased onto latest upstream `main`
- [ ] Checkpoint 6: History cleaned up with interactive rebase
- [ ] Checkpoint 7: Code review done
- [ ] `LEARNINGS-<your-id>.md` committed to your feature branch
- [ ] Tests pass
