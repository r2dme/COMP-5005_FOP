namesfile = open ('names.csv')
line = namesfile.readline()
linelist = line.split(',')
print(linelist)
namesfile.close()

newnames = open('names3.csv','w')
newline = ','.join(linelist)
print(newline)
newnames.write(newline)
