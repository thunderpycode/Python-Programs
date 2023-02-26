d={}
with open('readfile.txt') as f:
    lines = f.readlines()
    for line in lines:
         if line.strip() == "" :
             continue
         elif line.startswith("#"):
             continue
         print(line)
         key, value = line.strip().split('=') 
         d[key]=(value) 
print(d)
