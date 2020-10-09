from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
	path('', views.home, name="home"),
    path('search', views.search, name="search"),
    path('About_book/<int:id>', views.read, name="read"),
    path('like/<int:pk>', views.like_book, name="like_book"),
    path('comment_remove/<int:id>', views.remove_comment, name="remove_comment"),
    path('comment_reply_remove/<int:id>', views.remove_comment_reply, name="comment_reply_remove"),
    path('read_book/<int:id>', views.read_book, name="read_book"),
    path('favorite/<int:pk>', views.favorite_book, name="favorite_book"),
    path('show_favorite', views.show_favorite, name="show_favorite"),
    path('favorite_book/<int:id>', views.favorite_book, name="favorite_book"),
    path('About_book/<int:id>/comment', views.AddCommentView.as_view(), name='add_comment'),
    path('About_book/<int:id>/commentReply', views.AddCommentReplyView.as_view(), name='reply_comment'),
    path('About_book/comment/<int:id>', views.show_replys, name="show_replys"),
]

# if settings.DEBUG:
# 	urlpatterns += staticfiles_urlpatterns()
