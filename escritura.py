archivo="ejemplo.txt"
i=0
file_object=open(archivo, 'r+')

while i < 100:
    i=i+1
    file_object.write(str(i)+ "\n")
        
    contents = file_object.read()
    print(contents)

   

