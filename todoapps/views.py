from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Todo
from .serializers import TodoSerializers


# CBV - Class Base View
# FBV - Function Base View(students should always stick to this)

# post,get,put,patch,delete
# CREATE
# class CreateTodoView(APIView):
#     def post(self,request):
#         try:
#             serializers = TodoSerializers(data= request.data)
#             if serializers.is_valid():
#                 serializers.save()
#                 return Response({"Message":"Task added Successfully"},status =status.HTTP_201_CREATED)
#             return Response({serializers.errors},status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# using create and retrieve together
class CreateRetrieveView(APIView):

    def post(self, request):
        try:
            serializer = TodoSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Task added successfully"},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        try:
            todos = Todo.objects.all()
            serializer = TodoSerializers(todos, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class GetUpdateDeleteView(APIView):
    # retrieve/get
    def get(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializers(todo)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
    # Update/put
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers =  TodoSerializers(todo,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({"Error":(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        

    # # Delete
    def delete(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"Message":f"{todo.title} Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
