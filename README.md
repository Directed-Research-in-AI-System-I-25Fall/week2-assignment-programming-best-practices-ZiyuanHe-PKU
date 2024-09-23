aloha
## What I have learned:  
1. **Git Commands**:
   - `git clone`: Cloning a repository from GitHub.
   - `git checkout`: Switching branches.
   - `git branch`: Creating and managing branches.
   - `git commit`: Committing changes with messages.
   - `git push`: Pushing local changes to the remote repository. 
   - `git pull`: Pulling from the remote repository. 
   - `git log`: Viewing commit history. 

2. **Hugging Face**:
   - Loaded a pretrained ResNet model for inference.
3. **Others**
    - When in Step 8.**Pull for fun branch into the main branch, and resolve the conflict**  
      At first, I committed the inferenceMNIST.py in **main**, then I tried to merge **for_fun**(local branch) to the main branch, but the CLI read "Already up to date."  
        This is because A fast-forward merge occurs when the commits in the **for_fun** branch are a direct descendant of the **main** branch. When executing git pull, there will be no conflicts, and Git will simply move the **main** branch pointer to the latest commit of **for_fun**.   
      So in the end I tried to write the inferenceMNIST.py in **for_fun** branch and they merged correctly
