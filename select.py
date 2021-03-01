#coding:utf-8
import shutil
import os
import re
from tkinter import _flatten

readDir=r"D:\datamining\master.txt"
writeDir=r"D:\datamining\select.txt"
write={}
yearSet=set()

def Collect():
    readf=open(readDir,'r',encoding='utf-8-sig')
    for line in readf:
        curline = line.split(',')#每一行转为列表
        if curline[0] == "Oman":
            suicides_no=int(curline[4])
            popu_no=int(curline[5])
            year_no=int(curline[1])
            gdp_no=int(curline[10])
            if year_no not in yearSet:
                yearSet.add(year_no)
                write[year_no]={}
                write[year_no]["GDP"]=gdp_no
                write[year_no]["Suicide"]=suicides_no
                write[year_no]["Popu"]=popu_no
            else:
                write[year_no]['Suicide']=write[year_no]['Suicide']+suicides_no
                write[year_no]['Popu']=write[year_no]['Popu']+popu_no        
    readf.close()

def write_it():
    writef=open(writeDir,'w',encoding='utf-8')
    for key,value in write.items():
        suicide_100k=value['Suicide']/value['Popu']
        writeline='['+str(key)+','+str(value["GDP"])+','+str(suicide_100k)+']'+','+'\n'
        writef.write(writeline)
    writef.close()

Collect()
write_it()