from django import forms

class TextForm(forms.Form):
    text = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': "What's sparking in your mind?",
                'rows': 4,
                'id': 'text',
                'required': True
            }
        )
    )