from django import forms
from blog.models import Material


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MaterialForm(StyleFormMixin, forms.ModelForm):
    
    class Meta:
        model = Material
        fields = ('title', 'body', 'email')


    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if 'tex.pro' not in cleaned_data:
            raise forms.ValidationError('Необходима корпоративная почта')
        return cleaned_data