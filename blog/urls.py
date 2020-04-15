from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
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
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]