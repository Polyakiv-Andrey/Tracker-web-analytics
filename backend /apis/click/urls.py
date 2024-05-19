from django.urls import path
from apis.click.views import ClickCreateListAPIView, ClickRetrieveAPIView

urlpatterns = [
    path('clicks/', ClickCreateListAPIView.as_view(), name='click-list-create'),
    path('clicks/<int:pk>/', ClickRetrieveAPIView.as_view(), name='click-retrieve'),
]

app_name = "click"
