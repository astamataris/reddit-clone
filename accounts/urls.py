from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
    url(r'^signup/',views.signup, name="signup"),
    url(r'^login/',views.login_reddit, name="login_reddit"),
    url(r'^logout/',views.logout_reddit, name="logout_reddit"),
]
