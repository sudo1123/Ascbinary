# -*- coding: UTF-8 -*-
# Copyright (c) 2025 QU QI
# MIT Licensed (https://opensource.org/licenses/MIT)
import json
with open ("locals.json","r",encoding="utf-8") as l:
    locals=json.load(l) 
with open ("ascii_char_to_binary.json","r") as a:
    map=json.load(a)
lan_selection=input("请选择界面语言（1代表中文,2代表英文）Please select interface language (1 for Chinese, 2 for English):")
if lan_selection=="1":
    lan="CN"
if lan_selection=="2":
    lan="EN"
mode_selection=input(locals[lan]["mode_selection"])
output=[]
if mode_selection=="1":
    original_text=input(locals[lan]["ascii_binary_input"])
    for letter in original_text:
        for key in map.keys():
            if letter==key:
                output.append(map[key])
if mode_selection=="2":
    original_binary=input(locals[lan]["binary_ascii_input"])
    original_binary_list=original_binary.split(" ")
    for binary in original_binary_list:
        for key,value in map.items():
            if value==binary:
                output.append(key)
print(locals[lan]["output"]+str(output))