from django.forms import ModelForm
from app.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'body']
        