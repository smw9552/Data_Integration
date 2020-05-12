NPT_Uniprot_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\NPASS\\"
NPT_Uniprot_FileName = "NPASS_NPT_Uniprot_mapping_New.txt"

NPC_ChEMBL_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\NPASS\\"
NPC_ChEMBL_FileName = "NPASS_NPC_ChEMBL_mapping.txt"

NPASS_Info_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\NPASS\\"
NPASS_Info_FileName = "NPASS_activities_filtered_final.txt"

Output_FilePath = "C:\\Users\\Seomyungwon\\Dropbox\\Seomyungwon\\#Multi_Level_Hyper_Network\\#Data\\DB_data_process\\NPASS\\"
Output_FileName_NPC = "#NPC_Mapping_output.txt"
Output_FileName_NPT = "#NPT_Mapping_output.txt"


f_NPT_Uniprot = open(NPT_Uniprot_FilePath + NPT_Uniprot_FileName, 'r')
f_NPC_ChEMBL = open(NPC_ChEMBL_FilePath + NPC_ChEMBL_FileName, 'r')
f_NPASS_Info = open(NPASS_Info_FilePath + NPASS_Info_FileName, 'r')


NPT_Uniprot_ID = []
NPT_ID = []
NPT_Uniprot_Accession = []

NPC_ID = []
NPC_ChEMBL_ID = []

NPASS_NPC_ID = []
NPASS_NPT_ID = []
NPASS_activity_type = []
NPASS_activity_relation = []
NPASS_activity_value = []
NPASS_activity_units = []
NPASS_activity_relation_value = []
NPASS_assay_organism = []
NPASS_assay_tax_id = []
NPASS_assay_strain = []
NPASS_assay_tissue = []
NPASS_assay_cell_type = []
NPASS_ref_id = []
NPASS_ref_id_type = []

new_NPC_ChEMBL_ID = []
new_NPASS_NPC_ID = []
new_NPT_Uniprot_ID = []
new_NPT_Uniprot_Accession = []
new_NPASS_NPT_ID = []
new_NPASS_activity_type = []
new_NPASS_activity_relation = []
new_NPASS_activity_value = []
new_NPASS_activity_units = []
new_NPASS_activity_relation_value = []
new_NPASS_assay_organism = []
new_NPASS_assay_tax_id = []
new_NPASS_assay_strain = []
new_NPASS_assay_tissue = []
new_NPASS_assay_cell_type = []
new_NPASS_ref_id = []
new_NPASS_ref_id_type = []

#Read NPT-Uniprot File
while True:
    NPT_Uniprot_line = f_NPT_Uniprot.readline()
    if not NPT_Uniprot_line:break
    new_NPT_Uniprot_line = NPT_Uniprot_line.split("\t")

    NPT_Uniprot_ID.append(new_NPT_Uniprot_line[0].strip().replace('"',''))
    NPT_ID.append(new_NPT_Uniprot_line[1].strip().replace('"',''))
    NPT_Uniprot_Accession.append(new_NPT_Uniprot_line[2].strip().replace('"',''))

#Read NPC-ChEMBL File
while True:
    NPC_ChEMBL_line = f_NPC_ChEMBL.readline()
    if not NPC_ChEMBL_line: break
    new_NPC_ChEMBL_line = NPC_ChEMBL_line.split("\t")

    NPC_ID.append(new_NPC_ChEMBL_line[0].strip().replace('"', ''))
    NPC_ChEMBL_ID.append(new_NPC_ChEMBL_line[1].strip().replace('"', ''))

#Read NPASS file
while True:
    NPASS_line = f_NPASS_Info.readline()
    if not NPASS_line:break
    new_NPASS_line = NPASS_line.split("\t")

    NPASS_NPC_ID.append(new_NPASS_line[0].strip().replace('"',''))
    NPASS_NPT_ID.append(new_NPASS_line[1].strip().replace('"',''))
    NPASS_activity_type.append(new_NPASS_line[2].strip().replace('"',''))
    NPASS_activity_relation.append(new_NPASS_line[3].strip().replace('"',''))
    NPASS_activity_value.append(new_NPASS_line[4].strip().replace('"',''))
    NPASS_activity_units.append(new_NPASS_line[5].strip().replace('"',''))
    NPASS_activity_relation_value.append(new_NPASS_line[6].strip().replace('"',''))
    NPASS_assay_organism.append(new_NPASS_line[7].strip().replace('"',''))
    NPASS_assay_tax_id.append(new_NPASS_line[8].strip().replace('"',''))
    NPASS_assay_strain.append(new_NPASS_line[9].strip().replace('"',''))
    NPASS_assay_tissue.append(new_NPASS_line[10].strip().replace('"',''))
    NPASS_assay_cell_type.append(new_NPASS_line[11].strip().replace('"',''))
    NPASS_ref_id.append(new_NPASS_line[12].strip().replace('"',''))
    NPASS_ref_id_type.append(new_NPASS_line[13].strip().replace('"',''))

print("read data")

cnt_1 = 1

for npass_npc_id in NPASS_NPC_ID:

    print(str("Input NPC ID: ") + str(npass_npc_id))
    print(str("Data cnt: ") + str(cnt_1))

    for npc_id in NPC_ID:

        if str(npass_npc_id) == str(npc_id):

            new_NPASS_NPC_ID.append(str(npass_npc_id))
            new_NPC_ChEMBL_ID.append(NPC_ChEMBL_ID[NPC_ID.index(npc_id)])
            new_NPASS_activity_type.append(str(NPASS_activity_type[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_relation.append(str(NPASS_activity_relation[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_value.append(str(NPASS_activity_value[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_units.append(str(NPASS_activity_units[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_relation_value.append(str(NPASS_activity_relation_value[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_organism.append(str(NPASS_assay_organism[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_tax_id.append(str(NPASS_assay_tax_id[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_strain.append(str(NPASS_assay_strain[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_tissue.append(str(NPASS_assay_tissue[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_cell_type.append(str(NPASS_assay_cell_type[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_ref_id.append(str(NPASS_ref_id[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_ref_id_type.append(str(NPASS_ref_id_type[NPASS_NPC_ID.index(npass_npc_id)]))

    cnt_1 = cnt_1 + 1

NPASS_NPC_f = open(Output_FilePath + Output_FileName_NPC, 'w')

Data = str("NPC_ID") + "\t" + str("ChEMBL_ID") + "\t" + str("activity_type") + \
       "\t" + str("activity_relation") + "\t" + str("activity_value") + "\t" + str("activity_units") + "\t" + str("activity_relation_value") + "\t" + str("assay_organism") + "\t" + str("assay_tax_id") + \
       "\t" + str("assay_strain") + "\t" + str("assay_tissue") + "\t" + str("assay_cell_type") + "\t" + str("ref_id") + "\t" + str("ref_id_type") + "\n"

print(str("new_NPASS_NPC_ID: ") + str(len(new_NPASS_NPC_ID)))
print(str("new_NPC_ChEMBL_ID: ") + str(len(new_NPC_ChEMBL_ID)))
print(str("NPASS_Activity_type: ") + str(len(new_NPASS_activity_type)))
print(str("NPASS_Activity_relation: ") + str(len(new_NPASS_activity_relation)))
print(str("NPASS_Activity_value: ") + str(len(new_NPASS_activity_value)))
print(str("NPASS_Activity_unit: ") + str(len(new_NPASS_activity_units)))
print(str("NPASS_Activity_relation_value: ") + str(len(new_NPASS_activity_relation_value)))
print(str("NPASS_Assay_organism: ") + str(len(new_NPASS_assay_organism)))
print(str("NPASS_Assay_tax_id: ") + str(len(new_NPASS_assay_tax_id)))
print(str("NPASS_Assay_strain: ") + str(len(new_NPASS_assay_strain)))
print(str("NPASS_Assay_tissue: ") + str(len(new_NPASS_assay_tissue)))
print(str("NPASS_Assay_cell_type: ") + str(len(new_NPASS_assay_cell_type)))
print(str("NPASS_Assay_ref_id: ") + str(len(new_NPASS_ref_id)))
print(str("NPASS_Assay_ref_id_type: ") + str(len(new_NPASS_ref_id_type)))

for ai in range(0, len(new_NPASS_NPC_ID)):

    Data = Data + str(new_NPASS_NPC_ID[ai]) + "\t" + str(new_NPC_ChEMBL_ID[ai]) + "\t" + str(new_NPASS_activity_type[ai]) + "\t" + str(new_NPASS_activity_relation[ai]) + "\t"\
           + str(new_NPASS_activity_value[ai]) + "\t" + str(new_NPASS_activity_units[ai]) + "\t" + str(new_NPASS_activity_relation_value[ai]) + "\t" + str(new_NPASS_assay_organism[ai]) + "\t" \
           + str(new_NPASS_assay_tax_id[ai]) + "\t" + str(new_NPASS_assay_strain[ai]) + "\t" + str(new_NPASS_assay_tissue[ai]) + "\t" + str(new_NPASS_assay_cell_type[ai]) + "\t" \
           + str(new_NPASS_ref_id[ai]) + "\t" + str(new_NPASS_ref_id_type[ai]) + "\n"

NPASS_NPC_f.write(Data)
NPASS_NPC_f.close()
print("write NPC-ChEMBL mapping data")


new_NPT_Uniprot_ID = []
new_NPT_Uniprot_Accession = []
new_NPASS_NPT_ID = []
new_NPASS_activity_type = []
new_NPASS_activity_relation = []
new_NPASS_activity_value = []
new_NPASS_activity_units = []
new_NPASS_activity_relation_value = []
new_NPASS_assay_organism = []
new_NPASS_assay_tax_id = []
new_NPASS_assay_strain = []
new_NPASS_assay_tissue = []
new_NPASS_assay_cell_type = []
new_NPASS_ref_id = []
new_NPASS_ref_id_type = []



cnt_2 = 1

for npass_npt_id in NPASS_NPT_ID:

    print(str("Input NPT ID: ") + str(npass_npt_id))
    print(str("Data cnt: ") + str(cnt_2))

    for npt_id in NPT_ID:

        if str(npass_npt_id) == str(npt_id):

            new_NPASS_NPT_ID.append(str(npass_npt_id))
            new_NPT_Uniprot_ID.append(NPT_Uniprot_ID[NPT_ID.index(npt_id)])
            new_NPT_Uniprot_Accession.append(NPT_Uniprot_Accession[NPT_ID.index(npt_id)])
            new_NPASS_activity_type.append(str(NPASS_activity_type[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_relation.append(str(NPASS_activity_relation[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_value.append(str(NPASS_activity_value[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_units.append(str(NPASS_activity_units[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_activity_relation_value.append(str(NPASS_activity_relation_value[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_organism.append(str(NPASS_assay_organism[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_tax_id.append(str(NPASS_assay_tax_id[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_strain.append(str(NPASS_assay_strain[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_tissue.append(str(NPASS_assay_tissue[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_assay_cell_type.append(str(NPASS_assay_cell_type[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_ref_id.append(str(NPASS_ref_id[NPASS_NPC_ID.index(npass_npc_id)]))
            new_NPASS_ref_id_type.append(str(NPASS_ref_id_type[NPASS_NPC_ID.index(npass_npc_id)]))

    cnt_2 = cnt_2 + 1

NPASS_NPT_f = open(Output_FilePath + Output_FileName_NPT, 'w')

Data_2 = str("NPT_ID") + "\t" + str("Uniprot_ID") + "\t" + str("Uniprot_Accession") + "\t" + str("activity_type") + \
       "\t" + str("activity_relation") + "\t" + str("activity_value") + "\t" + str("activity_units") + "\t" + str("activity_relation_value") + "\t" + str("assay_organism") + "\t" + str("assay_tax_id") + \
       "\t" + str("assay_strain") + "\t" + str("assay_tissue") + "\t" + str("assay_cell_type") + "\t" + str("ref_id") + "\t" + str("ref_id_type") + "\n"

print(str("new_NPASS_NPT_ID: ") + str(len(new_NPASS_NPT_ID)))
print(str("new_NPT_Uniprot_id: ") + str(len(new_NPT_Uniprot_ID)))
print(str("new_NPT_Uniprot_Accession: ")) + str(len(new_NPT_Uniprot_Accession))
print(str("NPASS_Activity_type: ") + str(len(new_NPASS_activity_type)))
print(str("NPASS_Activity_relation: ") + str(len(new_NPASS_activity_relation)))
print(str("NPASS_Activity_value: ") + str(len(new_NPASS_activity_value)))
print(str("NPASS_Activity_unit: ") + str(len(new_NPASS_activity_units)))
print(str("NPASS_Activity_relation_value: ") + str(len(new_NPASS_activity_relation_value)))
print(str("NPASS_Assay_organism: ") + str(len(new_NPASS_assay_organism)))
print(str("NPASS_Assay_tax_id: ") + str(len(new_NPASS_assay_tax_id)))
print(str("NPASS_Assay_strain: ") + str(len(new_NPASS_assay_strain)))
print(str("NPASS_Assay_tissue: ") + str(len(new_NPASS_assay_tissue)))
print(str("NPASS_Assay_cell_type: ") + str(len(new_NPASS_assay_cell_type)))
print(str("NPASS_Assay_ref_id: ") + str(len(new_NPASS_ref_id)))
print(str("NPASS_Assay_ref_id_type: ") + str(len(new_NPASS_ref_id_type)))

for bi in range(0, len(new_NPASS_NPT_ID)):

    Data_2 = Data_2 + str(new_NPASS_NPT_ID[bi]) + "\t" + str(new_NPT_Uniprot_ID[bi]) + "\t" + str(new_NPT_Uniprot_Accession[bi]) + "\t" + str(new_NPASS_activity_type[bi]) + "\t" + str(new_NPASS_activity_relation[bi]) + "\t"\
           + str(new_NPASS_activity_value[bi]) + "\t" + str(new_NPASS_activity_units[bi]) + "\t" + str(new_NPASS_activity_relation_value[bi]) + "\t" + str(new_NPASS_assay_organism[bi]) + "\t" \
           + str(new_NPASS_assay_tax_id[bi]) + "\t" + str(new_NPASS_assay_strain[bi]) + "\t" + str(new_NPASS_assay_tissue[bi]) + "\t" + str(new_NPASS_assay_cell_type[bi]) + "\t" \
           + str(new_NPASS_ref_id[bi]) + "\t" + str(new_NPASS_ref_id_type[bi]) + "\n"

NPASS_NPT_f.write(Data)
NPASS_NPT_f.close()
print("write NPT-Uniprot mapping data")