from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post, Contact

# signup usercreation
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput (attrs={'class':'form-control'}),}


# login authenticationform
class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs= {'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autucomplete':'current-password', 'class':'form-control'}))

# post form creation for add 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'title':'Title', 'desc': 'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),}

#contact us
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        lables = {'name':'Name', 'email':'Email', 'address':'Address', 'message':'Write Message'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 'email':forms.EmailInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}), 'message':forms.Textarea(attrs={'class':'form-control'})}