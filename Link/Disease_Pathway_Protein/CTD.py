CTD_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Pathway_Protein\\Data\\"
CTD_FileName = "CTD_diseases_pathways.txt"

Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Pathway_Protein\\Data\\"
Info_FileName = "Uniprot_Protein_all_Info.txt"

OutputFilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Pathway_Protein\\"
OutputFileName = "Disease_Pathway_Protein_CTD.txt"

f_CTD = open(CTD_FilePath + CTD_FileName, "r")
f_Info = open(Info_FilePath + Info_FileName, "r")

CTD_Disease_Name = []
CTD_MeSH_ID = []
CTD_Pathway_Name = []
CTD_Pathway_ID = []
CTD_Gene = []

Info_Uniprot_ID = []
Info_Uniprot_Accession = []
Info_Uniprot_Gene = []

print("Input data")

while True:
    CTD_line = f_CTD.readline()
    if not CTD_line: break
    new_CTD_line = CTD_line.split("\t")

    CTD_Disease_Name.append(new_CTD_line[0].replace('"', '').strip())
    CTD_MeSH_ID.append(new_CTD_line[1].strip())
    CTD_Pathway_Name.append(new_CTD_line[2].replace('"', '').strip())
    CTD_Pathway_ID.append(new_CTD_line[3].replace('"', '').strip())
    CTD_Gene.append(new_CTD_line[4].replace('"', '').strip())

while True:
    Info_line = f_Info.readline()
    if not Info_line: break
    new_Info_line = Info_line.split("\t")

    Info_Uniprot_ID.append(str(new_Info_line[0]).replace('"', '').strip())
    Info_Uniprot_Accession.append(str(new_Info_line[1]).replace('"', '').strip())
    Info_Uniprot_Gene.append(new_Info_line[5].replace('"', '').strip())

print("Read data")

Final_MeSH_ID = []
Final_Disease_Name = []
Final_Pathway_Name = []
Final_Pathway_ID = []
Final_Gene = []
Final_Uniprot_ID = []
Final_Uniprot_Accession = []

for ctd_gene_id in CTD_Gene:

    for info_gene in Info_Uniprot_Gene:

        if str(ctd_gene_id) in str(info_gene):
            Final_MeSH_ID.append(CTD_MeSH_ID[CTD_Gene.index(ctd_gene_id)])
            Final_Disease_Name.append(CTD_Disease_Name[CTD_Gene.index(ctd_gene_id)])
            Final_Pathway_Name.append(CTD_Pathway_Name[CTD_Gene.index(ctd_gene_id)])
            Final_Pathway_ID.append(CTD_Pathway_ID[CTD_Gene.index(ctd_gene_id)])
            Final_Gene.append(str(ctd_gene_id))
            Final_Uniprot_ID.append(Info_Uniprot_ID[Info_Uniprot_Gene.index(info_gene)])
            Final_Uniprot_Accession.append(Info_Uniprot_Accession[Info_Uniprot_Gene.index(info_gene)])

print(len(Final_MeSH_ID))
print(len(Final_Disease_Name))
print(len(Final_Pathway_Name))
print(len(Final_Pathway_ID))
print(len(Final_Gene))
print(len(Final_Uniprot_ID))
print(len(Final_Uniprot_Accession))

Data = str("MeSH_ID") + "\t" + str("Pathway_Name") + "\t" + str("Pathway_ID")  + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession_ID") + "\n"

CTD_f = open(OutputFilePath + OutputFileName, 'w')

for ai in range(0, len(Final_MeSH_ID)):
    Data = Data + str(Final_MeSH_ID[ai]) \
           + "\t" + str(Final_Pathway_Name[ai]) \
           + "\t" + str(Final_Pathway_ID[ai]) \
           + "\t" + str(Final_Uniprot_ID[ai]) \
           + "\t" + str(Final_Uniprot_Accession[ai]) + "\n"

CTD_f.write(Data)
CTD_f.close()
print("write file")