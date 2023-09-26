fileRead = open("file1.txt",mode="r",encoding="utf-8")
fileWrite = open("file2.txt",mode="w",encoding="utf-8")

fileData = fileRead.readlines()

for line in fileData:
    fileWrite.write(line)

print("The contents have been copied!")

fileRead.close()
fileWrite.close()
