from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework import filters

# List and Create Notes
class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Fetch Note by ID
class NoteDetailView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Query Notes by Title Substring
class QueryNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            return Note.objects.filter(title__icontains=title_substring)
        return Note.objects.all()

# Update Note
class UpdateNoteView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
