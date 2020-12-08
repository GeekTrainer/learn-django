[2]: https://docs.djangoproject.com/en/3.1/topics/db/queries/ "Django Queries"

## Exploring the Django ORM
After we created the models for our app Django automatically created an API. This API allows us to easily create, retrieve, update and delete objects in our database. To begin this interaction we first have to call a python shell by entering the below command in the command line.

    python manage.py shell

Once the interactive console begins we then need to import the two models that were created for the **Hello, world!** app as below.

~~~
from hello_world.models import Question, Answer 
~~~

Before moving on to create an object, let's first test a query by asking Django to pull all questions that have been created. Since we have not created any questions a blank QuerySet should appear.

<img src="..\Module2\Module2_Images\Module2_Blank_Query.PNG" alt="Django Model Migration" style="margin-left: 30px;width:400px; height:auto" />

## Creating new objects

Now that we have imported our models into the python shell it is time to create an object. Since we are using **Hello, world!** and created a **Question** model let's first create a question for our database. Add the below line to the python interactive console.

~~~
q = Question(question_text='Is anyone out there?')
~~~

After entering the question then save it to the database by entering the command below. If we were working in SQL this would be the same command as **INSERT**.

~~~
q.save()
~~~

## Retrieving objects

Now that we have saved a question let's query the database to see if it was saved. When we queried the database earlier we asked for it to return all questions. Since we had not saved any questions it had returned a blank query. We will now perform the same query, but this time it should print out the question that was just saved.

<img src="..\Module2\Module2_Images\Module2_ReturnQuestion.PNG" alt="Django Model Migration" style="margin-left: 30px;width:400px; height:auto" />

## Modifying objects

Once objects are saved to a database there may be instances where you need to edit text or correct a misspelling. For instance, let's say after saving our first question we noticed that 'is' was not capitalized. 

~~~
q = Question(question_text='is anyone out there?')
~~~

In order to change that error in the database we would use that same variable to fix the text and then save it again to the database.

~~~
q.question_text = 'Is anyone out there?"

q.save()
~~~

Through this lesson we covered the basics of communicating with our database, but Django has provided many more functionalities. Explore this information further with Django [database queries][2].