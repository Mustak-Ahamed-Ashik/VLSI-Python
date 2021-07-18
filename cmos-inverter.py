import numpy as np
import matplotlib.pyplot as plt

beta=0.000240
Vt=0.7
Vds=np.linspace(0,5,num=100)
Vgs=np.arange(1,6)
Vt2=-0.7
Vds2=np.linspace(-5,0,num=100)
Vgs2=np.arange(-5,0)
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
    plt.plot(Vds,Ids,linewidth=2,label='Vgs= '+str(Vgs[j]))
for j in range (len(Vgs2)):
    Ids3=[]
    for i in range(len(Vds2)):
        if Vgs2[j]>Vt2:
            Ids2=0
        elif (Vgs2[j]<Vt2) & (Vds2[i]>=(Vgs2[j]-Vt2)):
            Ids2=(-beta*((Vgs2[j]-Vt2)-Vds2[i]/2))*Vds2[i]
        elif (Vgs2[j]<Vt2) & (Vds2[i]<(Vgs2[j]-Vt2)):
            Ids2=(-0.5*beta)*(Vgs2[j]-Vt2)**2
        Ids3.append(Ids2*1000)
    plt.plot(Vds2,Ids3,linewidth=2,label='Vgs= '+str(Vgs2[j]))
plt.title('IV characterstics curve of CMOS inverter')
plt.xlabel('Vds (volts)')
plt.ylabel('Ids (mA)')
plt.ylim([-3,3])
plt.xlim([-5,5])
plt.legend(loc='upper left',shadow=True)
plt.grid()
plt.show()

