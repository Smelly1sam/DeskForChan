#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  GUI.py
#  
#  Copyright 2015 bran <bran@bran-Satellite-C55-B>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

a = False
v = False
vg = False
varB = [a,v,vg]
lstB = ['a','v','vg']
print a
#imports

import configparser

#read in config
config = configparser.ConfigParser()
print config.read('settings.txt')

a = config.getboolean('Boards','a')
print a

#getting default values
for x in range(len(lstB)):
	varB[x] = config.getboolean('Boards',lstB[x])
	print varB[x]
	
#setting = open('settings.txt','r+')
#print setting





