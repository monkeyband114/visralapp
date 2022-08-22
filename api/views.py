from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from . models import Note
from .serializers import NoteSerializer
from api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getLists(request):
    list = Note.objects.all().order_by('-updated')
    serialize = NoteSerializer(list, many=True)
    return Response(serialize.data)
    

@api_view(['GET'])
def getList(request, pk):
    list = Note.objects.get(id=pk)
    serialize = NoteSerializer(list, many=False)
    return Response(serialize.data)


@api_view(['POST']) 
def createList(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serialize = NoteSerializer(note, many=False) 
    return Response(serialize.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    list = Note.objects.get(id=pk)
    serialize = NoteSerializer(instance=list, data=data)
    
    if serialize.is_valid():
        serialize.save()
    
    
    return Response(serialize.data)
    
    
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    
    return Response('Note was deleted')