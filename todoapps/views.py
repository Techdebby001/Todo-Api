from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Todo
from .serializers import TodoSerializers


# CBV - Class Base View
# FBV - Function Base View(students should always stick to this)

# post,get,put,patch,delete
# CREATE
class CreateTodoView(APIView):
    def post(self,request):
        try:
            serializers = TodoSerializers(data= request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({"Message":"Task added Successfully"},status =status.HTTP_201_CREATED)
            return Response({serializers.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
# RETRIEVE
# UPDATE
# DELETE