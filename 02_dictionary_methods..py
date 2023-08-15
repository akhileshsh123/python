myDict = { 
    "fast ": "In a Quick Manner",
    "harry": "A Coder",
    "marks ":[1,2,5],
    "anotherdict": {'harry': 'Player'},
    1:2
}
# dictionary Methods
# print (type(myDict.Keys())) Prints the Keys of the dictionary
# print (list(myDict.values())) 
# print(myDict.items()) Print the (Key,value) for all contents of the dictionary
print(myDict)
updatedict = {
    "Lovish": "Friend",
    "Shubham":"Friend",
    "harry": "A Dancer"
}
# myDict.update(updateDict) updates the dictionary by adding key-values pairs from update
# print(myDict)
# print(myDict.get("harry")) prints value associated with Key "harry"
# print(myDict["harry"]) throws an error as harry2 is not present in the dictionary
# the difference between.get and[sytax in Dictionaries]
# print(mydict.get("harry2")) returns none harry2 is not present in the dictionary
# print (myDict["harry2"])throws an error as harry2 is not present in the dictionary