def partition(filename,NumberofChunks):
    #opening file as read binary - bytearray
 with open(filename,'rb') as fls:
    f = fls.read()
    b = bytearray(f)
    fls.close()
    wordlength = len(b)

    #Predicting size of each piece
    size = int(wordlength/NumberofChunks)

    #Making Chunks names
    for i in range(0,NumberofChunks):
        chunkNames.append("filename"+str(i))

    #Making chunks
    start = 0
    end = size
    for i in range(0,NumberofChunks):
        arrayDict[i] = b[start:end]
        start += size
        end += size

    #chunk1 = b[0: size]
    #chunk2 = b[int(wordlength/NumberofChunks) :int(wordlength)]


chunkNames = [] #chunkName list
arrayDict = []  #array dictionary
# # Used Generator to generate chunk names
# def chunkNames():
   #  for i in range(1, NumberofChunks):
      #   yield + str(i)


#writing chunk bytearray to chunked files
def ChunkWrite(Numberofchunks,ext):
    for i in range(0, Numberofchunks):
      chunk = open(chunkNames[i]+'.'+ext,'wb')
      chunk.write(bytearray(arrayDict[i]))
      chunk.close()
 #k = open('test1.mp4','wb')
 #k.write(bytearray(chunk1))
 #k.close()
 #j = open('test2.mp4','wb')
 #j.write(bytearray(chunk2))
 #j.close()