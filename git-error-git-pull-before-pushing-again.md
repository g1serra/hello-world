> $ git push origin main
> To https://github.com/g1serra/hello-world.git
>  ! [rejected]        main -> main (non-fast-forward)
> error: failed to push some refs to 'https://github.com/g1serra/hello-world.git'
> hint: Updates were rejected because the tip of your current branch is behind
> hint: its remote counterpart. Integrate the remote changes (e.g.
> hint: 'git pull ...') before pushing again.
> hint: See the 'Note about fast-forwards' in 'git push --help' for details.
<br>
It appears that you have conflicts in your local branch that need to be resolved before pull, stash apply, or push.
<br>
To resolve the conflicts, you can follow these steps:
<br>
```
git commit -m "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
```
```
git pull origin main
```
```
git push -u origin main
```