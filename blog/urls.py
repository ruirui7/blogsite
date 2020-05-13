from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static#重要
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns#重要
# import debug_toolbar



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/app')),
    path('app/', include('app.urls')),
    path('clientapp/', include('clientapp.urls')),
]

# if settings.DEBUG:
# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	# urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]