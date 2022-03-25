
from rest_framework.serializers import ModelSerializer

from .models import Note
#change from here 
from .models import profiles

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    

#made chnage here(extra added)
class profileSerializer(ModelSerializer):
    class Meta:
        model = profiles
        fields = '__all__'
