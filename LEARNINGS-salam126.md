**Commands (5 pts):** List the exact git commands you ran for that checkpoint, in order.
**Reflection (5 pts):** 1–2 sentences explaining what you learned and why it matters.

Checkpoint 1
git add src/calculator.py
git status
git commit -m "fix"
git add src/validator.py
git commit -m "update"
git push origin feature/salam126

For this checkpoint I used add, commit, and push in order to push my changes and their commit messages
I learned that it is possible to make changes to different documents, save those changes to separate commits, and then push them together which is really useful when you are working on different tasks at once.

Checkpoint 2
git log --oneline
git revert 4dc20fb
git push

For this checkpoint, I undid a past commit but kept it visible in the history.
I learned that bad commits are not permanent, and that the effects of them can be undone without deleting them entirely from my list of commits. This is really useful because we are often going back and forth a lot when programming so it helps to be able to keep track of past commits that may not be currently applied.

Checkpoint 3
git checkout main
git add src/validator.py
git commit -m "Add is_positive helper function"
git log --oneline
git reset --head HEAD~1
git checkout feature/salam126
git cherry-pick 51b9b1f
git add src/validator.py
git cherry-pick --continue
git push

In this checkpoint I made a commit to the wrong branch and then moved it to the right one.
I learned that by using git cherry-pick I can move a commit to a different branch which is really cool since again, as programmers we may be working on multiple differnt things at once. Being able to move commits to different branches help with organizing our repositories as it suits our needs.

Checkpoint 4
git checkout -b experiment/salam126
git add .
git commit -m "Add experimental comment"
git checkout feature/salam126
git branch -D experiment/salam126
git reflog
git checkout -b recovered/salam126 a33c169
git checkout feature/salam126
git merge recovered/salam126
git push

In this checkpoint I made a branch, committed on it, deleted the branch, and then recovered the lost commit and recreated a branch that points to it.
I learned that you can use git reflog to recover lost commits event after a branch is delted. This is helpful since it showed me that git keeps a history of actions that I can use to restore previously made work.

Checkpoint 5
git remote -v
git remote add upstream https://github.com/mdurrani808/git_project_1.git
git fetch upstream
git checkout main
git reset --hard upstream/main
git checkout feature/salam126
git rebase main
git push --force-with-lease origin feature/salam126

In this checkpoint I synced my forked repo with the original upstream repo.
I leaned how rebasing works and how to safely force-push changes after rewriting the history.

Checkpoint 6
git log main.HEAD --oneline
git rebase -i main
git log --oneline
git push --force_with-lease

In this checkpoint I cleaned up the commit history using rebase.
I learned that you can change and delete commit messages with reword and squash. This is especially helpful when you are working with other people so that they can understand what you are doing at each commit better.