#!/usr/bin/env python
# -*- coding: utf-8 -*-
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4]
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]
T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

from math import sqrt

def moyenne1():
	somme = 0
	for i in L1:
		somme+=i
		moy1=sum(L1)/len(L1)
	print("moy1",moy1)
moyenne1()

def moyenne2():
	somme = 0
	for i in L2:
		somme+=i
		moy2=sum(L2)/len(L2)
	print("moy2",moy2)
moyenne2()

def sigma(L1):
	mean = sum(L1)/len(L1)
	var = sum((l-mean)**2 for l in L1) / len(L1)
	ecart = sqrt(var)
	return ecart
ecart=sigma(L1)
print("ecart1",ecart)
	
def sigma(L2):
	mean2 = sum(L2)/len(L2)
	var2 = sum((i-mean2)**2 for i in L2) / len(L2)
	ecart2 = sqrt(var2)
	return ecart2
ecart2=sigma(L2)
print("ecart2",ecart2)

