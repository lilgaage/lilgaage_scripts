#读取文件，mode默认是读取 mode='r'
with open("CeshiFiles/ceshi.py",encoding="utf8") as file1:
    ret = file1.read()
    print(ret)
print("-"*30)
#写入mode='w' 如果文件不存在则自动创建
#默认不支持中文 ，需要指定encoding="utf8"
with open("CeshiFiles/ghost.txt",encoding="utf8", mode='w') as file2:
    #默认写在文件的首行，换行需加\n
    file2.write("lilghost\n")
    file2.write("娃琳可")
with open("CeshiFiles/ghost.txt",encoding="utf8") as file2:
    ret = file2.read()
    print(ret)
print("-"*30)
#写入mode='w',写入时会覆盖文件原有的内容
# mode='a',写入时不会覆盖原有的内容
with open("CeshiFiles/ghost.txt",encoding="utf8",mode="a") as file3:
    file3.write("\n你你你你要跳舞吗")
with open("CeshiFiles/ghost.txt",encoding="utf8") as file3:
    ret = file3.read()
    print(ret)