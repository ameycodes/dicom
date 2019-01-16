import pydicom
d1 = pydicom.read_file("C:/Users/Amey Gondhalekar/Desktop/DICOM/bmode.dcm")
d2 = pydicom.read_file("C:/Users/Amey Gondhalekar/Desktop/DICOM/ttfm.dcm")

print(d1)
print(len(d1.keys()))    #No. of records

fw = open("dicomtags.txt","w")

for di in d1.values():
    fw.write(str(di.tag)+"\n")
fw.write("\nNext file\n")
for d in d2.values():
    fw.write(str(d.tag)+"\n")
fw.close()
