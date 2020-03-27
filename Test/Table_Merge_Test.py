import pandas as pd

InputFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\Merge_Ouput\\"
InputFileName_KEGG = "KEGG_Merge_Output.txt"
InputFileName_OTP = "OTP_Merge_Output.txt"
InputFileName_DisGeNET = "DisGeNet_Merge_Output.txt"
InputFileName_ChEMBL = "ChEMBL_Merge_Output.txt"

InputFileName_Merge_1 = ""
InputFileName_Merge_2 = ""

OutputFilePath = "C:\\Users\\seomy\\Desktop\\Merge_Test\\Merge_Ouput\\"
OutputFileName = "Final_Output.txt"

OutputFileName1 = "Test_output_1.txt"
OutputFileName2 = "Test_output_2.txt"

df_KEGG = pd.read_csv(str(InputFilePath+InputFileName_KEGG), sep='\t', engine='python', encoding='cp949')
df_OTP = pd.read_csv(str(InputFilePath+InputFileName_OTP), sep='\t', engine='python', encoding='cp949')
df_DisGeNET = pd.read_csv(str(InputFilePath+InputFileName_DisGeNET), sep='\t', engine='python', encoding='cp949')
df_ChEMBL = pd.read_csv(str(InputFilePath+InputFileName_ChEMBL), sep='\t', engine='python', encoding='cp949')


# Merge
#Merge_1 = pd.merge(df_KEGG, df_ChEMBL, how='outer', on='MeSH_ID')
#Merge_2 = pd.merge(df_DisGeNET, df_OTP, on='MeSH_ID')
#Merge_data = pd.merge(Merge_2, df_ChEMBL, how='outer', on='MeSH_ID')

# Concatenation (concat)
# axis=0로 설정하면 열이 늘어나는 형태로 테이블 합쳐짐
# axis=1로 설정하면 행이 늘어나는 형태로 테이블 합쳐짐
concat_1 = pd.concat([df_KEGG, df_ChEMBL, df_DisGeNET, df_OTP], axis=0)
#concat_2 = pd.concat([df_KEGG, df_ChEMBL, df_DisGeNET], axis=1, objs='MeSH_ID')

# write file
#Merge_1.to_csv(OutputFilePath + OutputFileName1, sep='\t')
#Merge_2.to_csv(OutputFilePath + OutputFileName2, sep='\t')

concat_1.to_csv(OutputFilePath + OutputFileName, sep='\t')
#concat_2.to_csv(OutputFilePath + OutputFileName2, sep='\t')