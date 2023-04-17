from django.shortcuts import render


def main_page(request):
    return render(request, 'education/main_page.html')
