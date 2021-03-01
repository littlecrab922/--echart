#coding:utf-8
import shutil
import os
import re
from tkinter import _flatten

readDir=r"D:\datamining\master.txt"
writeDir=r"D:\datamining\country.csv"
write={}
CountrySet=set()

def CollectCountry():
    readf=open(readDir,'r',encoding='utf-8-sig')
    for line in readf:
        curline = line.split(',')#每一行转为列表
        suicides_no=int(curline[4])
        if curline[0] not in CountrySet:
            CountrySet.add(curline[0])
            write[curline[0]]=suicides_no
        else:
            write[curline[0]]=write[curline[0]]+suicides_no
    readf.close()

def write_it():
    writef=open(writeDir,'w',encoding='utf-8')
    for key,value in write.items():
        writeLine=key+','+str(value)+'\n'
        writef.write(writeLine)
    writef.close()

CollectCountry()
write_it()