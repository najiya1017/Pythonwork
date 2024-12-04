class movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_movie(self,name,rating,duration,director,genre):

        self.title=name

        self.rating=rating

        self.run_time=duration

        self.director=director

        self.genre=genre

    def display_movie(self):

        print(self.title,self.genre,self.director)

movie_instance1=movie()

movie_instance2=movie()

movie_instance1.set_movie("ARM",9,120,"jithin lal","Thriller")

movie_instance2.set_movie("KGF",10,120,"prashanth neel","Thriller")

movie_instance1.display_movie()

movie_instance2.display_movie()


        