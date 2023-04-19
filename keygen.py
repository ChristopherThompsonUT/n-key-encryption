def keygen(foo):
    from collections import OrderedDict
    foo=''.join(OrderedDict.fromkeys(foo))
    result=''.join(OrderedDict.fromkeys(foo+'abcdefghijklmnopqrstuvwxyz. '))

    while(len(result)%len(foo)!=0):
        result+='+'

    commonchars=['a','s','i','n','t','o','e','r']
    uncommonchars=['b','c','d','f','g','h','j','k','l','m','p','q','u','v','w','x','y','z',' ','.']

    padgen = {
    "a":'0',
    "b":'0',
    "c":'0',
    "d":'0',
    "e":'0',
    "f":'0',
    "g":'0',
    "h":'0',
    "i":'0',
    "j":'0',
    "k":'0',
    "l":'0',
    "m":'0',
    "n":'0',
    "o":'0',
    "p":'0',
    "q":'0',
    "r":'0',
    "s":'0',
    "t":'0',
    "u":'0',
    "v":'0',
    "w":'0',
    "x":'0',
    "y":'0',
    "z":'0',
    ".":'0',
    " ":'0'
    }
    comm_counter=0
    uncomm_counter=80
    for b in range(0,len(foo)):#Run this for every value in the edited code
        for m in range(0,int(len(result)/len(foo))):#Run for each column values
            x=result[int(len(foo))*m+b]
            if x in commonchars:
                padgen[x]=str(comm_counter)
                comm_counter+=1
            elif x in uncommonchars:
                padgen[x]=str(uncomm_counter)
                uncomm_counter+=1
            else:
                x=x
    return padgen

'''This Part is the Dictionary Conversion for the code word. The code word will be "glove". An explanation of how to code transposes letters into numerals is given:
    Code word is given, and is the first row of a table, with the rest of the letters after in alphabetic order. No letters are repeated ("abacus" becomes "abcus")
   [[G L O V E]
    [A B C D F]
    [H I J K M]
    [N P Q R S]
    [T U W X Y]
    [Z . ' ' + +]]

Replace the 8 most common letters in the alphabet with the letters 0-7, starting from the left column to the right, top to bottom. ( A way to remember this is with "A Sin To Err")
[[G L 4 V 6]
 [0 B C D F]
 [H 3 J K M]
 [1 P Q 5 7]
 [2 U W X Y]
 [Z . ' ' + +]]

#Replace the other 20 characters with the numbers 81-99, in the same manner.
[[80 83 4  93 6 ]
 [0  84 88 94 97]
 [81 3  89 95 98]
 [1  85 90 5  7 ]
 [2  86 91 96 99]
 [82 87 92 +  + ]]
'''


replace_dict={#I'm noticing some of these are cut off, this making wrong characters. I'll try minimizing them to four characters at most. Avoid numbers or slashes, use only letters
        '"':'qxq',
        "'":'qxq',
        '0':'qxnz','1':'qxno','2':'qxnt','3':'qxnh','4':'qxnf','5':'qxnv','6':'qxnx','7':'qxns','8':'qxne','9':'qxnn',
        ',':'..',
        '/':'qxsl',
        #'//':'qxw',
        #'qxslqxsl':'qxds',
        '!':'qxme',
        '#':'qxps',
        '$':'qxds',
        '%':'qxpc',
        '&':'qxam',
        '(':'qxop',
        ')':'qxep',
        '*':'qxst',
        '+':'qxpl',
        '-':'qxsb',
        ':':'qxbb',
        ';':'qxsc',
        '<':'qxlt',
        '=':'qxeq',
        '>':'qxrt',
        '?':'qxum',
        '@':'qxat',
        '[':'qxob',
        "\\":'qxbs',
        ']':'qxeb',
        '^':'qxex',
        '_':'qxun',
        '`':'qxgr',
        '{':'qxos',
        '|':'qxvb',
        '}':'qxes',
        '~':'qxtl',
        #capital replacements
        'A':'qxca',
        'B':'qxcb',
        'C':'qxcc',
        'D':'qxcd',
        'E':'qxce',
        'F':'qxcf',
        'G':'qxcg',
        'H':'qxch',
        'I':'qxci',
        'J':'qxcj',
        'K':'qxck',
        'L':'qxcl',
        'M':'qxcm',
        'N':'qxcn',
        'O':'qxco',
        'P':'qxcp',
        'Q':'qxcq',
        'R':'qxcr',
        'S':'qxcs',
        'T':'qxct',
        'U':'qxcu',
        'V':'qxcv',
        'W':'qxcw',
        'X':'qxcx',
        'Y':'qxcy',
        'Z':'qxcz'
        
        
}
#INSERT Block of code that finds the 0th letter, adds it to the end of the number before, or adds a space before it.
def get_key(_dict,val): 
    for key, value in _dict.items(): 
         if val == value: 
             return key
