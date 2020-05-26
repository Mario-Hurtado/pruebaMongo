from django.http import HttpResponse
from django.shortcuts import render
from monitoring.auth0backend import getRole, getUserEmail
from django.contrib.auth.decorators import login_required
from tendero.models import Tendero
from tienda.models import Tienda

def home(request):
    return render(request, 'base.html')



@login_required
def authentication(request):

    #Se obtiene el rol del usuario
    role = getRole(request)

    if role == "Tendero Principal":
        
        #Se obtiene el email del usuario que ingresa
        email = getUserEmail(request)
        tendero = Tendero.objects.get(correo = email)
    
        context = {
        "data":tendero
        }

        return render(request,'tenderoLogin.html', context)

    elif role == "CEO":
        return render(request,'ceo.html')

    else:
        return HttpResponse("Unauthorized user")



