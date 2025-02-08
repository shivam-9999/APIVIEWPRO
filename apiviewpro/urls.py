
from django.contrib import admin
from django.urls import path
from apiapp.views import ProductListCreateAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('products/', ProductListCreateAPIView.as_view(), name='pr_l_cr'),
]
