from django.shortcuts import render
from haato.models import Miku
from plotly.offline import plot
import plotly.graph_objs as go

# Create your views here.


def miku(request):
    results = Miku.objects.all()
    context = {'mikus': results}

    if request.method == 'POST':
        x = request.POST['X']
        y = request.POST['Y']
        Miku(x=x,y=y).save()

    return render(request, "miku.html", context)
