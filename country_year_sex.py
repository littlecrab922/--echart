#coding:utf-8
import shutil
import os
import re
from tkinter import _flatten

readDir=r"D:\datamining\master.txt"
writeDir=r"D:\datamining\united_states_year_sex.csv"
writeYear={}
yearSet=set()

def Collect():
    readf=open(readDir,'r',encoding='utf-8-sig')
    for line in readf:
        curline = line.split(',')#每一行转为列表
        sex_no=int(curline[4])
        popu_no=int(curline[5])
        if curline[0] == "United States":
            year=int(curline[1])
            if year not in yearSet:
                yearSet.add(year)
                sex={}
                if curline[2] == "female":
                    sex["female"]=sex_no
                    sex["femalepopu"]=popu_no
                    sex["male"]=0
                    sex["malepopu"]=0
                elif curline[2] == "male":
                    sex["male"]=sex_no
                    sex["malepopu"]=popu_no
                    sex["female"]=0
                    sex["femalepopu"]=0
                writeYear[year]=sex
            else:
                if curline[2] == "female":
                    writeYear[year]["female"]=sex_no+writeYear[year]["female"]
                    writeYear[year]["femalepopu"]=popu_no+writeYear[year]["femalepopu"]
                elif curline[2] == "male":
                    writeYear[year]["male"]=sex_no+writeYear[year]["male"]
                    writeYear[year]["malepopu"]=popu_no+writeYear[year]["malepopu"]
    readf.close()

def write_it():
    writef=open(writeDir,'w',encoding='utf-8')
    for key,value in writeYear.items():
        writeLine=str(key)+','+str(value["female"])+','+str(value["femalepopu"])+','+str(value["female"]*100000/value["femalepopu"])+','+str(value["male"])+','+str(value["malepopu"])+','+str(value["male"]*100000/value["malepopu"])+'\n'
        writef.write(writeLine)
    writef.close()

Collect()
write_it()