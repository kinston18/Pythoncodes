from importlib.resources import contents


f=open("Pointer.txt", "w")
f.write("Prajjwal")
f.close()

f=open("Pointer.txt", "r")
content=f.read()
f.close()
print(content)