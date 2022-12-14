from django.shortcuts import render

from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, DashboardTaskByCategorySerializer, DashboardTaskCompletionStatSerializer, TaskSerializer
from .models import Category, Task
from .permissions import TaskPermission
from django.db.models import Count
from django.db.models.query_utils import Q
from rest_framework.response import Response
# Create your views here.


#modify PageNumberPagination: https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
class StandardResultSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    
    
    def get_queryset(self):
        return self.request.user.categories.all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated, TaskPermission]
    serializer_class = TaskSerializer
    pagination_class = StandardResultSetPagination
    #https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    #https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['completed']
    #Default ordering
    ordering = ['completed', '-created_at']

    def get_queryset(self):
        user = self.request.user
        completed = self.request.query_params.get('completed')
        priority = self.request.query_params.get('priority')
        category = self.request.query_params.get('category')

        query_params = {}
        if completed is not None:
            query_params["completed"] = completed
        if priority is not None:
            query_params["priority"] = priority
        if category is not None:
            query_params["category"] = category
        return Task.objects.filter(created_by=user, **query_params)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DashboardTaskCompletionStatViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user = self.request.user
        #https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        queryset = Task.objects.filter(created_by=request.user).values('completed').annotate(count=Count('completed'))
        serializer = DashboardTaskCompletionStatSerializer(queryset, many=True)
        return Response(serializer.data)

class DashboardTaskByCategoryViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        print(self.request.user)
        user = self.request.user
        task_filters = {}
        completed = self.request.query_params.get('completed')
        if completed is not None:
            task_filters['tasks__completed'] = completed
        queryset = Category.objects.filter(created_by=user).annotate(count=Count('tasks', filter=Q(**task_filters)))

        serializer = DashboardTaskByCategorySerializer(queryset, many=True)
        return Response(serializer.data)