
from django.forms import ModelForm
from . models import Todo_model

class TodoForm(ModelForm):
    class Meta:
        model = Todo_model
        fields = ['title']