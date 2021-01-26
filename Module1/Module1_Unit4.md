[1]: https://www.python.org/  "Install Python"

Creating a Django project is similar to creating any Python application. We start by creating a folder and then installing the package by using `pip`.

## Installation overview

Before installing Django we first need to make sure the correct Python version is installed for the framework. In order to check your installed version navigate to your command prompt and type the following.

```bash
# Windows
python --version 

# macOS or Linux
python3 --version 
```

By executing this command it will display what Python version is installed on your computer. For this module we are using the latest official version of Django and they recommend using Python 3 in order to have access to the latest Python features. If you do not have Python installed then proceed to the [Python website][1] to download the correct version.

## Creating a virtual environment

Before downloading Django it is a good idea to create a virtual environment in order to isolate it from other applications. If a virtual environment is not created and the framework is installed globally it could cause a conflict with other Python applications causing them to fail. 

Start by creating a folder that will contain the new project as this will also hold the folder for the virtual environment. 

1. In order to create the folder go to the command prompt.
1. Navigate to the desired directory and run the below command. For this example we will be creating a folder called **myfirstdjangoproject**. 

    ```bash
    # Windows
    md myfirstdjangoproject

    # macOS or Linux
    mkdir myfirstdjangoproject
    ```

1. After the folder is created go inside the new directory

    ```bash
    # Windows
    cd myfirstdjangoproject

    # macOS or Linux
    cd myfirstdjangoproject
    ```

1. Then enter the below code in the command line.

    ```bash
    # Windows
    python -m venv venv

    # macOS or Linux
    python3 -m venv venv
    ```

    After executing the command there should now be a new virtual environment named **venv** contained within the directory. 

## Activating a virtual environment

Now that the virtual environment has been created we have to activate it before installing Django.

1. Using the command prompt go to the directory where the virtual environment folder is located and type the below command.

    ```bash
    # Windows
    venv\\Scripts\\activate

    # macOS or Linux
    source ./venv/bin/activate
    ```

    By executing this command the virtual environment will start, and the command prompt should now look similar to below.

    ![Activated venv](../Module2/Module2_Images/venvcommandprompt.PNG)

    The name of the virtual environment will be in parentheses followed by the path that you are in currently. This command prompt is where you will begin installing the Django framework.

## Django installation

Now that the virtual environment has been activated it is time to download Django. 

1. Using the same command line type the below command.

    ```bash
    pip install Django
    ```

With this command the Django framework will begin to download, and once completed we can start developing our app!
