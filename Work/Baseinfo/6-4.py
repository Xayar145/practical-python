

def filematch(filename,substr):
    '''
        yield是一行一行输出的
    '''
    with open(filename,"r") as f:
        for line in f:
            if substr in line:
                yield line

for line in open ("Data/portfolio.csv"):
    print(line ,end = " ")

for line in filematch("Data/portfolio.csv",'IBM'):
    print(line ,end = " ")


