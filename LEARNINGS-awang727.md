### Role B (awang727)

## Checkpoint 1:
- git push origin feature/awang727
Learned how to write a comit message and push new code to feature branch.

## Checkpoint 2:
- git log --oneline | grep "BAD:"
- git push origin feature/awang727
Learned how to view the history of previous commits and changes. Can use a pipe with grep to find where the "BAD" commit was to look into the changes.

## Checkpoint 3:
- git push main
- git reset --hard f1deb1637b9abdb08ab38e208576e53deb497e44
- git cherry-pick
Learned to use git reset --hard to set a commit hash as a head and remove commit changes ahead of the head
and then cherry-pick to add commit changes from a hash to another branch. Useful if accidentally create commits
in the main branch but want to maintain the changes in another.

## Checkpoint 4:
- git checkout -b experiment/awang727
- git branch -D experiment/awang727
- git reflog
- git checkout -b recovered/awang727 7712b9e
- git merge recovered/awang727
Learned that you can create branches using another branch and delete branches as well. Then, using reflog, we can find the commit hash of a deleted branch and recover it and merge the recovered branch with the original.


## Checkpoint 5:
- git remote add upstream https://github.com/mdurrani808/git_project_1
- git fetch upstream
- git merge --ff-only upstream/main
- git rebase main
- git push --force-with-lease origin feature/awang727 
Learned how what rebasing a branch does and upstream compared to origin. 

## Checkpoint 6:
- git log main..HEAD --oneline
- git rebase -i main
- git push --force origin feature/awang727
Learned how to rewrite and edit commit history and squash commits to make readability better.