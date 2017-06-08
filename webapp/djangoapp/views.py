from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from djangoapp.models import Dreamreal, Online

from django.core.mail import send_mail
from django.http import HttpResponse
from webapp.tasks import do_something

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
        templist = {'username': username, 'pwd': userpwd}
        user_list.append(templist)
    return render(request, "index.html", {'data': user_list})


def hello(request):
    return redirect("http://www.baidu.com")
    # return render(request, "hello.html")


def article(request, articleId):
    return render(request, "article.html", {'data': articleId})


def articles(request, month, year):
    text = "Displaying articles of : %s/%s" % (year, month)
    return render(request, "article.html", {'data': text})


def block(request):
    # request.POST
    # request.GET
    # return HttpResponse("Hello World")
    return render(request, "block_template.html", {'data': user_list})


def crudops(request):
    # dreamreal = Dreamreal(
    #     website="www.polo.com",
    #     email="app@polo.com",
    #     name="polo",
    #     phone_number=1888888
    # )
    # # 新增数据
    # dreamreal.save()
    #
    # # 读取数据
    # objects = Dreamreal.objects.all()
    # res = "读取所有数据从DB:<br>"
    # for obj in objects:
    #     res += obj.name + "<br>"
    #
    # # 读取一条数据，where
    # polo = Dreamreal.objects.get(name="polo")
    # res += "读取一条数据：<br>" + polo.name
    #
    # # 删除一条数据
    # polo.delete()
    # res += "删除polo数据<br>"
    #
    # # 更新数据
    # dreamreal = Dreamreal(
    #     website="www.polo.com",
    #     email="app@polo.com",
    #     name="polo_update",
    #     phone_number=1888888
    # )
    # dreamreal.save()
    # res += "更新了一条数据<br>" + polo.name
    #
    # dreamreal = Dreamreal.objects.get(name="polo_update")
    # dreamreal.name = "polo_update_01"
    # dreamreal.save()

    # 删除所有数据
    # Dreamreal.objects.all().delete()

    # 外键
    onl1 = Online()
    onl1.domain = "site1.com"
    onl1.save()

    onl2 = Online()
    onl2.domain = "site2.com"
    onl2.save()

    dr1 = Dreamreal()
    dr1.name = "dr1_update"
    dr1.email = "dr1@sina.com"
    dr1.website = "www.dr1.com"
    dr1.phone_number = 144444
    dr1.online = onl1
    dr1.save()

    dr2 = Dreamreal()
    dr2.name = "dr2_update"
    dr2.email = "dr2@sina.com"
    dr2.website = "www.dr2.com"
    dr2.phone_number = 155555
    dr2.online = onl2
    dr2.save()

    res = "主外键关系建立<br>"

    onlObj = Dreamreal.objects.all()[0].online
    res += "主外键查询：domain：" + onlObj.domain + "，Id:" + str(onlObj.id) + "<br>"

    return HttpResponse(res)


def sendSimpleEmail(request,emailto):
    res = send_mail("hello paul", "comment tu vas?", "paul@yiibai.com", [emailto])
    return HttpResponse('%s' % res)

