from django.forms import ModelForm
from .models import Pota

class PotaForm(ModelForm):
    class Meta:
        model = Pota
        fields = ("PotaSize", 'PotaCost', 'PotaBirth', 'PotaName')