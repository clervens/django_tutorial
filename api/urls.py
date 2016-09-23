from . import views
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)
urlpatterns = router.urls
