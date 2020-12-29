When creating HTML forms developers can spend hours creating different data fields and designing layouts for the best user experience. Django speeds up the process by cutting out the repetitive work in HTML and coding the fields in Python. Discover how Django can control field behavior and automatically create HTML tags, but first let's take a look at an HTML form.

## HTML forms

We start by creating a basic HTML template and then inserting the form element `<form>...</form>` tags within the `<body>`. By inserting these tags we can then begin to define the required fields for a "Contact Us" form.

```html
<!DOCTYPE html>
<html>
    <body>

        <h2>HTML Forms</h2>

        <form action="request_visit" method="POST" >
            <label for="fname">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="lname">Reason for inquiry:</label><br>
            <input type="text" id="shelter_message" name="shelter_message"><br>
            <label for="lname">Contact Number:</label><br>
            <input type="text" id="phone_number" name="phone_number"><br><br>
            <input type="submit" value="Submit">
        </form> 

    </body>
</html>
```
From the example above you can see we have included the fields for a name, the reason for inquiry, and a contact number. We have also included an `action` and `method` attribute within the beginning `form` tag and lastly added a **"Submit"** button.

The **action** and **method** attributes are important to define as they are triggered when the user clicks **"Submit"**. After submitting the form the **action** attribute will look for the file to return the form data for further processing while the **method** attribute declares the type of request. 

As you can see this form has declared the type of request as a **POST** in order to update the data within our database. If we had intended for this form to retrieve information from the database then we would have used **GET**.

## Understanding Django forms

Now that we have covered creating a form in HTML let discuss how Django can speed up the process. The first thing that Django developed was a **forms** class. This class controls the form and dictates not only the behavior, but how it appears to the user. Since we have already designed our form in HTML let's convert it over to a Django form. The first thing we need to do is create a **forms**.**py** file in our app then enter the below code under the comment `# [TODO] Create class for forms`.

```python
# [TODO] Create class for forms
from django import forms

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea, label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)
```
For this form we have created the **ClientForm** class to hold the form elements, and also define the fields. One thing to notice is that we are not creating the `<form>...</form>` tags, or the **"Submit"** button that is required for the HTML template. When inserting this form those elements will have to be added to the template in order to work correctly.