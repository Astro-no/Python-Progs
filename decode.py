import pyshark
import sys
import yenc


filename = sys.argv[1]


file = pyshark.FileCapture(filename)


for pkt in file:

    
    cap = pkt.icmp.data_data

    
    data_list = cap.split(":")

    

    offset = ""

    for i in data_list:
        offset += chr(int(i, 0x10))

    

    inputFile = sys.argv[2]

    with open(inputFile, "a", encoding="latin-1") as f:
        f.write(offset)

    

    outputFile = sys.argv[3]
   
    yenc.decode(inputFile, outputFile)
