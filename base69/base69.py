
convertion_table = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z',36:'a',37:'b',38:'c',39:'d',40:'e',41:'f',42:'g',43:'h',44:'i',45:'j',46:'k',47:'l',48:'m',49:'n',50:'o',51:'p',52:'q',53:'r',54:'s',55:'t',56:'u',57:'v',58:'w',59:'x',60:'y',61:'z',62:'+',63:'/',64:'=',65:'@',66:'*',67:'-',68:'!',69:'#'}

def encode_base69(input):
        if type(input) == int:
            base69 = ''
            while input > 0:
                remainder = input % 70
                base69 = convertion_table[remainder] + base69
                input = input // 70
            base69 = '69*|' + base69
            return base69
        elif type(input) == str:
            return "We only support integers for now"


def decode_base69(input):
    input = input[4:]
    base = 0
    for i in range(len(input)):
        base += list(convertion_table.keys())[list(convertion_table.values()).index(input[i])] * (70 ** (len(input) - i - 1))
    return base



