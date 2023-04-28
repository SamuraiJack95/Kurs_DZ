
import os
import csv
import json
import re

# zd_1

# class Wordschit:
#    def __init__(self):
#       self.words = {}
#
#    def readfile(self, file_name):
#       with open(file_name, 'r', encoding='utf-8') as f:
#          words = re.split(r'[,.:;\s]+', f.read())
#          for word in words:
#             if word in self.words:
#                self.words[word] += 1
#             else:
#                self.words[word] = 1
#
#    def splinter(self):
#       if self.words:
#          return sorted(self.words, key= lambda x: self.words[x], reverse=True)[:10]
#
# res = Wordschit()
# res.readfile('pop.txt')
# print(res.splinter())

# zd_2

# class ConverterJOJO:
#    def __init__(self, csv_file_path):
#       self.csv_file_path = csv_file_path
#
#    def convert(self,json_file_path):
#       data = {}
#       with open(self.csv_file_path) as csv_file:
#          csv_reader = csv.DictReader(csv_file)
#          for row in csv_reader:
#             for key, value in row.items():
#                if key not in data:
#                   data[key] = []
#                data[key].append(value)
#       with open(json_file_path, 'w') as json_file:
#          json.dump(data, json_file, indent= 4)
#
# con = ConverterJOJO('csv_file_path.csv')
# con.convert('json_file_path.json')

# zd_3

class RamaFile:
   def __init__(self):
      self.story = {}

   def rename(self, file, new_name):
      self.story[file] = new_name
      os.replace(file, new_name)

b = RamaFile()

b.rename('biba.txt', 'boba.txt')
b.rename('boba.txt', 'buba.txt')
print(b.story)