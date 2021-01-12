
Another feature of using Django forms is the ability to use a 3rd party package named **crispy**. By implementing a `crispy` tag in forms we are able to call a `FormHelper` class that defines the rendering behavior. So instead of creating more HTML for our templates it gives us the ability to define the form attributes and layouts within our Python **forms** and **views** files. 

To see how **crispy** works to improve forms let's use what was just created to get client information. The below code has the fields defined as before, but we now have the ability to add the `FormHelper` class. By adding this class we are able to define items in the Python code that were previously added to the HTML template. Go to the **forms.py** file and input the below code under comments `# [TODO] import FormHelper and Submit from crispy` and `# [TODO] Add FormHelper() class`.

```python
# [TODO] import FormHelper and Submit from crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea)(label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)

    # [TODO] Add FormHelper() class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-clientForm'
        self.helper.form_class = 'shelterForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'contactForm'

        self.helper.add_input(Submit('submit', 'Submit'))
```

When adding `FormHelper()` we first need to call the base class constructor by using `super()` to override it. After overriding the base class we can then add the `FormHelper()` class and begin to define the attributes of the form that would have previously been included in the HTML template. Those items include the form `id`, `class`, `method`, `action` and `"Submit"` button.


Now that we have added the `FormHelper` class to our form to define the behavior let's see what it looks like in the HTML template. In this instance let's go back to the **contact.html** file that originally had this code added and add the below code under comment `<!-- TODO comment out the previous code and add the crispy tags -->`.

```html
<!-- TODO comment out the previous code and add the crispy tags -->
{% block content %}
    <!--  <h2 style="text-align: center; margin-top: 100px;">Contact Us</h2>
    
        <form action="contact" method="post">
            {% csrf_token %}
            {{ form }}
            <div style="width: 800px; margin: auto; text-align: center;">
                <input type="submit" value="Submit">
            </div>
        </form> -->

    {% load crispy_forms_tags %}
    {% crispy form form.helper %}

{% endblock %}
```

With the above `crispy` tags added we are calling the `form` variable used in the `contactForm` view to render the **Contact Us** form.

![ContactForm View](../Module5/Module5_Images/Module5_ContactFormView.PNG)

When this form is then called and rendered to the HTML template Django automatically formats the content into HTML tags.

![ContactForm View](../Module5/Module5_Images/Module5_CrispyFormHTML.PNG)

## Using Bootstrap with Crispy

In our previous example the layout of the fields were determined by the css file located in the static folder of our app. Another great benefit to using `crispy` is it allows the use of a very popular CSS framework named Bootstrap. Bootstrap is a free and open-source CSS framework with design templates included for buttons, forms, navigation, and many other components. In order to use this css framework just enter the below code under comments `# [TODO] import Layout from crispy`, `# [TODO] import StrictButton from crispy forms.bootstrap`, and `# [TODO] Add Bootstrap layout` in the **forms.py** file.

```python
# [TODO] Add Layout to crispy import
from crispy_forms.layout import Submit, Layout

# [TODO] Import StrictButton from crispy forms.bootstrap
from crispy_forms.bootstrap import StrictButton

class ClientForm(forms.Form):
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

With the above example we have laid out the three fields with the help of Bootstrap, and defined the direction at which the fields will be displayed. As you can see including `crispy_forms` allows form layout and behavior in a few simple steps.
