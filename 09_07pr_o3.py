
for i in range(2,21):
    for j in range(1,11):
        with open ( f" tables/ Multiplication _table_ of_{i}",'w') as f:
            for j in range (1,11):        
             f.write(f"(i)*(j)+(i*j)\n")
             break 