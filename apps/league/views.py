from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        template_name = 'home/home.html'
        return render(request, template_name)
