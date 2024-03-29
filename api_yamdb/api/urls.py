from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet,
                    registration_api_view, take_confirmation_code_view)

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('users', UserViewSet, basename='users')
v1_router.register('categories', CategoryViewSet, basename='title_categories')
v1_router.register('genres', GenreViewSet, basename='title_genres')
v1_router.register('titles', TitleViewSet, basename='title_titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='title_reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='title_comments'
)
urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', registration_api_view),
    path('v1/auth/token/', take_confirmation_code_view),
]
