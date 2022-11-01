from django.shortcuts import render

from .models import Tipper


def index(request):
    if request.GET:
        tippers = Tipper.objects.filter(model__iexact=request.GET.get('filter'))
    else:
        tippers = Tipper.objects.all()
    tipper_models = Tipper.Model.labels

    context = {
        'Tippers': tippers,
        'Models': tipper_models,

    }
    return render(request, 'home.html', context)


