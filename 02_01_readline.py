f =open ('sample.text')
# read first line
data = f.readline()
print(data)
# read second line
data = f.readline()
print(data)
# read third line
data = f.readline()
print(data)

f.close()