[1]: https://docs.djangoproject.com/en/3.1/ref/csrf/ "CSRF Details"

When learning Django we found out that **views** are an essential component to the framework as they handle what to return when a request is sent. So it's only logical that our form would be sent back to our **views**.**py** file for processing. In order to complete our form we now have the option to use an existing view, or create another one to handle this type of request. Enter the below code under the comment `# [TODO] Create view for ClientForm`.

```python
# [TODO] Create view for ClientForm
from django.http import HttpResponseRedirect

from .forms import ClientForm

def contactForm(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        # check if form is valid:
        if form.is_valid():
            # code to process data from from as appropiate
            return HttpResponseRedirect('thank_you')
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})
```
Since this is a new type of request we are creating another view for processing the form. As you can see above we are importing the name of the class that was created for the form, and we have created the definition that will be called when the template is sending a request. 

If the request happens to be **GET** then it will simply return a blank form that is ready for user input, but if the request is a **POST** it will automatically check if the data submitted is valid by executing the statement `if form.is_valid()`. If the data is valid it will continue to execute that block of code and bind the data to the form. If the data is not valid it will simply return the form to the template with the data that was previously entered by the user for correction. 

The other thing to notice about the form definition is what happens when the code executes properly for the two different types of requests. For the **POST** request we redirect the response to a **thank_you** template, and in the **GET** request it renders the form in the template.

```python
    # if a GET method creates a blank form
    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})
```
If the template sends a **GET** request then Python will process and render a blank form. The `return` statement sends the response with `render` defining the form. The first part of the **render** statement defines it as a **request**, the second section calls the template that will rendor our form, and the third part is defining the variable **"form"**. This variable can then be used in the template to call the form.

Now that we have created the form we need to add a "Contact Us" template. In the templates folder of the app create a file named **contact.html** and then enter the below code under the comment `<!--TODO: extend page layout and add form-->`.

```html
<!--TODO: extend page layout and add form-->

{% extends "index.html" %}

{% block title %}Contact Us{% endblock %}

{% block content %}
    <h2 style="text-align: center; margin-top: 100px;">Contact Us</h2>
    
        <form action="get_client" method="post">
            {% csrf_token %}
            {{ form }}
            <div style="width: 800px; margin: auto; text-align: center;">
                <input style="margin-top: 15px; background-color:rgb(51, 110, 219); color:white" type="submit" value="Submit">
            </div>
        </form>
    

{% endblock %}
```
As you can see we have included the `{{ form }}` variable in the template, added the `<form>` tags and `<input>` element for the **"Submit"** button. These elements together complete our **client_request.html** template, and it is ready for user input. Now that the form is ready for user input there is one more tag that was added to guard against Cross Site Request Forgeries. [CSRF][1] is automatically enabled by Django and is ready to use for **POST** requests. The only thing we need to do is add this tag `{% csrf_token %}` to our form code. Now that we have addressed the way form views are added let's see what Django created to speed up the process even further.

## Generic views for Create, Update and Delete 

Django has again tried to speed up the process of coding form views by providing Generic views. Generic views give us the ability to accomplish a basic task with less code, and easily check if a submitted form is valid before processing the information. We will now cover these views by creating forms that can interact with the database.

### Developing objects for Create

The first generic view will be **CreateView**. Find the **views**.**py** file in the app folder and enter the below code under the comment `# [TODO] Develop CreateView generic view for form`.

```python
# [TODO] Develop CreateView generic view for form
from django.views.generic.edit import CreateView

class CreateShelter(CreateView):
    model = Shelter
    fields = ['shelter_name', 'shelter_location']
    template_name = "shelter_form.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('shelter_list')
```
As you can see we have imported `CreateView`, defined our class **CreateShelter** to include the necessary fields, named the template it will use to render the form, and also defined what will happen if the form is valid. In this case it will save the information to the database then redirect to the **shelter_list** page. 

The next step in creating our form is to add the template. Now go to the **templates** folder of the app and create a file named **shelter_form.html** to enter the below code under the comment `<!--TODO: extend page layout and add form-->`.

```html
<!--TODO: extend page layout and add form-->
{% extends "index.html" %}

{% block title %}Add Shelter{% endblock %}

{% block content %}
    <h2 style="text-align: center; margin-top: 100px;">Create Shelter</h2>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <div style="width: 800px; margin: auto; text-align: center;">
            <input type="submit" value="Save">
        </div>
    </form>

{% endblock %}
```
As you can see we have extended the **index.html** template to keep the same layout, added the `csrf_token` for authentication when sending the POST, and finally the form tag. We also added `as_p` to the form tag to show a simple way to encase a form in HTML tags. In this case the form fields will be surrounded by the `<p>` tags.

![HTML Tags](../Module5/Module5_Images/Module5_GenericFormHTMLView.PNG)

The last two steps in the process is to add the link to the template, and then define the path. For the **index.html** file add the below code under the comment `<!-- TODO - Create the URL for the new template page shelter_form -->`.

```html
{% block sidebar %}
  {{ block.super }}
  <a href="shelter_spotlight" class="w3-bar-item w3-button">Shelter Spotlight</a>
  <!-- TODO - Create the URL for the new template page shelter_list -->
  <a href="shelter_list" class="w3-bar-item w3-button">Shelters</a>
  <a href="contact" class="w3-bar-item w3-button">Contact Us</a>
  <!-- TODO - Create the URL for the new template page shelter_form -->
  <a href="shelter_form" class="w3-bar-item w3-button">Create Shelter</a>
{% endblock %}
```
After adding the **shelter_form** link then add the path in the app **urls**.**py** file by copying the below code under the comment `# [TODO]: Add the path below for our Shelter CreateView`. While adding this form to the public site isn't practical you could eventually create another site just for updating the database through the use of these forms.

```python
urlpatterns = [
    path('home', views.index, name='index'),
    # [TODO]: Add the path below for our ShelterList ListView
    path('shelter_list', views.ShelterList.as_view(), name='ShelterList'),
    # [TODO]: Add the path below for our ShelterDetail DetailView
    path('<int:pk>', views.ShelterDetail.as_view(), name='ShelterDetail'),
    path('shelter_spotlight', views.spotlight, name='spotlight'),
    path('contact', views.contactForm, name='contactForm'),
    path('thank_you', views.thankyou, name='thankyou'),
    # [TODO]: Add the path below for our Shelter CreateView
    path('shelter_form', views.CreateShelter.as_view(), name='CreateShelter'),
]
```
Now that we have developed the **Create** object let's test it out by adding a new shelter. Go to the app in your web browser and you should now see a new link in the side navigation called **Create Shelter**. If you do not see the link right away you may need to refresh the browser. Click on the link and it will take you to the form that was just created. For the new shelter let's enter **Second Chance Shelter** for the shelter name, **Denver, CO** as the location and then click **Save**. If the form works correctly it will take you back to the **shelter_list** page and the new shelter should now appear in the list.

![Added Shelter](../Module5/Module5_Images/Module5_CreateNewShelterName.PNG)

### Creating objects for Update and Delete

We will now move on to create a template that will contain both the **Update** and **Delete** functions for the database. Go to the templates folder of the app and create a new file named **update_delete_shelters.html**. After creating the template then enter the below code under the comment `<!-- TODO - Add update and delete shelter lists below -->`.

```html
<!-- TODO - Add update and delete shelter lists below -->
{% extends "index.html" %}
{% block content %}

    <div class="row">
        <div class="column">
            <h2>Update Shelters</h2>
            <ul style="text-align: left; margin-left: 80px;">
                {% for get_shelters in current_shelter_list %}
                    <a href="{{ get_shelters.id }}/update" >{{get_shelters.shelter_name}}</a><br>
                    Location: {{get_shelters.shelter_location}}
                    <br><br>
                {% endfor %}
            </ul>
        </div>
        <div class="column">
            <h2>Delete Shelters</h2>
            <ul style="text-align: left; margin-left: 80px;">
                {% for get_shelters in current_shelter_list %}
                    <a href="{{ get_shelters.id }}/delete" >{{get_shelters.shelter_name}}</a><br>
                    Location: {{get_shelters.shelter_location}}
                    <br><br>
                {% endfor %}
            </ul>
        </div>
    </div>
{% endblock %}
```
For this page we have divided it into two columns. Each function will be contained in its own column with a list of current shelters. We have also added the shelter name as a URL that is associated with the shelter `id`. By adding this URL the database will then know what shelter information to return.  

In addition to the template we also need to create the two other templates that will hold the forms. The first template to create is **update_shelter.html**. Afer creating the template then add the below code under the comment `<!--TODO: extend page layout and add Update form-->`.

```html
<!--TODO: extend page layout and add Update form-->
{% extends "index.html" %}

{% block title %}Update Shelter{% endblock %}
{% block sidebar %}{% endblock %}

{% block content %}
    <h2 style="text-align: center; margin-top: 100px;">Update Shelter</h2>

    <form method="post">
        {% csrf_token %}
        <div style="text-align: center;">{{ form }}</div>
        <div style="width: 800px; margin: auto; text-align: center;">
            <input type="submit" value="Update">
        </div>
    </form>
{% endblock %}
```
The second template to create is named **delete_shelter.html**. After creating this template then also enter the below code under the comment `<!--TODO: extend page layout and add Delete form-->`.

```html
<!--TODO: extend page layout and add Delete form-->
{% extends "index.html" %}

{% block title %}Delete Shelter{% endblock %}

{% block content %}
    <h2 style="text-align: center; margin-top: 100px;">Delete Shelter</h2>

    <form method="post">
        {% csrf_token %}
        <p style="text-align: center;">Are you sure you want to delete "{{ object }}" dog shelter?</p>
        <div style="width: 800px; margin: auto; text-align: center;">
            <input type="submit" value="Confirm">
        </div>
    </form>

{% endblock %}
```
The next task is to now define the views. Go to the **views**.**py** file of the app and enter the below code under the comment `# [TODO] Create ListView to add shelters to update_delete_shelters template` and `# [TODO] Develop UpdateView and DeleteView for forms`.

```python
# [TODO] Create ListView to add shelters to update_delete_shelters template
class ShelterEdits(ListView):
    model = Shelter
    context_object_name = 'current_shelter_list'   # your own name for the list as a template variable
    template_name = "update_delete_shelters.html"

# [TODO] Develop UpdateView and DeleteView for forms
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class UpdateShelter(UpdateView):    
    model = Shelter
    fields = ['shelter_name', 'shelter_location']
    template_name = "update_shelter.html"

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/dog_shelters/update_delete_shelters')

class DeleteShelter(DeleteView):
    model = Shelter
    template_name = "delete_shelter.html"

    success_url = '/dog_shelters/update_delete_shelters'
```
In the first view addtion we created another **ListView** to feed the shelter lists to the **update_delete_shelters** template. In the next section we needed to import both **UpdateView**, and **DeleteView**. We are also defining the class for both of these functions, and what will happen when the form is considered valid.

After creating the views we then need to define the paths for all three templates in the app **urls**.**py** file by entering the below code under the comment `# [TODO]: Add the belows for our Shelter UpdateView, DeleteView and template page to call these functions`.

```python
  # [TODO]: Add the belows for our Shelter UpdateView, DeleteView and update_delete_shelters template page to call these functions
    path('<pk>/update', views.UpdateShelter.as_view(), name='UpdateShelter'),
    path('<pk>/delete', views.DeleteShelter.as_view(), name='DeleteShelter'),
    path('update_delete_shelters', views.ShelterEdits.as_view(), name='ShelterEdits'),
```
For the **Update** and **Delete** views we need to add the primary key `<pk>` in the path along with whether it will be updating or deleting the record. We are also adding the path for the **update_delete_shelters** template that will give you access to perform one of these functions.

The last thing we need to do is now add the template link to the **shelter_form** file. Add the below code under the comment `<!--TODO: Carry over parent links and add new update_delete_shelters link-->`.

```html
<!--TODO: add new link-->
{% block sidebar %}
  {{ block.super }}
  <a href="update_delete_shelters" class="w3-bar-item w3-button">Update/Delete Shelters</a>
{% endblock %}
```
That's it for adding these functions. Now let's try it out! Make sure all of the additions have been saved, and go to your app in the browser. Click on the **Create Shelter** link, and there should now be a new link named **Update/Delete Shelters**. Click on that link to go to the new template that was created for these functions.

![Update/Delete Page](../Module5/Module5_Images/Module5_UpdateDeleteTemplate.PNG)

Now that we are on this page click on the first shelter name under **Update**. For this shelter we have now changed **WA** to lowercase and then clicked **Update**

![Update Shelter Location](../Module5/Module5_Images/Module5_UpdateShelter.PNG)

After clicking the update button it should then take you back to the previous template and show the updated location for the shelter.

![Shelter Location Updated](../Module5/Module5_Images/Module5_ShelterLocationUpdated.PNG)

Now that we have updated a shelter name let's delete one. On the **Delete Shelters** column click on the shelter name **New Beginnings**, and it should then take you to the delete page as below.

![Confirm Delete](../Module5/Module5_Images/Module5_DeleteShelter.PNG)

Click the **Confirm** button, and it should then take you back to the previous list with that name deleted.

![Shelter Deleted](../Module5/Module5_Images/Module5_ShelterDeleted.PNG)
