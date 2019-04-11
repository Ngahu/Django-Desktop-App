from django.shortcuts import render
from django.views import View

class HomeView(View):
    """
    Description:render homa page.\n
    """
    template_name = 'home/index.html'
    def get(self,request,*args, **kwargs):
        context = {}
        return render(request,self.template_name,context)
        

