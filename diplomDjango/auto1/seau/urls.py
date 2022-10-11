from django.urls import path

from .views import index, by_order, AutoCreateView, ClientCreateView, WorkCreateView, ProductCreateView, OrderCreateView

urlpatterns=[
    path('add/', AutoCreateView.as_view(), name='add'),
    path('add1/', ClientCreateView.as_view(), name='add1'),
    path('add2/', WorkCreateView.as_view(), name='add2'),
    path('add3/', ProductCreateView.as_view(), name='add3'),
    path('add4/', OrderCreateView.as_view(), name='add4'),
    path('<int:order_id>/', by_order, name='by_order'),
    path('', index, name='index'),
]