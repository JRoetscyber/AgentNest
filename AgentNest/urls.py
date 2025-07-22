"""
URL configuration for AgentNest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Import these for custom error views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('apps.leads.urls', namespace='leads')), # Include URLs from the leads app
]

# Define custom error handlers
handler404 = 'AgentNest.views.custom_404'
handler500 = 'AgentNest.views.custom_500'
handler403 = 'AgentNest.views.custom_403'

# Add static files handling for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # For testing error pages in development
    urlpatterns += [
        path('404/', TemplateView.as_view(template_name='404.html')),
        path('500/', TemplateView.as_view(template_name='500.html')),
        path('403/', TemplateView.as_view(template_name='403.html')),
    ]