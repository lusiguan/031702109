import json
import re
import collections
# -*- coding: UTF-8 -*-

name=""
tel=""
mes=input()
tel=re.search(r'(\d{11})', mes).group()
mes_notel=re.sub(r'(\d{11})',"", mes)

name=re.search(r'(.+?),', mes_notel).group()
name_num=re.search(r'(\d)', name).group()
name=name.replace(name_num,"")
name=name.replace(',',"")
name=name.replace('!',"")

mes_addr=re.sub(r'(.+?),',"", mes_notel)

province=re.search(r'(.+?省)|(.+?自治区)|(.*?北京)|(.*?上海)|(.*?天津)|(.*?重庆)', mes_addr)
if province != None :
    province=re.search(r'(.+?省)|(.+?自治区)|(.*?北京)|(.*?上海)|(.*?天津)|(.*?重庆)', mes_addr).group()
    mes_two_addr=re.sub(r'(.+?省)|(.+?自治区)',"",mes_addr)
else:
    mes_two_addr=mes_addr

city=re.search(r'(.+?市)|(.*?北京)|(.*?上海)|(.*?天津)|(.*?重庆)', mes_two_addr)
if city != None :
    city=re.search(r'(.+?市)|(.*?北京)|(.*?上海)|(.*?天津)|(.*?重庆)', mes_two_addr).group()
    mes_three_addr=re.sub(r'(.+?市)|(.*?北京)|(.*?上海)|(.*?天津)|(.*?重庆)',"", mes_two_addr)
else :
    mes_three_addr=mes_two_addr

county=re.search(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)|(.+?旗)|(.+?自治旗)|(.+?林区)', mes_three_addr)
if county != None :
    county=re.search(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)|(.+?旗)|(.+?自治旗)|(.+?林区)', mes_three_addr).group()
    mes_four_addr=re.sub(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)|(.+?旗)|(.+?自治旗)|(.+?林区)',"", mes_three_addr)
else :
    mes_four_addr=mes_three_addr

stress=re.search(r'(.+?苏木)|(.+?民族苏木)|(.+?镇)|(.+?乡)', mes_four_addr)
if stress != None :
    stress=re.search(r'(.+?镇)|(.+?乡)|(.+?苏木)|(.+?民族苏木)', mes_four_addr).group()
    mes_five_addr=re.sub(r'(.+?镇)|(.+?乡)|(.+?苏木)|(.+?民族苏木)',"", mes_four_addr)
else :
    mes_five_addr=mes_four_addr

road=re.search(r'(.+?路)|(.+?巷)|(.+?街)|(.+?街道)', mes_five_addr)
if road != None :
    road=re.search(r'(.+?路)|(.+?巷)|(.+?街)|(.+?街道)', mes_five_addr).group()
    mes_six_addr=re.sub(r'(.+?路)|(.+?巷)|(.+?街)|(.+?街道)',"", mes_five_addr)
else :
    mes_six_addr=mes_five_addr

num=re.search(r'(.+?号)', mes_six_addr)
if num != None :
    num=re.search(r'(.+?号)', mes_six_addr).group()
    num=num.replace('.',"")
else :
    num=None

if province != None :
    mes_new_addr=province
else :
    province=""
    mes_new_addr=province

if city != None :
    mes_new_addr=mes_new_addr+' '+city
else:
    city=""
    mes_new_addr=mes_new_addr+' '+city

if county != None :
    mes_new_addr=mes_new_addr+' '+county
else:
    county=""
    mes_new_addr=mes_new_addr+' '+county

if stress != None :
    mes_new_addr=mes_new_addr+' '+stress
else:
    stress=""
    mes_new_addr=mes_new_addr+' '+stress

if road != None :
    mes_new_addr=mes_new_addr+' '+road
else:
    road=""
    mes_new_addr=mes_new_addr+' '+road

if num != None :
    mes_new_addr=mes_new_addr+' '+num

mes_new_addr=mes_new_addr.split(" ")
dictionary=collections.OrderedDict()
dictionary["姓名"]=name
dictionary["手机"]=tel
dictionary["地址"]=mes_new_addr

js=json.dumps(dictionary,ensure_ascii=False)

print(js)



