from django.urls import path,include
from rest_framework import routers
from shubham import views

router= routers.DefaultRouter()
router.register(r'Users',views.Useviewset)
router.register(r'Group',views.Groupviewset)


urlpatterns = [
    
    path('',include(router.urls)),
    path('',include('rest_framework.urls'),namespace='rest_framework')
]


urlpatterns+= router.urls
