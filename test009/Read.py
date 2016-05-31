def main():
    infile = open(data,"r")
    for i in range(5):
        line = infile.readline()
        print(line[:-1])
main()    
