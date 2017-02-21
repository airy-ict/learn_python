from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
user_list = [
    {'username': '刘备', 'pwd': 'liuxuande'},
    {'username': '关羽', 'pwd': 'guanerye'},
    {'username': '张飞', 'pwd': 'zhangyide'}
]

def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("Hello World")
    if request.method == 'POST':
        username = request.POST.get('username', None)
        userpwd = request.POST.get('userpwd', None)
        templist={'username': username, 'pwd': userpwd}
        user_list.append(templist)

    return render(request, "index.html", {'data': user_list})
