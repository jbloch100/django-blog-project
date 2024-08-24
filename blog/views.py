from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Post
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm

# Restricting access to superusers only
def superuser_required(user):
	return user.is_superuser

def post_list(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		post = Post(title=title, content=content, author=request.user)
		post.save()
		return redirect('post_detail', pk=post.pk)
	return render(request, 'blog/post_form.html')

# Restricting edit and delete access to post authors or staff members
@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)

	# Check if the user is the author of the post or a staff member
	if request.user != post.author and not request.user.is_staff:
		return HttpResponseForbidden("You are not allowed to edit this post.")
		
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_form.html', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
	post = get_object_or_404(Post, pk=pk)

	# Check if the user is the author of the post or a staff member
	if request.user != post.author and not request.user.is_staff:
		return HttpResponseForbidden("You are not allowed to delete this post")
	if request.method == 'POST':
		post.delete()
		return redirect('post_list')
	return render(request, 'blog/post_confirm_delete.html', {'post': post})

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)	# Create user object but don't save to the database yet
			user.is_staff = False # Ensure the user is not a staff member
			user.is_superuser = False # Ensure the user is not a superuser
			user.save()	# Save the user to the database
			return redirect('login')	# Redirect to the login page after successful sign-up
	else:
		form = UserCreationForm()
		
	# Always return the render function, even if the form is not valid or it's a GET request
	return render(request, 'registration/signup.html', {'form': form})
