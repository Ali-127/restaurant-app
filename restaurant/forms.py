from django import forms
from django.core.validators import MinLengthValidator


class OrderIDForm(forms.Form):
    orderid = forms.CharField(label="Order ID", validators=[MinLengthValidator(1)])
    
class AddForm(forms.Form):
    pass

class OrderForm(forms.Form):
    pass
