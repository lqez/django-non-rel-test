from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import mySerializer


@api_view(['POST'])
def save(request):
    serializer = mySerializer(data=request.DATA)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
