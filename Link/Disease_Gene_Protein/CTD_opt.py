CTD_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
CTD_FileName = "CTD_diseases_pathways.txt"

#Uniprot_Info_FilePath = "C:\\Users\\Seomyungwon\\Desktop\\FileSplitTest\\Uniprot\\"

Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
Info_FileName = "Uniprot_Protein_all_Info.txt"

OutputFilePath = "C:\\Users\\Seomyungwon\\Desktop\\Network_Temp\\Disease_Gene_Protein\\CTD\\"
OutputFileName = "Disease_Gene_Protein_CTD_New.txt"


f_CTD = open(CTD_FilePath + CTD_FileName, "r")
f_Info = open(Info_FilePath + Info_FileName, "r")
print("Input data")


CTD_Disease_Name = []
CTD_MeSH_ID = []
CTD_Pathway_Name = []
CTD_Pathway_ID = []
CTD_Gene = []

Info_Uniprot_ID = []
Info_Uniprot_Accession = []
Info_Uniprot_Gene = []

Final_MeSH_ID = []
Final_Disease_Name = []
Final_Pathway_Name = []
Final_Pathway_ID = []
Final_Gene = []
Final_Uniprot_ID = []
Final_Uniprot_Accession = []


while True:
    CTD_line = f_CTD.readline()
    if not CTD_line:break
    new_CTD_line = CTD_line.split("\t")

    CTD_Disease_Name.append(new_CTD_line[0].replace('"','').strip())
    CTD_MeSH_ID.append(new_CTD_line[1].strip())
    CTD_Pathway_Name.append(new_CTD_line[2].replace('"','').strip())
    CTD_Pathway_ID.append(new_CTD_line[3].replace('"','').strip())
    CTD_Gene.append(new_CTD_line[4].replace('"','').strip())

while True:
    Info_line = f_Info.readline()
    if not Info_line:break
    new_Info_line = Info_line.split("\t")

    Info_Uniprot_ID.append(str(new_Info_line[0]).replace('"','').strip())
    Info_Uniprot_Accession.append(str(new_Info_line[1]).replace('"','').strip())
    Info_Uniprot_Gene.append(new_Info_line[5].replace('"','').strip())


cnt = 1
for ctd_gene_id in CTD_Gene:

    print(str("Input data: ") + str(ctd_gene_id))
    print(str("Input data cnt: ") + str(cnt))

    for Info_gene in Info_Uniprot_Gene:


        if str(ctd_gene_id) in Info_gene:

            Final_MeSH_ID.append(CTD_MeSH_ID[CTD_Gene.index(ctd_gene_id)])
            Final_Disease_Name.append(CTD_Disease_Name[CTD_Gene.index(ctd_gene_id)])
            Final_Pathway_Name.append(CTD_Pathway_Name[CTD_Gene.index(ctd_gene_id)])
            Final_Pathway_ID.append(CTD_Pathway_ID[CTD_Gene.index(ctd_gene_id)])
            Final_Gene.append(str(ctd_gene_id))
            Final_Uniprot_ID.append(Info_Uniprot_ID[Info_Uniprot_Gene.index(Info_gene)])
            Final_Uniprot_Accession.append(Info_Uniprot_Accession[Info_Uniprot_Gene.index(Info_gene)])

    cnt = cnt+1

print(len(Final_MeSH_ID))
print(len(Final_Disease_Name))
print(len(Final_Pathway_Name))
print(len(Final_Pathway_ID))
print(len(Final_Gene))
print(len(Final_Uniprot_ID))
print(len(Final_Uniprot_Accession))

Data = str("MeSH_ID") + "\t" + str("Gene") + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession_ID") + "\n"
#CTD_f = open(OutputFilePath + OutputFileName, 'w')


# 파일 작성할 때 단위별로 작성 될 수 있도록 전체 List를 n 단위로 분할 작업 진행
# n은 분할 데이터 숫자

n = 100000
file_cnt = 1

Result_Final_MeSH_ID = [Final_MeSH_ID[i * n:(i + 1) * n] for i in range((len(Final_MeSH_ID) + n - 1) // n)]
Result_Final_Disease_Name = [Final_Disease_Name[i * n:(i + 1) * n] for i in range((len(Final_Disease_Name) + n - 1) // n)]
Result_Final_Pathway_Name = [Final_Pathway_Name[i * n:(i + 1) * n] for i in range((len(Final_Pathway_Name) + n - 1) // n)]
Result_Final_Pathway_ID = [Final_Pathway_ID[i * n:(i + 1) * n] for i in range((len(Final_Pathway_ID) + n - 1) // n)]
Result_Final_Gene = [Final_Gene[i * n:(i + 1) * n] for i in range((len(Final_Gene) + n - 1) // n)]
Result_Final_Uniprot_ID = [Final_Uniprot_ID[i * n:(i + 1) * n] for i in range((len(Final_Uniprot_ID) + n - 1) // n)]
Result_Final_Uniprot_Accession = [Final_Uniprot_Accession[i * n:(i + 1) * n] for i in range((len(Final_Uniprot_Accession) + n - 1) // n)]


for ai in range(0, len(Result_Final_MeSH_ID)):

    Temp_Final_MeSH_ID = Result_Final_MeSH_ID[ai]
    Temp_Final_Disease_Name = Result_Final_Disease_Name[ai]
    Temp_Final_Pathway_Name = Result_Final_Pathway_Name[ai]
    Temp_Final_Pathway_ID  = Result_Final_Pathway_ID[ai]
    Temp_Final_Gene = Result_Final_Gene[ai]
    Temp_Final_Uniprot_ID = Result_Final_Uniprot_ID[ai]
    Temp_Final_Uniprot_Accession = Result_Final_Uniprot_Accession[ai]

    for bi in range(0, len(Temp_Final_MeSH_ID)):

        Data = Data + str(Temp_Final_MeSH_ID[bi]) + "\t" \
               + str(Temp_Final_Gene[bi]) + "\t" \
               + str(Temp_Final_Uniprot_ID[bi]) + "\t" \
               + str(Temp_Final_Uniprot_Accession[bi]) + "\n"

    OutputFileName = str("Disease_Gene_Protein_CTD_new" + str("_") + str(file_cnt) + ".txt")

    file_cnt = file_cnt + 1

    CTD_f = open(OutputFilePath + OutputFileName, 'w')
    CTD_f.write(Data)
    CTD_f.close()
    print("Write file cnt: " + str(file_cnt))

    Data = str("MeSH_ID") + "\t" + str("Gene") + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession_ID") + "\n"


"""
for ai in range(0, len(Final_MeSH_ID)):

    Data = Data + str(Final_MeSH_ID[ai]) \
           + "\t" + str(Final_Gene[ai]) \
           + "\t" + str(Final_Uniprot_ID[ai]) \
           + "\t" + str(Final_Uniprot_Accession[ai]) + "\n"

CTD_f.write(Data)
CTD_f.close()
print("write file")
"""