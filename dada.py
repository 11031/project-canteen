with open("dada2.txt", "r") as file:
    lines=[line.strip().split(',') for line in file.readlines()]
    produse=[{'Date':line[0],'Name':line[3], 'Sales Amount':line[4],} 
    for line in lines]
    print(produse)

