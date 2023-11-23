from django.urls import include, path
from rest_framework import routers
from .views import EventViewSet, ParticipantViewSet
#get an instance of the router defined in rest_framework
router=routers.DefaultRouter()
#add product urls (get,post,put,delete) to the router
router.register(r'products',ParticipantViewSet,basename='participant')
router.register(r'clients',EventViewSet,basename='event')
#add address urls (get,post,put,delete) to the router

urlpatterns = [
    #path is used to define a new router
    #include is used to include the urls defined in the router
    #Urls defined in the router are:
    #http://localhost:8000/ecommerce/products/ => get all products (GET method)
    #http://localhost:8000/ecommerce/products/1/ => get the product with id=1 (GET method)
    #http://localhost:8000/ecommerce/products/ => post a new product (POST method)
    #http://localhost:8000/ecommerce/products/1/ => put the product with id=1 (PUT or PATCH method)
    #http://localhost:8000/ecommerce/products/1/ => delete the product with id=1 (DELETE method)
    #Same urls for clients
    path('',include(router.urls)),
    path('max_min_price/', ParticipantViewSet.as_view({'get': 'max_min_price'}), name='max_min_price'),
    #if we are on the 1st case (go to the views.py line 159)
    #path(r'<int:pk>/client_products/', CommandViewSet.as_view({'get': 'client_products'}), name='client_products'),
    path(r'client_products', ParticipantViewSet.as_view({'get': 'client_products'}), name='client_products'),
    path('not_satisfied/',ParticipantViewSet.as_view({'get':'not_satisfied_clients'})
         , name='not_satisfied_clients'),
]