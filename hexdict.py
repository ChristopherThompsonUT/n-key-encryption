from random import choice
from PIL import ImageColor

def rgb(red,green,blue):
    #returns a rgb as a hex value
    red=hex(red).replace('0x','')
    green=hex(green).replace('0x','')
    blue=hex(blue).replace('0x','')
    if len(red)==1:
        red='0'+red
    if len(green)==1:
        green='0'+green
    if len(blue)==1:
        blue='0'+blue
    return (red+green+blue)


hexdict={
    #Formatted Key Word:HexCode, comma
    'red':'ff0000',
    'orange':'ff7e27',
    'nitram':'a15000',
    'yellow':'ffff00',
    'justice':'FBFF29',
    'green':'008000',
    'maryam':'008141',
    'harley':'4ac925',
    'lime':'00ff00',
    'blue':'0000ff',
    'egbert':'0715cd',
    'gray':'808080',
    'silver':'c0c0c0',
    'maroon':'800000',
    'captor':'a1a100',
    'olive':'808000',
    'kindness':'34C217',
    'leijon':'416600',
    'teal':'008080',
    'aqua':'00ffff',
    'bravery':'F4A521',
    'mind':'06ffd3',
    'navy':'000080',
    'purple':'800080',
    'fuchsia':'ff00ff',
    'peixes':'77003c',
    'polo_blue':'98b4d4',
    'fuchsia_rose':'c3447a',
    'aqua_sky':'7fcdcd',
    'heat':'ff6d0a',
    'clockwork':'444444',
    'frost':'f9f9f9',
    'tigerlily':'e15d44',
    'karkat':'626262',
    'vantas':'626262',
    'blue_turq':'55b4b0',
    'zahhak':'000056',
    'pyrope':'008282',
    'sand_$':'dfcfbe',
    'chili':'9b2335',
    'blue_iris':'5b5ea6',
    'crocker':'00d5f2',
    'serket':'005682',
    'mimosa':'efc050',
    'honeysucle':'d65076',
    'tango':'dd4124',
    'malachite':'009b77',
    'felt':'2ed73a',
    'strider1':'e00707',
    'strider2':'f2a400',
    'radiand':'b565a7',
    'patience':'67FDFE',
    'rain':'9ae7f5',
    'shroomite':'2c1ae9',
    'marsala':'955251',
    'perseverance':'CE1BD6',
    'shade':'020202',
    'chlorophyte':'248900',
    'ampora':'6a006a',
    'serenity':'92a8d1',
    'rose_quartz':'f7cac9',
    'integrity':'3627FC',
    'english':'1f9400',
    'greenery':'88b04b',
    'ultra_violet':'6b5b95',
    'lalonde1':'b536da',
    'wind':'1c58a3',
    'lalonde2':'ff6ff2',
    'coral':'ff6f61',
    'shrek':'589b00',
    'makara':choice(['2b0057','4200b0','6c00da']),
    'star_purple':'985ca3',
    'light':'b5f0f9',
    'hierophant':'6ad398',
    'weber':'4B2682',
    'signus':'5d465f',
    'brigham':'002E5D',
    'crimtane':'a52548',
    'megido':'a10000',
    'elmo':'d6292d',
    'wolverine':'275D38',
    'aggie':'0F2439',
    'ute':'CC0000',
    'hot_pink':'FF69B4',
    'claire':'42a258',
    'judas':'11AFb0',
    'tritoh':'840405',
    'mcdolan':'ffc600',
    'devourer':'646c9c',
    'dammek':'7e4206',
    'kermit':'92c648',
    'gonzo':'697bbb',
    'animal':'ed2c23',
    'perforator':'822630',
    'piggy':'f4a1bd',
    'calvin':'c20000',
    'hobbes':'ff8900',
    'fozzie':'f89a1c',
    'rowlf':'86370e',
    'green_sun':"4bec13",
    'harry_anderson':'0671cd',
    'tavros_kid':'2b0057',
    'yiffany':"D00009",
    'funni': choice(['b00b69','420a55','042069','69d1cc', 'f42069', 'b4da55', '69b00b']),
    'intj' : choice(['1A1A1F', "1a2551", "4b3b65", "4c576b"]),
    'intp' : choice(['354551', '10445a', '2abcae', '90b0c0']),
    'entj' : choice(['1e1717', '3f1111', '1d4428', '775914']),
    'entp' : choice(['02d169', '59b993', '066a7e', '29c4f4']),
    'infj' : choice(['3c204c', '434172', '9799cc', 'a6d0e9']),
    'infp' : choice(['4f537e', '684c77', '659bb3', '83b4d5']),
    'enfj' : choice(["86c066", "578748", "f5b341", "da7f42"]),
    'enfp' : choice(['f07f14', 'e8425f', 'e3896b', 'feda3c']),
    'istj' : choice(['323b49', '4b7095', 'cfddef', 'eaf3fd']),
    'isfj' : choice(['4a69bc', '948fa9', 'e79e9c', 'ffecec']),
    'estj' : choice(['3e302e', '57292d', '34414f', '4c667d']),
    'esfj' : choice(['3f465c', '7a4b62', 'e72c60', 'd47d69']),
    'istp' : choice(['312d27', '4f3c25', '355953', 'ec7686']),
    'isfp' : choice(['fcc339', 'a67cbf', '6e5670', '404766']),
    'estp' : choice(['581e15', 'b82219', 'e66a0f', 'fcf874']),
    'esfp' : choice(['2e2e2e', '657531', 'f7aa38', 'ffd53c'])
}

htmldict=ImageColor.colormap
for z in htmldict:
    htmldict[z]=htmldict[z].replace('#','')

hexdict.update(htmldict)
hexdict['white']='fefefe'
hexdict['black']='010101'


