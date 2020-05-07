DisGeNet_Association_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
DisGeNet_Association_FileName = "DisGeNet_Gene-DB_ID.txt"

DisGeNet_Node_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
DisGeNet_Node_FileName = "DisGeNet_Disease_Node.txt"

Output_gene_mapping_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
Output_gene_mapping_FileName = "Disease_Gene_DisGeNet.txt"

DisGeNet_Disease_Gene_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
DisGeNet_Disease_Gene_FileName = "Disease_Gene_DisGeNet.txt"

Uniprot_Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_merge\\Link\\Disease_Gene_Protein\\Data\\"
Uniprot_Info_FileName = "Uniprot_Protein_all_Info.txt"

Output_FilePath = "C:\\Users\\Seomyungwon\\Desktop\\Network_Temp\\Disease_Gene_Protein\\DisGeNet\\"
Output_FileName = "Disease_Gene_Protein_DisGeNet_new.txt"

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

#Input gene - disease ID association data
while True:
    association_line = f_association.readline()
    if not association_line:break
    new_association_line = association_line.split("\t")

    Association_Gene.append(str(new_association_line[0]).replace('"','').strip())
    Association_DB_ID.append(str(new_association_line[1]).strip())

#Input disease MeSH, disease ID data
while True:
    node_line = f_Node.readline()
    if not node_line:break
    new_node_line = node_line.split("\t")

    Node_MeSH_ID.append(str(new_node_line[0]).strip())
    Node_DB_ID.append(str(new_node_line[1]).strip())

#Input uniprot ID, association ID, Gene data
while True:
    info_line = f_Info.readline()
    if not info_line:break
    new_info_line = info_line.split("\t")

    Info_Uniprot_ID.append(str(new_info_line[0]).replace('"','').strip())
    Info_Uniprot_Accession.append(str(new_info_line[1]).replace('"','').strip())
    Info_Uniprot_Gene.append(str(new_info_line[5]).replace('"','').strip())

print("Input data")

new_MeSH_ID = []
new_Gene_ID = []
new_DB_ID = []

# [DisGeNet MeSH disease id에 Gene ID mapping]
cnt = 1

for node_db_id in Node_DB_ID:

    print(str("Input DB ID: ") + str(node_db_id))
    print(str("Input data cnt: ") + str(cnt))

    for association_id in Association_DB_ID:

        if str(node_db_id) == str(association_id):

            new_MeSH_ID.append(str(Node_MeSH_ID[Node_DB_ID.index(node_db_id)]).strip())
            new_Gene_ID.append(str(Association_Gene[Association_DB_ID.index(association_id)]).strip())
            new_DB_ID.append(str(node_db_id).strip())

    cnt = cnt + 1

Data = str("MeSH_ID") + "\t" + str("DB_ID") + "\t" + str("Gene_ID") + "\n"

DisGeNet_f = open(Output_gene_mapping_FilePath + Output_gene_mapping_FileName, 'w')

for ai in range(0, len(new_MeSH_ID)):

    Data = Data + str(new_MeSH_ID[ai]).strip() + "\t" + str(new_DB_ID[ai]).strip() + "\t" + str(new_Gene_ID[ai]).strip() + "\n"

DisGeNet_f.write(Data)
DisGeNet_f.close()
print("write MeSH ID - Gene data")

# [DisGeNet MeSH - Gene 정보에 Uniprot ID, Accession ID mapping]

f_Disease_Gene = open(DisGeNet_Disease_Gene_FilePath + DisGeNet_Disease_Gene_FileName, 'r')

MeSH_ID = []
Gene_ID = []

Final_MeSH_ID = []
Final_Gene_ID = []
Final_Uniprot_ID = []
Final_Uniprot_Accession = []

num = 1

while True:
    disease_gene_line = f_Disease_Gene.readline()
    if not disease_gene_line: break
    new_disease_gene_line = disease_gene_line.split("\t")

    MeSH_ID.append(str(new_disease_gene_line[0]).strip())
    Gene_ID.append(str(new_disease_gene_line[2]).strip())

for gene in Gene_ID:

    print(str("Input DB ID: ") + str(gene))
    print(str("Input data num: ") + str(num))

    for Info_gene in Info_Uniprot_Gene:

        if (str(gene)) in Info_gene:

            Final_MeSH_ID.append(str(MeSH_ID[Gene_ID.index(gene)]).strip())
            Final_Gene_ID.append(str(gene.strip()))
            Final_Uniprot_ID.append(str(Info_Uniprot_ID[Info_Uniprot_Gene.index(Info_gene)]).strip())
            Final_Uniprot_Accession.append(str(Info_Uniprot_Accession[Info_Uniprot_Gene.index(Info_gene)]).strip())

    num = num + 1

Final_Data = str("MeSH_ID") + "\t" + str("Gene_ID") + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession_ID") + "\n"

Final_DisGeNet_f = open(Output_FilePath + Output_FileName, 'w')

for bi in range(0, len(Final_MeSH_ID)):

    Final_Data = Final_Data + str(Final_MeSH_ID[bi]).strip()+ "\t" + str(Final_Gene_ID[bi]).strip() + "\t" + str(Final_Uniprot_ID[bi]).strip() + "\t" + str(Final_Uniprot_Accession[bi]).strip() + "\n"

Final_DisGeNet_f.write(Final_Data)
Final_DisGeNet_f.close()

print("write final file")
