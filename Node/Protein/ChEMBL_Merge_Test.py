ChEMBLFilePath = "C:\\Users\\seomy\\Desktop\\"
ChEMBLFileName = "ChEMBL_Protein_Info.txt"

Uniprot_Info_FilePath = "C:\\Users\\seomy\\Desktop\\"
Uniprot_Info_FileName = "Uniprot_Protein_Info.txt"

OutputFilePath = "C:\\Users\\seomy\\Desktop\\"
OutputFileName = "ChEBML_Protein_Merge_Output_new.txt"

f_chemble = open(ChEMBLFilePath + ChEMBLFileName, 'r')
f_uniprot = open(Uniprot_Info_FilePath + Uniprot_Info_FileName, 'r')

Uniprot_Info_ID = []
Uniprot_Info_Accession_ID = []

ChEMBL_Info_ID = []
ChEMBL_Info_Name = []
ChEMBL_Info_Accession_ID = []
ChEMBL_Info_Type = []

while True:
    line = f_chemble.readline()
    if not line:break
    new_line = line.split("\t")

    ChEMBL_Info_ID.append(str(new_line[0]).replace('"','').strip())
    ChEMBL_Info_Name.append(str(new_line[1]).replace('"','').strip())
    ChEMBL_Info_Accession_ID.append(str(new_line[2]).replace('"','').strip())
    ChEMBL_Info_Type.append(str(new_line[3]).replace('"','').strip())

while True:
    line2 = f_uniprot.readline()
    if not line2:break
    new_line2 = line2.split("\t")

    Uniprot_Info_ID.append(str(new_line2[0]).replace('"','').strip())
    Uniprot_Info_Accession_ID.append(str(new_line2[1]).replace('"','').strip())

new_Uniprot_ID = []
new_ChEMBL_ID = []
new_Protein_name = []
new_Uniprot_Acession_ID = []
new_Type = []

for uniprot_id in Uniprot_Info_Accession_ID:

    for chembl_id in ChEMBL_Info_Accession_ID:

        if (str(chembl_id) == str(uniprot_id) or str(chembl_id).lower().__contains__(str(uniprot_id).lower())):

            new_Uniprot_ID.append(Uniprot_Info_ID[Uniprot_Info_Accession_ID.index(uniprot_id)])
            new_ChEMBL_ID.append(ChEMBL_Info_ID[ChEMBL_Info_Accession_ID.index(chembl_id)])
            new_Protein_name.append(ChEMBL_Info_Name[ChEMBL_Info_Accession_ID.index(chembl_id)])
            new_Uniprot_Acession_ID.append(chembl_id)
            new_Type.append(ChEMBL_Info_Type[ChEMBL_Info_Accession_ID.index(chembl_id)])

print(len(new_Uniprot_ID))
print(len(new_ChEMBL_ID))
print(len(new_Protein_name))
print(len(new_Uniprot_Acession_ID))
print(len(new_Type))


Data = str("Uniprot_ID") + "\t" + str("DB_ID") + "\t" + str("Protein_Name") + "\t" \
       + str("Uniprot_Accession_ID") + "\t" + str("Protein_Type") + "\n"

ChEMBL_f = open(OutputFilePath + OutputFileName, 'w')

for ai in range(0, len(new_Uniprot_ID)):

    Data = Data + str(new_Uniprot_ID[ai]) + "\t" + \
           str(new_ChEMBL_ID[ai]) + "\t" + \
           str(new_Protein_name[ai]) + "\t" + \
           str(new_Uniprot_Acession_ID[ai]) + "\t" + \
           str(new_Type[ai]) + "\n"

ChEMBL_f.write(Data)
ChEMBL_f.close()
print("write file")



