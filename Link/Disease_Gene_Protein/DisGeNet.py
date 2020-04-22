DisGeNet_Association_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data_processing\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data_processing\\"
DisGeNet_Association_FileName = "DisGeNet_Gene-DB_ID.txt"

DisGeNet_Node_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data_processing\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data_processing\\"
DisGeNet_Node_FileName = "DisGeNet_Disease_Node.txt"

Uniprot_Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data_processing\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data_processing\\"
Uniprot_Info_FileName = "Uniprot_Protein_all_Info.txt"

Output_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data_processing\\DB_data_merge\\Link\\Disease_Gene_Protein\\"
Output_FileName = "Disease_Gene_Protein_DisGeNet.txt"


f_association = open(DisGeNet_Association_FilePath + DisGeNet_Association_FileName, 'r')
f_Node = open(DisGeNet_Node_FilePath + DisGeNet_Node_FileName, 'r')
f_Info = open(Uniprot_Info_FilePath + Uniprot_Info_FileName, 'r')

Association_Gene = []
Association_DB_ID = []

Node_MeSH_ID = []
Node_DB_ID = []

Info_Uniprot_ID = []
Info_Uniprot_Accession = []
Info_Uniprot_Gene = []


while True:
    association_line = f_association.readline()
    if not association_line:break
    new_association_line = association_line.split("\t")

    Association_Gene.append(str(new_association_line[0]).replace('"','').strip())
    Association_DB_ID.append(str(new_association_line[1]).strip())

while True:
    node_line = f_Node.readline()
    if not node_line:break
    new_node_line = node_line.split("\t")

    Node_MeSH_ID.append(str(new_node_line[0]).strip())
    Node_DB_ID.append(str(new_node_line[1]).strip())

while True:
    info_line = f_Info.readline()
    if not info_line:break
    new_info_line = info_line.split("\t")

    Info_Uniprot_ID.append(str(new_info_line[0]).replace('"','').strip())
    Info_Uniprot_Accession.append(str(new_info_line[1]).replace('"','').strip())
    Info_Uniprot_Gene.append(new_info_line[5].replace('"','').strip())


print("Input data")

new_MeSH_ID = []
new_Gene_ID = []
new_DB_ID = []

for node_db_id in Node_DB_ID:

    for association_db_id in Association_DB_ID:

        if (str(node_db_id) == str(association_db_id)):

            new_Gene_ID.append(Association_Gene[Association_DB_ID.index(association_db_id)])
            new_MeSH_ID.append(Node_MeSH_ID[Node_DB_ID.index(node_db_id)])
            new_DB_ID.append(str(node_db_id))



Final_MeSH_ID = []
Final_DB_ID = []
Final_Gene = []
Final_Uniprot_ID = []
Final_Uniprot_Accession_ID = []


for new_gene_id in new_Gene_ID:

    for info_uniprot_gene_id in Info_Uniprot_Gene:

        if (str(new_gene_id) in str(info_uniprot_gene_id)):

            Final_MeSH_ID.append(new_MeSH_ID[new_Gene_ID.index(new_gene_id)])
            Final_DB_ID.append(new_DB_ID[new_Gene_ID.index(new_gene_id)])
            Final_Gene.append(str(new_gene_id))
            Final_Uniprot_ID.append(Info_Uniprot_ID[Info_Uniprot_Gene.index(info_uniprot_gene_id)])
            Final_Uniprot_Accession_ID.append(Info_Uniprot_Accession[Info_Uniprot_Gene.index(info_uniprot_gene_id)])



print(len(Final_MeSH_ID))
print(len(Final_DB_ID))
print(len(Final_Gene))
print(len(Final_Uniprot_ID))
print(len(Final_Uniprot_Accession_ID))

#차후에 수정 가능
Data = str("MeSH_ID") + "\t" + str("Gene") + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession_ID") + "\n"

DisGeNet_f = open(Output_FilePath + Output_FileName, 'w')

for ai in range(0, len(Final_MeSH_ID)):

    Data = Data + str(Final_MeSH_ID[ai]) \
           + "\t" + str(Final_Gene[ai]) \
           + "\t" + str(Final_Uniprot_ID[ai]) \
           + "\t" + str(Final_Uniprot_Accession_ID[ai]) + "\n"

DisGeNet_f.write(Data)
DisGeNet_f.close()
print("write file")