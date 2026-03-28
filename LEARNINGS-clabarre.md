Checkpoint 1:
git commit tests\test_calculator.py -m 'fix' 
git commit .gitignore -m 'update'
git branch feature/clabarre
git push origin feature/clabarre

Reflection: I learned how to commit files with commit messages and navigate different 
branches in a project. This is fundamental for using git.

Checkpoint 2:
git checkout feature/clabarre
git log --oneline
git revert 6ca467b
git push origin feature/clabarre

Reflection: I learned to use git log to find specific commits and revert them. 
This is important because I know how to undo any mistakes I may introduce while coding.

Checkpoint 3:
git checkout main
git add src\validator.py
git commit -m 'Add is_positive helper function'
git log --oneline

git checkout feature/clabarre
git cherry-pick 3060e71
git add src\validator.py
git commit -m 'Add is_postive helper function'

git checkout main
git revert 3060e71

Reflection: This checkpoint taught me how to manage commits between branches and use 
the cherry-pick command. I also learned to resolve merge conflicts which is important 
when commits interact with the same file.

Checkpoint 4:
git branch -c experiment/clabarre
git add src\calculator.py
git commit -m "random commit"

git checkout feature/clabarre
git branch -D experiment/clabarre
git reflog
git branch -c recovered/clabarre
git checkout recovered/clabarre
git checkout feature/clabarre
git branch -f recovered/clabarre 726259c
git merge recovered/clabarre
git add src\calculator.py
git commit -m 'succesful recovery'

Reflection: This taught me how to navigate reflog to find 'lost' history and recover changes.
This is especially important if a mistake is made and needs to corrected. I also learned how 
to use the merge command and more branch manipulation.

Checkpoint 5:
git checkout main
git reset --hard upstream/main
git checkout feature/clabarre
git log main..HEAD --oneline
git rebase -i main
git add src\calculator.py
git rebase --continue
git push --force-with-lease

Reflection: 
I learned how to cleanup commit history before committing making my commit history less cluttered
and allowing others to easily understand the work I completed. This is especially important when 
working on a project with others who need to review your work.
