Another feature of using Django forms is the ability to use a tag named **crispy**. By implementing **crispy** forms we are able to call the **FormHelper** class that defines the rendering behavior. So instead of creating more HTML for our templates it gives us the ability to define the form attributes and layouts within our Python **forms** and **views** files. 

To see how **crispy** works to improve forms let's use what was just created to get client information. The below code has the fields defined as before, but we now have the ability to add the **FormHelper**. By adding this class we are able to define items in the Python code that were previously added to the HTML template.

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    visit_reason = forms.CharField(widget=forms.Textarea)(label='Reason for visit:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-clientForm'
        self.helper.form_class = 'shelterForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_request'

        self.helper.add_input(Submit('submit', 'Submit'))
```
When adding **FormHelper** we first need to call the base class constructor by using **super** and then override it. After overriding the base class we can then add the **FormHelper** class, and begin to define the attributes of the form that would have previously been included in the HTML template. Those items include the form id, class, method, action and **"Submit"** button.

Now that we have added **crispy_forms** to our form and called the **FormHelper** class to define the form behavior let's see what it looks like in the HTML template. In this instance we have a blank template except for the **crispy** tags at the beginning.

```
{% load crispy_forms_tags %}
{% crispy example_form example_form.helper %}
```
With the above tags we are calling the form and **FormHelper** through **crispy**. By including these tags the output will now automatically be formatted into an HTML template. 

## Using Bootstrap3 with Crispy

In our previous example we made seperate variables to call out each field and define the behavior, but we also have the option to use a very popular CSS framework named Bootstrap3.

```python
from crispy_forms.bootstrap import InlineField

helper.form_class = 'form-horizontal'
helper.label_class = 'col-lg-2'
helper.field_class = 'col-lg-8'
helper.layout = Layout(
    'client_name',
    'visit_reason',
    'contact_number',
    StrictButton('Send', css_class='btn-default'),
)
```
With the above example we have created the three fields, and defined the direction at which the fields will be displayed along with the layout. As you can see including **Crispy** forms allows form layout and behavior in a few simple steps. 