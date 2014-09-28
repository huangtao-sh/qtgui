from re import compile
from codecs import BOM_UTF8,BOM_LE,BOM_BE
# 写文本文件，使用utf-8编码，不带BOM
def write_file(file_name,text,encoding='utf-8'):
    with open(file_name,'w',encoding=encoding) as fn:
        if isinstance(text,list):
            fn.writelines(text)
        else:
            fn.write(text)
        
BOM_CODE={
    BOM_UTF8:'utf_8',
    BOM_LE:'utf_16_le',
    BOM_BE:'utf_16_be',
    }
    
DEFAULT_CODES=['utf8','gbk','utf16','big5']

def decode_file(d):
    for k in BOM_CODE:
        if k==d[:len(k)]:
            text=d[len(k):].decode(BOM_CODE[k])
            return text.splitlines()
    for encoding in DEFAULT_CODES:
        try:
            text=d.decode(encoding)
            return text.splitlines()
        except:
            continue
    raise Exception('解码失败')    

# 全部读取文件，并进行解码，解码失败则触发异常
def read_file(file_name):
    with open(file_name,'rb')as fn:
        return decode_file(fn.read())
    
class element:
    def __init__(self,tag=None,attrib=None,data=None):
        if tag:
            self._data=[tag,attrib,None]
        else:
            self._data=data
        if self._data[1]==None:
            self._data[1]={}
        if self._data[2]==None:
            self._data[2]=[]

    @property
    def tag(self):
        return self._data[0]

    @tag.setter
    def tag(self,v):
        self._data[0]=v

    @property
    def attrib(self):
        return self._data[1]
    
    @attrib.setter
    def attrib(self,v):
        self._data[1]=v

    def childs(self):
        return [child for child in self]

    def __iter__(self):
        for child in self._data[2]:
            yield element(data=child)

    def append(self,element):
        self._data[2].append(element._data)

    def to_text(self,level=0):
        s='    '*level+self.tag
        for k in self.attrib:
            v=self.attrib[k]
            if isinstance(v,str):
                v='[%s]'%(v)
            s+=(' %s=%s'%(k,v))
        s=[s,]
        for c in self:
            s.append(c.to_text(level+1))
        return '\n'.join(s)
    def to_xml(self,level=0):
        t=[]
        for k in self.attrib:
            v=self.attrib[k]
            t.append('%s="%s"'%(k,v))
        s=['%s<%s %s'%('    '*level,self.tag,' '.join(t)),]
        for c in self:
            s.append(c.to_xml(level+1))
        if len(s)>1:
            s[0]+='>'
            s.append('%s</%s>'%('    '*level,self.tag))
        else:
            s[0]+='/>'

        return '\n'.join(s)

def sub_element(elem,tag=None,attrib=None,data=None):
    e=element(tag,attrib,data)
    elem.append(e)
    return e

def parser(file_name=None,content=None):
    partten=compile(r'( *)(?:'
        r'([a-zA-Z_][a-zA-Z0-9_]*)\s*'
        r'(?:=\s*(".*?"'
        r"|'.*?'"
        r'|\[.*?\]'
        r'|0[xX][0-9a-fA-F]+|[+-]?\d+\.?\d*'
        r'|[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*'
        r'))?'
        r')?(#.*$)?'
        )    
    
    owner=[]
    owner_count=0
    if file_name:
        lines=read_file(file_name)
    elif content:
        lines=content.splitlines()
    for line in lines:
        t=partten.findall(line)
        if t:
            level=t[0][0].count('    ')
            attr={}
            tag=None
            for r in t:
                if r[1] and r[2]:
                    v=r[2]
                    if v[0]=='[':
                        v=v[1:-1]
                    attr[r[1]]=v
                elif r[1]:
                    tag=r[1]
                if(tag is None)and attr:
                    tag='property'
        if tag:
            node=element(data=[tag,attr,None])
            if level:
                owner[level-1].append(node)
            if level<owner_count:
                owner[level]=node
            else:
                owner.append(node)
                owner_count+=1
    return owner and owner[0] 
                
