with open("this txt") as f:
    contentb = f.read()
    
    with open("copy.txt", 'w') as f:
        f.write(contentb)
     