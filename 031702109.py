import json
import re
import collections
# -*- coding: UTF-8 -*-

mes=input("message:")
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

county=re.search(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)', mes_three_addr)
if county != None :
    county=re.search(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)', mes_three_addr).group()
    mes_four_addr=re.sub(r'(.+?区)|(.+?自治州)|(.+?自治县)|(.+?县)',"", mes_three_addr)
else :
    mes_four_addr=mes_three_addr

stress=re.search(r'(.+?街)|(.+?镇)|(.+?乡)', mes_four_addr)
if stress != None :
    stress=re.search(r'(.+?街)|(.+?镇)|(.+?乡)', mes_four_addr).group()
    home=re.sub(r'(.+?街)|(.+?镇)|(.+?乡)',"", mes_four_addr)
    home=home.replace('.',"")
else :
    home=mes_four_addr

if province != None :
    mes_new_addr=province
if city != None :
    mes_new_addr=mes_new_addr+' '+city
if county != None :
    mes_new_addr=mes_new_addr+' '+county
if stress != None :
    mes_new_addr=mes_new_addr+' '+stress
if home != None :
    mes_new_addr=mes_new_addr+' '+home

mes_new_addr=mes_new_addr.split(" ")
dictionary=collections.OrderedDict()
dictionary["姓名:"]=name
dictionary["手机:"]=tel
dictionary["地址:"]=mes_new_addr
js=json.dumps(dictionary,ensure_ascii=False)
print(js)
