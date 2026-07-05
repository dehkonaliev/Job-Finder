from .views import LoginView, UserUpdateView, SignUpView,  logout_view, UserDeleteView, ProfileView
from django.urls import path

urlpatterns = [
    path('my-profile/<slug:username>', ProfileView.as_view(), name='my-profile'),
    path('logout', logout_view, name='logout'),
    path('update-profile', UserUpdateView.as_view(), name='update-profile'),
    path('sing-up', SignUpView.as_view(), name='sign-up'),
    path('login', LoginView.as_view(), name='login'),
    path('delete-account', UserDeleteView.as_view(), name='delete-account')
]