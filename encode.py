from PIL import Image
import numpy as np
import bitarray
def encode(impath,message):
    messagebits = bitarray.bitarray()
    messagebits.frombytes(message.encode('utf-8'))
    message = messagebits.tolist()
    rawIm = Image.open(impath)
    pIm = np.array(rawIm)
    for bitdex in range(len(message)):
        pbitdex = int(np.floor(bitdex/3))
        cbitdex = int(bitdex%3)
        pixelPos = (int(np.floor(pbitdex/pIm.shape[1])),pbitdex%pIm.shape[1],cbitdex)
        color = pIm[pixelPos[0],pixelPos[1],pixelPos[2]]
        if (color == 255):
            pIm[pixelPos[0], pixelPos[1], pixelPos[2]] = 254
        if message[bitdex]:
            if (color%2==0):
                if (color!=254):
                    pIm[pixelPos[0], pixelPos[1], pixelPos[2]] += 1
                else:
                    pIm[pixelPos[0], pixelPos[1], pixelPos[2]] -= 1
        else:
            if (color%2==1):
                pIm[pixelPos[0], pixelPos[1], pixelPos[2]] +=1
    bitdex = len(message)
    pbitdex = int(np.floor(bitdex/3))
    cbitdex = int(bitdex%3)
    pixelPos = (int(np.floor(pbitdex/pIm.shape[1])),pbitdex%pIm.shape[1],cbitdex)
    pIm[pixelPos[0], pixelPos[1], pixelPos[2]] = 255
    return Image.fromarray(pIm)
