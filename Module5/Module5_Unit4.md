## HTML forms

Before we start looking at the Django forms let's first look at an HTML form. We start by creating a template with the required HTML so we are able to insert the form element **\<form>...\</form>** within the **\<body>**. By inserting this **form** element we are then able to start defining the required fields.

```html
<!DOCTYPE html>
<html>
    <body>

        <h2>HTML Forms</h2>

        <form action="request_visit" method="POST" >
            <label for="fname">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="lname">Reason for visit:</label><br>
            <input type="text" id="shelter_message" name="shelter_message"><br>
            <label for="lname">Contact Number:</label><br>
            <input type="text" id="phone_number" name="phone_number"><br><br>
            <input type="submit" value="Submit">
        </form> 

    </body>
</html>
```
From the example above you can see we have included the fields for a name, the reason for visit, and their contact number. We have also included an **action** and **method** attribute within the beginning **form** tag and lastly added a **"Submit"** button.

The **action** and **method** attributes are important to define as they are triggered when the user clicks **"Submit"**. After submitting the form the **action** attribute will look for the file to return the form data for further processing while the **method** attribute declares the type of request. 

As you can see this form has declared the type of request as a **POST** in order to update the data within our database, but if the intention was to retrieve data then we would have used **GET**.

## Understanding Django forms

Now that we have covered HTML forms let discuss how Django contributes to the process of creating and processing forms. When creating HTML forms developers can not only spend hours creating different data fields, but also designing the layout for the best user experience. Django speeds up that process by automatically creating HTML forms, preparing the data for rendering and processing the submitted forms.

The first thing that Django developed was a **forms** class. This class controls the form and dictates not only the behavior, but how it appears to the user. Since we have already designed our form in HTML let's convert it over to a Django form. The first thing we need to do is create a **forms.py** file in our app to contain the below code.

```python
# [TODO] Create class for forms
from django import forms

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    visit_reason = forms.CharField(widget=forms.Textarea, label='Reason for visit:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)
```
For this form we have created the **ClientForm** class to hold the form elements, and also define the fields. One thing to notice is that we are not creating the **\<form>...\</form>** tags, or the **"Submit"** button that is required for the HTML template. When inserting this form those elements will have to be added to the template in order to work correctly.

## CSRF Tokens