from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        labels = {
            'name': 'নাম ',
            'email': 'ইমেইল',
            'title': 'পদবী',
            'image': 'ছবি',
            'responsibilities': '',
            'bio': 'নিজের সম্পর্কে কিছু কথা',
            'facebook': 'ফেসবুক',
            'linkedin': 'লিঙ্কড ইন',
            'birthday': 'জন্মদিন'
        }
        
        fields = ['name', 'email', 'title', 'image',
         'responsibilities', 'bio', 'facebook',
         'linkedin', 'birthday']