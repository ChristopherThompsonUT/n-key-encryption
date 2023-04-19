from PIL import Image
from hexdict import rgb
from keygen import keygen, replace_dict, get_key

z=input("Picture to put in?")

img=Image.open(z)
#These next few lines of code turn the image into the 24 bit depth color format.
if img.mode=="RGBA":
    img.load()
    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask = img.split()[3])
    background.save(z, "PNG", quality=100)
    img=background

c1,c2,bgc='','',''
r=0

while (len(c1)+len(c2)+len(bgc)!=9):#while color vars are all empty
    pix = img.getpixel((r,0))#look at rth pixel in first row
    if (pix!=(0,0,0) and pix!=(255,255,255)):#if it's not black or white...
        if (len(c1)!=0 and len(c2)!=0):#...and if c1 and c2 are filled
            if (pix==c1):#see if the pixel is the same as one of the colors
                r+=1#and continue
            else:#...or if the pixel is not the same as one of the colors
                bgc=pix#assign bgc
                break#get outta here
        else:#...or if c1 and c2 are not filled
            c1=pix#fill them
            c2=img.getpixel((r,1))
    else:#else continue
        r+=1
        

width,height=img.size
const=0
keyarray1,keyarray2=[],[]
for i in range(0,int(height/2)):
    '''turn the image rows into numbers'''
    key1=''
    key2=''
    for j in range(0,width):
        pix=img.getpixel((j,2*i))
        if pix==(0,0,0):
            const=-1
        elif pix==(255,255,255):
            const=1
        elif pix==c1:
            key1+='1'
        else:
            key1+='0'
    keyarray1.append(const*int(key1,2))
    for j in range(0,width):
        pix=img.getpixel((j,2*i+1))
        if pix==(0,0,0):
            const=-1
        elif pix==(255,255,255):
            const=1
        elif pix==c2:
            key2+='1'
        else:
            key2+='0'
    keyarray2.append(const*int(key2,2))

def value(pix):
    return int(rgb(pix[0],pix[1],pix[2]),16)

m=(value(c2)-value(c1))/(keyarray2[0]-keyarray1[0])

message=''
for z in range(0, len(keyarray1)):
    b=value(c1)-m*keyarray1[z]
    message+=str(int(b+value(bgc)*16**6))

keyword=input('keyword')
keydict=keygen(keyword)
keydict = {y:x for x,y in keydict.items()}
message+=' '
decode=''
for z in range(1,len(message)):
    try:
        q=message[z-1]
    except:
        break
    try:
        p=message[z-1]+message[z]
    except:

        break
    if q=='8' or q=='9':
        decode+=keydict[p]
        message=message[1:]
    else:
        decode+=keydict[q]
        message=message[0:]



replace_dict={y:x for x,y in replace_dict.items()}

for i in replace_dict:
             decode=decode.replace(i,replace_dict[i])
print(decode.replace('qw'+get_key(keygen(keyword),'0'),get_key(keygen(keyword),'0')))
input()
