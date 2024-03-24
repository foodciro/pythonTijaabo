from django.urls import path
from.import views


urlpatterns=[
    path('', views.apioverview, name='apioverview'),
    path('product-list/',views.ShowAll,name='product-deatil'),
    path('product-deatil/<int:pk>',views.viewproduct,name='product-list'),
    path('product-create/',views.Createproduct,name='product-create'),
    path('product-update/<int:pk>',views.Updateproduct,name='product-update'),
    path('product-delete/<int:pk>',views.deleteproduct,name='product-delete')
]