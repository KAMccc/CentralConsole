#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

_OFF_LIST_DESIGNERS_REMINDERS = ['zhengdongke@corp.netease.com', 'hedapeng@corp.netease.com']

# 反馈内容为空
# 回复群聊
def ContentIsNullCallPopo(popo, send_user):
    mesg = '[美术资源进度跟踪]\n' \
            +send_user + '\n反馈内容为空!'
    _CallPopo(popo, mesg)

# 没@策划
# 回复群聊
def NoneDesignerCallPopo(popo, send_user):
    mesg = '[美术资源进度跟踪]\n' \
            + send_user + '\n当前没有@对应策划!'
    _CallPopo(popo, mesg)

# 策划不在名单内
# 回复群聊 ， 显示策划名字
# 提醒PMA
def DesignerNotOnTheListCallPopo(group, send_user, offListDesigners):
    
    # call - 1 to group
    mesgToGroup = "[美术资源进度跟踪]\n" \
                + "     ".join(offListDesigners) \
                + "     不在策划名单内"
    _CallPopo(group, mesgToGroup)

    mesgToReminder = "[美术资源进度跟踪]" \
                    + "\n有 @策划 不在策划名单内，请添加" \
                    + "\n群:" + group \
                    + "\n提交者： " + send_user \
                    + "\n不在策划名单内列表：" + "      ".join(offListDesigners)

    # call - 2 to reminders
    for reminder in _OFF_LIST_DESIGNERS_REMINDERS:
        _CallPopo(reminder, mesgToReminder)

# 正常入库，群里反馈， 提醒策划
def ToTableCallPopo(group, send_user, toTableDesigners, content):

    # call - 1 to group
    mesgToGroup = "[美术资源进度跟踪]\n" \
                    + "提交已记录\n"

    for designerTup in toTableDesigners:
        mesgToGroup += designerTup[1] + ' TODO：网页链接\n'

    _CallPopo(group, mesgToGroup)

    # call - 2 to designers
    mesgToDesigner = "[美术资源进度跟踪]" \
                    + "\n美术资源有更新啦~" \
                    + "\n" \
                    + "\n内容：" \
                    + content \
                    + "TODO：网页链接"
    for designerTup in toTableDesigners:
        _CallPopo(designerTup[0], mesgToDesigner)


def _CallPopo(popo, mesg):

    mesg = str(mesg).encode('utf-8')

    data = {
        'message': mesg,
        'popo': popo,
    }

    requests.post('http://192.168.46.10:8000/tools/send_popo_message/', data=data)