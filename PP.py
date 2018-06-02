import os
def sa(s):
    return s.strip('\n').strip(',')+'\n'
def op(i):
    f=open("srt//"+i,'w',encoding="utf-8")
    orr=open("musixmatch//"+i,'r',encoding="utf8")
    file=open("orginal.srt",encoding="utf-8")
    text=list()
    c=0
    for j in orr:
        if(j!='\n'):
            text.append(j.strip(','))
      
    
    for k in file:
        if(k.upper().isupper()):
            f.write(sa(text[c])+'\n')
            c+=1
        else:
            f.write(k)
    print(i)
if("srt" not in os.listdir()):
    os.mkdir("srt")
ls=os.listdir("musixmatch")
print(ls)

for i in ls:
    print(i)
    op(i)

    
    
    
    
    
    

