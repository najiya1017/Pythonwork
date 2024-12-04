#sequence of characters

#string ==> object class

#class ==> template or blueprint 

#class str:

    # attributes

    # methods

#class str:

    #def capitalize() ==> converts first letter upper case

    #def casefold() ==> converts all characters into lowercase

    #def isalpha() ==> returns true if all characters are alphabets in the give text

    #def isdigit() ==> returns true if all characters in the string are digits.

    #def isalnum() ==> returns true if the string contains alphabets or number.

    #def startswith(str) ==> returns true if the string starts with the string user specified,case sensitive

    #def endswith ==> returns true if the string ends with the string user specified,case sensitive

    # def split(separator, maxsplit)==> Split a string into a list where each word is a list item
    
    #def strip() ==> removes the specified charcter from both right and left of the string.IF character not specified it removes white spaces

    #def lstrip() ==> removes the specified character from the left side

    #def rstrip() ==> removes the specified charcter from the right side

    #def replace(old character,new character,no.of character to be removed)

    #slicing,string_object[start index:end index:step]==>remove the words specified within the range , eg->text[2:10:2],slice from 2 to 9 and increment by 2

    #def index(character)==> returns index of the specified character



#MODEL OF  DEFINING CLASS,ITS ATTRIBUTES,METHODS AND CALLING IT.
class bottle:

    color:str

    shape:str

    material:str

    def open():

        pass

    def closs():

        pass

    def refill():

        pass


pigeo_bottle=bottle() #creating object

milton_bottle=bottle()

pigeo_bottle.open() #calling method using object

