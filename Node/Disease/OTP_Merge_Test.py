MappingFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
MappingFileName = "OTP_MeSH_ID.txt"

InfoFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
InfoFileName = "OTP_Disease_Info.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\"
OutputFileName= "OTP_Merge_Output.txt"

f_mapping = open(MappingFilePath + MappingFileName, 'r')
f_info = open(InfoFilePath + InfoFileName, 'r')

# OTP mapping file 순서
OTP_Disease_Mapping_Name = []
OTP_Disease_Mapping_MeSH_ID = []

# OTP info file 순서
OTP_Disease_Info_ID = []
OTP_Disease_Info_Name = []

while True:
    line = f_mapping.readline()
    if not line:break
    new_line = line.split("\t")

    OTP_Disease_Mapping_Name.append(str(new_line[0]).replace('"','').strip())
    OTP_Disease_Mapping_MeSH_ID.append(str(new_line[1]).replace('"','').strip())

while True:
    line2 = f_info.readline()
    if not line2:break
    new_line2 = line2.split("\t")

    OTP_Disease_Info_ID.append(str(new_line2[0]).replace('"','').strip())
    OTP_Disease_Info_Name.append(str(new_line2[1]).replace('"','').strip())

new_MeSH_ID = []
new_OTP_ID = []
new_Disease_Name = []

for mapping_name in OTP_Disease_Mapping_Name:

    for info_name in OTP_Disease_Info_Name:

        if (str(info_name).lower() == (str(mapping_name).lower())):
            new_Disease_Name.append(info_name)
            new_MeSH_ID.append(OTP_Disease_Mapping_MeSH_ID[OTP_Disease_Mapping_Name.index(mapping_name)])
            new_OTP_ID.append(OTP_Disease_Info_ID[OTP_Disease_Info_Name.index(info_name)])


print(len(new_Disease_Name))
print(len(new_MeSH_ID))
print(len(new_OTP_ID))


Data = str("MeSH_ID") + "\t" + str("DB_ID") + "\t" + str("Disease_Name") + "\n"

OTP_f = open(OutputFilePath + OutputFileName, 'w')

for ai in range(0, len(new_Disease_Name)):

    Data = Data + str(new_MeSH_ID[ai]).strip() + "\t" \
           + str(new_OTP_ID[ai]) + "\t" \
           + str(new_Disease_Name[ai]).strip() + "\n"

OTP_f.write(Data)

OTP_f.close()
print("write file")