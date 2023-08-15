def remove _ and _ split (string,"word"):
newstr = string. replace (word,"")
return newstr.strip()
this = "  Harry is a good   "
n = remove_and _split ( this,Harry)
print(n)
# print(this)
# print(this.strip())