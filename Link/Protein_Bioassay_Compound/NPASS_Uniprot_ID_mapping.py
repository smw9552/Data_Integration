NPASS_NPT_Uniprot_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\DB_data_process\\NPASS\\"
NPASS_NPT_Uniprot_FileName = "NPASS_NPT_Uniprot_mapping.txt"

Uniprot_Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Pathway_Protein\\Data\\"
Uniprot_Info_FileName = "Uniprot_Protein_all_Info.txt"

OutputFilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\DB_data_process\\NPASS\\"
OutputFileName = "NPASS_NPT_Uniprot_mapping_New.txt"

f_NPT = open(NPASS_NPT_Uniprot_FilePath + NPASS_NPT_Uniprot_FileName, 'r')
f_Info = open(Uniprot_Info_FilePath + Uniprot_Info_FileName, 'r')

NPT_ID = []
NPT_Uniprot_accession = []

Info_Uniprot_ID = []
Info_Uniprot_Accession = []


new_NPT_ID = []
new_Uniprot_ID = []
new_NPT_Uniprot_Accession = []

#Read NPASS
while True:
    NPASS_line = f_NPT.readline()
    if not NPASS_line:break
    new_NPASS_line = NPASS_line.split("\t")

    NPT_ID.append(new_NPASS_line[0].strip().replace('"',''))
    NPT_Uniprot_accession.append(new_NPASS_line[1].strip().replace('"',''))


#Read Uniprot
while True:
    Uniprot_line = f_Info.readline()
    if not Uniprot_line:break
    new_Uniprot_line = Uniprot_line.split("\t")

    Info_Uniprot_ID.append(new_Uniprot_line[0].strip().replace('"',''))
    Info_Uniprot_Accession.append(new_Uniprot_line[1].strip().replace('"',''))

print("Input data")
cnt = 1

for NPT_Accession in NPT_Uniprot_accession:

    print(str("Input NPT-Uniprot_Accession: ") + str(NPT_Accession))
    print(str("Input data cnt: ") + str(cnt))

    for Uniprot_Accession in Info_Uniprot_Accession:

        if NPT_Accession in Uniprot_Accession:

            new_NPT_ID.append(str(NPT_ID[NPT_Uniprot_accession.index(NPT_Accession)]).strip())
            new_Uniprot_ID.append(str(Info_Uniprot_ID[Info_Uniprot_Accession.index(Uniprot_Accession)]).strip())
            new_NPT_Uniprot_Accession.append(str(NPT_Accession).strip())

    cnt = cnt + 1

Data = str("Uniprot_ID") + "\t" + str("DB_ID") + "\t" + str("Uniprot_Accession") + "\n"


NPT_f = open(OutputFilePath + OutputFileName, 'w')

for ai in range(0, len(new_NPT_ID)):

    Data = Data + str(new_Uniprot_ID[ai]) + "\t" + str(new_NPT_ID[ai]) + "\t" + str(new_NPT_Uniprot_Accession[ai]) + "\n"

NPT_f.write(Data)
NPT_f.close()
print("write NPT - Uniprot ID")
