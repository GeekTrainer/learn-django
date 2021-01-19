
Another feature of using Django forms is the ability to use a 3rd party package named **crispy**. By implementing a `crispy` tag in forms we are able to call a `FormHelper` class that defines the rendering behavior. This function allows us to skip some of the HTML code for our templates and gives us the ability to define the form attributes and layouts within our Python **forms** and **views** files. 

To see how **crispy** works to improve forms let's create another form to capture client information. With the addition of the `FormHelper` class we are now able to define items in the Python code that were previously added to the HTML template. 

1. Go to the **forms.py** file and input the below code under comments `# [TODO] import FormHelper and Submit from crispy` and `# [TODO] Add crispy contact form`.

```python
# [TODO] import FormHelper and Submit from crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# [TODO] Add crispy contact form
class CrispyClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea, label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-clientForm'
        self.helper.form_class = 'shelterForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'contactForm'
        # [TODO] Add Bootstrap layout before submit button

        self.helper.add_input(Submit('submit', 'Submit'))
```

When adding `FormHelper()` we first need to call the base class constructor by using `super()` to override it. After overriding the base class we can then add the `FormHelper()` class and begin to define the attributes of the form that would have previously been included in the HTML template. Those items include the form `id`, `class`, `method`, `action` and `"Submit"` button.

2. Now that the crispy form has been added go to the **views.py** file and add the below code under comment `# [TODO] Process and render crispy contact form`.

```python
# [TODO] Process and render crispy contact form
def crispycontactForm(request):
    if request.method == 'POST':
        form = CrispyClientForm(request.POST)
        # check if form is valid:
        if form.is_valid():
            # code to process data as appropriate
            return HttpResponseRedirect('thank_you')
    else:
        form = CrispyClientForm()

    return render(request, 'crispycontact.html', {'form': form})
```

3. The next step for this task go to the **index.html** template file and add the below code under comment `<!-- TODO - Create the URL for the new crispy form -->`.

```html
<!-- TODO - Create the URL for the new template page shelter_list -->
<a href="shelter_list" class="w3-bar-item w3-button">Shelters</a>
<a href="contact" class="w3-bar-item w3-button">Contact Us</a>
<!-- TODO - Create the URL for the new crispy form -->
<a href="crispycontact" class="w3-bar-item w3-button">Crispy Form</a>
```

4. The last step that needs to be completed is adding the path for the new view. Go to the app **urls.py** files and add the below code under comment `# [TODO]: Add the path below for crispy form`.

```python
   path('shelter_spotlight', views.spotlight, name='spotlight'),
    path('contact', views.contactForm, name='contactForm'),
    # [TODO]: Add the path below for crispy form
    path('crispycontact', views.crispycontactForm, name='crispycontactForm'),
```

Now that we have completed the form and added the URL let's see what the code looks like in the HTML template. For this example let's create another template.

1. Go to the app template folder and create the **crispycontact.html** file and add the below code.

```html
{% extends "index.html" %}

{% block title %}Contact Us{% endblock %}

{% block content %}

    {% load crispy_forms_tags %}
    {% crispy form form.helper %}

{% endblock %}
```

With the above `crispy` tags added we are now able to call the `form` variable used in the `crispycontactForm` view to render the **Crispy Form** web page.

![ContactForm View](../Module5/Module5_Images/Module5_CrispyContactFormView.PNG)

When this form is then called and rendered to the HTML template Django automatically formats the content into HTML tags.

![ContactForm View](../Module5/Module5_Images/Module5_CrispyFormHTML.PNG)

## Using Bootstrap with Crispy

In our previous example the layout of the fields were determined by the css file located in the static folder of our app. Another great benefit to using `crispy` is it allows the use of a very popular CSS framework named Bootstrap. Bootstrap is a free and open-source CSS framework with design templates included for buttons, forms, navigation, and many other components. 

1. To begin using this css framework go to the **forms.py** file and enter the below code under comments `# [TODO] Add Layout to imports`, `# [TODO] import StrictButton`, and `# [TODO] Add Bootstrap layout before submit button`.

```python
# [TODO] Add Layout to imports
from crispy_forms.layout import Submit, Layout

# [TODO] Import StrictButton
from crispy_forms.bootstrap import StrictButton

class CrispyClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea, label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-clientForm'
        self.helper.form_class = 'shelterForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'contactForm'

        # [TODO] Add Bootstrap layout before submit button
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'client_name',
            'inquiry_reason',
            'contact_number')

        self.helper.add_input(Submit('submit', 'Submit'))
```

With the above example we have laid out the three fields with the help of Bootstrap and defined the direction at which the fields will be displayed. As you can see including `crispy_forms` allows form layout and behavior in a few simple steps.
