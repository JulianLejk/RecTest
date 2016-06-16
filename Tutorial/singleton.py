# -*-coding: utf -8 -*-
class Cars(object):
    def __init__(self,brand,color,year):
        self.color =color
        self.year  = year
        self.brand = brand

    def __repr__(self):

            return self.brand,self.color,self.year

    def __set__(self,brand,color,year):
        self.color = color
        self.year  = year
        self.brand = brand





