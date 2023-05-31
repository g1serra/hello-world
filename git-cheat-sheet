If you want to push commits to your own repository after cloning another repository, you'll need to update the remote URL of the Git repository to point to your own repository. Here's what you can do:

1. Navigate to the cloned repository's directory:
   ```bash
   cd repo1
   ```

2. Check the current remote URL of the repository:
   ```bash
   git remote -v
   ```

   This command will show you the current remote URL, which should be something like:
   ```
   origin    https://github.com/g1serra/repo1.git (fetch)
   origin    https://github.com/g1serra/repo1.git (push)
   ```

3. Change the remote URL to your own repository:
   ```bash
   git remote set-url origin https://github.com/your-username/repo2.git
   ```

   Replace `your-username` with your GitHub username, and `repo2` with the name of your own repository.

4. Verify the new remote URL:
   ```bash
   git remote -v
   ```

   The output should now show your own repository's URL as the remote URL.

5. Push your commits to the new repository:
   ```bash
   git push origin master
   ```

   This command pushes the commits from the local `master` branch to the remote repository.

Now, your commits will be pushed to your own repository (`https://github.com/your-username/repo2.git`) instead of the original repository (`https://github.com/g1serra/repo1.git`).
