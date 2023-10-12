import csv
import threading
import time
import pandas as pd
from inputimeout import inputimeout, TimeoutOccurred

url =f"https://docs.google.com/spreadsheets/d/1LdEoLhX5j2FMLNyETuh2LctygJno5qHuz_F8_LY2urg/edit#gid=0"
url_1 = url.replace('/edit#gid=', '/export?format=csv&gid=')
data = pd.read_csv(url_1)
index = data["Index"].tolist()
qs = data["Question"].tolist()
option1 = data["1"].tolist()
option2 = data["2"].tolist()
option3 = data["3"].tolist()
timer = data["Timer"].tolist()
# gameover = data["Gameover"].tolist()
inputs = ["1"]
ind2 = '1'
ind = 0
f = open('ascii-art.txt', 'r')

def ask(q):
  global myinput
  print(qs[q])
  print('(', 1, ") ", option1[q])
  print('(', 2, ") ", option2[q])
  mytimeout = 10 * 60 * 60 if timer[q] == 1 else (7.5 *int(timer[q]))  #change to 60
  try:
    myinput = inputimeout("Your Decision: ", timeout=mytimeout)
    assert myinput == "1" or myinput == "2" or myinput == "3"
    print("\n")
  except AssertionError:
    error = "Value must be in the options!! Try again ... "
    print(error.upper())
    print("\n")
    print(ind,myinput)
    ask(q)
  except TimeoutOccurred:
    print("Secret Option Unlocked: " + option3[q])
    myinput = "3"
    print("\n")
    retry()
  else:
    retry()
  finally:
    print("\n")
  #run input

def run(myinput):
  global inputs, ind2
  inputs.append(myinput)
  ind2 = "-".join(inputs)
  ind = index.index(ind2)
  ask(ind)

def retry():
  global ind, ind2, inputs
  try:
    run(myinput)
  except ValueError as e:
    print(f.read()) # game over
    print("Your path was:",ind2)
    i = input("Do you want to try again? (Y/N): ".upper())
    while(i):
      if i.upper() == "Y":
        ind = 0
        ind2 = '1'
        inputs = ["1"]
        print("\n")
        ask(ind)
        break
      elif i.upper() == "N":
        print("Thank you for playing!")
        exit()
      else:
        print("Invalid Input! Try again...")
        i = input("Do you want to try again? (Y/N): ".upper())
        continue
  except Exception as e:
    print("i have no idea",e)
ask(index.index('1-0'))
# REFS:
#https://codeinstitute.net/global/blog/how-to-wait-in-python/
# https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
# https://colab.research.google.com/drive/1yseP61BUYZWVE7THXKVCWQeQDEp03lBw
# https://www.w3schools.com/python/ref_string_join.asp
# https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python
# https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/