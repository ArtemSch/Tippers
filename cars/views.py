from django.shortcuts import render
from django.views import View

from .models import Tipper


class TippersListAPIView(View):
    def get_queryset(self):
        return Tipper.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET:
            tippers = Tipper.objects.filter(model__iexact=request.GET.get('filter'))
        else:
            tippers = self.get_queryset()

        selects = Tipper.objects.values_list('model', flat=True).distinct()
        context = {'Tippers': tippers,
                   'Selects': selects
                   }
        return render(request, 'home.html', context)
