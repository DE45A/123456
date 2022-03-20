from django.shortcuts import render
from haato.models import Miku
from plotly.offline import plot
import plotly.graph_objs as go

# Create your views here.


def add(request):
    results = Miku.objects.all()
    context = {'mikus': results}

    if request.method == 'POST':
        x = request.POST['X']
        Miku(x=x).save()

    return render(request, "add.html", context)


def test(request):
    x = []
    fbk = Miku.objects.all()
    for i in fbk:
        x.append(i.x)
    plot_div = plot([go.Bar(x=x)], output_type='div')
    return render(request, "home.html", context={'plot_div': plot_div})


def dele(request):
    results = Miku.objects.all()
    context = {'mikus': results}

    if request.method == 'POST':
        y = request.POST['ID']
        did = Miku.objects.get(id=y)
        Miku.delete(did)
    return render(request, 'dele.html', context)
