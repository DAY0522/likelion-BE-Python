# 7.

from movies import*
import random


class RandomCinema(Movie,Cinema):
    na=input('영화 입력:' )
    Mov=Movie(na,'몰라','홍진욱')
    ci=Cinema()
    #print(f"{self.cinema_list}")
    r=random.randint(0,2)
    print(f"{ci.cinema_list[r]}") 






