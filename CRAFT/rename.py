import os 
os.chdir("result")
for path in os.listdir("."):
    os.rename(path,path[4:])