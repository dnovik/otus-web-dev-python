from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import AccountItem
from .serializers import AccountItemSerializer
from rest_framework.request import Request
from rest_framework.response import Response


class AccountItemListView(APIView):

    def get(self, request: Request):
        items = AccountItem.objects.all()
        serializer = AccountItemSerializer(items, many=True)

        return Response(data=serializer.data)

    def post(self, request: Request):
        serializer = AccountItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountItemDetailView(APIView):

    def get(self, request: Request, pk):
        item = get_object_or_404(AccountItem, pk=pk)
        serializer = AccountItemSerializer(item)

        return Response(serializer.data)

    def post(self, request: Request):
        serializer = AccountItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, pk):
        new_item = request.data
        current_item = AccountItem.objects.get(pk=pk)
        serializer = AccountItemSerializer(current_item, new_item)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk):
        item = AccountItem.objects.get(pk=pk)
        item.delete()
        return Response('Account was deleted succesfully', status=status.HTTP_204_NO_CONTENT)

