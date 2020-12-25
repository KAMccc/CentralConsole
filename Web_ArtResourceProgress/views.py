#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Designers, ResourcesDetails

def IndexView(request):

    designers = Designers.objects.all()

    return render(request, "ARP.html", {'designers': designers})
    # return HttpResponse("Welcome to the Web_ArtResourceProgress! _ kam")


def Detailds(request):
    
    popo_mail = request.GET.get('popo_mail')
    nickname = request.GET.get('nickname')
    db = ResourcesDetails.objects.all()

    count = db.filter(designer= popo_mail).count()
    table = db.filter(designer= popo_mail)

    # print("m type ", type(m))
    context = {
        "designer" : popo_mail,
        "count" : count,
        "table": table,
        "nickname": nickname,
    }

    return render(request, "detail.html", context= context)

def DetaildPost(request):
    print("request.body={}".format(request.body))