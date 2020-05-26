from ..models import Tendero

def get_all_tenderos():
    tenderos = Tendero.objects.all()
    return tenderos


