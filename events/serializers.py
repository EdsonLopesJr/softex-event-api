from rest_framework import serializers
from events.models import Event
from rest_framework.exceptions import ValidationError

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if end_date and start_date and end_date < start_date:
            raise ValidationError({'end_date': 'A data de término deve ser maior ou igual à data de início.'})
        
        return data

    def validate_name(self, value):
        if Event.objects.filter(name=value).exists():
            raise serializers.ValidationError("Evento já existe com esse nome.")
        return value
        

