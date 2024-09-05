from django.http import JsonResponse
from django.urls import path, include
from .views import NoteListCreateView, NoteDetailView, QueryNotesView, UpdateNoteView

def api_root(request):
    return JsonResponse({
        'message': 'Welcome to the Notes API!',
        'endpoints': {
            'list_create_notes': '/api/notes/',
            'query_notes': '/api/notes/query/',
            'note_detail': '/api/notes/{id}/',
            'update_note': '/api/notes/{id}/update/',
        }
    })

urlpatterns = [
    path('', api_root, name='api_root'),  # This will handle the /api/ route
    path('notes/', NoteListCreateView.as_view(), name='list_create_note'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/query/', QueryNotesView.as_view(), name='query_notes'),
    path('notes/<int:pk>/update/', UpdateNoteView.as_view(), name='update_note'),
]
