from django.urls import path, include
from portafolio.views import PortafolioP, registro_userView, portafolioView


urlpatterns = [
    path('', PortafolioP.as_view(), name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/registro_user', registro_userView.as_view(),name='registro_user'),
    path('portafolioNew/', portafolioView.as_view(), name='portafolioNew'),
]

