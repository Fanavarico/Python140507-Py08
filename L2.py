"""
In The Name of GOD
Created on Fri Oct 16 10:44:10 2026

@author: Ali Pilehvar Meibody

L2





Machine (computeer, phone , ) --> 0,1 Binary 

Human (en, fa,....)


programming --> dastoor dadan be computer (machine)

human (en,fa) <-------> machine (binary)


human (en,fa) <---Interface (programming language)----> machine (binary)


programming language--> C , C++ , python ,....

fargheshon --> sorat, karbord ,......

Python --> yek zabani , zaban ensan nazdike, 
            ketabkhane haye moteaded , karbord haye ziad dare
            noghte sefr --> mikhonish badesh tasmim migiri kodom bakhsh beri
            
            

computer --> Python ro mishnase ? NA




computere shoma b 2 chiz naiz dare

    1- Python(Ipython kernel) --> python ro tabdil mikone b zabane binary
    2- Editor/IDE (Integratd develpment environement mohite toseye yek[arche])
        VS Code / spyder / pycharm / jupyter ,.....
        
        
codetono mizanid tooye EDITOR/IDE , run mizanid --> ersal mishe --> ipython kernel 
--> tabdil mikone b binary --> machine mikhone (ejra mikone)


programming --> dastor midm b machine


rahe 1 (basic) --> 1-pythono download konid 2-spydero  --> ROOT rishe 


Root --> python root , spyder rooot 


python 3.10.13  


-.-.- ---> adad avalie --> asle version python2 , 3 
-.... --> 3.1  3.4 -> version 3.4 vizhegi ezafe shode

3.4.10 

3.4.11   --> 3 , vzihegiashi , 11 --> buggi fix



3.10 

yesal dg 3.30  , update koni --> porozhge haye ghablit -->moshjel bikhore
ag update nakoni 


rahe 2 (stanbdard) --> Anaconda --> Environemnts mohit haro besazid


3 ta mohit misaz --> to harmohit -> python berizi , spyder 


anaconda --> ejazeye modirate mohit (env)

laptobemon -->koli .py dare 

vase ejra vase baz krdn --> editor/ide 


commnet, description ,.. --z> gheyre pythonic --Z>

ye khate --> hashtag 
ag chand khate --> qutation 


ipython kernel --> ignore (skip ) sarfe nazar, nadide migiratesh

-----------------------
Python --> langauge --> vocabs, grammar 


gheyr az comment , python 3 bakhshe 


known ------------

1- Python built in functions (tavabeye dakheli)
yekseri tavabe hastan , ke yekseri vazayef daran
() --> dsakheel spyder --> narenji

spyder --> man ino mishnasam 

print()
type()
len()
input()
.....





2- Keywords --> banafsh -->
logice ipython --> codio run mikoni
az bala b paein az chap b rast (ensan mikhone)
age in mantegh (logic) ro bekhahi taghir bdi 
bqqyad biay az keywords esteafde koni 

if elsse for while ,....



unknown --> narenji, banafsh --> sefid

3-Variable (moteghayer)
esme zarf --> ghanon dare 
    1-known nabashe (prin , open ,..)
    2- ba adad shoro nemishe
    3- charactere _ ro mishanse,space 
            student name --> student_name , StudentName 
    4- case sensitive name , Name , NAME ,namE ,,..
    
    
    
zarf --> esm , megdhar dare 

yekchizio zakhire koni --> dakhele on zarf mirizi 

age = 10

zarf sakhtam --> esmesh age , dakheelsh 10 


dakhele zarf ---> 

    3.1. Numbers --> int,float , complex 
            algebric operations --> = () ** * / // % + - 
            comparisonal --> == != > >= < <=
    3.2.  Bool -_>  True , False
    
    3.3. Str --> string --> reshte
    reshte ei az charaacter haye dakhele keyboardet
    
    
    
    3.4. Iterables 
            3.4.1. 
            3.4.2.


"""



print('Hello world!')


# yedone bezari chnata chzii bezri

#salam man aliu hastam

print('salam man ali hastam')

#3 ta zarf baham printesh koni

a = 'salam'
b='man'
c= 'ali hastam'

print(a,b,c)

#salam man ali hastam



#--------------
#int --> integer --> sahih ->
#-binahayt, -5 , -4,-3,-2,-1,0,1,2,3,.....

a= 10 


b = 20 


print(a)


#type --> typesho mige
type(a) #Out[9]: int


#len -> andaze --> str ha
len(a) #TypeError: object of type 'int' has no len()



#dfloat
#ashari

c = 10.4343

print(c) #10.4343


type(c) #Out[13]: float



#algebric operation 

# ** , * , / , + , -

# a + b = c

a = 20 
b =10

c = a + b 

print(c) #30

#**
c = a ** 2  
print(c) #400



c = a * b 
print(c) #200


c = a / b 

print(c) #2.0
type(c) #Out[21]: float

c = a // b 
print(c) #2
type(c) #Out[24]: int

#40 / 3 --> 13.333
a=40
b=3
c =   a/ b
print(c) #13.333333333333334

#40 / 3 --> baghimande 
#13 * 3 --> 39 --> 40 - 39 =->1 

c = a % b 
print(c) #1


a = 40
b = 41


c = a % 2
print(c) #0

c = b % 2
print(c) #1

c = a + b


c = a - b 


#parantez olaviat

c = (a**2)/ (b + 3) 



#-----> operation (amaliat haye jabri)


#amaliate moghayesei -_> comparisonal 


# == 
# != 
# >
# >= 
# <
# <=

#---> aya >??????
a=100
b=10

print(a>b) #True

#bale, yes --> True

c = a > b 
print(c) #True

type(c) #Out[34]: bool


a = True 
b = False 


a= 10 
b = 20

b = a


print(a) #10
print(b) #10

#meghdare dakhele zarfe a 
#ro beriuz dakhele zarfe b





#--------------------------------
#zarfi bename name 
#ali ro berizam 


name = ali

#NameError: name 'ali' is not defined

#meghdare dakhele zarfe ali ro
#beriz dakhele zarfe name


name = 'ali'

name = "ali"

#yek zarf besaz bename name
#toosh megdhare ali ro beriz

#sentence = 'ali's name'
#sentence = "ali's name"



#man harchi khastam benevism az keybordm --> dkahele qutation mizrm


chaarcter = 'a'

name = 'ali'

full_name = 'ali pilehvar meibody'

sentence = 'in the name of god , welcome to the class of fanavari co'


print(full_name)

type(full_name) #Out[43]: str

len(full_name) #Out[44]: 20


#---------------------
a = 2

b = '2'

#c = b + 'ali' -->mishe

#c  = b + 4 #nmishe

print(b*10) #2222222222

#taghsime 

#b -> esm bbin  

#tehran

b = 'tehran'

b/10 #TypeError: unsupported operand type(s) for /: 'str' and 'int'

b='2'

print(b/2) #TypeError: unsupported operand type(s) for /: 'str' and 'int'

print(10*b)

#entezar --> 20
#-->2222222222
#-->tehrantehran

#malaiat --> anjam nmide, ya naghes anjam mide


print(a==b) #False

print(type(a))

print('ali' -'i') #TypeError: unsupported operand type(s) for -: 'str' and 'str'


#*
print('===============')

print('='*30)

#str --> zarbo taghsimo ... nist 

# zarb , jam beyne str ha --> ghanone ma 



print(type(a)) #int
print(type(b)) #str
print(a==b) #False


#--------------------------------
#str fahmide beshe

#1--> name = ali    name = 'ali'
#2----> a=2  b='2'


#zarf ha (variables) -->
#  1-numbers 2-bool 3-str

#3.3.1. Definition ->tarifi krdn
name = 'ali pilehvar meibody'

print(name)

#3.3.2. Len -->

len(name) #Out[52]: 20

print(len(name))

#3.3.3. access (dastresi)

#element dastresu character --> 

#dakhele computer --> az sefr

name = 'ali pilehvar meibody'
# a l i <> p i l e 
# 0 1 2 3 4 5 

#az name i ro bede
#az name indexe 2 ro bede


name[2] #Out[55]: 'i'

print(name[2]) #i

zarf = name[2]
print(zarf) #i


#3.3.4. slicing 

name = 'ali pilehvar meibody'


#esm ro az name joda kon
#ali ro az name joda kon
#a l i ro az name joda kon
#indexe 0 1 2 ro az name joda kon
#indexe 0 ta 2 ro az name joda kon

#ta --> :
#hamishe enteha -> exclude --> shamel nemishavad
#gheyre mashmool

name[0:3]  #az name idnexe 0 ta 3-1(2)

#Out[59]: 'ali'





full_name = 'ali pilehvar meibody'
name = full_name[0:3] 

print(name)


#tedade balaye variable
#2--> spyder -> in featureo dare
#vs code ,...

#print()


name = 'ali'
print(name)




full_name = 'ali pilehvar meibody'

last_name = full_name[4:12]
# az indexe 4 ta 11 ro bede

print(last_name) #pilehvar


full_name = 'ali pilehvar meibody'

full_name[0:12] #Out[64]: 'ali pilehvar'

full_name[:12] #az 0 
#by default (pishfarz)



full_name[4:] #Out[65]: 'pilehvar meibody'



full_name = 'ali pilehvar meibody'

full_name[0:12:1]

#az 0 indexe 0 --> indexe 11 
#yeki yeki

full_name[0:12]

#yekiam


full_name[0:12:2] #Out[66]: 'aiplha'

#az indedxe 0 t a11 yeki darmion (2 ta 2ta)



#3.3.5 change

full_name = 'ali pilehvar meibody'

full_name[0] = 'b'

#TypeError: 'str' object does not support item assignment



full_name = 'ali pilehvar meibody'


name1=full_name[:3] #ali
 
name2=full_name[4:12] #pilehavr

name3=full_name[13:] #meibody

new_name = name1+name2+name3

print(new_name) #alipilehvarmeibody

#bozorgesh jakrd


#yekseri kar ha-->sakht anjam mishe
#yekseri kar ha 0>< nashodanie

#tavabe ma niaz darim ke be sorate khas 
#baraye string ha neveshte shdoe bashe





#--------------------------------
#3.3.6. Str functions -------

#tavabeye string ha --< tavabayee reshte ha

#upper() 

name = 'ali'


#tavabe dakheli --> known --> mishnaskht 
#baraye aksare type hga bood
#print()
#type()
#len()


#tabe --> tabe eye str --> str ha

#upper(name)

#zarf.function()
name = 'ali'


#nokte dovom --> tavabe emal nemishan, khoroji midan

name.upper() #Out[71]: 'ALI'

print(name) #ali

new_name = name.upper()

print(name) #ali

print(new_name) #ALI


#--------------------------
name = 'ali'

city = 'TEHRAN'


sentence = 'in the name of god'


new_name = name.upper()

print(new_name) #ALI


city_lower = city.lower()

print(city) #TEHRAN

print(city_lower) #tehran


#title --> horofe avale har klaame ro bozorg mikone

new_sentence = sentence.title()

print(new_sentence) #In The Name Of God


new_sentence2 = sentence.capitalize()
print(new_sentence2) #In the name of god


#.upper() --> kolesho bozorg mikone
#.lower() --> kolesho kochikmikone
#.title() --> titelesh mikoen (avalin character har kalame)
#.capitalize() --> aval,in harfe str ,baghiaro kochik mikone



#https://www.w3schools.com/python/python_ref_string.asp

'''

Method	Description

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values from a dictionary in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning



'''

'''
az 50 ta tabe  3 no tabe darim

1- convert  tabdil

.lower()
.upper()
.title()
.capitalize()




2 - adad pas midan 
.count()
.find() 


3 - True false pas midan --> soalian
.islower()


'''

full_name= 'ali pilehvar meibody'

name = 'ali'

name.upper()


#repalce ? character --> character

#a --> b 


new_name = name.replace('a','b')


print(new_name) #bli



#name.replace(a,b) XXXXXXXXXX


full_name= 'ali pilehvar meibody'

new_full_name = full_name.replace(' ','')

print(new_full_name) #alipilehvarmeibody


#upper()
#lower()
#title()
#capitalize()
#replace()
#strip() --> 


a = 'ali'

b= 'ali '


print(a==b) #False

print(len(a)) #3

print(len(b)) #4


b[3] #Out[91]: ' '
a[3]  #IndexError: string index out of range


#normalize --> 

#space haye rasto chap ro hazf koni

#replace(' ','')

c=b.strip()

print(c) #ali

len(c) #Out[95]: 3

print(a==c) #True

full_name= '    ali pilehvar meibody  '
 
full_name.replace(' ','') #Out[97]: 'alipilehvarmeibody'

full_name.strip() #Out[98]: 'ali pilehvar meibody'


#-------numberi --> adad pas bede


#.count()
full_name= 'ali pilehvar meibody'

full_name.count('a') #Out[99]: 2

full_name.count('z') #Out[103]: 0
 




#.find
full_name.find('a') #Out[102]: 0

full_name.find('z') #Out[104]: -1

#find index --> -1 --> peyda nashod


#.find() --> developperaye python 
#false , error , 


#00convert0000
#--lower()
#--upper()
#title()
#capitalize()
#replace()
#strip()

#00adad00
#count()
#find()


#00sharti00 --> is shoro mishan

#True False

city = 'tehran'

city.islower() #Out[105]: True


city = 'TeHran'

city.islower() #Out[106]: False

#islower() -->is_all_lower()



country='IRAN'

country.isupper() #Out[107]: True

#islower()
#isupper()
#isdigit()

#istitle()


zarf = 'chizi'

zarf2 = '237892837'


zarf3= 'ali2833762765'
#type joftesh str

#isdigit()

zarf.isdigit() #Out[109]: False
zarf2.isdigit() #Out[110]: True

zarf3.isdigit() #Out[113]: False


#check kone ke hamash az adad 

'''
1-python built in functions
print()
len()
type()
input()





2- keywords


3- variables 

    3.1.Numbers
    3.2. Bool
    3.3. Str 
        3.3.1 definitions
        3.3.2 index, access
        3.3.3. slicing
        3.3.4 change XXX
        3.3.5. Str fucntions
            zarf.function()
            emal nemishan, khoroji midan
            
            3.3.5.1. Convert
                .lower()
                .upper()
                .title()
                .capitalize()
                .replace(old,new)
                .strip() .rstrip() .lstrip()
            
                .split()***
                
               
                
            3.3.5.2. Number midan
                .count('char') --> 0
                .find('char') --> -1
                
            3.3.5.3. True , false --> Is
                .islower() -->hame lower bashan trye
                .isupper() -->hsme upper bashan tremide
                .istitle() --> title bashe
                
                .isdigit() --> age hame adad bashad true
                
                .isalnum()
                .isalpha()
                
         
                
    3.4. Iterables --> list, tuple, set , dictionary
    
    if 
    
    


Jalas ebadi --> taklif l1 , l2 





'''


print('salam') #salam


zarf = input('esmet chie?:')

print(zarf) #ali

#Input --> dakheelsh harchi benevsii -> print mishe
#montazer vaymise ta neveshte beshe enter zade beshe

#Khoroji ro dakheel yek zarf miridi


#1--->: zibaei

#2--->khorojie input hamishe str hast

sen = input('senet cheghadre?:')


print(sen) #16

print(type(sen)) #<class 'str'>




#--------------------------------
a='10'
b = int(a)

#ok





city = 'tehran'
b = int(city)
#ValueError: invalid literal for int() with base 10: 'tehran'






sen = input('senet cheghadre?:')

#int koni ya float

new_sen = float(sen)



#---professsional

sen  = float(input('senet cheghadre?:'))




#--------esm kahsi begiri

zarf = input('harchi:')


#----adad begiri

#sahih bashe
zarf = int(input('harchi:'))

#ashari bashe
zarf = float(input('harchi:'))



#------TASK 1--------------------
'''
aval yek appie namayesh bede ------------ 
bad soal kone bege esme mahsool chi --> product_name
gheymnat chande --> price 

esme_mahsolo bozorg kone 
price --> 10% takhfif emal kone


mahsoole ... gheymate nahaei felan


'''

print('---------------------')

print(30*'-')

product_name = input('esme mahsool chist?:')
price = float(input('gheymate mahsool chande?:'))


upper_product_name = product_name.upper()

#final_price = price - 10/100 * price
#final_price = 90/100 * price 
#final_price = 9/10 * price  
final_price = 0.9 * price 


print('gheymate nahaeie mahsoole',upper_product_name, 'hast:',final_price)

#gheymate nahaeie mahsoole ZARA hast: 90.0




'''
soale badi --->


Yek app daeirm minevism 

mikhahim az karbar etelaatesho begirim 

esmesho begirim, senesh , shomare cartesh , mojoodisho


esmesh ro besorate title namayesh bedim bgim jenab/,,, 
ba hesabe shomare cart ...... ba sene ... mojoditoon 

1 % mojodi ro azash kam konim


esmetoon : alipilehvar  
sen : 30 
shoamre cart :2323723
mojoodi : 4000


jenabe Ali Pilehvar Meibody ba shomare carte 32382392832 
mojodie shoma hast 3960 toman hast.


fasele haram hazf kone


'''


name = input('esmet chie?:')
age = int(input('senet cheghadre?:'))
card_number  = input('shoamr ekartet chie:')
balance = float(input('mojodit chande?:'))


#new_name = name.upper()
#new_name2 = new_name.strip()

new_name = name.upper().strip()

#new_balance = balance - 1/100 * balance
#new_balance = balance - 1/100 * balance
#new_balance = 100/100 * balance - 1/100 * balance

#new_balance = 99/100 * balance

#1 % karmozde balance
new_balance = 0.99 * balance

#print('jenabe/sarkare new_name ba shomare karte card_number , mojodie nahaeu shoma hast new_balance ')
#print('jenabe/sarkare', new_name  ,'be shoamre karte',card_number,'mojodie nahaeie shoma hast:',new_balance)

#fstring 
#print('jenabe/sarkare new_name ba shomare karte card_number , mojodie nahaeu shoma hast new_balance ')

print(f'jenabe/sarkare {new_name} ba shomare karte {card_number} , mojodie nahaeu shoma hast {new_balance} ')



#jenabe/sarkare ALI ba shomare karte 61043223332499e , mojodie nahaeu shoma hast 99.0 



#-----------------

name = 'ali'


print('salam name')

print('salam',name)


print(f'salam {name}')



'''

Python 08 jalase 2 


Taklife 1 : Tavabe ye string haro dar yek file bename str_functions.py done done 
besoorate random yek string besazid va done done estefade konid va yek ya do khat ozih benevisid

masalan

name = 'ali'
new_name = name.title()
print(new_name) #Ali

#in tabe miad avale har harf ro bozorg mikone




Taklife 2 : az user esme mahsool va gheymat ro begirid va 25 % takhfif emal konid
bad be user neshon bedid --> Gheymaten Nahaei mahsoole 'Esme mahsol besorate title' hast
'gheymate bad az 25% takhfif'



Taklife 3 : az user esme mahsool, gheymate mahsool va darsade takhfif begirid va roye
gheymat, darsadi ke user dade ro emal konid va benevisid -->
gheymate nahaei mahsoole 'esme mahsool besoorate bozorg va bedone space' hast 'gheymate
nahaei bad az takhfif'



Taklife 4 : az user esmesho begirid va hamchenin tedade horofe esmesho begirid .
badesh age doros gofte bood print beshe True , age ghalat gofte bood print beshe False

**Nokte : az mabahesi ke ta alan tadris shode faghat mitonid estefade konid na mabahesi ke
dar jalasate badi tadris mishe



4 Ta file .py besazid va file haro az tarighe email be emaile ai.course22.alipilehvar@gmail.com

ba subjecte --> L2_name_lastname   yani esmo famileton masalan L2_Farhad_majidi 

ersal konid


moafagh bashid





'''

