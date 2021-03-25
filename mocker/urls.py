from django.conf.urls import url

from mocker import views

urlpatterns = [
    url(r'^clicks/$', views.click_count, name="click_count"),
    url(r'^get_users', views.get_users, name="get_users")
]