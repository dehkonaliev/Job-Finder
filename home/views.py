from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        if request.user.role == 'employer':
            base_template = 'emp-base.html'
        return render(request, 'home.html', {'base_template': base_template})