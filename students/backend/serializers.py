from rest_framework.serializers import ModelSerializer
from .models import students

class studentserializer(ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'