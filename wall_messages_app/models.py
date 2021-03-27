from django.db import models
from first_app.models import User

class Messages(models.Model):
	message = models.TextField()
	user = models.ForeignKey(User, related_name='messages', on_delete = models.CASCADE)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now= True)

class Comments(models.Model):
	comment = models.TextField()
	user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
	message = models.ForeignKey(Messages, related_name='message_comment', on_delete = models.CASCADE)
	created_at= models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now = True)

	