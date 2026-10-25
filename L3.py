"""
In The Name of God
Created on Fri Oct 23 10:28:12 2026

@author: apm





Human (en,fa) <-----Python -------> Machine (0,1bainary)




Computer pythono ---> 
    1- Ipython kernelo berizid (python)
    2- Editor/IDE 
    
raveshe basic --> pythono download, spydero download 

root (kole computeret ) ham python ham spyder


Anaconda --> distrubter 
Evuironment haye mokhtalef besazim --> chandin pythono spyder 
project (porozhe) --> professional (herfei , standard)




Tooye python shoro b code zadi mikonid
ta zamani k code minevisi chizi etefagh nmiofte
vaghty ke run mizni --> IDE/EDITOR ---> Ipython -->
machine --> javabo barmigrdone --> console


az bala be paein , az chap be rast
harja error khord ghat mishe edame nemide --> 
error --> console


comment # qutation estefade 

pythonic code bzni 



kole python b chan bakhsh taghsim

1- Python built in fucntion (tavabe dakheli python)
yek amalkard daran
print() --> namayesh
len() ---> tool
type() --> no
input() --> vorodi migire 
....


input() ---> in yek tabe hast --> print() aval kar mikone

esm = input('esmet chie?')

dota nokte

nokteye 1 --> hamishe string mide , '15'

esm = int(nput('esmet chie?')) #sen  ,... 

esm = float(nput('esmet chie?')) #price , vazn , ....


nokteye 2 --> az bala be paein chap b rast , ipython
vaghty b input brese --> wait mikone . ya shoma bayad
ykchizi vared konid ya stopo




narenji --> man mishnasam 


2- Keywords --> vaghty bekhahim logic ro taghir bdim

if , else, elif , for , while ,.........


Unknown --> nemishnase --> sefid
esme yek zarf 

3- variables

esme zarf --> zarf daeim dakhelesh megdhar mirizim
va megdhar hay emtoefavet

shorot dashtim abraye esme zarf .

    3.1. Numbers (int,float,complex)
        arithmatic operation (** , * , / , // , + , -)
        compatisonal operation ( == , != , > , >= , < , <=)
        
    3.2. Boolean (True , False)
    
    3.3. String (reshte) --> reshte ei az characteer haye keybaord
    
    esm = 'dsgsdidsh'
    esm = ali
    esm = 'ali'
    
    esm[0]='b'  #Unchangable
    
    --> .replace('a','b')
    
    esm ='2'
    a = 2
    
    print(zarf)
    
    print(type(zarf)) #str
    print(len(zarf)) #andaxze
    
    
    access --> dastressi --> index --> 0 
    
    zarf[index]
    
    zarf[0] -->indexe 0 ro bde
    
    zarf[-1] ---> az akhar bede
    zarf[-2]  az rast 
    
    
    slicing --> yek bajkhshi az kalame
    
    zarf[start:end]  end is excluded 
    zarf[2:5]  -->2,3,4 ro bde
    
    zarf[2:5:1]
    zarf[2:5:2]
    
    zarf[start:end:step]
    
    
    
    str functions (methods) --> yekseri tavabe
    boodan k fght baray kjian?? baraye str ha
    
    Strings --> lower()
    
    
    zarf='ali'
     
    lower(zarf) xxxxx
    zarf.lower()
    
    
    3 no boodan 
    
    in tavabe emal nemishan, khoroji midan
    
    new_zarf = zarf.lower()
    
    noe A--> convert
    
    new_zarf = zarf.lower()
    zarf.upper()
    zarf.title()
    zarf.capitalize()
    zarf.replace()
    zarf.strip() 
    zarf.rstrip() .lstrip()
    
    
    
    
    noe B -->  Adad pas midadan 
    
    zarf.count('a')  #---> adad   , 0
    
    zarf.find('a') #--> -1   , az chap avalino peyda kone indexo
    
    zarf.index()
    
    
    noe C --> True , False 
    
    isupper()
    islower()
    isdigit() #aya hamash az adade
    isalpha()
    isalnum()
   
    
   3.4.Iterabless
   chandin meghdar dakhele yek moteghayer
   mutliple values inside one variable
   
       3.4.1. List  --> order (index) , changable, allow duplicated
       
       
    
    
    
    
    
    
    
    

"""

zarf = 'ali'


zarf[0] #Out[1]: 'a'

zarf[2] #Out[2]: 'i'

zarf[-1] #Out[3]: 'i'
zarf[-2] #Out[4]: 'l'
zarf[-3] #Out[5]: 'a'



zarf = 'ali'


zarf[-1] #i

zarf[-1:] #Out[6]: 'i'

zarf[-1::-1] #Out[7]: 'ila'

zarf[::-1] # Out[9]: 'ila'






zarf = 'ALI'


new_zarf = zarf.lower()

print(zarf) #ALI --> emal nemishan 
print(new_zarf) #ali

#emal nemishan , khoroji midan


zarf ='ALI  '

new_zarf = zarf.lower()

new_zarf2 = new_zarf.strip()



#-------
zarf ='ALI  '

new_zarf = zarf.lower().strip()






#-------------------------------------
#emal msihan , khoroji nemidan



#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#product_name = input('esme mahsoolet chie?:').title().strip()


product_name = input('esme mahsoolet chie?:')


product_price = float(input('gheymate mahsool?:'))


#final_price = product_price - (25/100) * product_price
final_price = 0.75 * product_price
final_name = product_name.title().strip()


#print('gheymate nahaeie mahsoole',final_name,'hast:',final_price)

print(f'gheymate mahsoole {final_name} hast {final_price}')

'''
esme mahsoolet chie?:zara
gheymate mahsool?:100
gheymate mahsoole Zara hast 75.0
'''



#-----------

product_name = input('esme mahsoolet chie?:')
product_price = float(input('gheymate mahsool?:'))
discount = float(input('darsadde takhfif bede(0-100):'))

#final_price =product_price - (discount/100) * product_price
final_price = (1 - discount/100) *  product_price 
final_name = product_name.title().strip()

print(f'gheymate mahsoole {final_name} hast {final_price}')

'''
esme mahsoolet chie?:zara
gheymate mahsool?:100
darsadde takhfif bede(0-100):40
gheymate mahsoole Zara hast 60.0
'''



'''
esme mahsoolet chie?:zara
gheymate mahsool?:120
darsadde takhfif bede(0-100):120
gheymate mahsoole Zara hast -23.999999999999993
'''


#------------
esm  = input('esmet chie?:') #.replace(' ','')
tedad_character = int(input('tedade charactere esmet chghdre?:'))

#len(esm) toole reshte  --> source of truth
#tedad_character --> claim 
print(len(esm)==tedad_character)


'''
esmet chie?:ali
tedade charactere esmet chghdre?:3
True



esmet chie?:ali
tedade charactere esmet chghdre?:4
False
'''


#-----------------------------------------
#-----------------------------------------
#-----------------------------------------

#yek value ro berizim dakhele yek zarf 

# a = 10

# a = 10.3323
# city = 'Tehran'


#man bekham multiple values inside one variable
#chandin megdhar dakhele yek zarf (moteghayer)

#iterables --> ghabele iteration hastan

'''
Iterables --> 
    1- List
    2- Tuple
    3- Set
    4- Dictionary
    
'''


#----------------------------------------
'''        3.4.1. List        '''
#----------------------------------------

#definition -----------

#10,20,30,40,50 

zarf  = [10,20,30,40,50]

zarf  = [10,10,10,40,50]


#esm = beraket[element , element , ]
zarf  = list([10,20,30,40,50])


#adad bzari ? 
#Mutliple values --> hachi

zarf = [10,10.3434 , True, 'Ali']


print(zarf) #[10, 10.3434, True, 'Ali']

print(type(zarf)) #<class 'list'>

print(len(zarf)) #4 #tedad eleement




#access-----------

#ye element ro mikham

zarf[0] #Out[27]: 10


zarf = [10,10.3434 , True, 'Ali']

zarf[2]



#slicing------------

zarf[0:3] #0 1 2

new_zarf =zarf[0:3]

print(new_zarf) #[10, 20, True]




#change ?? --------------------
#str unchanagbale --> list changable

#10.3434 ---> 20

#acccsess --> indexe ? 0--> 1

zarf[1] = 20

print(zarf) #[10, 20, True, 'Ali']



#---------------------
# List functions --------> tavabe ei k baraye ?
#baray list ha 

#.insert()


#zarf.tabe()

#zarf.tabe()



#farghe str function va list fucntion

#1--> function ha baraye listan, baraye str ha
#2** --> emal mishan, khoroji nemidan .

#zarf.felan()  
#rooye zarf emal mishe
zarf = [10,20,30,40]

zarf[1] = 100

print(zarf) #[10, 100, 30, 40]

#jaye indexe 1 100 shode



#dar indexe 1 , felan adado incorporate 

#insert()


zarf = [10,20,30,40]

#index, value 
#1 , 100

#.insert(index,value)

zarf.insert(1,100)


print(zarf) #[10, 100, 20, 30, 40]


#---------------------------
#---------------------------
zarf = [10,20,30,40]


zarf.insert(3,100)
print(zarf) #[10, 20, 30, 100, 40]




zarf = [10,20,30,40]

zarf.insert(4,100)
print(zarf) #[10, 20, 30, 40, 100]



#zarf.insert(10,100)
#print(zarf) #[10, 20, 30, 40, 100, 100]



#tabe --> append()

zarf = [10,20,30,40]
zarf.append(100)
print(zarf) #[10, 20, 30, 40, 100]





#---remove()

zarf = [10,20,30,40]

#.remove(element)

zarf.remove(20)

print(zarf) #[10, 30, 40]




#.pop(index)
#ham emal mikone ham khoroji mide 
zarf = [10,20,30,40]

zarf.pop(1)

#new_zarf = zarf.pop(1)

#rooye zarf emal mishe --> [10,30,40]
#on chizi k hazf krde ro --> 20 

#zzarfe khali
zarf = []




zarf = [10,20,30,40]

zarf.clear()

print(zarf) #[]
#.clear()



#kole zarfo ba jash hazf koni 

#keyword 

del zarf 

#print(zarf) #NameError: name 'zarf' is not defined
#har variabli --> del delete koni



#----------------------------
a=[10,20,30]
b=[40,50,60]


#b ro b a ezafe konam, b tahesh

a.append(b)


print(len(a)) #4

print(a)
#[10, 20, 30, [40, 50, 60]]
# 4 ta element 

a[3] #Out[57]: [40, 50, 60]


#nokte --> append(element)

#element haye dakhele yek listo brizi tahe on yeki list

#extend()


a=[10,20,30]
b=[40,50,60]


a.extend(b)


print(a) #[10, 20, 30, 40, 50, 60]

print(len(a)) #6



#-----------------
a=[10,20,30]
b=a

a.append(40)

print(a) #[10, 20, 30, 40]
print(b)  #[10, 20, 30, 40]


#list ha -->b = a --> har kari k rooye a anjam bdi
#rooye a ham anjam mishe

#copy begiri on lahze , snapshot begiri az a 
a=[10,20,30]
b=a.copy()
a.append(40)

print(a) #[10, 20, 30, 40]
print(b) #[10, 20, 30]




a=[10,20,30]
a.count(10) #Out[67]: 1


a.index(10) #0







a=[10,80,60,100]
a.sort()
print(a) #[10, 60, 80, 100]


a.reverse()
print(a) #[100, 80, 60, 10]




b=[100,60,40,20]

b.reverse()

print(b) #[20, 40, 60, 100]

#reverse mikone dostan 


#reevrse() kari b tartib ndre



#reverse sorting --> .sort().reverse()





a=['zara','ali','baran']

a.sort()


print(a) #['ali', 'baran', 'zara']


a=['zara','ali','baran','Ali']

a.sort()

print(a) #['Ali', 'ali', 'baran', 'zara']

#aval bozorga sort mikone
#kochikaro sort mikone



a=['zara',100, 'ali',10, 'baran','Ali']
a.sort()

print(a)

#TypeError: '<' not supported between instances of 'int' and 'str'

#.sort() --> tamaman str darid
#.sort() --> tamaman adad darid


a=['zara', 'ali', 'baran','Ali','@','2']

a.sort()

print(a) #['2', '@', 'Ali', 'ali', 'baran', 'zara']
#0 1 2 3 4... ! @ # $ % ^ & * () .......





'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''




'''
az user
esme mahsool ro begire
code mahsool ro begire
gheymate mahsool ro begire

3 ta sho **done done** berize too yek list 
bename product_information

bad print kone gheymate mahsole .. ba code ... hast .. 
az **list inaro bekeshe** biron va print kone



'''
product_information=[]

product_name = input('ESME mahsool?:')
product_information.append(product_name)

product_code = input('code mahsool:')
product_information.append(product_code)

product_price = float(input('price mahsool:'))
product_information.append(product_price)
#product_information = [product_name,product_code,product_price]

#print(product_information) #['zara', 'z1', 100.0]

#print('gheymate mahsole',product_name,'ba code',product_code,'hast',product_price)
#print('gheymate mahsole',product_information[0],'ba code',product_information[1],'hast',product_information[2])
print(f'Gheymate mahsoole {product_information[0]} ba code {product_information[1]} hast {product_information[2]}')

'''
ESME mahsool?:zara
code mahsool:z10
price mahsool:10
Gheymate mahsoole zara ba code z10 hast 10.0
'''




#================================
'''

Iterables --->
multiple value in one variablae
chandin meghdar dar yek zarf


    List --> order(index) , changable , allow duplicated
    
    Tuple --> order(index) , unchnagble , allow duplicated
            listi hast k changable nist
            
    set --> no order(no index) , unchangable , No duplicated
        --> set haye riazi majmoe haye riazi
            
            
        




'''


a_list= [10,20,30,40]
a_list= list([10,20,30,40])


#parantez
b_tuple = (10,20,30,40)
b_tuple=tuple([10,20,30,40])


print(b_tuple) #(10, 20, 30, 40)
print(type(b_tuple)) #<class 'tuple'>
print(len(b_tuple)) #4


#access ---------

a_list[0] #Out[87]: 10

b_tuple[0] #Out[88]: 10



a_list[0:2] #Out[89]: [10, 20]
b_tuple[0:2] #Out[90]: (10, 20)





#---change-------
a_list[0]=100
print(a_list) #[100, 20, 30, 40]


b_tuple[0]=100
print(b_tuple)
#TypeError: 'tuple' object does not support item assignment



#tuple --> gheyre ghabele change
#tuple ---> list --> taghir
#list --> tuple 

print(b_tuple) #(10, 20, 30, 40)
print(type(b_tuple)) #<class 'tuple'>
b_tuple[0]=100 #TypeError: 'tuple' object does not support item assignment

#casting 
a = list(b_tuple)
print(a) #[10, 20, 30, 40]
print(type(a)) #<class 'list'>

a[0]=100
print(a) #[100, 20, 30, 40]

b_tuple = tuple(a)

print(b_tuple) #(100, 20, 30, 40)
print(type(b_tuple)) #<class 'tuple'>



#tuple function -->
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

'''





b = (10)

print(type(b)) #<class 'int'>


b = (10,)
print(type(b)) #<class 'tuple'>


b = ()


#----------------------------


c = {10,20,30}
c=set([10,20,30])

#**sete khali {}



print(c) #{10, 20, 30}

c[0] #TypeError: 'set' object is not subscriptable



a=[10,20,30]
b= (10,20,30)
c= {10,20,30}

#soal tarh akrdan --> 
#broo y loisti drim felan kon inkar kon onkar kon 
#yek listi bargardon k tekrari tooshnabashe



d = [10,10,10,20,30,50]

zarf = set(d)

print(zarf) #{10, 20, 50, 30}



a={10,20,30}
b={20,30}


a.difference(b) #Out[110]: {10}


a.intersection(b) #Out[111]: {20, 30}


'''

Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

'''



#============================================
'''
iterables --->
    list --> order(index),changable, allow duplicated
    []  ,[index]  [index]=new  .append() .insert() .remove() .pop()
    
    tuple --> order(index) , unchangable, allow duplicated
    () (,)  [index]  no , Casting , ;...
    Database va functions 
    
    
    set --> no order , unchangable, no duplicated
    sete riazi, hazfe element haye tejkrari
    {} ,... .difference() .intersection() ....
    
    

'''



a=['ali',30,'0912....','Iran','ai....@gmail.com']



a[3]='Switzerland'

a[2]='0919...'


#100 ta infromation dashte bashe ,

#-
#a['country'] = 'switzerlan'

#a['phone'] = '0919...'


'''
list

index    value
0         10
1          valu2



tuple
index    value
0        val1
1        val2


set 
value
val1
val2



dictionary
key  value
key1  val1
key2  val2
key3 val3





a=['ali',30,'0912....','Iran','ai....@gmail.com']

list
index     value
0           ali
1            30 
....

a[0]




dictionary
key         value
esm         ali
sen          30



a[esm]



'''


a=['ali',30,'0912....','Iran','ai....@gmail.com']

#b = { element1  , .....}
#b = {key:element  , ....}

b = {'esm':'ali' , 'sen':30 ,'phone' :'0919,..'}

a[0] #Out[117]: 'ali'

a[0]='reza'




b['esm'] #Out[118]: 'ali'
b['esm'] = 'reza'

#kilidvazhe mitavand yektya bashe --> esm yedonas



#------------------------------------
#------------------------------------
#------------------------------------
#sakht ...........

b = {'esm':'ali' , 'sen':30 ,'phone' :'0919,..'}


#access-------
#esm ro begiram
b['esm'] #Out[120]: 'ali'
b['shahr'] #KeyError: 'shahr'


#standard tare ---->
b.get('esm') #Out[122]: 'ali'
b.get('shahr') #None #error behet nmide
b.get('shahr','tehran')  #ag shahr  #Out[124]: 'tehran'





#---------------------------
#elemeneto change konm

#b['esm']='reza'

b.update('esm','reza')
#TypeError: update expected at most 1 argument, got 2

b.update({'esm':'reza'})

print(b) #{'esm': 'reza', 'sen': 30, 'phone': '0919,..'}



#ezafe

#esm, sen , phone

b['country'] ='iran'

print(b)
#{'esm': 'reza', 'sen': 30, 'phone': '0919,..', 'country': 'iran'}



b.update({'shahr':'tehran'})
print(b)
#{'esm': 'reza', 'sen': 30, 'phone': '0919,..', 'country': 'iran', 'shahr': 'tehran'}



'''

Loops

Keys()
values()
items()


'''


#--------kilidha------------
zarf = b.keys()

print(zarf)
#dict_keys(['esm', 'sen', 'phone', 'country', 'shahr'])

print(type(zarf)) #<class 'dict_keys'>

zarf = list(b.keys())
print(zarf) #['esm', 'sen', 'phone', 'country', 'shahr']
print(type(zarf))




zarf = b.values()
print(zarf) #dict_values(['reza', 30, '0919,..', 'iran', 'tehran'])

print(type(zarf)) #<class 'dict_values'>

zarf = list(b.values())
print(zarf)
print(type(zarf))



b.items()
'''
Out[140]: dict_items([('esm', 'reza'), ('sen', 30), ('phone', '0919,..'), ('country', 'iran'), ('shahr', 'tehran')])
'''


'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''



'''
Variables

zarf --> meghdar


    1-Numbers
    2- Boolean
    3- string
    4- Iterables
        4.1. List --> general
        4.2. Tuple --> DB 
        4.3. Set --> majmoe riazi
        4.4. Dictionary --> information
        
1--> REVIEW IN JALASE
2--> TAKLIF HAYE IN JALSE




'''


#keywordds --> logivc rro taghir -> algorithm miad


'''
------> 2- Keywords --> dastoorat --> banafsh

        2.1. Conditional statement (dastoorate sharti)
        
        
        2.2. Loops (halghe ha)
        
        2.3. Tavabe (Functions)
        
        2.4. Class (Object oriented programming)

'''





'''
2.1. Conditional statement (dastoorate sharti)

'''



print('salam')

#hamishe --> python az bala b paein az chap b rast



sen = 20
print('salam')

#10 --> salam
#20 --> salam

#dastoore khate  1267 (print salam) hich vabastegi b hoichi

#python az bala b paein chap b rast mikhone





#print('salam')   **Faghat** dar soorati ejra beshe
#k sen >18 bashe
'''
sen=20
agar sen>18:
print('salam')
'''



'''
structure --> sakhtar

agar --> if 
jolosh --> shart --> yekchizi k True y aFalse dashte bashe

--> == != > < >= <=
--> .islowe() .is...
---> function() 



if shart:
    dastooor 
    



'''


sen = int(input('senet cheghadre?:'))

print('salam')

#logic --> standsarde

#dastore print salam ro shartish konm






sen = int(input('senet cheghadre?:'))
if sen>18:
    print('salam')




#senet cheghadre?:10


'''
senet cheghadre?:20
salam
'''


#yek dastoore??
#dodsstoor

sen = int(input('senet cheghadre?:'))
if sen>18:
    print('salam')
    print('khoobi')
    
    
#ta madami k -> tooye tab --> Body 


#10 --> hichi
#20 --> salam , khobi 




sen = int(input('senet cheghadre?:'))
if sen>18:
    print('salam')
    print('khoobi')
    
    
print('khodafez')




#10 --> khodafez
#20 --> salam khobi khodafez

'''
mikhay benevisi --> sakhatar

if shart:
    dastoorati k sharti mishe
    
shart --> yechizi k tru false bde



mikhay befahmish-->


shart True ? --> dastoe ejra
shartt False --> dastro ejra nmishe

if shart:
    dastoor


'''

name = 'ali'

if len(name)>2:
    print('salam')



#--------------
'''
az moshtari name mahsoool begire
va code takhfif

age code takhfif --> 
'Z12' print kone takhfif emal shod


'''


product_name = input('name mahsool:')
code_takhfif = input('code takhfif:')

print('takhfif emal shod')


#hame jore takhfif emal shod --> minevise



#------------------------
product_name = input('name mahsool:')
#code_takhfif = input('code takhfif:').upper()
code_takhfif = input('code takhfif:')

if code_takhfif=='Z12':
    print('takhfif emal shod')


'''
name mahsool:zara
code takhfif:Z12
takhfif emal shod



name mahsool:zara
code takhfif:z13
'''


'''
az user mahsol begir, gheymate mahsol, code takhfif  Z12 begir
age doros bood , 20 % az gheymate mahsol kam kon
'''


product_name = input('name mahsool?:')
product_price = float(input('gheymate mahsool?:'))
discount_code = input('code takhfif:')


if discount_code=='Z12':
    #new_price = product_price - 20/100 * product_price
    #new_price = 80/100 * product_price
    new_price = 0.8 * product_price
    print('takhfif emal shod')
    print('gheymate nahaei:',new_price)
    
'''
name mahsool?:zara
gheymate mahsool?:100
code takhfif:Z12
takhfif emal shod
gheymate nahaei: 80.0



zara , 100 , z18 --> hichi nmishe


'''







#print('z12'=='Z12') #False



product_name = input('name mahsool?:')
product_price = float(input('gheymate mahsool?:'))
discount_code = input('code takhfif:')


if discount_code.upper() =='Z12':
    #new_price = product_price - 20/100 * product_price
    #new_price = 80/100 * product_price
    new_price = 0.8 * product_price
    print('takhfif emal shod')
    print('gheymate nahaei:',new_price)
    

#z12 , Z12 --> takhfif emal mishe



#----------------------------------------

product_name = input('name mahsool?:')
product_price = float(input('gheymate mahsool?:'))
discount_code = input('code takhfif:')


if discount_code.upper() =='Z12':
    #new_price = product_price - 20/100 * product_price
    #new_price = 80/100 * product_price
    new_price = 0.8 * product_price
    print('takhfif emal shod')
    print('gheymate nahaei:',new_price)
    

'''

  Cell In[155], line 2
    product_price = float(input('gheymate mahsool?:'))

ValueError: could not convert string to float: 'hashtsad '
'''






product_name = input('name mahsool?:')
product_price = input('gheymate mahsool?:')
discount_code = input('code takhfif:')


if product_price.isdigit():
    price = float(product_price)
    if discount_code.upper() =='Z12':
        #new_price = product_price - 20/100 * product_price
        #new_price = 80/100 * product_price
        new_price = 0.8 * product_price
        print('takhfif emal shod')
        print('gheymate nahaei:',new_price)
        
    
    
    


#--------------------------------
'''
Dastoorate shartii --> 3 no darim


1- Just if
agar shart True bood  >18--> print salam
agar shart False bod ? <18 --> hichi

agar shart False bashe baramon mohem nis ejra nmsihe





2- if else
2 rahi doros koni
age bod inkar ag nabod onkar
ag true bod kare 1 , age fals ebod kare 2 



3- if elif ... else

'''
   
sen = int(input('senet cheghadre?:'))

if sen>18:
    print('salam')





'''
product name , price , print kone 
mahsool ba in gheymat
aya taeid mikonid ya na --> agar taraf nevesht yes
benevis sabt shod

harjori nevesht yes taeid kone




'''
 

product_name = input('name mahsool:')
product_price = float(input('price mahsool:'))

print('producte shoma ba moshakahsate',product_name,'va ba gheymate',product_price)

#print('aya taeiid mikoni ya na?')
answer = input('aya taeewid mikonid etelaate fogh ra(yes/no):')

if answer == 'yes':
    print('sabt shod')


#yes --> sabt shod
#no --> na
#bale --> 
#kdshdsh --> na


print('Yes'=='yes') #False 

#YES 
#Yes
#YeS
#yes   
#   yes





product_name = input('name mahsool:')
product_price = float(input('price mahsool:'))

print('producte shoma ba moshakahsate',product_name,'va ba gheymate',product_price)

#print('aya taeiid mikoni ya na?')
answer = input('aya taeewid mikonid etelaate fogh ra(yes/no):')

if answer.lower().strip() == 'yes':
    print('sabt shod')





#----------------

product_name = input('name mahsool:')
product_price = float(input('price mahsool:'))
print('producte shoma ba moshakahsate',product_name,'va ba gheymate',product_price)
#print('aya taeiid mikoni ya na?')
answer = input('aya taeewid mikonid etelaate fogh ra(yes/no):')
if answer.upper().strip() == 'YES':
    print('sabt shod')




'''









'''

