from django.urls import path

from .views import (ProductListView, ProductDetailView, CategoryListView, CategoryDetaileView,
                    FileListView, FileDetaileView
                    )


urlpatterns = [

    path('categories/', CategoryListView.as_view(), name= 'category_list'),
    path('categories/<int:pk>/', CategoryDetaileView.as_view()),

    path('products/', ProductListView.as_view(), name= 'product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name= 'product-detail'),
    path('products/<int:product_id>/files/', FileListView.as_view(), name= 'file_list' ),
    path('products/<int:product_id>/files/<int:pk>/', FileDetaileView.as_view(), name= 'file_detaile')

]