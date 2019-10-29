from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="Music, Artist 정보",
   ),
)

urlpatterns = [
    path('musics/', views.musics_index, name='music_index'),
    path('musics/<int:music_pk>/', views.detail, name='detail'),
    path('musics/<int:music_pk>/reviews/', views.review_create, name='review_create'),
    path('reviews/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
    path('artists/', views.artists_index, name='artists_index'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),

    path('redoc/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
    
]