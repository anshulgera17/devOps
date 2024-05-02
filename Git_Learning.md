# Git commands use, learning data and questions for interview


## GIT FUNDAMENTALS

-  Who invented Git and why? 
-  What is a Git repository?
-  What are the different states a file can be in according to the "git status" command?
-  How would you compare Git to a traditional version control tool like CVS?
-  What is the purpose of Git GUI?
-  Are there any types of files you can't commit to Git?
-  What does a Git repository typically contain?
-  How can you tell if a folder contains a Git repository?
-  Is there a difference between a local and a remote Git repo?
-  What is unique about a bare repo?
-  How do you create or initialize a bare repository?
-  What is a clone in Git? How do you clone a remote repo?
-  What is a fork? Is a fork part of Git?
-  Name three popular Git GUI tools.

## COMMON GIT COMMANDS

-  Name some git commit message best practcies.
-  Why must you add files to the Git Index?
-  What does the "git log" command do?
-  What does the "git reflog" command do?
-  What does it mean to 'git log a dog?'
-  What common switches are used with the commit command?
-  How would you explain the Git index to a 5 year old?
-  How do you undo the previous commit?
-  What does "git commit -a" do?
-  Can "git commit -a" be used with new files?
-  What two properties must be set in your config before a commit can take place?
-  Name four Git config scopes.
-  Explain the commit workflow in Git.
-  Where is Git configuration stored?
-  Does Git support pull requests?
-  Can you revert a single file from a commit?
-  What's the difference between revert and reset?
-  How do you find a listing of files that were included in a commit?
-  What does it mean to squash a commit?
-  When would you issue a "git pull"?
-  What does origin typically refer to?
-  What impact does a fetch have on your local worktree?
-  What happens to files in the index during a soft reset?
-  What happens to files in the index during a hard reset?
-  What happens to files in the working tree during a mixed reset?
-  When would you use pull vs fetch?
-  Why might a git pull be rejected?

## GIT BRANCHING

-  What is a branch in Git?
-  What is a 'topic branch?'
-  How do Git branches support isolated development?
-  What is special about the master branch?
-  Can you delete the master branch?
-  Does Git support branch protection?
-  What does HEAD represent in Git?
-  What is a detached HEAD?
-  How do you clone a specific branch?
-  How do you clone a specific commit?
-  How do you fix a detached HEAD?
-  Why has the master branch been renamed to main?
-  How do you delete a Git branch?
-  Is it possible to recover a deleted branch?
-  How do you create a new Git branch?
-  Can the tip of two branches share the same commit id?
-  What are "remote tracking branches" in Git?
-  When do you use a "git cherry-pick"?
-  Can you "git cherry-pick" a commit from the same branch?
-  What's the relationship between a revert and a cherry-pick?

## MERGE STRATEGIES & CONFLICTS

-  When should a developer merge code?
-  Can you merge code within the same branch?
-  What would trigger a merge conflict?
-  Explain to me how you go about resolving a merge conflict.
-  Explain to me what an octopus merge strategy does as if I was a 5 year old.
-  What happens to files that are problematic during a mere conflict.
-  Explain to me what a recursive merge strategy does like I was a Python developer.
-  How do you abort a commit when there is a merge conflict.
-  Explain the 'ours merge strategy' to me.
-  How do you permanentaly resolve a merge conflict?
-  Compare and contrast a merge vs a rebase.
-  What are different merge strategies?
-  What is a fast forward merge? 
-  How do you turn fast-forward merging off?
-  Explain resolve merge strategy to me like I was a Python developer.
-  Explain the subtree merge strategy to me like I was a Python developer.

## TAGS

-  What is a Git tag and when should you use one?
-  What does "git tag" do to your commit history?
-  Can you reset to a Git tag?

## SWITCHES & HOOKS

-  What does the "git checkout" command do?
-  What does the "git switch" command do?
-  Which should you use, checkout or switch?
-  What is a Git hook?
-  What type of event can trigger a Git hook?

## ADVANCED GIT 

-  When would you use the 'git diff' command?
-  What happens when a file already added to the repo is added to the .gitignore file?
-  Compare and contrast a fast forward merge with a recursive merge
-  Name two key benefits Git's branch model provides developers.
-  What does 'git log a dog' mean?
-  What is the effect a Git merge has on the commit history when compared to a Git rebase?
-  Why is a rebase safer than a forced push?
-  What's the difference between a revert and reset?
-  When would you use Git's "blame" command?
-  When would you use a Git submodule?
-  When would clone a Git repo, are all of the submodules clones as well?
-  What happens when you ammend a commit?
-  What's the difference between "git clone" and "git pull?"
-  What's the difference between HEAD and a commit id?
-  What is the difference between git log and reflog?
-  What does the Git clean command do?
-  How would you remove all untracked files in Git?
-  When would you use the "git bisect" command?

## GIT STASH

-  When would you use the Git Stash command?
-  How do you create a Git stash?
-  What files are affected by the Git stash command?
-  When would you use the "git stash apply" command?
-  What's the difference between "git stash pop" and "git stash apply?"
-  When would you drop a Git stash?
-  What does "git stash list" do?
-  Can you pop a Git stash by its name?

## GIT & GITHUB

-  What's the difference between Git and GitHub?
-  Who owns GitHub?
-  Name three features GitHub provides that Git does not.
-  How do you push an existing project to GitHub?
-  How do you clone a GitHub repo over HTTP?
-  What is a GitHub access token and how do you create one?
-  How do you push a new local branch to an existing GitHub repo?
-  What is required to authenticate to GitHub with SSH?
-  What's the difference between GitHub and GitLab?
-  Why might a company choose BitBucket over GitHub?
-  How can you view the commit history of a specific file in GitHub?
-  What's the difference between a fork and a clone?

## GIT WORKFLOWS

-  What are the benefits of using a branch strategy like GitFlow?
-  Briefly explain how GitFlow works?
-  Why would a team use GitHub Flow?
-  What's the difference between GitHub Flow and GitLab Flow?
-  What two branches are never deleted in GitFlow?

## Git Configuration in ec2 instance

```
Create a repo folder 
$ Mkdir repo 
$ cd repo
$ git init --bare
```

## Git-hub

- Username : anshulgera17
- Email: anshulgera17@gmail.com
- .gitconfig file having details in ubuntu 

## files in .git folder
- COMMIT_EDITMSG
- HEAD
- config
- description
- index

## folders in .git 
- hooks
- info
- logs
- objects
- refs

## Configure git in terminal

- `git config --global user.name “anshulgera17”`
- `git config --global user.email anshulgera17@gmail.com`
- `git clone (url)`

- Create file and folders inside /C/git/ `git add filename`
- Checking status `git status`
- `git commit -m “comments” filename`
- `git push -u origin master`

- `git archive --format=zip master^ README >file.zip`
- `git diff`
- `git pull`
- Change to last commit state `git reset --hard HEAD`
- `git tag -a v1.0 -m 'this is version 1.0 tag'`

- `git config -l` ask for username and emailid
- Check the git config using `/etc/gitconfig` file

- Unstage the git file using `git reset HEAD fileName`
- `git log` for showing the logs after commit
- `git rm fileName` for delete a file
- `git checkout -- fileName` If you delete file using rm command then you can recover using command 
- If we want to ignore files and don’t wanna add those in git but present in that folder then we can add that file name in `.gitignore` file or any particular extension like `.jpg` files. Or you can ignore whole folder
- `git clone existingFolder NewFolder` for crating clone of the folder and then you can work in that folder
- `git config -` shows more detailed configuration
- `git log --oneline` shows better for comments and changes in logs
- `git log -p` for more information use
- `git branch branchName` create a branch in git
- we can modify in the new folder and create new files in that folder new branch
- Then run `git checkout master` means we switched back to master branch.

- `git commit -a -m “comment ”  -a` is used if we want to commit untracked file (means we didn’t run `git add` command and did the changes in file)

- `git config --list` 
- `git merge develop-branch`
- `git checkout develop` go to develop branch
- `git diff`
- `git diff HEAD` 
- `git diff --staged HEAD` check staged code and compare
- `git diff commit_ID1 commit_ID2` compare between commits
- `git diff HEAD HEAD^` compare with last commit
- `git branch -m mybranch develop` 
- `git branch -d develop` delete branch develop
- `git reset HEAD~` revert back file
- `git reset HEAD sample.txt` revert back file from staging
- `git log --since="2 days ago"` logs based on time
- `git log --oneline --graph --decorate` oneline logs
- `git checkout --filename.txt` if file deleted then revert back
- `git config --global alias.history "log --all --graph --decorate --oneline"`


## Git Commands

- `git config`
- `git config –global user.name “[name]”`  
- `git config –global user.email “[email address]”`
- `git init`
- `git init [repository name]`
- `git clone`, `git clone [url]`
- `git add`, `git add [file]`
- `git commit`, `git commit -m “[ Type in the commit message]”`
- `git diff` , `git diff –staged`, `git diff [first branch] [second branch]`
- `git reset`, `git reset [file]`, `git reset [commit]`, `git reset –hard [commit]`
- `git status`
- `git rm`, `git rm [file]`
- `git log`, `git log –follow[file]`
- `git show`, `git show [commit]`
- `git tag`, `git tag [commitID]`
- `git branch`, `git branch [branch name]`, `git branch -d [branch name]`
- `git checkout`, `git checkout [branch name]`, `git checkout -b [branch name]`
- `git merge`, `git merge [branch name]`
- `git remote`, `git remote add [variable name] [Remote Server Link]`
- `git push`, `git push [variable name] master`, `git push [variable name] [branch]`, `git push –all [variable name]`, `git push [variable name] :[branch name]`
- `git pull`, `git pull [Repository Link]`
- `git stash`, `git stash save`, `git stash pop`, `git stash list`, `git stash drop`
