from django.forms import ModelForm
from .models import QuesModel



class addQuestionform(ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"
