from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProdutsListAPIView
from apps.products.api.views.products_view import ProductListApiView,ProductCreateApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name= 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='Indicator'),
    path('category_products/', CategoryProdutsListAPIView.as_view(), name='CategoryProduts'),
    path('product/list/', ProductListApiView.as_view(), name='product_list'),
    path('product/create/', ProductCreateApiView.as_view(), name='product_create'),
]