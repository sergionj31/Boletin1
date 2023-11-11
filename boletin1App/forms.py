from django import forms
import datetime
import re
from django.core.exceptions import ValidationError

class Formulario(forms.Form):
    fechaInicio = forms.DateField(initial=datetime.date.today)
    fechaFin = forms.DateField(initial=datetime.date.today, help_text="Igual o superior a la fecha de inicio.")

    DIAS_DE_LA_SEMANA = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]

    dias_semana = forms.MultipleChoiceField(
        choices=DIAS_DE_LA_SEMANA,
        widget=forms.CheckboxSelectMultiple,
    )

    correo = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        fechaInicio = cleaned_data.get('fechaInicio')
        fechaFin = cleaned_data.get('fechaFin')
        dias_semana = cleaned_data.get('dias_semana')
        correo = cleaned_data.get('correo')

        if correo is not None and not re.match(r'^.+@iesmartinezm\.es$', correo):
            raise ValidationError('El correo electrónico debe tener el formato XXX@iesmartinezm.es')

        if fechaFin < fechaInicio:
            raise ValidationError('La fecha fin debe ser mayor o igual a la fecha inicio')

        if not dias_semana:
            raise ValidationError('Debes elegir al menos un día de la semana')

        if len(dias_semana) > 3:
            raise ValidationError('El máximo de días que puedes elegir es: 3')

        return cleaned_data




