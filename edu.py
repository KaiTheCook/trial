import requests
from bs4 import BeautifulSoup

# url = 'https://manascinema.com/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"lxml")
#
# products = soup.find_all("a",class_="creation-item")
#
# for product in products:
#     age = product.find("div",class_="age").text
#     title = product.find("div",class_="creation-title").text
#     genre = product.find("div",class_="creation-info").text
#     image = product.find("img")['src']
#
#
#     print(age)
#     print(title)
#     print(genre)
#     print(url + image)
#
#     print("-----"*20)
# url = "https://cinematica.kg/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text,"lxml")
#
# movies_grid_in_home = soup.find_all("a",class_="movie-dummy")
# for movie in movies_grid_in_home:
#     title = movies_grid_in_home.find("div",class_="movie-title").text
#     poster = movies_grid_in_home.find("img")['src']
#
#     print(title)
#     print(poster)
#     print("-----------" * 20)

#
# class Movie:
#     def __init__(self,title,image,genre,age):
#         self.title = title
#         self.image = image
#         self.genre = genre
#         self.age = age
#
#
#     def __str__(self):
#         return f"{self.title}\n {self.genre}\n {self.age}\n {self.image}"
#
#
#     @classmethod
#     def from_parser(cls,title,image,genre,age):
#         # title = movie_tag.find("div",class_="creation-title").text
#         # image = movie_tag.find('img')['src']
#         # genre = movie_tag.find("div",class_="creation-info").text
#         # age =
#         return cls(title,image,genre,age)
#
#
#     def to_dict(self):
#         return{
#             "title" : self.title,
#             "genre" : self.genre,
#             "age" : self.age,
#             "image" : self.image
#         }

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v134.dom import get_attributes

driver = webdriver.Chrome()
driver.get("https://cinematica.kg/")
time.sleep(3)
elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")
for element in elements:
    title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
    image = element.find_element(By.XPATH, ".//img").get_attribute("src")

    print(title)
    print(image)
    print("----"*20)

driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cinematica.kg/")
time.sleep(3)
elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")
for element in elements:
    title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
    image = element.find_element(By.XPATH, ".//img").get_attribute("src")

    print(title)
    print(image)

driver.quit()

"синематика"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v134.dom import get_attributes

# driver = webdriver.Chrome()
# driver.get("https://cinematica.kg/")
# time.sleep(3)
# elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")
# for element in elements:
#     source = element.get_attribute("href")
#     title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
#     image = element.find_element(By.XPATH, ".//img").get_attribute("src")
#
#     print("link to the movie", source)
#     print(title)
#     print(image)
#     print("----"*20)
#
# driver.quit()

# class MyMyclass:
#
#     @staticmethod
#     def hello():
#         print("Hello")
#


# class MyMath:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# a = MyMath(1, 2)
#
# print(MyMath.add(1, 2))

#

print("3d commit")
