#!/usr/bin/env python
# -*- coding: utf-8 -*-

_BLANK_STRING = [' ', '\n', '\t', '\r']

_NICKNAME_OUT = ['|', '海神', '樱花', '策划', '程序', '文案', '系统', '战斗', 'X22', 'X21', '\n', ' ', '\r', '\t']

def IsBlank(content):

    if (content is None) or content == '':
        return True

    for c in content:
        if not (c in _BLANK_STRING):
            return False

    return True

def ParsingNickname(nickname):
    import re

    # 带括号名字，括号内即为姓名 @LorryKane(刘云凯) 
    if ('(' in nickname) and (')') in nickname:
        name = re.findall(r'[(](.*?)[)]', nickname)[0]
        return name

    # 不带括号，进行剔除
    name = nickname
    for key in _NICKNAME_OUT:
        name = name.replace(key, '')
    
    return name
    