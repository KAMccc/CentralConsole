#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

import pymysql

from pprint import pprint

from . import string_utils, popo_utils

@csrf_exempt
def GetPopoResourcePost(request):
    # date = request.GET()
    # send_user=zhengdongke%40corp.netease.com
    # message=%25resourceget+%0D%0A1111111
    # group=1542560
    send_user = request.POST.get('send_user')
    message = request.POST.get('message').replace(" ", "")[9:]
    group = request.POST.get('group')

    content = message.split('@')[0]
    designers = message.split('@')[1:]

    # print('send_user:', send_user)
    # print('message:', message)
    # print('group:', group)
    # print('content:', content)
    # print('designers:', designers)

    # 内容为空
    if string_utils.IsBlank(content):
        popo_utils.ContentIsNullCallPopo(group, send_user)
        return HttpResponse(-1)
    
    # 没有@策划
    if len(designers) == 0:
        popo_utils.NoneDesignerCallPopo(group, send_user)
        return HttpResponse(-1)

    with connection.cursor() as cursor:
        sql = "SELECT * FROM designers WHERE nickname='%s';" % ('郑栋珂')
        cursor.execute(sql)
        res = cursor.fetchone()
        print('type ', type(res))
        pprint(res)

    
    offListDesigners = [] # 名单外的策划
    toTableDesigners = [] # 入库名单 [('zhengdongke@corp.netease.com', '郑栋珂')] 
    for designer in designers:
        name = string_utils.ParsingNickname(designer)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM designers WHERE nickname='%s'" % (name)
            cursor.execute(sql)
            res = cursor.fetchone()
        
        # res => <class 'tuple'>
        # ('zhengdongke@corp.netease.com', '郑栋珂')
        if res is None:
            offListDesigners.append(designer)
            continue

        # 校验名单，获取popo，表链接
        designer_popo = res[0]
        toTableDesigners.append(res)

        # 入库
        with connection.cursor() as cursor:
            sql = "INSERT INTO artresourceprogress (date, designer, initiator, content)" + \
            "VALUES (now(), '%s', '%s', '%s')" % (designer_popo, send_user, content)
            cursor.execute(sql)
    
    # popo提醒 - 策划不在名单内
    if len(offListDesigners) > 0:
        popo_utils.DesignerNotOnTheListCallPopo(group, send_user, offListDesigners)

    # popo提醒 - 入库
    if len(toTableDesigners) > 0:
        popo_utils.ToTableCallPopo(group, send_user, toTableDesigners, content)

    return HttpResponse(0)
