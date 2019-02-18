from django import forms
from .models import Appointment
from psychologues.models import Psychologue, Competence, Intervention
from client.models import Client
from bootstrap_datepicker_plus import DateTimePickerInput
# https://pypi.org/project/django-bootstrap-datepicker-plus/
# https://media.readthedocs.org/pdf/django-bootstrap-datepicker-plus/latest/django-bootstrap-datepicker-plus.pdf
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('client', 'intervention', 'scheduled_on')
        widgets = {
            'scheduled_on': DateTimePickerInput(), # default date-format %m/%d/%Y will be used
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('psy_user')
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.psychologue = Psychologue.objects.get(user = user)
        self.fields['client'].queryset = Client.objects.filter(psychologue = self.psychologue)
        self.competences = Competence.objects.filter(psychologue = self.psychologue)
        self.fields['intervention'].queryset = Intervention.objects.filter(nom_fr__in=[i.intervention for i in self.competences])
    