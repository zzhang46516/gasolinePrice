from django.shortcuts import render

from .models import UpdatePrice, States


def index(request):
    states = States.objects.all()

    if request.method == "POST":
        state = request.POST.get('dropdown')
        state_id = States.objects.get(states=state).id
        queryset = UpdatePrice.objects.filter(state=state_id).order_by('-release_date')[0]
    else:
        queryset = None
    context = {
        'states': states,
        'queryset': queryset
    }

    return render(request, 'index.html', context)

