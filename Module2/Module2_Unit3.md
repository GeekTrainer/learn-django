[1]: https://www.sqlite.org/download.html "Link to SQLite webpage"

## Exercise: Creating A SQLite Database In Django

Now that we have finished creating our first app, it's time to set up the database. For this example we will be using SQLite for the Django database and VSCode will be used to complete all of the required tasks. Also, remember to start up the virtual environment before beginning.

The first step in our exercise is to navigate to the inner **myfirstproject** folder and go to the **settings.py** file. As you look through the file you will notice Django has provided the start-up code for our database, but before we can go any further we need to first go to a command or terminal window and enter the below command.

```bash
python manage.py migrate
```

By running this command, Django searches for the **INSTALLED_APPS** setting within the **settings.py** file and creates any necessary tables according to the default settings.

## Displaying The Schema

Now that Django has completed the necessary setup for our SQLite database, let's uncover the two ways to check out the schema. The first will be through the SQLite command line and the second will be in VSCode.

[!NOTE] This task assumes SQLite is already installed, but if not then go to the SQLite website to download the [SQLite application][1].

1. The first way to check out the schema of the newly created database is to use the SQLite command line. For this task, browse through the file explorer and find the newly created database file and double click on the file.

    <img src="..\Module2\Module2_Images\Module2_DBImage.PNG" alt="SQLite Database Folder" style="margin-left: 30px;width:100px; height:auto" />

    By clicking on the file it will open a new window. Once the new window is open and you are able to see the SQLite command line, enter **.schema** to display the schema of the database.

    <img src="..\Module2\Module2_Images\Module2_SQLiteCommandLine.PNG" alt="SQLite Database Folder" style="margin-left: 30px;width:350px; height:auto" />

2. The second option to check out the contents of the database is to view it in VSCode. While there are different extensions available, we choose to install the **vscode-sqlite** extension.

    <img src="..\Module2\Module2_Images\Module2_VSC_SQLiteExt.PNG" alt="SQLite Database Folder" style="margin-left: 30px;width:250px; height:auto" />

    After installing this extension, hold down **CTRL + Shift + P** to view the command palette. Enter **SQLite: Open Database**, and then choose the appropriate database from the dropdown list. This will then open up a new view in the Explorer Pane where you can now view the database structure.

    <img src="..\Module2\Module2_Images\Module2_VSC_SQLiteDBOpen.PNG" alt="SQLite Database Folder" style="margin-left: 30px;width:250px; height:auto" />
