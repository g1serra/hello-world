If you want to push commits to your own repository after cloning another repository, you'll need to update the remote URL of the Git repository to point to your own repository. Here's what you can do:

Navigate to the cloned repository's directory:
```
cd repo1
```
Check the current remote URL of the repository:
```
git remote -v
```
This command will show you the current remote URL, which should be something like:
```
origin    https://github.com/g1serra/repo1.git (fetch)
origin    https://github.com/g1serra/repo1.git (push)
```
Change the remote URL to your own repository:
```
git remote set-url origin https://github.com/your-username/new-repo2.git
```
Replace `your-username` with your GitHub username, and `new-repo2` with the name of your own repository.
<br>
Verify the new remote URL:
```
git remote -v
```
The output should now show your own repository's URL as the remote URL.
```
origin    https://github.com/g1serra/new-repo2.git (fetch)
origin    https://github.com/g1serra/new-repo2.git (push)
```
```
git branch -M main
```
```
git status
```
```
git add .
```
```
git commit -m "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
```
Here's the Bash version of the Git commit command with the current date and time as the commit message:
```
git commit -m "$(date +'%Y-%m-%d %H:%M:%S')"
```
Push your commits to the new repository:
```
git push origin main
```
This command pushes the commits from the local `main` branch to the remote repository.

Now, your commits will be pushed to your own repository (`https://github.com/your-username/new-repo2.git`) instead of the original repository (`https://github.com/g1serra/repo1.git`).
