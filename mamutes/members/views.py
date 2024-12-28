from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TaskForm
from .models import MembroEquipe

from rest_framework import viewsets
from .models import Column, Task
from .serializers import ColumnSerializer, TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
def sidebar(request):
    members = MembroEquipe.objects.all()
    return render(request,"partials/_sidebar.html", {'members':members})

def Top(request):
    return render(request, 'partials/Top.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sidebar')   
        else:
            members = MembroEquipe.objects.all()
            return render(request, "partials/_sidebar.html", {'members':members})

    else:
        return redirect('sidebar')

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        column_id = self.request.query_params.get('column')
        if column_id:
            return self.queryset.filter(column_id=column_id)
        return self.queryset


def kanban_view(request):
    items = Task.objects.all()
    return render(request, 'kanbam.html',{'items': items})


@api_view(['PATCH'])
def update_task_status(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Log os dados recebidos
    print("Dados recebidos:", request.data)

    new_status = request.data.get('status')
    if not new_status:
        return Response({"error": "Status not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    task.status = new_status
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)
