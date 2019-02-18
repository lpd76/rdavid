from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Appointment, Status
from .forms import AppointmentForm
from django.urls import reverse_lazy

# Create your views here.
class AppointmentCreateView(CreateView):
    model=Appointment
    # fields = ('client', 'intervention', 'scheduled_on')
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_detail')
    context_object_name = 'appointments'
       
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AppointmentCreateView, self).dispatch(*args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        kwargs.update({'psy_user': self.request.user})
        return kwargs
    # add Status active
    def form_valid(self, form):
        form.instance.status = Status.objects.get(nom_fr='active')
        return super().form_valid(form)
    
    
class AppointmentListView(ListView):
    model=Appointment
    
    
    
class AppointmentDetailView(DetailView):
    model=Appointment
    template_name = 'appointments/appointment_details.html'
    context_object_name = 'appointment'
    
class AppointmentUpdateView(UpdateView):
    model=Appointment
    fields = ['note', 'status']
    template_name_suffix = '_update_form'