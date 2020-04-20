MappingFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
MappingFileName = "KEGG_MeSH_ID.txt"

InfoFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
InfoFileName = "KEGG_Disease_Info.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
OutputFileName = "KEGG_Merge_Output.txt"

f_mapping = open(MappingFilePath+MappingFileName, 'r')
f_info = open(InfoFilePath+InfoFileName, 'r')

KEGG_Disease_Mapping_Name = []
KEGG_Mapping_MeSH_ID = []
KEGG_Disease_Info_Name = []
KEGG_Code = []
KEGG_Disease_Category = []

while True:
    line = f_mapping.readline()
    if not line:break
    new_line = line.split('\t')

    KEGG_Disease_Mapping_Name.append(str(new_line[0]).replace('"','').strip())
    KEGG_Mapping_MeSH_ID.append(str(new_line[1]).replace('"','').strip())

while True:
    line2 = f_info.readline()
    if not line2:break
    new_line2 = line2.split("\t")

    KEGG_Disease_Info_Name.append(str(new_line2[0]).replace('"','').strip())
    KEGG_Code.append(str(new_line2[1]).replace('"','').strip())
    KEGG_Disease_Category.append(str(new_line2[2]).replace('"','').strip())

"""
#Dictionary 선언
KEGG_Mapping_Dic = {}
KEGG_Info_Dic = {}

#Dictionary 값 추가 방법
for ai in range(0, len(KEGG_Disease_Mapping_Name)):
    KEGG_Mapping_Dic[str(KEGG_Disease_Mapping_Name[ai])] = str(KEGG_Mapping_MeSH_ID[ai])

for bi in range(0, len(KEGG_Code)):
    KEGG_Info_Dic[str(KEGG_Disease_Info_Name[bi])] = str(KEGG_Code[bi])
"""

new_MeSH_ID = []
new_KEGG_code = []
new_Disease_name = []
new_Disease_category = []

for mapping_name in KEGG_Disease_Mapping_Name:

    for info_name in KEGG_Disease_Info_Name:

        #contain으로 값 찾아내게 되면 정확한 단어가 아니라 비슷한 경우 같이 포함되는 문제가 발생함
        #contain은 list 내부에서 값을 찾아내는데 활용 가능하나 정확한 값을 비교할 때는 활용하면 안됨
        #if(info_name.lower().__contains__(str(mapping_name).lower())):

        # 파일을 읽으면서 동일한 순서로 담기기 때문에 index 추적을 통해 계산 진행
        # KEGG의 경우 disease name이 key 값으로 겹치기 때문에 이름을 활용하여 두 데이터 (mapping, info)를 합칠 때 활용
        # 새로운 리스트를 만들어서 각 데이터들을 순서대로 담아서 정리함
        # 새로운 리스트 데이터들을 활용해서 나중에 하나의 파일로 정리하여 작성할 때 활용하면 됨
        if (str(info_name).lower() == (str(mapping_name).lower())):
            new_Disease_name.append(info_name)
            new_MeSH_ID.append(KEGG_Mapping_MeSH_ID[KEGG_Disease_Mapping_Name.index(mapping_name)])
            new_KEGG_code.append(KEGG_Code[KEGG_Disease_Info_Name.index(info_name)])
            new_Disease_category.append(KEGG_Disease_Category[KEGG_Disease_Info_Name.index(info_name)])

print(len(new_Disease_name))
print(len(new_MeSH_ID))
print(len(new_KEGG_code))
print(len(new_Disease_category))

print(new_Disease_name[1000])
print(new_MeSH_ID[1000])
print(new_KEGG_code[1000])
print(new_Disease_category[1000])

Data = str("MeSH_ID") + "\t" + str("DB_ID") + "\t" +str("Disease_Name") + "\t" + str("Disease_Category") + "\n"
KEGG_f = open(OutputFilePath+OutputFileName, 'w')

for ci in range(0, len(new_Disease_name)):

    Data = Data + str(new_MeSH_ID[ci]).strip() + "\t"\
           + str(new_KEGG_code[ci]).strip() + "\t"\
           + str(new_Disease_name[ci]).strip() + "\t" \
           + str(new_Disease_category[ci]).strip() + "\n"

KEGG_f.write(Data)

KEGG_f.close()
print("write file")