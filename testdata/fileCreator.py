import os

os.system("RD Testdata /S /Q")
os.system("mkdir Testdata")

for i in range(100):
    os.system("python testdataGen.py > Testdata/test"+str(i)+".data")
