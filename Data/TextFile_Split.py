f = open("C:\\Users\\Seomyungwon\\Desktop\\FileSplitTest\\Uniprot_Protein_all_Info.txt", 'r')
lines = f.readlines()
f.close()

cnt = 1
FileName_Num = 1

for line in lines:
    fileName = "Uniprot_split_" + str(FileName_Num) + ".txt"

    fw = open(fileName, "a")
    fw.write(line)
    fw.close()

    # 분할하려는 line 숫자를 cnt에 넣어주면 됨
    if cnt == 50000:
        FileName_Num = FileName_Num + 1
        cnt = 0

    cnt = cnt + 1