from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({"category": serializer.data})

    def post(self, request):
        category = request.data.get("category")
        # Create an article from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.name)})

    def put(self, request, pk):

        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()

        return Response({
            "success": f"Category '{category_saved.name}' updated successfully"
        })

    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({
            "message": f"Category with id '{pk}' has been deleted."
        }, status=204)