import math
import random

# class Vektor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f'(x: {self.x:.4f}, y: {self.y:.4f})'
    
#     @property
#     def intenzitet(self):
#         return math.hypot(self.x, self.y)

# v1 = Vektor(3.5, 9)

# print(v1)
# print(v1.x)
# print(v1.y)
# print(v1.intenzitet)

# class Kvadrat:
#     def __init__(self, a):
#         self.a = a
    
#     def __str__(self):
#         return f'Kvadrat stranice {self.a}'
    
#     @property
#     def povrsina(self):
#         return self.a ** 2
    
#     @povrsina.setter
#     def povrsina(self, nova_povrsina):
#         self.a = math.sqrt(nova_povrsina)

# k1 = Kvadrat(4)

# print(k1)
# print(k1.povrsina)

# k1.povrsina = 36

# print(k1)
# print(k1.povrsina)

# class Osoba:
#     def __init__(self, ime, prezime, jmbg):
#         self.ime = ime
#         self.prezime = prezime
#         self.jmbg = jmbg
    
#     def __str__(self):
#         return f'Ja sam {self.ime} {self.prezime}'

# class Student(Osoba):
#     def __init__(self, ime, prezime, jmbg, indeks, smer):
#         Osoba.__init__(ime, prezime, jmbg)

#         self.indeks = indeks
#         self.smer = smer
    
#     def __str__(self):
#         return f'Moje ime je {self.ime} {self.prezime}. Ja sam student na smeru {self.smer} i moj broj indeksa je {self.indeks}.'

# pperic = Student('Pera', 'Peric', 1010997710022, 2020900900, 'SII')

# print(pperic)

# class Vektor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f'(x: {self.x}, y: {self.y})'
    
#     @property
#     def intenzitet(self):
#         return math.hypot(self.x, self.y)
    
#     def __lt__(self, other):
#         return self.intenzitet < other.intenzitet
    
#     def __gt__(self, other):
#         return self.intenzitet > other.intenzitet

#     def __le__(self, other):
#         return self.intenzitet <= other.intenzitet

#     def __ge__(self, other):
#         return self.intenzitet >= other.intenzitet
    
#     def __eq__(self, other):
#         return self.intenzitet == other.intenzitet
    
#     def __ne__(self, other):
#         return self.intenzitet != other.intenzitet

# v1 = Vektor(3.5, 9.0)
# v2 = Vektor(5.6, 2.3)

# merenja = [1.2, 2.3, 3.4, 2.3, 1.2, 0]

# br_el = len(merenja)

# for i in range(br_el):
#     merenje = merenja[i]
#     print(merenje)

# for i in range(len(merenja)):
#     print(merenja[i])

# for merenje in merenja:
#     print(merenje)

# def get_tempertura_sa_senzora ():
#     return random.random() * 30 + 15

# while True:
#     trenutna_temp = get_tempertura_sa_senzora()

#     print(f'Trenutna temperatura: {trenutna_temp}')

#     if trenutna_temp > 43:
#         print('Ukljuci gasenje pozara.')

# def get_tempertura_sa_senzora ():
#     while True:
#         temp = random.random() * 30 + 15
#         yield temp

# for trenutna_temp in get_tempertura_sa_senzora():
#     print(f'Trenutna temperatura: {trenutna_temp}')

#     if trenutna_temp > 43:
#         print('Ukljuci gasenje pozara.')

# def vrati_dva_broja_za_redom ():
#     yield random.randint(1, 1000)
#     yield random.randint(500, 800)

# for broj in vrati_dva_broja_za_redom():
#     print(broj ** 3)

# class Vektor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f'[ {self.x}, {self.y} ]'
    
#     @property
#     def intenzitet(self):
#         return math.hypot(self.x, self.y)
    
#     @classmethod
#     def load (cls, fajl):
#         with open(fajl, 'r') as f:
#             while True:
#                 red = f.readline().strip()

#                 if red == '':
#                     break

#                 delovi = red.split(' ')
#                 x = float(delovi[0])
#                 y = float(delovi[1])

#                 yield Vektor(x, y)

# max_v = Vektor(0, 0)

# for v in Vektor.load('vektori.txt'):
#     if max_v.intenzitet < v.intenzitet:
#         max_v = v

# print(max_v)