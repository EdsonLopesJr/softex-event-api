from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from events.models import Event
from events.serializers import EventSerializer

@api_view(['GET'])
def events_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def event_create(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_409_CONFLICT)