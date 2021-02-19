# Title

Deploying a Django application to Azure with PostgreSQL

## Role(s)

- student
- developer

## Level

- intermediate

## Product(s)

- Django
- Azure App Services
- Visual Studio Code

## Prerequisites

- HTML/CSS
- Git
- npm
- Python

## Summary

To make our application available to the world we need to host it somewhere. We are going to deploy our application to Azure, and create a database for our data.

## Learning objectives

1. Configuring the project for deployment
2. Deploying the project

## Chunk your content into subtasks

Identify the subtasks of *module title*

| Subtask | What part of the introduction scenario does this subtask satisfy? | How will you assess it: **Exercise or Knowledge check**? | Which learning objective(s) does this help meet? | Does the subtask have enough learning content to justify an entire unit? If not, which other subtask will you combine it with? |
| ---- | ---- | ---- | ---- | ---- |
| How to get an application ready for deployment | Configuring the project for deployment | Exercise | Configuring the project for deployment | yes |
| Performing the deployment | Deploying the project | Exercise | Deploying the project | Yes |
| Using crispy-forms to improve data display | Improving form display | Exercise | Improving form display | yes |

## Outline the units

1. **Deploying to Azure**

    SQLite and locally hosting our application is perfect for development, but we need something better for production. We will see how to prepare our application for deployment and perform the steps necessary to deploy it.

1. **Exercise - Obtain the starter**

    To streamline this module, we provided a starter project you can use.

    1. Cloning the repository
    2. Installing the necessary libraries
    3. Open Visual Studio Code

1. **Deployment considerations**

    When developing our application, we take certain shortcuts for the sake of convenience. When we deploy to production, however, many of these settings need to change. We will explore how to prepare our application for deployment.

    - Debug mode
    - Secret key
    - Allowed hosts
    - Static files

1. **Exercise - Preparing our application for deployment**

    Let's walk through the necessary steps to deploy our application.

    - Updating files for deployment

    1. Adding the necessary libraries
    2. Creating a production settings file
    3. Configuring our application

1. **Deployment considerations**

    When we are ready to deploy our application, we need to ensure we have the necessary components available, and our method selected. We will see what's needed to ensure a successful deployment.

    - Deployment options
    - Database considerations
    - Creating the database schema

1. **Exercise - Deploy to Azure**

    Let's deploy our application!

    - Preparing VS Code
    - Deploying the application
    - Creating the database

    1. Install the extensions
    2. Deploy the application
    3. Create the database
    4. Configure application settings
    5. Create the database
    6. Create the schema and superuser
    7. Browse to the site
1. **Summary**

    We saw how to deploy our application to production!

1. **Knowledge check**

    What types of questions will test *learning objective*? *[(Knowledge check guidance)](https://review.docs.microsoft.com/learn-docs/docs/id-guidance-knowledge-check)*

    - Multiple choice

## Notes

Note any additional information that may be beneficial to this content such as links, reference material, etc.

- [Django](https://docs.djangoproject.com/)
- [Tutorial: Deploy a Django web app with PostgreSQL in Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=bash%2Cclone)
