from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class SignupForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    fname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    
class Slam_detail(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    home=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    pno=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    born=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    become=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    dream=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    sport=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    relation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    look=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    eat=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    movies=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    dislike=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    crazy=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    moment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    holiday=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    friendship=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    withyou=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    hobbies=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    truth=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    you=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    love=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    date=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    pic=forms.ImageField()
    
    