from django import forms
from .models import Login
# label -> will change the field name
# initial -> will show inside the field
# disabled -> will stop the field
# help_text -> will show under the field to help the user
# widget -> change the unput type like for password
# required -> make the field required


# Another way to make forms in django
# class LoginForm(forms.Form):
    # username = forms.CharField(max_length=50, required=True)
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput)

# third method to create form in django
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__' # or ['username', 'password'] ->to choose what fields i want
       