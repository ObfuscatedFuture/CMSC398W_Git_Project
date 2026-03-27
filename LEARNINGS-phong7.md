The Git commands you used for each checkpoint
1-2 sentences per checkpoint describing what you learned

Checkpoint 1
git add tests/test_calculator.py
git commit -m "fix"
git add src/calculator.py
git commit -m "update"
git push origin feature/phong7

For this checkpoint I utilized git add, commit, and push to upload the poor commit messages.
I learned that you can make multiple commits and then push all of them at once to GitHub
which is important when working on a project with multiple people.

Checkpoint 2
git log --oneline
git revert 66f6716

For this checkpoint I utilized git log --oneline and git revert to view the commit history and revert the commit that was bad.
I learned that you can revert a commit and it will create a new commit that undoes the changes of that commit without removing it from history which is important when working with multiple
people since you don't want to edit the history of a project.

Checkpoint 3
git switch main
git add src/validator.py 
git commit -m "Add is_positive helper function"
git log
git reset --soft HEAD~1
git cherry-pick ef7e407
git cherry-pick --continue

For this checkpoint I utilized git switch, add, commit, log, reset --soft HEAD~1, and cherry-pick.
I learned that you can pick a commit from one branch and apply it to another branch even
when that commit is no longer on that original branch which is important if you want to
move a commit from one branch to another.


Checkpoint 4
git switch -c experiment/phong7
git add src/validator.py
git commit -m "checkpoint 4 comment"
git switch feature/phong7git branch
git branch -D experiment/phong7
git reflog
git switch -c recovered/phong7 ca8f9f1
git switch feature/phong7
git merge recovered/phong7

For this checkpoint I utilized git switch, add, commit, branch, reflog, and merge.
I learned that you can use git reflog to view the commit history and then merge a commit
from a deleted branch into a current branch which is important if you want to take a
commit from a deleted branch.

Checkpoint 5
git remote add upstream https://github.com/mdurrani808/git_project_1
git fetch
git switch main
git fetch upstream
git merge upstream/main
git switch feature/phong7
git rebase main
git push --force-with-lease origin feature/phong7

For this checkpoint I utilize git remote, fetch, merge, rebase, and push.
I learned that you can use git rebase to make the current branch point to the tip of another
branch which is important if you want the parent pointer to be the same as the branch you are rebasing from. Additionally, I learned that you can use force push a change.

Checkpoint 6
git log main..HEAD --oneline
git rebase -i main
git push --force-with-lease

For this checkpoint I utilize git rebase, log, and push.
I learned that you can use git rebase to squash and reword commits easily which is important
if you want to make the commit history cleaner.