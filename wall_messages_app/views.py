from django.shortcuts import render, HttpResponse, redirect
from first_app.models import User
from .models import Messages, Comments 

def index(request):
	if 'User' in request.session:
		logged_User = User.objects.get(id=request.session['User'])
		request.session['User'] = logged_User.id
		context = {
		"logged_User" : logged_User,
		"all_messages": Messages.objects.all(),
		"all_comments":Comments.objects.all(),
		"all_posters":User.objects.all()		
		}
		return render(request, 'index.html', context)
	else:
		print('user must be logged in') 
		return redirect('/')

def post_message(request):
	Messages.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['User']))
	return redirect('/wall')

def comment(request):
	user = User.objects.get(id=request.session['User'])
	message = Messages.objects.get(id=request.POST['message'])

	Comments.objects.create(comment=request.POST['comment'], user=user, message=message)
	return redirect('/wall')

def delete_message(request, message_id):
	delete_message = Messages.objects.get(id=message_id)
	delete_message.delete()
	return redirect('/wall')

	
	
	# poster = User.objects.get(id=request.session['User'])
	
	# message = Messages.objects.get(id=request.POST['message'])

	# Comments.objects.create(comment=request.POST['comment'], user=user, message=message)

