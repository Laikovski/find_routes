from django.forms import ModelForm, TextInput
from cities.models import City



class CityForm(ModelForm):


    class Meta:
        model = City
        fields = ('name',)
        labels = {
            'name': 'Add City',
            'class': 'form-label'
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }