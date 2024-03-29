import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyscript import Element

delta_x = 1/365    # years

x = np.arange(2020,2028,delta_x)


transmissibilityA = .0072
transmissibilityB = .0089       # infections/contact

contact_factorA = 6*365
contact_factorB = 70*365 # contacts/year/person

infectious_duration = 1/365     # years
recovery_factor = 1/infectious_duration    # 1/years
death_rate = .02    # individuals/individual
initial_vaccination_rate = 0   # individuals/individual
ongoing_vaccination_rate = .5   # (individuals/individual)/year

groupA = .45




#R0 = transmissibility * contact_factor * infectious_duration
#print(f"The basic reproduction number R0 is: {R0}")


S = np.empty(len(x))
I = np.empty(len(x))
R = np.empty(len(x))
V = np.empty(len(x))
D = np.empty(len(x))

usa_pop = 300e6

initial_vaccination_rate = initial_vaccination_rate * groupA

S[0] = usa_pop * (1 - initial_vaccination_rate)
V[0] = usa_pop * initial_vaccination_rate
I[0] = 1
R[0] = 0
D[0] = 0


for i in np.arange(1,len(x)):
  
   
    	
    infectionA = transmissibilityA * I[i-1] * (S[i-1]/usa_pop) * contact_factorA * groupA
    infectionB = transmissibilityB * I[i-1] * (S[i-1]/usa_pop) * contact_factorB * (1-groupA)
		
    recovery = (1 - death_rate) * recovery_factor * I[i-1]
    death = (death_rate) * recovery_factor * I[i-1]
    
    vaccination = ongoing_vaccination_rate * S[i-1] * groupA    # ind/year
   
    Sprime = -infectionA - infectionB + recovery - vaccination
    Iprime = infectionA + infectionB - recovery - death
    Rprime = 0
    Dprime = death
    Vprime = vaccination

    S[i] = S[i-1] + Sprime * delta_x
    I[i] = I[i-1] + Iprime * delta_x
    R[i] = R[i-1] + Rprime * delta_x
    D[i] = D[i-1] + Dprime * delta_x
    V[i] = V[i-1] + Vprime * delta_x


el = Element("pop_s")
el.write((S[-1]/usa_pop) * 100)
el = Element("pop_v")
el.write((V[-1]/usa_pop) * 100) 
plt.plot(x,S/1e6,color="blue",label="Susceptible")
plt.plot(x,I/1e6,color="red",label="Infected")
plt.plot(x,R/1e6,color="orange",label="Recovered (none)")
plt.plot(x,D/1e6,color="black",label="Deceased")
plt.plot(x,V/1e6,color="green",label="Vaccinated")
plt.title("45% of the population following covid guidelines")
plt.xlabel("year")
plt.ylabel("millions of individuals")
plt.legend()
el = Element("graph")
#el.write(plt.show())
#print((.01 * usa_pop) * 100) 
el = Element("death")
el.write(f"A total of {int(D[-1])} people died ({D[-1]/usa_pop*100:.2f}% of pop)")
