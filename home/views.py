from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.role == 'employer':
                base_template = 'emp-base.html'
            
            return render(request, 'home.html', {'base_template': base_template})
        else:
            return redirect('login')