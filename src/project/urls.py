from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email as allauthemailconfirmation
from django.urls import path, re_path
from allauth.account.views import confirm_email
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/', confirm_email, name='account_confirm_email'),
    path('admin/', admin.site.urls),
    path('api/', include('blogs.api.urls'))
]
