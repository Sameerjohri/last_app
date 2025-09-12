from django import forms			 # type: ignore
from .models import Member

class MemberForm(forms.ModelForm):
  class Meta:
        model = Member
        fields = ['fname','lname','email','passwd','age']