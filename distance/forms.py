from django.forms import ModelForm
from .models import Distance


class getEndPointForm(ModelForm):
    class Meta:
        model = Distance
        fields = ['start_point', 'end_point']
        labels = {
            'end_point': 'Final Destination'
        }
