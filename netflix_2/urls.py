from django.urls import path, include
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet#,MovieActorAPIView,CommentAPICreate,CommentAPIList,CommentAPIDelete
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Movie Application Rest API',
        default_version='v1',
        description='Swagger docs for Rest API',
        contact=openapi.Contact('Orifjon Ziyodullayev <orifziyodullaev@gmail.com>'),
    ),
        public = True,
        permission_classes=(permissions.AllowAny,)

    )



router = DefaultRouter()
router.register('movies',MovieViewSet)
router.register('actors',ActorViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name='swagger-docs'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='redoc-docs')
   # path('movies/<int:id>/actors/',MovieActorAPIView.as_view(),name='movie-actor'),

   # path('auth/comment/',CommentAPIList.as_view(),name='comment'),
   # path('auth/comment/create/',CommentAPICreate.as_view(),name='create'),
   # path('auth/comment/delete/<int:pk>/',CommentAPIDelete.as_view(),name='delete'),
    #path('api-token-auth/',views.obtain_auth_token),
]