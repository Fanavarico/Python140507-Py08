"""
In The Name of GOD

Created on Fri Oct 30 10:19:21 2026

@author: Ali Pilehvar Meibody



L4








Human <----------Python-------> Computer(Binary)

3 bakhsh tagghsim mikrdim

1- Python built in function (tavabe ye dakhelie python)
print() len() type() input()


2- Keywords --> logic (manteghe) barnamaro taghir bdim
if , else, elif , for , while ,.....



3- Variables --> Moteghaywr ha -->
vaghty ke yek value (meghdar) dakhele yek zarf berizim

esme zarf --> sharayet daran

3.1. Numbers --> int, float, complex
        () , = , ** , * , / , + , - 
        c = a * b + c
        a = (a*b) + c
        
        
        if a>10 : 
        
        if (a>10):
            
        
        a = 10 * 2 + 3
        
        print(a) #23
        
        a = (10 * 2) + 3
        print(a) #23
        
        a = 10 * (2+3)
        print(a) #50
        
        comaprisonal --> == != > >= < <=
        
3.2. Boolean --> True False

3.3. String --> reshte ei az character ha --> qutation

name = ali --> zarfe name mosavie zarfe ali
name = 'ali'

a=2
a='2' motefavet hast

index --> 0    zaf[index]  zarf[start:end] end shamel nmishod
str functions --> new_zarf = zarf.lower()
.lower() .upper() ,..... , find() count() ,.... isdigit() 


3.4. iterables --> mutliple values inside one variable berizim 

     3.4.1. List --> default 
             order (index) , changable, allow duplicated
             
             a = [10,20,30,]
             a[index]
             a[start:end]
             a[index] = new_value
             
             list functions --> ina emal mishodan khoroji nmidadan
             zarf.append(10)
             zarf.insert(1,10)
             zarf.clear()......
             
             
      3.4.2. Tuple --> database
          order(index) , unchangable, allow duplicated
          
          tuple yej lliste ke unchanagable
          
          a= (10,20,30,40)
          a=(10,)
          
          a[index]
          a[index] =ew Valeu XXXXXX
          b=list(a)   taggjhir  a=tuple(b)
          
          
       3.4.3. Set --> Mjmooe riazi ha
               no order (index ndre) , unchangabel , no duplicated
               
               a={10,20,30,40}
               
               tavabeye interswection, differenc eejtema eshterak
               
               
               
        3.4.4. Dictionary --> information (etelaat )
        
        
        a=['ali',30,'0912....']
        
        a={'esm':'ali'  ,'sen' :30 }
        
        index value
        
        
        
        key  value
        
        a[key]
        
        a[key]=value
        
        a[new_key]=new_value
        
        tavabe ham dahsta\
            
            

            
"""


#===================================
#===================================
#===================================

sen = 'sahsdjhsddsjh'
print('salam')


'''
sen = 10 , 20 , ....

chon print('salam') hich gone dependency vabastegi ya
hich mashroit nist be khate dige ei

agar yek khat ro shoma mikhahid mashrot kondi , shaerti koni 

---> if --> conditional statameent --> dastoorate sharti

'''


#dar sorati in ejra beshe ke sen bishtr az 20 bashe


sen = 40

if sen>20:
    print('salam')
    


#10 -->sen>20 --> false -->a san baz nmishe -_> ejra nmsihe

#40-->sen>20 --> true --> abz mishe --> print(salam) -->salam

sen = 40

if sen>20:
    print('salam')
    print('khoobi')
    a=10
    b=a+50
    print(b)
    
    
print('khodafez')   

#1 tab -> 4 ta space --> ta madami 1 tab az if fasdeel darim
#body --> badaneye ife 


#40 --> salam khobi, 60 , khodafez
#5--> khodafez

'''
     shart()
       |
       |
    ---------
    |True    | False
    |        |
  Dastoor    |
    |-------|
        |
        |
        |


if --> just if --> fght yedone if -->
rahzan amal mikone -->

yek code az bala maid , fght onaei k esharteshon true hast ro
migire va majbor mikone ke ejra konand



do ta shart



sen >18 , vazn <100 

ham sen>18 ham vazn<100 --> joftesh bayad True beshe

print('salam')
'''

sen = int(input('senet chghdre?:'))
vazn = float(input('vaznet:'))

if sen>18 and vazn<100:
    print('salam')
    


#AND --> 

print(True and True) #True
print(False and True) #False
print(True and False) #False
print(False and False) #False


#and --> zamani True mishe ke hatman joftesh true bashe


#print('salam ) ejra msihe --> zshart true bashe
#shart --> and beyne dotashart
#true --> do joftesh true bashe

#sen>18 ham vazn<100

sen = int(input('senet chghdre?:'))
vazn = float(input('vaznet:'))

if sen>18 and vazn<100:
    print('salam')
     
    
#sen = 10 , vazn = 200 --> ejra nmsihe
#sne=20 , vazn = 110

#sen = 20  , vaazn = 100

#sen = 20  , vazn = 80  --> true



#yeki --> tafsire code --> tafire
#neveshtan --> and ???
#zamani k do shart ya bishtr bashe
#and --> va, ham 

#sharte 1 va sharte 2 
#ham sharte 1 ham sharte2 

#---> shart1 and shart2

#shart --> True false, and


if sen>18 and vazn<100:
    print('salam')
     
    
    
if sen>18:
    if vazn<100:
        print('salam')



#ya --> hjadeaghal yeki ,.....

#ya sen>18 ya vazn <100
#hedaghal senesh >18 ya vaznesh <100
#-->or



print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False



if sen>18 or vazn<100:
    print('salam')
    
#sen>18 vazn<100 ok
#sen>18 ok
#vazn<100 ok    

#hatman joftesh true nashe

#if and and and and :
    
  
#tamame shartaro --> list

#shartz = [sen>18 , vazn<100 ,a>100]
    
#hameye sarta True bshe (and) --> all()
#ya hadegahal yeki #(or) ---> any()


shartz1=[True,True,True]
shartz2=[True,True,False]
shartz3=[True,False,False]
shartz4 =[False,False,False]

all(shartz1) #Out[12]: True
all(shartz2) #Out[13]: False
all(shartz3) #Out[13]: False
all(shartz4) #Out[13]: False



any(shartz1) #true
any(shartz2) #true
any(shartz3) #true
any(shartz4) #false




#shartz = [sen>18 , vazn<100 ,a>100]
#hamash agar hamash true bdo felan chiz ejra bshe

#if all(shartz):
#    dastooor
    



#if any(shartz):
#     dastooor





my_users=['ali','vahid','hamid']

#ali dar in list hast agar bod salam ejra bshe
#true ya false bde

#'ali' in my_users -> True , False
   
if 'ali' in my_users:
    print('salam')

#saalam



if 'reza' in my_users:
    print('salam')
    
#false --> ejra nmsihe


#if my_users.index('ali') != -1:
  
    
#------------------------
if sen>10:
    print('salam')
    
#sen>10 -->  salam

#if sen<=10:

if not sen>10:
    print('salam')
    

if 'ali' not in my_users:
    print('salam')
    
#salam --> age ali dar list nabashe salam
#ag bashe --> hichi


if 'ali' in my_users and 'vahid' in my_users:
    print('salam')
    
    


shartz=['ali' in my_users , 'vahid' in my_users , 'hamid' in my_users]
    
if all(shartz):
    print('salam')



zarf = 'ali'

if zarf :
    print('salam')
    
    

    
zarf = None

if zarf :
    print('salam')
    



#if zarf:
#    zaarf.sukgsdhgfdzv




'''
Conditional Statement --> dastoorate sharti --> 3 ta


1- Just if --> yedone if --> rahzan
yani joloye kasani ro migire k sharteshon --> True hast 

aga shart True --> dastor ro ejra kon
age fals bod -> hichi --> veelsh kon --> kari bash


     shart()
       |
       |
    ---------
    |True    | False
    |        |
  Dastoor    |
    |-------|
        |
        |
        |



2 - if else --> do rahi
agar shart True bood -->< dastoore 1
age false bod -> dastoore 2




     shart()
       |
       |
    ---------
    |True    | False
    |        |
  Dastoor1    dastoor2
    |-------|
        |
        |
        |

    

shart --> true , faklse

treue --> dastore 1
false --> dastore2


shart,dastoor1 , dastoor2


sen>18 --> salam , sen ghanoni nist

        
'''

if sen>18:
    print('salam')
else:
    print('sen ghanoni nist')
    
'''
     sen>18()
       |
       |
    ---------
    |True    | False
    |        |
  salam    sen ghanni nist
    |-------|
        |
        |
        |

'''

#1--> agar code takhfif doros bod bege emal shod
#age nabod -> hichi nage

#just if 


product_name = input('name mahsool chie?:')
code_takhfif = input('code takhfif:')

if code_takhfif=='z12':
    print('doros bood')
    
    
#ag doros bod bege emal shod , age nabod --> code takhfif eshtebahe
#--> dorahi doro skonam
#age shod --> kar1
#ag nashod --> kar2

#if else

product_name = input('name mahsool chie?:')
code_takhfif = input('code takhfif:')

if code_takhfif=='z12':
    print('emal shod')
else:
    print('code takhfif nadorost ast')


'''
11:40
'''
    
#=======================

#Tamrine L3 


#Barresi etelaate vorodi -----
zarf= input('yek reshte :')

print('only digit:',zarf.isdigit())

#.......





#modiriate liste nomarate tamrin

scores = [15,18,12,20,16]

scores.append(19)

print(scores)

scores.remove(12)
print(scores)

scores[1]=17
print(scores)

scores.insert(2,14)
print(scores)


scores.sort()
print(scores)
scores.reverse()
print(scores)


print(len(scores))

    
    
    
#-----tamrin3 

a=[10,20,30]
b=[40,50]

a.append(b)

print(a)
#[10, 20, 30, [40, 50]]

print(len(a)) #4

a[3] #Out[25]: [40, 50]


a.extend(b)
print(len(a)) #6

print(a)

#10, 20, 30, [40, 50], 40, 50]

a=[10,20,30]
b=[40,50]
a.extend(b)

print(a)

#[10, 20, 30, 40, 50]
print(len(a)) #5



#---tamrin4-----
student=('ali',21,'tehran')

print('name daneshjoo:',student[0])
#name daneshjoo: ali

student[1]=22
#TypeError: 'tuple' object does not support item assignment

student_list = list(student)

print(student_list)
#['ali', 21, 'tehran']

print(type(student_list))
#<class 'list'>

student_list[1]=22

print(student_list)
#['ali', 22, 'tehran']


student_list[2]='shiraz'
print(student_list)
#['ali', 22, 'shiraz']

print(type(student_list)) #<class 'list'>

student = tuple(student_list)

print(student)
#('ali', 22, 'shiraz')

print(type(student))
#<class 'tuple'>



#---dictionary
student = { "name": "Ali", "age": 20, "city": "Tehran", "score": 17}

print(student['name']) #Ali
student.get('name')

student['something']
#TypeError: tuple indices must be integers or slices, not str

student.get('something') #None
student.get('something','felan')


print(student['score']) #17


student['university'] = 'UT'

student.update({'university':'UT'})

#student['city'] = 'shiraz'
student.update({'city':'shiraz'})
    

zarf = student.get('phone','Not Found')



student = { "name": "Ali", "age": 20, "city": "Tehran", "score": 17}

if student.get('phone') == None:
    print('Not found')

#Not found


if zarf :
    print('salam')

student.keys()

student.values()

print(student)





#---systeem etebarsanjie code takhfif

product_name = input('name mahsool:').strip().title()
product_price = float(input('gheyamte mahsool:'))
discount_code = input('code takhfif:')


#zarfe_jadid = product_name.function()


if discount_code.upper()=='PYTHON20':
    product_price = 0.8 * product_price 
    

print(product_price)



#-----------
product_name = input('name mahsool:').strip().title()
product_price = float(input('gheyamte mahsool:'))
discount_code = input('code takhfif:').upper()

'''
agar code dorso bood -> 20% takhfi
agar nabdo --> hamon gheymat

if else

shart 1 ---> 


'''

if discount_code=='PYTHON20':
    final_price  = 0.8 * product_price
    print(final_price)
else:
    print(product_price)


    







if discount_code=='PYTHON20':
    final_price  = 0.8 * product_price
else:
    product_price = product_price
    
print('product_name',':',product_name,'orifinal price:',product_price,'final_price',final_price )

#har variable e k fght dar yek if ya else sakhti 
#nmitoni dar edame azash estefade koni -->



if discount_code=='PYTHON20':
    final_price  = 0.8 * product_price
else:
    final_price = product_price
    
print('product_name',':',product_name,'orifinal price:',product_price,'final_price',final_price )



'''
1----> just if

shart --> 

agar true bood --> ejra bshe
age false --> hich


     shart()
       |
       |
    ---------
    |True    | False
    |        |
  Dastoor    |
    |-------|
        |
        |
        |




dastoor -->1 khat chandin khat --> madami yek tab jolo

if shart:
    dass
    dass
    dasss
    dadssss
    
    
    



2 - if else --> do rahi
agar shart True bood -->< dastoore 1
age false bod -> dastoore 2




     shart()
       |
       |
    ---------
    |True    | False
    |        |
  Dastoor1    dastoor2
    |-------|
        |
        |


if shart:
    dastorr11
    dsdds
    dssdsdsd
    dsdsdd
    dssdsdd
else:
    dastppr2
    sasdd
    dsssd
    dsdsdss
    



3-----> if else elif


if sen>18 ---> salam

--> ghanoni nist



if sen>18:
    print('salam')
else:
    print('ghanoni nist')



>18 --> salam
<18 ------> aya >15 --> eb ndre  <15 -> be hich onvan


dorahi haye to dar tooo


if else elif

     shart1
       |
       |
    ---------
    |True    | False 
    |        |
  dastoo1      shart2
    |         |
    |    ----------
    |    |True    | 
    |   eb ndre    be hich onvan
    |----|       |
    |     ---------
    -----------
        |
        |




    shart
      |
      |
   ---------
   |True    | False <18
   |        |
 sakam       sen>15
   |         |
   |    ----------
   |    |True    | 
   |   eb ndre    be hich onvan
   |----|       |
   |     ---------
   -----------
       |
       |



    
    shart1
      |
      |
   ---------
   |True    | False 
   |        |
 dastoor1   shart2
   |         |
   |    ----------
   |    |True    | false
   |   das2    das3
   |----|       |
   |     ---------
   -----------
       |
       |


if shart1:
    das1
elif shart2:
    das2
else:
    das3




    shart1
      |
      |
   ---------
   |True    | False 
   |        |
 dastoor1   shart2
   |         |
   |    ----------
   |    |True    | false
   |   das2    shart3
   |----|       |
   |    ----------
   |    |True    | false
   |   das3    das4
   
   |     ---------
   -----------
       |
       |


if shart1:
    dast1
elif shart2:
    dast2
elif shart3:
    dast3
else:
    dast4
    
    





'''

#1---->
#just if ----> >18 --> salam , gheyresh --> chich
if sen>18:
    print('salam')



#2---->if elsde -> do rahi

if sen>18:
    print('salam')
else:
    print('gheyre ghanoni')



#3---> 
if sen>18:
    print('salam')
elif sen>15:
    print('eb nadare')
else:
    print('b hich onvan')
    
    
    
'''

age yechi bkehay catch --> error, sharti -> rahzan
--> just if 



age bekahhi dorahi baz koni, dorah --> if else



age dorahi haye too dar too -->
    --> mutliple selection 
    --> range 


'''

#adade 1 bgirid az user , 2vom begiri 
#bad yek operation (jam,tafrigh,taghsim,zarb)


#agar jam ro entkehab krde bood --> +  print
#agar tafrigh ---> - print
#agar taghsim -> / print


numb1 = float(input('adade avaleto befres:'))
numb2 = float(input('adade dovometo befres:'))
operation = input('amaliateto befres(jam,tafrigh,tagghsim,zarb):')

#agar operation=='jam' --> numb1 + nujmb2

if operation =='jam':
    result  = numb1 + numb2
    print(result)
    
    
if operation =='tafrigh':
    result  = numb1 - numb2
    print(result)
    
   
if operation =='zarb':
    result  = numb1 * numb2
    print(result)
    
    
    
if operation =='taghsim':
    result  = numb1 / numb2
    print(result)
    
#Logic --> doroste
#efficient , optimize



'''


     agar jam
       |
     ----------- 
     |           |
     +          tafrigh
     |       -----------
     |        |
     |        -          zarb
     |                    |
     |              ----------
     |              *       TAGHSIM
     |                       |
     |                  -----------
     |                  /        |
     |                         eshtebah neveshti
     |                             |
     -------------------------------
                 |
                 |


''' 



numb1 = float(input('adade avaleto befres:'))
numb2 = float(input('adade dovometo befres:'))
operation = input('amaliateto befres(jam,tafrigh,tagghsim,zarb):')

if operation=='jam':
    print(numb1+numb2)
elif operation=='tafrigh':
    print(numb1 - numb2)
elif operation=='zarb':
    print(numb1 * numb2)
elif operation =='taghsim':
    print(numb1 / numb2)
else:
    print('shoma bayad yeki az in 4 gozine ro entkehab konid (zarb,tafrigh,taghsim,jam')


#---range

#score daneshjo o begir

#20-18 --> A
#18-16 --> B
#16-14 --> c
#14-10 --> d
#<10 --> f

score = float(input('scoret ro begoo:'))


#if score<20 and score>18: #  18<x<20
    

#if 18<score<20:
#    print('salam')
    

score = float(input('scoret ro begoo:'))

if score>20:
    print('socret bish az 20 nmitavamnd bashad')
    #raise ValueError('socret bish az 20 nmitavamnd bashad')
elif score>18: #18<x<20
    print('A')
elif score>16: #16 < x <18
    print('B') 
elif score>14: #14 < x <16
    print('C')
elif score>10: #10<x<14
    print('D')
elif score>0: #0<x<10
    print('F')
else : #0<
    print('nomre nemitavand manfi bashad')
    

'''
    adad    ---   -----   --- 
    

-binahyaat        0     10     14   16  18   20      + Binahayat
           ------    F      D     C    B   A   --------




just if --> catch jkonim 

if len(password)<8:
    print('errorr')





if else --> dorahi darim
agar code takhfif doros bod emal jkon age nabod gheymat asli




if elif -->     dorahi haye to dar too
    muyltiple selection , jam , tafrigh 
    range --->
    
'''
    


'''

Az user vazn va ghadesho bgirid , BMI esho ehsab koni

BMI = vazn / ghad**2


>=40 --> chaghi mofrat
25 =< BMI <40 --> ezafe vazn
18.5 =< BMI < 25 --> normal
<18.5 laghari



'''

vazn = float(input('vaznet chegahdre ?:'))
ghad = float(input('ghadet cheghadre?:'))

BMI = vazn / (ghad**2)

if BMI>=40:
    print('chaghi mofrat')
elif BMI>=25:  #<40 --> >25
    print('ezafe vazn')
elif BMI>=18.5:  #18.5 --> 25
    print('normal')
else:
    print('laghari')



#----andle

vazn = float(input('vaznet chegahdre ?:'))
ghad = float(input('ghadet cheghadre?:'))

BMI = vazn / (ghad**2)

if BMI>=40:
    print('chaghi mofrat')
elif BMI>=25:  #<40 --> >25
    print('ezafe vazn')
elif BMI>=18.5:  #18.5 --> 25
    print('normal')
elif BMI>=0 : #0 <---<18.5
    print('laghari')
else: #<0
    print('BMI nemitavand manfi shavad')


#------
vazn = float(input('vaznet chegahdre ?:'))

ghad = float(input('ghadet cheghadre?:'))



if vazn<0 or ghad<0:
    #print('vazn va gahd nmitavand manfi bashad')
    raise ValueError('vazn va gahd nmitavand manfi bashad')

    
BMI = vazn / (ghad**2)

if BMI>=40:
    print('chaghi mofrat')
elif BMI>=25:  #<40 --> >25
    print('ezafe vazn')
elif BMI>=18.5:  #18.5 --> 25
    print('normal')
else:
    print('laghari')


#------
vazn = float(input('vaznet chegahdre ?:'))

ghad = float(input('ghadet cheghadre?:'))

#checks= [vazn>0 , ghad>0 , ghad!=0]
checks= [vazn>0 , ghad>0 ]

if all(checks):
    BMI = vazn / (ghad**2)
    
    if BMI>=40:
        print('chaghi mofrat')
    elif BMI>=25:  #<40 --> >25
        print('ezafe vazn')
    elif BMI>=18.5:  #18.5 --> 25
        print('normal')
    else:
        print('laghari')

else:
    print('adad na motabar ast')
    
    
    
#------------
vazn = abs(float(input('vaznet chegahdre ?:')))
ghad = abs(float(input('ghadet cheghadre?:')))


BMI = vazn / (ghad**2)

if BMI>=40:
    print('chaghi mofrat')
elif BMI>=25:  #<40 --> >25
    print('ezafe vazn')
elif BMI>=18.5:  #18.5 --> 25
    print('normal')
else:
    print('laghari')







#----------------------------------------------


print('salam')




print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')






print('salam')

#chon mikhahim mnatyeghe baranamro beham bznim


#repeat(10):
#    print('salam')



'''
,masale --> yek dastoor ro chandin bar tekrar konim


puython chize amdeie bename repeat nadare
repat(10)--> n dastooro

for ---> manteghe

shoamrande --> zarf --> i  , j , k , esm,,...

be ezafe in zarfe i dar yek list 

i= 1 -->dastoro ejra --> print('salam') -->salam
i = 2--> dastoro ejra kon --> print('salam') -->salam
i=3 -->dastoro ejra kon-->print('salam') -->salam
i=4 --> dastoro ejra kon --> print('salam') 
i=5 --> dastor ejrs ->print(salam) -->salam

'''

for i in [1,2,3,4,5]:
    print('salam')
    
    


#10
#--#----------

print('-'*10) #----------





print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 
print('-'*10) 





#yek khat ino benevisam 10 bar ejra konm

#repeat(10):
#    print('-'*10) 
    


#for --> shoamrande i --> [] list -->

for i in [1,2,3,4,5,6,7,8,9,10]:
    print('-'*10)
    
    
'''
zarf --> i -->

i=1 --> dastoro ejra mikone -->print('-'*10) --> ----------

i= 2 -->datdoro ejra 



i=10 


----------
----------
----------
----------
----------
----------
----------
----------
----------
----------




'''



for i in ['ali','vahid','hamid']:
    print('salam')
    
    
    
'''

zarf --> i -->

i=ali --> dastroo ejra mikone --> print('salam') -->salam
i=vahid --> dastoro ejra mikone -->print('salam') -->salam
i = hamid --> dastoro ejra mikone -->print('salam') -->salam

'''


for i in ['ali','vahid','hamid']:
    print('salam')
    
    
    
    
    
for i in [1,2,3]:
    print('salam')
    
    
    
for i in [12,189,3223]:
    print('salam')
    
    






for i in ['ali','vahid','hamid']:
    print('salam',i)
    
    
'''
i=ali --> dastoro ejra mikone -->print('salam',i) --> print('salam','ali') -->salam ali
i = vahid --> dastoro ejra mikone -->print('salam',i)--> print('salam','vahid') --> salam vahid
i = hamid --> dastoro ejra mikone --> print('salam',i)-->print('salam','hamid') -->salam hamid


salam ali
salam vahid
salam hamid



'''

for i in ['ali','vahid','hamid']:
    print('salam','i')
    
'''
salam i
salam i
salam i
'''


#Loop --> halghe ha 

#static repeat , dynamic repeat()

'''
Takalif .....
matn ---> 




'''

    
