from django.test import TestCase

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string_utils

if __name__ == "__main__":

    # str1xxx = ' hah    \n \t h \n'
    # str2xxx = ' \n \r \t'

    # v1xxx = string_utils.IsBlank(str1xxx)
    # v2xxx = string_utils.IsBlank(str2xxx)    

    # print('v1', v1xxx)
    # print('v2', v2xxx)

    str1 = 'LorryKane(刘云凯) '
    str2 = '海神|樱花|刘梦蝶'
    str3 = '罗皓'

    print(string_utils.ParsingNickname(str1))
    print(string_utils.ParsingNickname(str2))
    print(string_utils.ParsingNickname(str3))