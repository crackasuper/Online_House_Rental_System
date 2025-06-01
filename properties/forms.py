from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    """
    Form for creating and editing properties
    """
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'property_type', 'address',
            'city', 'state', 'zip_code', 'price', 'bedrooms',
            'bathrooms', 'area', 'is_available', 'is_featured'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'min': 0}),
            'bedrooms': forms.NumberInput(attrs={'min': 0}),
            'bathrooms': forms.NumberInput(attrs={'min': 0, 'step': 0.5}),
            'area': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'}) 