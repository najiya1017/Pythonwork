class Cuisine:

    cuisine_name:str

    def __init__(self,name):

        self.cuisine_name=name

    def display_cuisine(self):

        print(self.cuisine_name)

    
class MealType:

    m_type:str

    def __init__(self,m_type):

        self.m_type=m_type

    def display_mealtype(self):

        print(self.m_type)


class Dish(Cuisine,MealType):

    dish:str

    def __init__(self,name,m_type,dish):

        Cuisine.__init__(self,name)

        MealType.__init__(self,m_type)

        self.dish=dish

    def display_dish(self):

        self.display_cuisine()

        self.display_mealtype()

        print(self.dish)


d_instance=Dish("Indian","Ghee Roast","Break Fast")

d_instance.display_dish()

