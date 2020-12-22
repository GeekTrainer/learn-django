[1]: https://git-scm.com/downloads "Git website downloads"
[2]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Clone GutHub repository"
[6]: https://docs.djangoproject.com/en/3.1/ref/django-admin/ "Command-line Utility"

For this module in the learning path we are continuing to build on an app named **dog_shelters**. If you are following the learning path then you have already downloaded the Django framework and created the project which means you can skip to the step **Cloning the GitHub repository** to retrieve the app starting files. If you are not following the learning path then follow the below steps before beginning this module. 

## Creating a new directory

The first step in our process is to create a folder that will contain the new project. In order to create the folder go to the command prompt, navigate to the desired directory and run the below command. For this example we will be creating a new folder called **mydjangoproject**. 

```bash
# Windows
md mydjangoproject

# macOS or Linux
mkdir mydjangoproject
```
## Creating a virtual environment

Now that the new directory has been created let's create a virtual environment to hold the Django framework. Make sure you are in the newly created directory, and run the following in the command prompt.

```bash
# Windows
py -3 -m venv venv

# macOS or Linux
python3 -m venv venv
```
After executing the command there should now be a new virtual environment named **venv** contained within the directory.

## Activating a virtual environment

Now that the virtual environment has been created we have to activate it before installing Django. Using the command prompt go to the directory where the virtual environment folder is located and type the below command.

```bash
venv\Scripts\activate
```
By executing this command the virtual environment will start, and the command prompt should now look similiar to below.

![Activated venv](../Module2/Module2_Images/venvcommandprompt.PNG)

The name of the virtual environment will be in parentheses followed by the path that you are in currently. This command prompt is where you will begin installing the Django framework.

## Django installation

Now that the virtual environment has been activated it is time to download Django. Using the same command line type the below command.

```bash
pip install Django
```
By executing this command the Django framework will begin to download, and once completed we need to install one more library in order for Django to be able to process images. Enter the below command in the command prompt.

```bash
pip install Pillow
```
Once this has completed we can now create our first project.

## Create a project with Django-admin

Now that Django is installed we are ready to begin the process of creating a project, but before we actually start coding there is one thing we have to do to create a Django project. In the same command prompt type the following:

```bash
django-admin startproject mydjangoproject
```
After running the above command the new project should appear in your chosen directory. In this instance you would see a new folder called 'mydjangoproject'.

## Navigating the project structure

Now that the Django project has been created let's look at the structure to see what was included.

    mydjangoproject/
            manage.py
            mydjangoproject/
                    __init__.py
                    settings.py
                    urls.py
                    asgi.py
                    wsgi.py

1. The first or outer **mydjangoproject** in the structure is your root directory which contains the entire project.
2. Next you have **manage.py**. This is a command-line utility that is created in every Django project and actually has the same function as 'django-admin'. Below is an example of how this could be used if you were inside the project folder and wanted to see the available subcommands. 

    ```bash   
    django-admin help
    ```
    OR
    ```bash
    python manage.py help
    ``` 
    For more information about the Django CLI, you can consult the [django-admin documentation][6].

3. The inner **mydjangoproject** is considered the Python package for your project.
4. Next we have **init.py** and if you look at the contents of this file you will notice that it is empty. Don't worry as this should be empty as it functions to tell Python that this directory should be considered a package.
5. Next in line we have **settings.py**. This file contains all of your settings or configurations.
6. Next is **urls.py**. This file contains the urls within the project.
7. Lastly we have **asgi.py** and **wsgi.py**. These last two files serve as the entry point for your web servers depending on what type of server is deployed.

## Deploying the project

Now that Django is installed, a project has been created, and we have examined the project structure it is time to make sure our project is working correctly.

Navigate to the **mydjangoproject** root directory and enter the following.

```bash      
python manage.py runserver
```

If the project runs correctly it will start to perform system checks, and start your development server. Copy and paste the url of your development server in your preferred browser, and you should see a Django 'Congratulations' page with a rocket taking off.

## Retrieving the starter app

### Installing Git

Now that our Django project is complete we need to retrieve the starter app for this module by cloning the GitHub repository. In order to clone the repository Git needs to be installed on your computer. If Git isn’t installed on your computer then go to the [Git website][1] to install the latest version. 

### Cloning the GitHub repository

Now that Git has been installed we can use it to [clone][2] our GitHub repository. To begin open a command prompt and navigate to the previously created directory **mydjangoproject**. Once in the directory start the cloning process by entering the following in the command prompt.

```bash
# [TODO] Needs final github link
git clone https://github.com/????
```
Once this has completed you should now see the **dog_shelters** app within the directory.
