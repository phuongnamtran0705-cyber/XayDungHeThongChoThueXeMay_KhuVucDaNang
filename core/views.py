from django.http import HttpResponse


def home(request):
    return HttpResponse("RentMTB - He thong cho thue xe may khu vuc trung tam Da Nang")
