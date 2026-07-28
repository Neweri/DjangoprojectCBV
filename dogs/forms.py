from datetime import datetime

from django import forms

from dogs.models import Dog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        # fields = '__all__' # (все поля которые есть в модели)
        exclude = ('owner',) #(те поля которые есть в модели)

    def clean_birth_date(self):
        cleaned_data = self.cleaned_data.get('birth_date')
        if cleaned_data:
            now_year = datetime.now().year
            if now_year - cleaned_data.year > 32:
                raise forms.ValidationError('Собака должна быть моложе 32 лет')
            return cleaned_data
        return cleaned_data