# https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
from django.shortcuts import render, get_object_or_404
from .models import Psychologue
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import  UpdateView, TemplateView

# Create your views here.
def psychologues_profile(request, pk):
    psychologue_info = get_object_or_404(Psychologue, pk=pk)
    context = {'psy': psychologue_info,}
    return render(request, 'psychologues/psy_profile.html', context)

@login_required
def psychologues_home(request):
    psychologue = get_object_or_404(Psychologue, user = request.user.id)
    context = {'psychologue':psychologue}
    return render(request, 'psychologues/psy_home.html', context)

class PsycologueUpdateView(UpdateView):
    model = Psychologue
    fields = ('avatar')
    
# https://stackoverflow.com/questions/36846395/embedding-a-plotly-chart-in-a-django-template   
import plotly.offline as opy
import plotly.graph_objs as go   
class PsychologueDashBoard(TemplateView):
    template_name = 'psychologues/graph.html'

    def get_context_data(self, **kwargs):
        context = super(PsychologueDashBoard, self).get_context_data(**kwargs)

        x = [-2,0,4,6,7]
        y = [q**2-q+3 for q in x]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                            mode="lines",  name='1st Trace')

        data=go.Data([trace1])
        layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context
    