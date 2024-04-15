from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_task(request):
    request.data['user'] = request.user.id
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        enviar_email_tarefa_agendada(request.user, serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def tasklist(ListView):
    return HttpResponse('TO Do list')

from django.core.mail import send_mail
from django.conf import settings

def enviar_email_boas_vindas(usuario_email, usuario_name):
    assunto = 'Bem-vindo ao TODO list!!'
    mensagem = f'Olá! Obrigado por se inscrever no TODO list, {usuario_name}. Esperamos que você aproveite nossa plataforma.'
    remetente = settings.EMAIL_HOST_USER
    destinatario = [usuario_email]
    send_mail(assunto, mensagem, remetente, destinatario)


def enviar_email_tarefa_agendada(user, task_data):
    assunto = 'Tarefa Agendada!'
    mensagem = f'Olá! {user.username}, sua tarefa {task_data["title"]} foi agendada para {task_data["task_date"]}. Esperamos que você aproveite nossa plataforma.'
    remetente = settings.EMAIL_HOST_USER
    destinatario = [user.email]
    send_mail(assunto, mensagem, remetente, destinatario)   