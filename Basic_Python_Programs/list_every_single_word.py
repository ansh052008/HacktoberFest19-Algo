
print("This program lists out every single word alphabetically froma given file.")
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lin=line.split()
    for k in lin:
        if k not in lst:
    		lst.append(k)
lst.sort()
print(lst)
