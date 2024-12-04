#_init_() => constructor attributes initialise 

#_str_()  => object string reprasentation

#self       => current instance

#super()    => parent class

class Animal:
    name:str
    sepecies:str

    def _init_(self,name,species):
        self.name=name
        self.sepecies=species

    def _str_(self):
        return self.name

class lion(Animal):
    def _init_(self,name,species):
        super()._init_(name,species)

    def sound(self):
        print("roar")

lion_instance=lion("lion","carnivorous")
print(lion_instance)
print(lion_instance.sound())