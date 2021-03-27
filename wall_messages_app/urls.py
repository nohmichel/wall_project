from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('messages/create', views.post_message),
	path('messages/comment', views.comment), 
	path('delete_message/<int:message_id>', views.delete_message, name="delete_message")

]