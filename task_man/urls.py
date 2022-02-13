"""task_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

from users import views as user_v
from tasks import views as tasks_v


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", user_v.register, name="register"),
    path("", tasks_v.index, name="index"),
    path("create-task", tasks_v.create_task, name="create-task"),
    path("mark_done/<int:task_id>", tasks_v.mark_done, name="mark_done"),
]
