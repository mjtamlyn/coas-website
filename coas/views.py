from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Clubs(TemplateView):
    template_name = 'clubs.html'
