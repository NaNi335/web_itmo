from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import User


# Create your views here.
def detail(request, user_id):
    try:
        p = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User doesn't exist")
    return render(request, 'detail.html', {'owner': p})