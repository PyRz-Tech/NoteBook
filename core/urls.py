from django.urls import path
from .views import (
    dashboard,
    begin,
    logout_view,
    note_detail,
    capture_vibe,
    notes
    )


app_name='core'
urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('begin/', begin, name='begin'),
    path('logout/', logout_view, name='logout'),
    path('note_detail/<int:pk>/', note_detail, name='note_detail'),
    path('capture_vibe/', capture_vibe, name='capture_vibe'),
    path('notes/', notes, name='notes')
]
