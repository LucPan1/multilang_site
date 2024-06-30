from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('set-language/', views.SetLanguageView.as_view(), name='set_language'),
    # path('chat/', views.ChatBotView.as_view(), name='chat')
]