import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numAcciones = 10

def banditArm10(action):
    mu = [0.3,-0.9,1.5,0.4,1.2,-1.5,-0.2,-1.1,0.7,-0.4]
    assert(len(mu)==numAcciones)
    sigma = 1
    s=np.random.normal(mu[action],sigma,1)
    return s

def resetarQ():
    Q = []
    N = []
    for i in range(numAcciones):
        Q.append(0.0)
        N.append(0)

    Q = np.array(Q)
    return Q,N

epsilon = 0.1
num_pasos = 1000
num_exper = 200
AverageRewards=[]

for i in range(num_pasos+1):
    AverageRewards.append(0.0)

for j in range(num_exper):
    Q,N = resetarQ()
    for i in range(num_pasos):
        randNum = np.random.random()
        # Acción A - valor del 0 al 9
        Abest = np.random.choice(np.flatnonzero(Q==Q.max()))

        if(randNum > epsilon):
            A = np.random.choice(np.flatnonzero(Q==Q.max()))
        else:
            A = int(np.random.random()*10)
            if(A==10):
                A=9

        # Recompensa R
        R = banditArm10(A)

        # Num. Recompensas N
        N[A] = N[A] + 1

        # Valor acción Q
        Q[A] = Q[A] + (R-Q[A])/float(N[A])
        AverageRewards[i+1]=AverageRewards[i+1]+banditArm10(A)[0]
        #AverageRewards.append(Q[Abest])

for i in range(num_pasos+1):
    AverageRewards[i] = AverageRewards[i]/num_exper


#print(Q)
print(AverageRewards)
df = pd.DataFrame(AverageRewards,index=range(len(AverageRewards)))
lines=df.plot.line(ylim=[-1,2])
plt.show()
