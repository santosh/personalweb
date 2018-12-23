from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^about/$', views.about),
    # uncomment below line if you wanna keep separate homepage
    # re_path(r'^$', views.home),
    # showing the blog content on the homepage
    re_path(r'^$', articles_views.article_list, name="home"),
    re_path(r'^articles/', include('articles.urls')),
    re_path(r'^accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
