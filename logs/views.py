from django.shortcuts import render, HttpResponse

# Create your views here.
def get_log_list(request):
    return render(request, 'logs/my_page.html')