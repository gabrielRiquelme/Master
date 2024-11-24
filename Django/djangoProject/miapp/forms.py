from django import forms

class Form_article(forms.Form):

    title = forms.CharField(
        label="Titulo"
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )
