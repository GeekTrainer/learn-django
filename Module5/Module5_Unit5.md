When learning Django we found out that **views** are an essential component to the framework as they handle what to return when a request is sent. So it's only logical that our form would be sent back to our **views.py** file for processing. In order to complete our form we now have the option to use an existing view, or create another one to handle this type of request.

```python
# [TODO] Create view for form
from django.http import HttpResponseRedirect

from .forms import ClientForm

def contactForm(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        # check if form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})
```
Since this is a new type of request we are creating another view for processing the form. As you can see above we are importing the name of the class that was created for the form, and we have created the definition that will be called when the template is sending a request. 

If the request happens to be **GET** then it will simply return a blank form that is ready for user input, but if the request is a **POST** it will automatically check if the data submitted is valid by executing the statement **if form.is_valid()**. If the data is valid it will continue to execute that block of code and bind the data to the form. If the data is not valid it will simply return the form to the template with the data that was previously entered by the user for correction. 

The other thing to notice about the form definition is what happens when the code executes properly for the two different types of requests. For the **POST** request we redirect the response to a **thanks** template, and in the **GET** request it renders the form in the template.

```python
    # if a GET method creates a blank form
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})
```
If the template sends a **GET** request then Python will process and render a blank form. The **return** statement sends the response with **render** defining the form. The first part of the **render** statement defines it as a **request**, the second section calls the template that will rendor our form, and the third part is defining the variable **"form"**. This variable can then be used in the template to call the form.

```html
<!--TODO: extend page layout and add form-->

{% extends "index.html" %}

{% block title %}Contact Us{% endblock %}

{% block content %}
    <h2 style="text-align: center; margin-top: 100px;">Contact Us</h2>
    
        <form action="get_client" method="post">
                {{ form }}
            <div style="width: 800px; margin: auto; text-align: center;">
                <input style="margin-top: 15px; background-color:rgb(51, 110, 219); color:white" type="submit" value="Submit">
            </div>
        </form>
    

{% endblock %}
```
As you can see we have included the **form** variable in the template, added the **\<form>** tags and **\<input>** element for the **"Submit"** button. These elements together complete our **client_request.html** template, and it is ready for user input.

### Generic views 


### Creating objects for Create, Edit and Delete