'''
Created on 6 mars 2021

@author: schav
'''
# -*- coding : utf-8 -*-

from django.shortcuts import render

def welcome(request):
    return render(request,'welcome.html')

def login(request):
    return render(request,'login.html')