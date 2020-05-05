from django.urls import path,include
from home import views
# from .views import PostDetailView
# from django.views.generic import ListView,DetailView
from django.conf import settings

urlpatterns=[
    path('',views.index,name="index"),
    path('reviews',views.reviews,name="reviews"),
    # path('reviews/<int:pk>/',PostDetailView.as_view()),
    path('', include('social_django.urls', namespace='social')),
    path('logout',views.logout,name="logout"),  
    path('login',views.login,name="login"),
    path('free-plan',views.freePlan,name="freePlan"),
    path('paid-plan',views.paidPlan,name="paidPlan"),
]