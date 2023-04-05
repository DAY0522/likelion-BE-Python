class Movie:
    def ________(self, name, genre, produce):
        self.name = name
        self.genre = genre
        self.produce = produce

    def new(self, name, genre, produce):
        self.name = name
        self.genre = genre
        self.produce = produce

    
    def show_name(name):
        print('영화의 이름은', name, '입니다.')



class Cinema:

    def __init__(self):
        self.cinema_list=['CGV', 'MEGABOX', 'LOTTE']

    def add(self,newone):
        self.cinema_list.append(newone)
        print(self)





        

    
        

    