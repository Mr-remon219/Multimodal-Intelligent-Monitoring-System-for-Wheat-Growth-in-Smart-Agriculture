from django.http import HttpResponse

def index(request):
    file = open("web_page/page.txt", "r+")
    page = file.read()
    file.close()
    return HttpResponse(page)
