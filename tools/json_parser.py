#!/usr/bin/python3

#----------------------------------------------------
# File name     : json_parser.py
# Despription   : JSON Parser
# Author        : Romconstruct
# E-mail        : mail@romconstruct.org
# Website       : www.romconstruct.org
# Date          : 2018/02/08
#----------------------------------------------------

import json
from pprint import pprint

'''
Example:
workingDir = os.getcwd()
filePath = os.path.join(os.path.sep, workingDir, 'data', 'json', 'char.json')

data = jsonData.readJSONFile(filePath)
'''

class jsonData(object):

    @classmethod
    def readJSONFile(cls, path):
        with open(path, 'rU', encoding='utf-8') as jFile:
            resp = json.loads(jFile.read())
        pprint(resp)
        return resp
