from PIL import Image
import numpy as np
import bitarray
def decode(impath):
    rawIm = Image.open(impath)
    pIm = np.array(rawIm)
    bset = []
    for pdex in range(pIm.shape[0]*pIm.shape[1]*3):
        pixelPos = (int(np.floor(pdex / pIm.shape[1])), int(np.floor((pdex % pIm.shape[1])/3)), int(pdex%3))
        color = pIm[pixelPos[0],pixelPos[1],pixelPos[2]]
    #print(color)
        if color==255:
            break
        bset.append(bool(color%2))
    aIm = bitarray.bitarray(bset).tobytes().decode('utf-8')
    return aIm