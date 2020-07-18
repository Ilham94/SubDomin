#!/bin/python2.7
#-*- coding: utf-8 -*-
"""
Copyright (c) 2020 Dst
"""

import os, time, sys, json, re, requests
from var_animate import *

logo = banner('SUBDOMINAN','Ilham_Maulana','1.0 Scanner')
alert = animvar()
input = animinput()
## Coloring ##
c = color().show
me = c('red')
bi = c('blue')
i = c('green')
cy = c('cyan')
pu = c('white')
os.system('clear')
print(logo)
print('{}Team{}: {} t.me/config_Free1 \n').format(cy,me,pu)
host = input.ask('Host')
if 'www' in host:
    host = host.replace('www.','')
elif 'http://' in host:
    host = host.replace('http://','')
elif 'https://' in host:
    host = host.replace('https://','')

r = requests.get('https://api.hackertarget.com/hostsearch/?q='+host).text
if 'error check your search parameter' in r:
   time.sleep(1)
   print('\n'+alert.false('SALAH TOLOL'))
   time.sleep(1)
   exit()

scan = r.split('\n')
a = 1

for i in scan:
    rgx = re.search('(.*?),(.*)',i)
    print('{}   ---- {}{} {}----').format(bi,me,a,bi)
    try:
       print('{}Host{}: {}{}').format(cy,me,pu,rgx.group(1))
       print('{}Ip{}: {}{}').format(cy,me,pu,rgx.group(2))
    except AttributeError: pass
    a += 1
