from scipy.stats import norm
import random
import time
import matplotlib.pyplot as plt
from graph import Graph
peopleDictionary = []
#simulation of a single person
class Person():
    def __init__(self, startingImmunity):
        if random.randint(0,100)<startingImmunity:
            self.immunity = True
        else:
            self.immunity = False
        self.contagiousness = 0 
        self.mask = False
        self.contagiousDays = 0
        #use gaussian distribution for number of friends; average is 5 friends
        self.friends = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0))
    def wearMask(self):
        self.contagiousness /= 2
        
def initiateSim():
    numPeople = int(input("Population: "))
    startingImmunity = int(input("Percentage of people with natural immunity: "))
    startingInfecters = int(input("How many people will be infectious at t=0: "))
    for x in range(0,numPeople):
        peopleDictionary.append(Person(startingImmunity))
    for x in range(0,startingInfecters):
        peopleDictionary[random.randint(0,len(peopleDictionary)-1)].contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
    daysContagious = int(input("How many days contagious: "))
    lockdownDay = int(input("Day for lockdown to be enforced: "))
    maskDay = int(input("Day for masks to be used: "))
    return daysContagious, lockdownDay, maskDay
def runDay(daysContagious, lockdown):
    #this section simulates the spread, so it only operates on contagious people, thus:
    for person in [person for person in peopleDictionary if person.contagiousness>0 and person.friends>0]:
        peopleCouldMeetToday = int(person.friends/2)
        if peopleCouldMeetToday > 0:
            peopleMetToday = random.randint(0,peopleCouldMeetToday)
        else:
            peopleMetToday = 0
            
        if lockdown == True:
            peopleMetToday= 0
            
        for x in range(0,peopleMetToday):
            friendInQuestion = peopleDictionary[random.randint(0,len(peopleDictionary)-1)]
            if random.randint(0,100)<person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity==False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
                print(peopleDictionary.index(person), " >>> ", peopleDictionary.index(friendInQuestion))
            
    for person in [person for person in peopleDictionary if person.contagiousness>0]:
        person.contagiousDays += 1
        if person.contagiousDays > daysContagious:
            person.immunity = True
            person.contagiousness = 0
            print("|||", peopleDictionary.index(person), " |||")
            
lockdown = False
daysContagious, lockdownDay, maskDay = initiateSim()
contegoius_people_list=[]

for x in range(0,100):
    if x==lockdownDay:
        lockdown = True
        
    if x == maskDay:
        for person in peopleDictionary:
            person.wearMask()
            
    print("DAY ", x)
    runDay(daysContagious,lockdown)
    
    number_of_conatagious_people=len([person for person in peopleDictionary if person.contagiousness>0])
    contegoius_people_list.append(number_of_conatagious_people)
    
    print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")

graph=Graph(contegoius_people_list=contegoius_people_list)
graph.draw()
