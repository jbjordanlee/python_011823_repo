#!/usr/bin/python

import json
import mymodule011623

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", action="store", type="string", dest="file", help="<file>")
(options, args) = parser.parse_args()

if options.file == None:
  print("Please use --help for options!!!")
else:
  o = open(options.file)
  print(o.read())

class eastcoasttrip():
  extra_time_off = "Yes, extra time off!!!"
  extra_view_seen = "Yes, extra view seen!!!"

  def __init__(self, whichcity, whatevent):
    self.whichcity = whichcity
    self.whatevent = whatevent

  def whattoeat(self, food):
    print("During winter break visit city like " + self.whichcity + " engage activity like " + self.whatevent + " eat food like " + food + " which can be an life time uniqe experience you do not want to miss!!!")

e1 = eastcoasttrip("NYC", "Visit Top of the Rock!!!")
print(e1.whichcity)

e1.whattoeat("Vienanese Pho")

class eastcoasttrip2(eastcoasttrip):
  pass

e2 = eastcoasttrip2("Boston", "Attend Boston Tea Party & Ship Musium")
print(e2.whatevent)

e2.whattoeat("Sandwiches from Tatee Bakery & Cafe")

# dict

thisdict = {
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

for a in thisdict:
  print(a)

for b in thisdict:
  print(thisdict[b])

print("use dictionary keys method to list keys")
for c in thisdict.keys():
  print(c)

print("Use dictionary values method to list values")
for d in thisdict.values():
  print(d)

for e,f in thisdict.items():
  print(e,f)

thisdict["Thurs"] = "Four"

print(thisdict)

# json convert from dict to string format using json dumps fuction

g = json.dumps(thisdict)
print("convert dict thisdict to string format using json dumps fuction")
print(g)
print(type(g))

print("convert string format back to dict format using json loads function and print out one of the dict values")
h = json.loads(g)
print(h["Wed"])

# revert dict keys and values

reversedict = {}

for i in thisdict:
  reversedict[thisdict[i]] = i

print("Original dict is: ", thisdict)
print("After reverse keys & values in dict becomes: ", reversedict)

# list

thatlist = ["one", "two", "three"]

for j in thatlist:
  print(j)

# get rid of duplicated items in list

k = ["A", "A", "B", "C", "C", "C", "D"]

l = []

for m in k:
  if m not in l:
    l.append(m)

print("Original list is: ", k)
print("after get rid of dulicated items list becomes: ", l)

# running method from imported module

mymodule011623.greeting("Jordan")

# fuction

def sumup(n,o):
  print("Sum of " + str(n) + " and " + str(o) + " is " + str(n + o))

sumup(7,5)

# while 

grade = 9
print("You are attending grade " + str(grade) + " now ")

while grade < 12:
  grade+=1
  print("You will be attending grade " + str(grade) + " next ")

print("Congrats, You will be attending college after all of these!!!") 

# try except

ttoday = " MLK holiday "

try:
  print("Today is :" + today)
except:
  print("Today is NOT defined!!!")
