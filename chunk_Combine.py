with open('test1.mp4',"rb") as chk :
    f = chk.read()
    b = bytearray(f)

with open('test2.mp4',"rb") as chk :
    f = chk.read()
    b1 = bytearray(f)

combine = b + b1

filez = open('output.mp4','wb')
filez.write(bytearray(combine))
filez.close()