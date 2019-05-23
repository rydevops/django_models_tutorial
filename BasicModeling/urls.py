from django.urls import path
from BasicModeling.views import IndexView

# Configure namespacing
app_name = "BasicModeling"

# Configure URL routing
urlpatterns = [    
    path('', IndexView.as_view(), name='index-view'),
]
