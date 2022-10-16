from blog import views as blog_views
from django import urls
from rest_framework import routers

urlpatterns = [
    urls.path("post/", blog_views.PostListCreateView.as_view()),
    urls.path("post/<int:pid>/", blog_views.PostRetrieveUpdateDestroyView.as_view()),
    urls.path("post/<int:pid>/comment/", blog_views.CommentListCreateView.as_view()),
    urls.path(
        "post/<int:pid>/comment/<int:cid>/",
        blog_views.CommentUpdateDestroyView.as_view(),
    ),
]
