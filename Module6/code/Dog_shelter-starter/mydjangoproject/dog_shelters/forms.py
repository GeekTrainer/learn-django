# [TODO] Create class for forms
from django import forms

# [TODO] import FormHelper and Submit from crispy
from crispy_forms.helper import FormHelper
# [TODO] import Layout from crispy
from crispy_forms.layout import Submit, Layout

# [TODO] import StrictButton from crispy forms.bootstrap
from crispy_forms.bootstrap import StrictButton

class ClientForm(forms.Form):
    client_name = forms.CharField(label='Name:', max_length=100)
    inquiry_reason = forms.CharField(widget=forms.Textarea, label='Reason for inquiry:', max_length=100)
    contact_number = forms.CharField(label='Contact Number:', max_length=100)

    # [TODO] Add FormHelper() class
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