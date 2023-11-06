from django.conf import settings #para img rota no usar fuera de development
from django.conf.urls.static import static #para img rota no usar fuera de development
from django.contrib import admin
from django.urls import path, include #importo includes tambien
from core.views import index, contact #importo el index.html y el contact

urlpatterns = [
    path('', include('core.urls')), #aca lo cambio a include y apunto al home declarado en core/urls.py
    path('dashboard/', include('dashboard.urls')), #rooteo las urls que declare en el urls.py de dashboard
    path('items/', include('item.urls')), #importo las urls de items con include
    #path('contact/', contact, name='contact'), #puesto en core/urls.py
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #agrego esta linea para las imagenes