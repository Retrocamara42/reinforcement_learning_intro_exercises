import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numAcciones = 10
epsilon = 0.1
num_pasos = 10000
alfa = 0.1
mu = [0,0,0,0,0,0,0,0,0,0]
num_exper = 100

def banditArm10(action):
    assert(len(mu)==numAcciones)
    sigma = 1
    s=np.random.normal(mu[action],sigma,1)
    return s

def actualizarMus():
    for i in range(len(mu)):
        randNum = (np.random.random() - 0.5)
        mu[i] = mu[i] + randNum

def resetearMus():
    for i in range(len(mu)):
        mu[i] = 0

def resetarQ():
    Q1 = []
    Q2 = []
    N = []

    for i in range(numAcciones):
        Q1.append(0.0)
        Q2.append(0.0)
        N.append(0.0)
    Q1 = np.array(Q1)
    Q2 = np.array(Q2)

    return Q1,Q2,N

AverageRewards1=[]
AverageRewards2=[]

for i in range(num_pasos+1):
    AverageRewards1.append(0.0)

for i in range(num_pasos+1):
    AverageRewards2.append(0.0)


for j in range(num_exper):
    Q1,Q2,N = resetarQ()
    for i in range(num_pasos):
        randNum = np.random.random()
        # Acción A - valor del 0 al 9
        Abest1 = np.random.choice(np.flatnonzero(Q1==Q1.max()))
        if(randNum > epsilon):
            A1 = np.random.choice(np.flatnonzero(Q1==Q1.max()))
        else:
            A1 = int(np.random.random()*10)
            if(A1==10):
                A1=9

        randNum = np.random.random()
        # Acción A - valor del 0 al 9
        Abest2 = np.random.choice(np.flatnonzero(Q2==Q2.max()))
        if(randNum > epsilon):
            A2 = np.random.choice(np.flatnonzero(Q2==Q2.max()))
        else:
            A2 = int(np.random.random()*10)
            if(A2==10):
                A2=9

        # Recompensa R
        R1 = banditArm10(A1)
        R2 = banditArm10(A2)

        actualizarMus()

        # Num. Recompensas N
        N[A1] = N[A1] + 1

        # Valor acción Q1
        Q1[A1] = Q1[A1] + (R1-Q1[A1])/float(N[A1])

        # Valor acción Q2
        Q2[A2] = Q2[A2] + (R2-Q2[A2])*alfa
        #AverageRewards.append(banditArm10(Abest)[0])
        AverageRewards1[i+1]=AverageRewards1[i+1]+banditArm10(A1)[0]
        AverageRewards2[i+1]=AverageRewards2[i+1]+banditArm10(A2)[0]
        #AverageRewards1.append(R1)
        #AverageRewards2.append(R2)

    print(mu)
    resetearMus()




for i in range(num_pasos+1):
    AverageRewards1[i] = AverageRewards1[i]/num_exper

for i in range(num_pasos+1):
    AverageRewards2[i] = AverageRewards2[i]/num_exper

df = pd.DataFrame(AverageRewards1,index=range(len(AverageRewards1)))
lines=df.plot.line() #(ylim=[-1,2])
plt.show()

df = pd.DataFrame(AverageRewards2,index=range(len(AverageRewards2)))
lines=df.plot.line() #(ylim=[-1,2])
plt.show()
