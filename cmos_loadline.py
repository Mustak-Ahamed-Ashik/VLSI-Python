import numpy as np
import matplotlib.pyplot as plt

beta=0.000240
Vt=0.7
Vds=np.linspace(0,5,num=100)
Vgs=np.arange(1,6)

plt.figure(figsize=(15,10))
for j in range (len(Vgs)):
    Ids=[]
    for i in range(len(Vds)):
        if Vgs[j]<Vt:
            Ids1=0
        elif (Vgs[j]>Vt) & (Vds[i]<=(Vgs[j]-Vt)):
            Ids1=(beta*((Vgs[j]-Vt)-Vds[i]/2))*Vds[i]
        elif (Vgs[j]>Vt) & (Vds[i]>(Vgs[j]-Vt)):
            Ids1=(0.5*beta)*(Vgs[j]-Vt)**2
        Ids.append(Ids1*1000)
    plt.plot(Vds,Ids,linewidth=2)
    Vds2=np.flip(Vds)
    plt.plot(Vds2,Ids,linewidth=2)
plt.title('Load line analysis of CMOS inverter')
plt.xlabel('Vout (volts)')
plt.ylabel('Ids (mA)')
plt.ylim([0, 3])
plt.xlim([0, 5])
plt.grid()
plt.show()

