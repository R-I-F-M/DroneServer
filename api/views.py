from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DroneServer
from .serializers import ServerSerializers


class PrimaryRequest(APIView):
    def get(self, request):
        controllers = DroneServer.objects.all()
        serializer = ServerSerializers(controllers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ServerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecondaryRequest(APIView):
    def get(self, request, pk):
        try:
            controller = DroneServer.objects.get(pk=pk)
            serializer = ServerSerializers(controller)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DroneServer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            controller = DroneServer.objects.get(pk=pk)
            serializer = ServerSerializers(controller, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DroneServer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            controller = DroneServer.objects.get(pk=pk)
            controller.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DroneServer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
