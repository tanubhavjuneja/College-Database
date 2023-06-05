import openpyxl
import json
label_list = [
    ["B.Sc. (Honours) Computer Science"],
    ["B.Sc. (Honours) Chemistry"],
    ["B.Sc. (Honours) Botany"],
    ["B.Sc. (Honours) Electronic Science"],
    ["B.Sc. (Honours) Life Science"],
    ["B.Sc. (Honours) Mathematics"],
    ["B.Sc. (Honours) Physical Science"],
    ["B.Sc. (Honours) Physics"],
    ["B.Sc. (Honours) Zoology"],
    ["B.Com. Programme"],
    ["B.Com. (Honours)"],
    ["B.A. (Honours) Business Economics"],
    ["B.A. (Honours) Economics"],
    ["B.A. (Honours) English"],
    ["B.A. (Honours) Hindi"],
    ["B.A. (Honours) Punjabi"],
    ["B.A. (Honours) Political Science"],
    ["B.A. (Honours) Humanities and Social Sciences"],
    ["B.A. (Honours) History"]
]
iq=openpyxl.load_workbook("C:/Users/Tanubhav Juneja/Downloads/College.xlsx")
iqq=iq.active
rownum = int(iqq.max_row)
print(rownum)
for i in range(2,rownum+1):
    cnc="C"+str(i)
    cnd="D"+str(i)
    cne="E"+str(i)
    cnf="F"+str(i)
    cng="G"+str(i)
    aan=iqq[cnc].value
    ban=iqq[cnd].value
    can="+91 "+str(int(iqq[cne].value))
    dan=iqq[cnf].value
    ean=iqq[cng].value
    list=[aan,ban,can,dan,ean]
    if ban[4:7]=="CSC":
        label_list[0].append(list)
    elif ban[4:7]=="BCS":
        label_list[9].append(list)
    elif ban[4:7]=="BPS":
        label_list[6].append(list)
    elif ban[4:7]=="MTS":
        label_list[5].append(list)
    elif ban[4:7]=="HIS":
        label_list[18].append(list)
    elif ban[4:7]=="ZOO":
        label_list[8].append(list)
    elif ban[4:7]=="CHM":
        label_list[1].append(list)
    elif ban[4:7]=="BLS":
        label_list[4].append(list)
    elif ban[4:7]=="POL":
        label_list[16].append(list)
    elif ban[4:7]=="PHY":
        label_list[7].append(list)
    print(list)
file=open("college_list.json",'w')
file.truncate(0)
json.dump(label_list,file)
file.close()
