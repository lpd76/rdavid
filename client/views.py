
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ClientForm
from .models import Client
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from psychologues.models import Psychologue


# Create your views here.

class ClientView(DetailView):
    model=Client
    template_name = 'client/detail.html'
    context_object_name = 'client'
    
    def get_object(self):
        return Client.objects.get(uuid = self.kwargs.get('uuid'))
       
class ClientListView(ListView):
    template_name = 'client/client_list.html'
    paginate_by = 10
    context_object_name = 'clients'
    
    def get_queryset(self):
        self.psychologue = Psychologue.objects.get(user = self.request.user)
        return Client.objects.filter(psychologue = self.psychologue)
    
class ClientListView2(ListView):
    template_name = 'client/client_list.html'
    paginate_by = 10
    context_object_name = 'clients'
    
    def get_queryset(self):
        # https://stackoverflow.com/questions/37688730/django-ajax-search-function
        # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
        self.psychologue = Psychologue.objects.get(user = self.request.user)
        try:
            a = self.request.GET.get('suggestion')
        except KeyError:
            a = None
        if a:
            client_list = Client.objects.filter(psychologue = self.psychologue, nom__contains=a)
        else:
            client_list = Client.objects.filter(psychologue = self.psychologue)
            
        return client_list
class ClientListView3(ListView):
    template_name = 'client/client_list.html'
    paginate_by = 10
    context_object_name = 'clients'
    
    def get_queryset(self):
        # https://stackoverflow.com/questions/37688730/django-ajax-search-function
        # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
        self.psychologue = Psychologue.objects.get(user = self.request.user)
        a = self.request.GET.get('suggestion')
        if a:
            client_list = Client.objects.filter(psychologue = self.psychologue, nom__contains=a)
        else:
            client_list = Client.objects.filter(psychologue = self.psychologue)
        return client_list

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_changelist')
    def form_valid(self, form):
        # set the psychologist of the client
        form.instance.psychologue = Psychologue.objects.get(user = self.request.user)
        return super().form_valid(form)
    # https://stackoverflow.com/questions/5806224/sending-request-user-object-to-modelform-from-class-based-generic-view-in-django
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientCreateView, self).dispatch(*args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super(ClientCreateView, self).get_form_kwargs()
        kwargs.update({'psy_user': self.request.user})
        return kwargs
    
class ClientDetailView(DetailView):
    model = Client





