Let's setup our application for production by updating some of the most common settings.

## Adding libraries

We will use two new libraries for our project:

- whitenoise to serve static files
- dotenv to manage settings

Let's install those into our project.

1. Inside **Visual Studio Code**, open **requirements.txt**
1. Add the following to the end of **requirements.txt**

    ```text
    whitenoise
    python-dotenv
    ```

1. Open a new terminal window by clicking **Terminal** > **New terminal**
1. Install the libraries by executing the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Enabling dotenv

[dotenv](https://github.com/theskumar/python-dotenv) is the most common method for managing environmental variables and other settings you don't wish to deploy to production or to source control. You create a file named **.env** (thus the name dotenv) with a collection of key/value pairs. The file is read by calling `load_dotenv`, which places all values into your environmental values for the application.

> ![IMPORTANT]
> Whenever using dotenv and Git or GitHub, make sure **.env** is listed in your **.gitignore** file to prevent it from being published to a public source control repository.

1. Create a new file in the root folder called **.env**
1. Add the following values to configure the debug and secret key options; create your own secure string

    ```text
    DEBUG=True
    SECRET_KEY=<SOME RANDOM STRING>
    ```

1. Open **manage.py**
1. Load the settings from **.env** by adding the following code below the line which reads `# TODO: Load environmental settings`

    ```python
    # TODO: Load environmental settings
    from dotenv import load_dotenv
    load_dotenv()
    ```

1. Open **settings.py**
1. Read the updated secret key by **REPLACING** the line below the comment `TODO: Replace the secret key setting` with the following:

    ```python
    # TODO: Replace the secret key setting
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```

1. Read the debug value by **REPLACING** the line below the comment `TODO: Replace the debug setting` with the following

    ```python
    # TODO: Replace the debug setting
    from distutils import util
    DEBUG = util.strtobool(os.getenv('DEBUG'))
    ```

## Update allowed hosts

`ALLOWED_HOSTS` controls the servers allowed to host or run your application. We will configure it to allow our site to run from Azure and locally.

1. Inside **settings.py**, **REPLACE** the line below the comment `TODO: Replace allowed hosts**

    ```python
    # TODO: Replace allowed hosts
    ALLOWED_HOSTS = [
        '.azurewebsites.net',
        'localhost',
        '127.0.0.1'
    ]

## Configure whitenoise

whitenoise is a service to serve static files. In our application, this will ensure the admin site is displayed properly.

1. Inside **settings.py**, enable the middleware for whitenoise by adding it to the list of `MIDDLEWARE` below the comment which reads `TODO: Register WhiteNoiseMiddleware`

    ```python
    # TODO: Register WhiteNoiseMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ```

1. At the bottom of **settings.py**, configure `STATIC_ROOT` for all static files by adding the following code below the comment which reads `TODO: Configure STATIC_ROOT`

    ```python
    # TODO: Configure STATIC_ROOT
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

1. Save all files by clicking **File** > **Save all**

You have now configured a Django application for production.
