myDict ={
     "Panka" : "Fan",
     " Dabba ": "Box",
     "Vastu": "Item"
 }
print("Options are ",myDict.Keys() )
a = input ("Enter the Hindi word\n")
# print ( "The meaning of your word is :", myDict[a])
 
# Below line will not throw an error if the Key is not present in the  dictionary

print("The meaning of your word is :",myDict.get(a))