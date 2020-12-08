[1]: https://docs.djangoproject.com/en/3.1/topics/install/ "Django Installation Guide"
[2]: https://www.python.org/  "Install Python"
[3]: https://www.djangoproject.com/ "Django Website"
[4]: https://www.djangoproject.com/start/ "Get Started with Django"
[5]: https://docs.djangoproject.com/en/3.1/intro/install/ "Django Quick Install Guide"
[6]: https://docs.djangoproject.com/en/3.1/faq/install/#faq-python-version-support "Django Python Version"

While the Django framework may have a little bit of a learning curve, they have provided everything you need to get started on their [website][3]. When browsing you will see the choice to either go through the [tutorials and documentation][4], or just downloading the framework.

## Installation overview

Once deciding to click the download button you will be given two options for the framework depending on which platform version you would like to use. For this lesson we are using the latest official version.

There is also the option to browse through the Django [installation guide][1] or their [quick install guide][5], but before downloading check that your [Python version][6] is the one that Django recommends. 

[!NOTE] If you do not have the recommended version of Python, then go to the [Python website][2] to download the correct version.

## Exercise: Creating a virtual environment

Before downloading Django it is a good idea to create a virtual environment. By creating a virtual environment to hold the Django framework it will then not affect any other applications that might be in development. For this exercise we will be using Powershell, and a Windows environment.

The first step is to open **Windows Powershell** and go to the desired directory that will contain the new virtual environment. Once the directory has been reached enter the below command.

    py -3 -m venv venv

When complete there should be a new virtual environment named **venv** contained within the directory. 

## Activating a virtual environment within VSCode

Now that the virtual environment has been created we have to activate it before working on the project. For this example we will be working within VSCode using the **Terminal** To activate the environment 

In order to activate the virtual environment access the **Terminal** within VSCode. Go to the directory where the virtual environment is located, and once in the correct directory type the below command.

    venv\Scripts\activate

## Exercise: Django installation

Now that the virtual environment has been activated it is time to download Django. Using the same command line within the VSCode Terminal type the below command.

    pip install Django

With this command the Django framework will be downloaded, and we are ready to start developing our apps!