from django.shortcuts import render, HttpResponse


def get_log_list(request):
    return render(request, 'logs/my_page.html')
