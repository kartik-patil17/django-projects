from .models import myTodos
from django.forms import ModelForm

class todoForm(ModelForm):
    class Meta:
        model = myTodos
        fields = '__all__'
