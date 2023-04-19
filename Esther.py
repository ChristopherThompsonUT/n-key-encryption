'''TODO Have the program check the image and if it isn't equal to the original, change the keyword'''
from math import floor
from random import randrange, sample
from hexdict import hexdict
from keygen import keygen, replace_dict, get_key
print("Type your message")
message = input("Message: ")


test_message=message

#Remove any incompatable characters, and cleans up the message
for r1 in replace_dict:
        message=message.replace(r1,replace_dict[r1])

#Break string into ten characters
broken_message = []
repeater = 0
divlen=5#typically 7, can be changed for test purposes. I found anything over a 10 causes error in the decoding process
repeater_max = floor(len(message)/divlen)
if (len(message)%divlen==0):
        repeater_max-=1

while repeater <= repeater_max:
	broken_message.append(message[0:divlen])
	message = message[divlen:]
	repeater += 1



keyword=input("key word?")
cipherkey =keygen(keyword)
starter=get_key(cipherkey,'0')


for z in range(0, len(broken_message)):
        print(broken_message[z])
        if (broken_message[z][0]==starter):
                print("Possible Error in Translation, test if message translate correctly")
                broken_message[z]='qw'+broken_message[z]


#This next block of code converts the letters into a string of numbers
repeater = 0
while (repeater <= repeater_max):
        for r1 in "abcdefghijklmnopqrstuvwxyz. ":
                broken_message[repeater]=broken_message[repeater].replace(r1,cipherkey[r1])                
        broken_message[repeater]=int(broken_message[repeater])
        repeater += 1


#block of functions to define the color variables
def randgen():
        hexlist=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        valuergb=[''.join(sample(hexlist,2)),''.join(sample(hexlist,2)),''.join(sample(hexlist,2))]
        value10=int(''.join(valuergb),16)
        return valuergb, value10
def dictgen(_in):
        valuergb=[hexdict[_in][0:2],hexdict[_in][2:4],hexdict[_in][4:6]]
        value10=int(''.join(valuergb),16)
        return valuergb, value10

def hextest(_in):
        if len(_in) == 6:
                for z in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                       _in= _in.replace(z,"")
                if len(_in)==0:
                        return True
                else:
                        return False
        else:
                return False
def hexgen(_in):
        valuergb=[_in[0:2],_in[2:4],_in[4:6]]
        value10=int(''.join(valuergb),16)
        return valuergb, value10


background10,color110,color210=0,0,0
while(background10==0):
        _in=input('Background Color?')
        if _in=="random":
                bvaluergb, background10=randgen()
        elif _in in hexdict:
                bvaluergb, background10=dictgen(_in)
        elif (hextest(_in)):
                bvaluergb, background10=hexgen(_in)
        else:
                print("Sorry, I don't recognize that value")

while(color110==0):
        _in=input('Color1?')
        if _in=="random":
                color1rgb, color110=randgen()
        elif _in in hexdict:
                color1rgb, color110=dictgen(_in)
        elif (hextest(_in)):
                color1rgb, color110=hexgen(_in)
        else:
                print("Sorry, I don't recognize that value")

while(color210==0):
        _in=input('Color2?')
        if _in=="random":
                color2rgb, color210=randgen()
        elif _in in hexdict:
                color2rgb, color210=dictgen(_in)
        elif (hextest(_in)):
                color2rgb, color210=hexgen(_in)
        else:
                print("Sorry, I don't recognize that value")

for r1 in range(0,len(broken_message)):
        broken_message[r1]=broken_message[r1]-(16**6)*background10

slope = ((-1)**randrange(0,2))*randrange(1,5)

#append the values to the lists
x1,x2=[],[]
x1bin,x2bin=[],[]
for r1 in range(0,len(broken_message)):
        x1.append((color110-broken_message[r1])*slope)
        var1=x1
        x1bin.append(bin(abs((color110-broken_message[r1])*slope)).replace('0b',''))

        x2.append((color110-broken_message[r1])*slope)
        var2=x2
        x2bin.append(bin(abs((color210-broken_message[r1])*slope)).replace('0b',''))
print(len(max(x2bin + x1bin)))
img_max=len(max(x2bin + x1bin)) + 4

'''
OK, so it turns out this code was just complicating things. I just lowered the breaking value at the begininng and prettymuch eliminated the need for this

var1.sort(),var2.sort()
#this is one monster of a code. I Hate Myself Because of this 11/6/19 22:35
if img_max<=max(len(bin(abs(var1[0])).replace('0b','')),len(bin(abs(var1[-1])).replace('0b',''))):
        img_max=max(len(bin(abs(var1[0])).replace('0b','')),len(bin(abs(var1[-1])).replace('0b','')))+3
else:
        img_max=img_max

#These next few lines determine the max width of the image if it needs to go over 64 pixels.
minvar=min([bin(min(x1)).replace('-0b','').replace('0b',''),bin(min(x2)).replace('-0b','').replace('0b','')])
maxvar=max([bin(max(x1)).replace('0b','').replace('-0b',''),bin(max(x2)).replace('0b','').replace('-0b','')])

if maxvar>minvar:
        damvar=maxvar
if minvar>maxvar:
        damvar=minvar


if len(damvar)>=63:
        print('adjusting size')
        img_max=len(damvar)+3
'''

#test prints - use official decoder to test values
'''print(''.join(bvaluergb))
print(''.join(color1rgb))
print(''.join(color2rgb))
#print(x1)
print(x1bin)
#print(x2)
print(x2bin)
'''
from PIL import Image, ImageDraw

image=Image.new('RGB',(img_max,len(2*x2)))
draw = ImageDraw.Draw(image)
for r1 in range(0,len(x1)):
        if (x1[r1]>0):
                draw.line((0,2*r1, img_max,2*r1), fill='#ffffff')#rrggbb
        else:
                draw.line((0,2*r1,img_max,2*r1), fill="#000000")
        #draw x1 values
        r3=0
        for r2 in x1bin[r1]:
                if (r2=='0'):
                        image.putpixel(((img_max-len(x1bin[r1])+r3),2*r1), (int(bvaluergb[0],16),int(bvaluergb[1],16),int(bvaluergb[2],16),255))
                        
                else:
                        image.putpixel(((img_max-len(x1bin[r1])+r3),2*r1), (int(color1rgb[0],16),int(color1rgb[1],16),int(color1rgb[2],16),255))

                r3+=1

        r3=0
        if(x2[r1]>0):
                draw.line((0,2*r1+1,img_max,2*r1+1),fill='#ffffff')
        else:
                draw.line((0,2*r1+1,img_max,2*r1+1),fill="#000000")

        for r2 in x2bin[r1]:
                if (r2=='0'):
                        image.putpixel(((img_max-len(x2bin[r1])+r3),2*r1+1), (int(bvaluergb[0],16),int(bvaluergb[1],16),int(bvaluergb[2],16),255))
                        
                else:
                        image.putpixel(((img_max-len(x2bin[r1])+r3),2*r1+1), (int(color2rgb[0],16),int(color2rgb[1],16),int(color2rgb[2],16),255))

                r3+=1

image.save("img1.png","PNG")
input()





