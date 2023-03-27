""" Product form """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Testimony


class ProductForm(forms.ModelForm):
    """ Product form """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey style-input'


class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony
        fields = ('body',)
