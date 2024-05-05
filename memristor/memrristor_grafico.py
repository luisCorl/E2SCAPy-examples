from matplotlib import pyplot as plt
import numpy as np
import copy

def vexor(init,fin,paso):
    out = [init]
    tempo = copy.deepcopy(init)
    total_iter = (fin-init)/paso
    for i in range(int(total_iter)):
        tempo += paso
        out.append(tempo)
    return out
def vexor2(init,fin,paso,num):
    out = [num]
    tempo = copy.deepcopy(init)
    total_iter = (fin-init)/paso
    for i in range(int(total_iter)):
        out.append(num)
    return out
def S(A,w,t,v1):
    w = 2*np.pi*1e3
    
    return 0.5*2*np.pi*1e3*np.cos(2*np.pi*1e3*t) 

def calculo(vexor,s):
    ron=100.7
    roff=12.6e3
    k=17803.4
    m=3
    R1 = 100e9;
    R2 = 10
    R3 = 10e6;
    R4 = 10
    C1 = 1
    A = 1.2
    w = 50*2*np.pi
    t = vexor(0,0.2,0.001)
    yv1 = vexor2(1,len(t),1,0)#V(te)
    yv2 = vexor2(1,len(t),1,0)#V(Y)
    yg1 = vexor2(1,len(t),1,0)
    yg2 = vexor2(1,len(t),1,0)
    yv3 = vexor2(1,len(t),1,0)
    print(yv3)
    
    V1 = 0
    V2 = 0.0
    V3 = 0
    G1 = 0.001
    G2 = 9000
    print(t)
    print('long t',len(t))
    print('long yn',len(yv1))
    print(s(A,w,t[0],yv1[0]))
    for k in range(0,len(t),1):
        
        V1 = A*np.sin(w*t[k])
        S = s(A,w,t[k],V1)
        
        
        
        V2 = R3*V1*(C1*S*G1*R1*R2 + G1*R2 - G2*R1)/(C1*S*G1*R1*R2*R3 + C1*S*R1*R2 + C1*S*R1*R3 + G1*R1*R2 + G1*R2*R3 + G2*R1*R2 + R1 + R2 + R3)
        V3 = R2*V1*(C1*G1*R1*R3*S + G1*R1 + G1*R3 + G2*R1)/(C1*G1*R1*R2*R3*S + C1*R1*R2*S + C1*R1*R3*S + G1*R1*R2 + G1*R2*R3 + G2*R1*R2 + R1 + R2 + R3)
       

        yv1[k] = V1
        yv2[k] = V2
        yv3[k] = V3
        
        
    return t,yv1,yv2,yv3,yg1,yg2
t,yv1,yv2,yv3,yg1,yg2 = calculo(vexor,S)

##creando objeto de plt
fig, axs = plt.subplots(4,1,figsize=(4,8))

axs[0].plot(t[:len(t)-1], yv1[:len(yv1)-1], color='blue')
axs[0].set_xlabel('Tiempo')
axs[0].set_ylabel('yv1')
axs[0].set_title('voltaje nodo 1')
axs[0].grid(True)

axs[1].plot(yv1[:len(yv1)-1], yv2[:len(yv2)-1], color='green')
axs[1].set_xlabel('yv2')
axs[1].set_ylabel('yv1')
axs[1].set_title('histeresis')
axs[1].grid(True)

axs[2].plot(t[:len(t)-1], yv2[:len(yv2)-1], color='red')
axs[2].set_xlabel('Tiempo')
axs[2].set_ylabel('yv2')
axs[2].set_title('voltaje nodo 2')
axs[2].grid(True)

axs[3].plot(t[:len(t)-1], yv3[:len(yv3)-1], color='black')
axs[3].set_xlabel('t')
axs[3].set_ylabel('yv3')
axs[3].set_title('histeresis')
axs[3].grid(True)

plt.tight_layout()
plt.show()
