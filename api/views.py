
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .serializers import profileSerializer
from .models import Note
from .models import profiles
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },

        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns an single note object'
        },
        {
            'Endpoint':'/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in'
        },
        {
            'Endpoint':'/notes/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        }
    ]
    return Response(routes)
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all() #sqldata
    serializer=NoteSerializer(notes,many=True)  #converts sql data stored to python
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)  #from database
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(
        body=data['body'] 
    )
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    note = Note.objects.get(id=pk)
    serializer=NoteSerializer(note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')


#ADDED EXTRA VIEW
@api_view(['GET'])
def getprofiles(request):
    profile = profiles.objects.all()  # from database
    serializer = profileSerializer(profile, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createprofile(request):
    data = request.data
    note = profiles.objects.create(
        email=data['email'],
        password=data['password'],
        name=data['name'],
        address=data['address'],
        phone=data['phone'],
        workingHours=data['workingHours'],
        city=data['city'],
        uid=data['uid'],


    )
    serializer = profileSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getprofile(request, e):
    profile = profiles.objects.get(email=e)  # from database
    serializer = profileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getcities(request):
    profile = profiles.objects.all()  # from database
    serializer = profileSerializer(profile, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getIns_city(request,city):
    profile = profiles.objects.filter(city__iexact=city)  # from database
    serializer = profileSerializer(profile, many=True)
    return Response(serializer.data)







