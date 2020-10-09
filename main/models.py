from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Books(models.Model):
	# user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booklist", null=True)
	title = models.CharField(max_length=200)
	book = models.TextField()
	date_added = models.DateTimeField(default=timezone.now)
	barcode = models.CharField(max_length=200)
	isbn = models.CharField(max_length=200)
	book_image = models.ImageField(upload_to="book_images", blank=True)
	author = models.CharField(max_length=200)
	likes = models.ManyToManyField(User, related_name="book_name", blank=True)
	favorite = models.ManyToManyField(User, related_name="favorite_book", blank=True)
	

	def __str__(self):
		return f"Books('{self.title}','{self.author}', '{self.date_added}')"

	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse('home')

class Comments(models.Model):
	book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="comments", null=True)
	title = models.CharField(max_length=200, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_user", null=True)
	comments = models.TextField(help_text="Write your comment here",blank=True)
	date_added = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name="comments_likes", blank=True)

	def __str__(self):
		return f"Comments( '{self.user.username}','{self.book}', '{self.date_added}')"

class CommentsReplys(models.Model):
	comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="comment_reply", null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_user", null=True)
	reply = models.TextField(help_text="Write your comment here",blank=True)
	date_replied = models.DateTimeField(default=timezone.now)
	likes = models.ManyToManyField(User, related_name="comments_reply_like", blank=True)
	def __str__(self):
		return f"Comment Replys( '{self.comment.user.username}','{self.reply}', '{self.date_replied}')"


# '{self.book.title}',
class BuyBook(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book_name = models.CharField(max_length=200)
	telephone = models.IntegerField()
	date_purchased = models.DateTimeField(default=timezone.now)
	address = models.CharField(max_length=100)
	card_no = models.IntegerField()

	def __str__(self):
		return (f"Buy('{self.book_name}','{self.telephone}','{self.date_purchased}','{self.address}','{self.card_no}',)")