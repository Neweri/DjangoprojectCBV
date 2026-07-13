from django import forms

from dogs.models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__' # (те поля которые есть в модели)
        # exclude = (те поля которые есть в модели)