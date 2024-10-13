from django.urls import path
from . import views
from .views import TestView,MovieListView,RegisterView,UserCollectionView,CollectionViewUUID,RequestCounterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('test/',TestView.as_view(),name='test-endpoint'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/',MovieListView.as_view(),name='movie-list'),
    path('register/',RegisterView.as_view(),name='register'),
    path('collection/',UserCollectionView.as_view(),name='collection-list'),
    path('collection/<uuid:collection_uuid>/',CollectionViewUUID.as_view(),name='collection-details'),
    path('request-count/',RequestCounterView.as_view(),name="request-count"),
    path('request-count/reset',RequestCounterView.as_view(),name="request-count-reset")
]
