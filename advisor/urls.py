"""advisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from advisor_app import views as advisor_app_views
import advisor_app

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/advisor/', advisor_app_views.advisor_list),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', advisor_app_views.RegisterView.as_view(), name='auth_register'), 
    path('user/<int:user_id>/advisor/', advisor_app_views.get_list_of_advisors),
    path('user/<int:user_id>/advisor/<int:advisor_id>/', advisor_app_views.book_advisor),
    path('user/<int:user_id>/advisor/booking/', advisor_app_views.get_booked_calls),
]
