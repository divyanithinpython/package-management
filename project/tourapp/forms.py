from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


from.models import*
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']



class PackageForm(forms.ModelForm):
    class Meta:
        model=Pakage
        fields=['location','image','image1','image2','price','start_date','end_date','shortdescription','fulldescription','total_seats','available_seats']
class BookingForm(forms.ModelForm):
    class Meta:
        model=TravelBook
        fields=['firstname','lastname','email','phone','destination','seats']





class PackageSearchForm(forms.Form):
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')
