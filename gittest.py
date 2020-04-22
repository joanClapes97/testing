"""
We work locally here and we have a repository on our githb account.
Now, clone the repository on the same directory as here, /Joan.
We work on this file/project, but also New_employee works on that from another
folder which can be in any computer. Let's do it (we are Joan)
Use Git Bash on Windows
Once cloned, put our files inside the repository we cloned.

# NOTE: the repository contains a hided directory, .git, which allows
us to communicate with it
"""

"""
Enter the repo, see (master) at the beggining of the command line. Now, since we
have added files in there, do git status first to see how we are doing.
Then, do git add gittest.py , then git commit -m "first commit" , and
finally do git push to communicate with GitHub the changes we have made.
"""

"""
Now, the new employee will then for example clone the repo and he will have
what Joan pushed. Then, both employees are working locally, but can communicate
with GitHub, with the repository which is saved locally somewhere.
"""

"""
Now, if Joan makes another commit and pushes it, then New employee has to
do git pull.
"""

"""
git branch
git branch name_branch
git checkout name_branch
"""

def summ(a, b):
    return a+b
