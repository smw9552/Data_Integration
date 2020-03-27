MappingFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\DisGeNet\\"
MappingFileName = "#DisGeNet_MeSH_ID_new.txt"

InfoFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\DisGeNet\\"
InfoFileName = "#DisGeNet_Disease_Info_new.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\DisGeNet\\"
OutputFileName= "DisGeNet_Merge_Output_new.txt"

f_mapping = open(MappingFilePath + MappingFileName, 'r')
f_info = open(InfoFilePath + InfoFileName, 'r')

#DisGeNET_Mapping file 순서
DisGeNET_Disease_Mapping_Name = []
DisGeNET_Disease_Mapping_MeSH_ID = []

#DisGeNET Info file
DisGeNET_Disease_Info_ID = []
DisGeNET_Disease_Info_Name = []
DisGeNET_Disease_Info_Type = []
DisGeNET_Disease_Info_MeSH_Class = []
DisGeNET_Disease_Info_MeSH_Heading = []
DisGeNET_Disease_Info_SemanticType = []

"""
#DisGeNET Info file 순서
DisGeNET_Disease_Info_GeneID = []
DisGeNET_Disease_Info_GeneSymbol = []
#DSI: Disease Specificity Index
DisGeNET_Disease_Info_DSI = []
#DPI: Disease Pleiotropy Index
DisGeNET_Disease_Info_DPI = []
DisGeNET_Disease_Info_ID = []
DisGeNET_Disease_Info_Name = []
DisGeNET_Disease_Info_Type = []
DisGeNET_Disease_Info_Class = []
DisGeNET_Disease_Info_SemanticType = []
DisGeNET_Disease_Info_Score = []
DisGeNET_Disease_Info_EI = []
DisGeNET_Disease_Info_YearInitial = []
DisGeNET_Disease_Info_YearFinal = []
DisGeNET_Disease_Info_NumOfPMID = []
DisGeNET_Disease_Info_NumOfSNPs = []
DisGeNET_Disease_Info_Source = []
"""

while True:
    line = f_mapping.readline()
    if not line:break
    new_line = line.split("\t")

    DisGeNET_Disease_Mapping_Name.append(str(new_line[0]).replace('"','').strip())
    DisGeNET_Disease_Mapping_MeSH_ID.append(str(new_line[1]).replace('"','').strip())


while True:
    line2 = f_info.readline()
    if not line2:break
    new_line2 = line2.split("\t")

    DisGeNET_Disease_Info_ID.append(str(new_line2[0]).replace('"','').strip())
    DisGeNET_Disease_Info_Name.append(str(new_line2[1]).replace('"','').strip())
    DisGeNET_Disease_Info_Type.append(str(new_line2[2]).replace('"','').strip())
    DisGeNET_Disease_Info_MeSH_Class.append(str(new_line2[3]).replace('"','').strip())
    DisGeNET_Disease_Info_MeSH_Heading.append(str(new_line2[4]).replace('"','').strip())
    DisGeNET_Disease_Info_SemanticType.append(str(new_line2[5]).replace('"','').strip())


print("Input data in list")


new_MeSH_ID = []
new_DisGeNET_ID = []
new_Disease_name = []
new_Type = []
new_MeSH_Class = []
new_MeSH_Heading = []
new_SemanticType = []

for mapping_name in DisGeNET_Disease_Mapping_Name:

    for info_name in DisGeNET_Disease_Info_Name:

        if (str(info_name).lower() == (str(mapping_name).lower())):
            new_Disease_name.append(info_name)
            new_MeSH_ID.append(DisGeNET_Disease_Mapping_MeSH_ID[DisGeNET_Disease_Mapping_Name.index(mapping_name)])
            new_DisGeNET_ID.append(DisGeNET_Disease_Info_ID[DisGeNET_Disease_Info_Name.index(info_name)])
            new_Type.append(DisGeNET_Disease_Info_Type[DisGeNET_Disease_Info_Name.index(info_name)])
            new_MeSH_Class.append(DisGeNET_Disease_Info_MeSH_Class[DisGeNET_Disease_Info_Name.index(info_name)])
            new_MeSH_Heading.append(DisGeNET_Disease_Info_MeSH_Heading[DisGeNET_Disease_Info_Name.index(info_name)])
            new_SemanticType.append(DisGeNET_Disease_Info_SemanticType[DisGeNET_Disease_Info_Name.index(info_name)])

print(len(new_MeSH_ID))
print(len(new_DisGeNET_ID))


Data = str("MeSH_ID") + "\t" + str("DB_ID") + "\t" + str("Disease_Name") + "\t" \
       + str("Disease_Type") + "\t" + str("Disease_MeSH_Class") + "\t" \
       + str("Disease_MeSH_Heading") + "\t" + str("Disease_SemanticType") + "\n"

DisGeNET_f = open(OutputFilePath + OutputFileName, 'w')

for ai in range(0, len(new_Disease_name)):

    Data = Data + str(new_MeSH_ID[ai]).strip() + "\t" \
           + str(new_DisGeNET_ID[ai]).strip() + "\t" \
           + str(new_Disease_name[ai]).strip() + "\t" \
           + str(new_Type[ai]).strip() + "\t" \
           + str(new_MeSH_Class[ai]).strip() + "\t" \
           + str(new_MeSH_Heading[ai]).strip() + "\t" \
           + str(new_SemanticType[ai]).strip() + "\n"

DisGeNET_f.write(Data)

DisGeNET_f.close()
print("write file")