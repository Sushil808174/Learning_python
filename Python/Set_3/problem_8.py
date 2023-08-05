
f1 = open("input.txt","r")
str = f1.read();
list = str.split(" ");
length = len(list);
print("length is",length)
f1.close();

createAndwriteFile = open("output.txt","a")
content = f"Number of words :{length}"
createAndwriteFile.write(content);
createAndwriteFile.close();
