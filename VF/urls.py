"""VF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.views.static import serve
import xadmin
from django.contrib import admin

from users.views import IndexView,LoginView,RegisterView,LogoutView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView
from .settings import MEDIA_ROOT#, STATIC_ROOT
from operation.views import BoardView,SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^board/$', BoardView.as_view(), name='board'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^captcha/', include('captcha.urls')),
	url(r'^tinymce/', include('tinymce.urls')),#富文本编辑框
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(),name='user_active'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(),name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetPwdView.as_view(),name='reset_pwd'),
    url(r'^modifypwd/$',ModifyPwdView.as_view(),name='modify_pwd'),
    url(r'^board/$', ModifyPwdView.as_view(), name='msg_board'),
    url(r'^video/', include('videos.urls',namespace='video')),
    url(r'^user/', include('users.urls', namespace='user')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root':MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT}),
]
