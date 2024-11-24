from django import forms
from django.core import validators

class Form_article(forms.Form):

    title = forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese su titulo',
                'class':'titulo_form_article'
            }
        ),
    validators=[
        validators.MinLengthValidator(4,'Titulo muy corto.'),
        validators.RegexValidator('^[A-Za-z0-9*$','El titulo esta mal formado','invalid_title')
    ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
        validators.MinLengthValidator(20,'Contenido'),
        validators.RegexValidator('^[A-Za-z0-9*$','contenido esta mal formado','invalid_title') 
        ]
        )


    content.widget.attrs.update({
        'placeholder':'Ingrese su contenido',
        'class':'titulo_form_article',
        'id':'contenido_form'
        })
    
    public_options=[
        (1,'si'),
        (0,'no')
    ]

    public = forms.TypedChoiceField(
        label='publicado?',
        choices= public_options
    )
