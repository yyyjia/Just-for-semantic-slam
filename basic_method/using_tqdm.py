#!/usr/bin/python
#coding:utf-8

#tqdm (显示循环的进度条)
import time
from tqdm import *
for i in tqdm(range(1000)):
    time.sleep(.02)    #进度条每0.1s前进一次，总时间为1000*0.1=100s
