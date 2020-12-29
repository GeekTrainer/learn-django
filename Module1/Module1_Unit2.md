[1]: https://git-scm.com/downloads "Git website downloads"
[2]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Clone GutHub repository"

For this module in the learning path we will be going through the steps to install the Django framework, creating a Django project, and then finish by creating a **"Hello, world!"** app. We have provided both the starting files, and the solution files for the project in GitHub. This module does cover all of the steps to create the project and app, but you do have the option to clone the starting file structure from GitHub. 

## Creating a new directory

The first step in our process is to create a folder that will contain the new project. In order to create the folder go to the command prompt, navigate to the desired directory and run the below command. For this example we will be creating a new folder called **myfirstproject**. 

```bash
# Windows
md myfirstproject

# macOS or Linux
mkdir myfirstproject
```

## Installing Git

In order to retrieve the files contained within GitHub we need to clone the repository. To begin the cloning process Git needs to first be installed on your computer. If Git isn’t installed on your computer then go to the [Git website][1] to install the latest version. 

## Cloning the GitHub repository

Now that Git has been installed we can use it to [clone][2] our GitHub repository. To begin open a command prompt and navigate to the previously created directory **myfirstproject**. Once in the directory start the cloning process by entering the following in the command prompt.

```bash
# [TODO] Needs final github link
git clone https://github.com/????
```
Once this has completed you should now see the **myfirstproject** project folder with the **hello_world** app within the directory.