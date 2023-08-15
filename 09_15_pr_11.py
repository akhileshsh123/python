oldname = "sample.txt"
newname ="renamed _by_python.txt"
with open (oldname) as f:
    content =f.read()
    with open (newname, "w")as f:
        f.write( content)
        
        os._remove(oldname)

    