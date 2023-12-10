# Git commands use, learning data and questions for interview

- Q1. What is SCM ?
- Q2. What is difference between git and svn ?
- Q3. What is Git ?
- Q4. What is the command to write a commit message in Git ?
- Q5. What is bare repository in Git ?
- Q6. What language used in Git ?
- Q7. In Git how do you revert the commit that has already been pushed and made public ?
- Q8. What is the difference between git pull and git fetch ?
- Q9. What is ‘staging area’ 

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
