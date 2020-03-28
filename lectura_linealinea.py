with open("ejemplo.txt") as file_object:
    lines = file_object.readlines()
i=0
for line in lines:
    i=i+1
    print(line.rstrip() + "linea {}".format(i))