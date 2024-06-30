from django.views import generic
from django.views.generic import TemplateView
from .models import Articles

from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.translation import activate

# l'affichage de la page index qui va afficher les blogs
class ArticleList(generic.ListView):
    model = Articles
    template_name = 'index.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

# changer la langue
class SetLanguageView(View):
    def post(self, request):
        language = request.POST.get('language', 'fr')  # Langue par défaut 'fr' si non spécifiée
        request.session['django_language'] = language
        activate(language)  # Active la langue sélectionnée pour la session en cours
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# class ChatBotView(View):
#     def post(self, request):
#         user_message = request.POST.get('message')
#         chatbot = ChatBot(**settings.CHATTERBOT)
#         response = chatbot.get_response(user_message)
#         return JsonResponse({'response': response.text})        