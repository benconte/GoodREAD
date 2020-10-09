from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Books, Comments, CommentsReplys
from .forms import CommentForm, CommentReplyForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def error_404_view(request, exception):
	return render(request, 'main/404.html')


def home(request):
	context = {"context":Books.objects.all()}
	return render(request, "main/home.html", context)



def search(request):
	# context = {"context":Books.objects.all()}
	
	if request.method == "GET":
		query = request.GET.get('q')


		if query:
			match = Books.objects.filter(title__icontains=query)
			

			if match:
				print("match found")
				context = {'match': match,
							'length': len(match),
						  }
				return render(request, "main/search.html", context)
			else:
				messages.warning(request, 'no results found')
				print(dir(messages))
				return HttpResponseRedirect("/")

		else:
			messages.warning(request, 'Enter a search')
			return HttpResponseRedirect('/')

	return HttpResponseRedirect('/')


def like_book(request, pk):
	book = get_object_or_404(Books, id=request.POST.get('book_id'))#getting the book which takes the like
	liked = False
	if book.likes.filter(id=request.user.id).exists():#check if the like has been liked by a specific user
		book.likes.remove(request.user)
		liked = False
	else:
		book.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('read', args=[str(pk)]))

def favorite_book(request, id):
	book = get_object_or_404(Books, id=id)
	if book.favorite.filter(id=request.user.id).exists():
		book.favorite.remove(request.user)

	else:
		book.favorite.add(request.user)

	return HttpResponseRedirect(reverse('read', args=[str(id)]))


@login_required
def show_favorite(request):

	return render(request, 'main/favorite.html', {})


def read(request, id):
	bk = Books.objects.get(id=id)
	# comment = Comments.objects.all()
	if bk:
		stuff = get_object_or_404(Books, id=id)
		total_likes = stuff.total_likes()
		liked = False
		is_favorite = False

		if stuff.favorite.filter(id=request.user.id).exists():
			is_favorite = True

		
		if stuff.likes.filter(id=request.user.id).exists():
			liked = True

		context = {
			'read':bk,
			'total_likes':total_likes,
			'liked': liked,
			'is_favorite': is_favorite,
			# 'comment': comment
			}
		return render(request, "main/display.html", context)

@login_required
def read_book(request, id):
	bk = Books.objects.get(id=id)
	if bk:
		stuff = get_object_or_404(Books, id=id)
		total_likes = stuff.total_likes()
		liked = False
		is_favorite = False

		if stuff.favorite.filter(id=request.user.id).exists():
			is_favorite = True

		
		if stuff.likes.filter(id=request.user.id).exists():
			liked = True

		context = {
			'read':bk,
			'total_likes':total_likes,
			'liked': liked,
			'is_favorite': is_favorite
			}
		return render(request, "main/book.html", context)


# @login_required
class AddCommentView(LoginRequiredMixin,CreateView):
	model = Comments
	form_class = CommentForm
	# fields = '__all__'
	template_name = 'main/add_comment.html'

	def form_valid(self, form):
		form.instance.book_id = self.kwargs['id']
		form.instance.user = self.request.user
		return super().form_valid(form)

	success_url = reverse_lazy('home')


# @login_required
class AddCommentReplyView(LoginRequiredMixin,CreateView):
	model = CommentsReplys
	form_class = CommentReplyForm
	# fields = '__all__'
	template_name = 'main/reply_comment.html'

	def form_valid(self, form):
		form.instance.comment_id = self.kwargs['id']
		form.instance.user = self.request.user
		return super().form_valid(form)

	success_url = reverse_lazy('home')

def remove_comment(request, id):
	# in this function you don't need to add verification because i added them in the template
	comment = get_object_or_404(Comments, id=id)

	if comment:
		comment.delete()
		messages.success(request, 'Comment deleted successfully')
		return HttpResponseRedirect('/')
	else:
		messages.warning(request, 'Can\'t delete comment')
		return HttpResponseRedirect('/')

def remove_comment_reply(request, id):
	# in this function you don't need to add verification because i added them in the template
	comment = get_object_or_404(CommentsReplys, id=id)

	if comment:
		comment.delete()
		messages.success(request, 'Comment deleted successfully')
		return HttpResponseRedirect('/')
	else:
		messages.warning(request, 'Can\'t delete comment')
		return HttpResponseRedirect('/')

# @login_required
# class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# 	model = Comments
# 	success_url = '/'

# 	def test_func(self):
# 		comment = self.get_object()
# 		if self.request.user == comment.user.username:
# 			return True
# 		return False


def show_replys(request, id):
	reply = Comments.objects.get(id = id)
	if reply:
		context = {
			'reply':reply
		}

		return render(request, "main/comment_replys.html", context)

	else:
		return redirect("home")

