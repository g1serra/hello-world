> $ git push origin main
> <br>
> To https://github.com/g1serra/hello-world.git
> <br>
>  ! [rejected] main -> main (non-fast-forward)
>  <br>
> error: failed to push some refs to 'https://github.com/g1serra/hello-world.git'
> <br>
> hint: Updates were rejected because the tip of your current branch is behind
> <br>
> hint: its remote counterpart. Integrate the remote changes
> <br>
> hint: 'git pull ...') before pushing again.
> <br>
> hint: See the 'Note about fast-forwards' in 'git push --help' for details.
<br>
It appears that you have conflicts in your local branch that need to be resolved before pull, stash apply, or push.
<br>
**To resolve the conflicts, you can follow these steps:**
<br>
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
