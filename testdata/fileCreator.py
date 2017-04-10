import os

os.system("RD Testdata")
os.system("mkdir Testdata /S /Q")

for i in range(100):
    os.system("python testdataGen.py > Testdata/test"+str(i)+".data")
