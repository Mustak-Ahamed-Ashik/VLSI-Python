import numpy as np
import matplotlib.pyplot as plt

beta=0.000240
Vt2=-0.7
Vds2=np.linspace(-5,0,num=100)
Vgs2=np.arange(-5,0)
plt.figure(figsize=(15,10))
for j in range (len(Vgs2)):
    Ids=[]
    for i in range(len(Vds2)):
        if Vgs2[j]>Vt2:
            Ids2=0
        elif (Vgs2[j]<Vt2) & (Vds2[i]>=(Vgs2[j]-Vt2)):
            Ids2=(-beta*((Vgs2[j]-Vt2)-Vds2[i]/2))*Vds2[i]
        elif (Vgs2[j]<Vt2) & (Vds2[i]<(Vgs2[j]-Vt2)):
            Ids2=(-0.5*beta)*(Vgs2[j]-Vt2)**2
        Ids.append(Ids2*1000)
    plt.plot(Vds2,Ids,linewidth=2,label='Vgs= ' +str(Vgs2[j]))
plt.title('I-V curve of PMOS')
plt.xlabel('Vds (volts)')
plt.ylabel('Ids (mA)')
plt.ylim([-3,0])
plt.xlim([-5,0])
plt.legend(loc= 'lower left', shadow=True)
plt.show()
