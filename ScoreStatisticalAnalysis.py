import numpy as np
import math
import random

k= 2000
w= 10
candidateDetails= [[0.0 for xxx in range(w)] for yyy in range(k)]
# hardwork, Aptitude, Resources, fortune, time taken, Score, markseasy, marksmedium, markshard, questions answered

for l in range(k):
    #Generating random data for-
    #hardwork
    candidateDetails[l][0]= float(random.randint(0,10000)/10000.0)

    #Aptitude
    candidateDetails[l][1]= float(random.randint(0,10000)/10000.0)

    #Resources
    candidateDetails[l][2]= float(random.randint(0,10000)/10000.0)

    #fortune
    candidateDetails[l][3]= float(random.randint(-10000,10000)/10000.0)

    #Assuming the distribution of questions based on difficulty level.
    quesEasy= 40
    quesMedium= 50
    quesHard= 50

    #Calculating a variable weighted on the first 3 Candidate detail
    total = 0.0
    total = np.power(candidateDetails[l][0],(0.1))*np.power(candidateDetails[l][1],(0.15))*np.power(candidateDetails[l][2],(0.1))*quesEasy + np.power(candidateDetails[l][0],(0.2))*np.power(candidateDetails[l][1],(0.25))*np.power(candidateDetails[l][2],(0.2))*quesMedium + np.power(candidateDetails[l][0],(0.3))*np.power(candidateDetails[l][1],(0.3))*np.power(candidateDetails[l][2],(0.3))*quesHard
    
    for i in range(140): #For every question
        
        if (float(random.randint(0,10000)/10000.0)) <= (np.power(candidateDetails[l][0],(0.1))*np.power(candidateDetails[l][1],(0.15))*np.power(candidateDetails[l][2],(0.1))*quesEasy/total):
            # We are defining easyness variable to categorize the current question.
            easyness = 0
        else:
            if (float(random.randint(0,10000)/10000.0)) <= ((np.power(candidateDetails[l][0],(0.1))*np.power(candidateDetails[l][1],(0.15))*np.power(candidateDetails[l][2],(0.1))*quesEasy+np.power(candidateDetails[l][0],(0.2))*np.power(candidateDetails[l][1],(0.25))*np.power(candidateDetails[l][2],(0.2))*quesMedium)/total):
                easyness = 1
            else:
                easyness = 2

        if easyness == 0 and quesEasy>0:
            # assuming this much time taken is required to solve this particular question
            candidateDetails[l][4] += (0.1*(1-(0.25+0.47*np.power(candidateDetails[l][1],0.6))) + 0.25*(1-(0.25+0.47*np.power(candidateDetails[l][0],0.6))) + 0.15*(1-(0.25+0.47*np.power(candidateDetails[l][2],0.2))))*math.exp(0.06*candidateDetails[l][3])*8
            if candidateDetails[l][4] > 250.0:
                break
            if (float(random.randint(0,10000)/10000.0)) <= 0.15+ 0.8*((0.5*np.power(candidateDetails[l][1],0.6) + 0.6*np.power(candidateDetails[l][0],0.6)*np.power(candidateDetails[l][2],0.2))*math.exp(0.08*candidateDetails[l][3])):
                candidateDetails[l][5] += 3.001
                candidateDetails[l][6] += 3.001
        
                quesEasy -= 1
            else:
                if (float(random.randint(0,10000)/10000.0)) > (np.power(candidateDetails[l][0],1.2)*np.power(candidateDetails[l][1],0.8)*np.power(candidateDetails[l][2],1)):
                    # if he answered question wrong
                    candidateDetails[l][5] -= 1.0
                    candidateDetails[l][6] -= 1.0
                    quesEasy -= 1

        elif easyness == 1 and quesMedium>0:
            candidateDetails[l][4] += (0.25*(1-(0.25+0.47*np.power(candidateDetails[l][1],0.6))) + 0.3*(1-(0.25+0.47*np.power(candidateDetails[l][0],0.6))) + 0.15*(1-(0.25+0.47*np.power(candidateDetails[l][2],0.2))))*math.exp(0.06*candidateDetails[l][3])*9
            if candidateDetails[l][4] > 250.0:
                break
            if (float(random.randint(0,10000)/10000.0)) <= 0.07+0.83*((0.5*np.power(candidateDetails[l][1],0.6) + 0.4*np.power(candidateDetails[l][0],0.6)*np.power(candidateDetails[l][2],0.15))*math.exp(0.08*candidateDetails[l][3])):
                candidateDetails[l][5] += 3.002
                candidateDetails[l][7] += 3.002
                quesMedium -= 1
            else:
                if (float(random.randint(0,10000)/10000.0)) > (np.power(candidateDetails[l][0],1.2)*np.power(candidateDetails[l][1],0.8)*np.power(candidateDetails[l][2],1)):
                    candidateDetails[l][5] -= 1.0
                    candidateDetails[l][7] -= 1.0
                    quesMedium -= 1

        elif quesHard>0:
            candidateDetails[l][4] += (0.4*(1-(0.25+0.47*np.power(candidateDetails[l][1],0.6))) + 0.2*(1-(0.25+0.47*np.power(candidateDetails[l][0],0.6))) + 0.2*(1-(0.25+0.47*np.power(candidateDetails[l][2],0.2))))*math.exp(0.06*candidateDetails[l][3])*9
            if candidateDetails[l][4] > 250.0:
                break
            if (float(random.randint(0,10000)/10000.0)) <= 0.05+0.8*((0.55*np.power(candidateDetails[l][1],0.6) + 0.3*np.power(candidateDetails[l][0],0.6)*np.power(candidateDetails[l][2],0.1))*math.exp(0.08*candidateDetails[l][3])):
                candidateDetails[l][5] += 3.003
                candidateDetails[l][8] += 3.003
                quesHard -= 1
            else:
                if (float(random.randint(0,10000)/10000.0)) > (np.power(candidateDetails[l][0],1.2)*np.power(candidateDetails[l][1],0.8)*np.power(candidateDetails[l][2],1)):
                    candidateDetails[l][5] -= 1.0
                    candidateDetails[l][8] -= 1.0
                    quesHard -= 1
    candidateDetails[l][9] = 140-quesEasy-quesMedium-quesHard

#sorting the candidateDetails based on their Score in descending order.
candidateDetails.sort(key = lambda x: x[5], reverse=True)

#printing the top 10 students
for i in range(10):
    print(candidateDetails[i])
    print("")
