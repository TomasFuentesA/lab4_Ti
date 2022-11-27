import math as mt
import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist
import matplotlib.patches as mpatches

x1=[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.5, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 19.5, 20.0]
y1=[-43.5, -43.8, -44.0, -44.4, -47.4, -46.8, -46.0, -52.8, -49.9, -50.0, -49.0, -50.0, -52.8, -56.6, -60.6, -56.9, -55.5, -52.7, -53.2, -53.3, -54.3, -55.8, -58.9, -57.0, -55.8, -58.5, -59.4, -57.4, -60.5, -55.4, -60.4, -64.8, -63.0, -69.1, -66.9, -78.6, -73.2, -77.0, -79.5, -76.1, -76.9, -71.5, -76.1, -75.9, -74.6, -69.2, -83.5, -73.4, -81.9, -77.5]

x2=[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.5, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 19.5, 20.0]
y2=[-41.5, -43.4, -43.7, -53.2, -47.2, -46.2, -44.0, -43.1, -50.2, -54.8, -52.2, -48.3, -50.7, -51.2, -52.9, -50.9, -51.6, -54.8, -55.1, -53.1, -54.8, -55.1, -59.4, -61.5, -63.7, -65.9, -59.1, -58.2, -56.1, -57.7, -58.6, -60.9, -68.3, -61.5, -64.1, -68.2, -65.6, -69.6, -66.7, -69.7, -68.3, -73.3, -70.3, -72.1, -74.6, -74.7, -74.0, -72.8, -72.8, -74.5, ]

x3=[1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.5, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 19.5, 20.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.5, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 19.5, 20.0]
y3=[-43.5, -43.8, -44.0, -44.4, -47.4, -46.8, -46.0, -52.8, -49.9, -50.0, -49.0, -50.0, -52.8, -56.6, -60.6, -56.9, -55.5, -52.7, -53.2, -53.3, -54.3, -55.8, -58.9, -57.0, -55.8, -58.5, -59.4, -57.4, -60.5, -55.4, -60.4, -64.8, -63.0, -69.1, -66.9, -78.6, -73.2, -77.0, -79.5, -76.1, -76.9, -71.5, -76.1, -75.9, -74.6, -69.2, -83.5, -73.4, -81.9, -77.5, -41.5, -43.4, -43.7, -53.2, -47.2, -46.2, -44.0, -43.1, -50.2, -54.8, -52.2, -48.3, -50.7, -51.2, -52.9, -50.9, -51.6, -54.8, -55.1, -53.1, -54.8, -55.1, -59.4, -61.5, -63.7, -65.9, -59.1, -58.2, -56.1, -57.7, -58.6, -60.9, -68.3, -61.5, -64.1, -68.2, -65.6, -69.6, -66.7, -69.7, -68.3, -73.3, -70.3, -72.1, -74.6, -74.7, -74.0, -72.8, -72.8, -74.5]

def MSE(l1,l2):
    n = len(l1)

    x_sum = sum(l1)
    y_sum = sum(l2)

    x_sum2 = sum(mt.pow(i,2) for i in l1)
    xy_sum = sum(l1[i]*l2[i] for i in range(len(l1)))

    a = (n*xy_sum - (x_sum*y_sum))/(n*x_sum2 - (mt.pow(x_sum,2)))
    b = (y_sum/n) - (a*(x_sum/n))


    y = [m*a + b for m in l1]

    return y

x1 = [10*mt.log10(i) for i in x1]
x2 = [10*mt.log10(i) for i in x2]
x3 = [10*mt.log10(i) for i in x3]


y1 = [10**(i/10) for i in y1]
y1 = [10*mt.log10(1/i) for i in y1]

y2 = [10**(i/10) for i in y2]
y2 = [10*mt.log10(1/i) for i in y2]

y3 = [10**(i/10) for i in y3]
y3 = [10*mt.log10(1/i) for i in y3]

s1 = MSE(x1,y1)

s2 = MSE(x2,y2)

s3 = MSE(x3,y3)


def CDF(mean, std, pl):
    cdf = [NormalDist(mu=mean, sigma=std).cdf(i) for i in pl]
    return cdf

def piso_3(l1,l2,mse,cdf):

    fig, [ax, ax1] = plt.subplots(2,1)
    ax.scatter(l1,l2, color="blue")
    ax.plot(l1,mse, color="red")
    fig.suptitle("Piso 3")
    ax.set_title("Recta Meanshift Error")
    ax.set_xlabel("10*log(d)")         
    ax.set_ylabel("PL [dB]")
    l_1 = mpatches.Patch(color='blue', linestyle='-' ,label='PL')
    l_2 = mpatches.Patch(color='red', linestyle='-' ,label='MSE')
    ax.legend(handles=[l_1,l_2])
    ax.grid(True)
    
    ax1.set_title(r'CDF $\mu='+str(np.mean(mse))[0:5]+',\ \sigma='+str(np.std(mse))[0:5]+'$')
    cdf3 = CDF(np.mean(mse), np.std(mse), l2)
    ax1.scatter(l2,cdf3, color="green", marker="o", linewidths=0.00001)
    ax1.set_xlabel(r'PL[dB]')
    ax1.set_ylabel("Probabilidad")
      
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.savefig('Piso3.svg')
    fig.clear()
    plt.close(fig)


def piso_4(l1,l2,mse,cdf):

    fig, [ax2, ax3] = plt.subplots(2,1)
    ax2.scatter(l1,l2, color="blue")
    ax2.plot(l1,mse, color="red")
    fig.suptitle("Piso 4")
    ax2.set_title("Recta Meanshift Error")
    ax2.set_xlabel("10*log(d)")         
    ax2.set_ylabel("PL [dB]")
    l_1 = mpatches.Patch(color='blue', linestyle='-' ,label='PL')
    l_2 = mpatches.Patch(color='red', linestyle='-' ,label='MSE')
    ax2.legend(handles=[l_1,l_2])
    ax2.grid(True)

    ax3.set_title(r'CDF $\mu='+str(np.mean(mse))[0:5]+',\ \sigma='+str(np.std(mse))[0:5]+'$')
    cdf3 = CDF(np.mean(mse), np.std(mse), l2)
    ax3.scatter(l2,cdf3, color="green",marker='o', linewidths=0.00001)
    ax3.set_xlabel(r'PL[dB]')
    ax3.set_ylabel("Probabilidad")
    
    
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.savefig('Piso4.svg')
    fig.clear()
    plt.close(fig)

def piso_3_4(l1,l2,mse,cdf):

    fig, [ax4, ax5] = plt.subplots(2,1)
    ax4.scatter(l1,l2, color="blue")
    ax4.plot(l1,mse, color="red")
    fig.suptitle("Piso 3 y 4")
    ax4.set_title("Recta Meanshift Error")
    ax4.set_xlabel("10*log(d)")         
    ax4.set_ylabel("PL [dB]")
    l_1 = mpatches.Patch(color='blue', linestyle='-' ,label='PL')
    l_2 = mpatches.Patch(color='red', linestyle='-' ,label='MSE')
    ax4.legend(handles=[l_1,l_2])
    ax4.grid(True)
    
    ax5.set_title(r'CDF $\mu='+str(np.mean(mse))[0:5]+',\ \sigma='+str(np.std(mse))[0:5]+'$')   
    ax5.scatter(l2,cdf3, color="green", marker='o', linewidths=0.00001)
    ax5.set_xlabel(r'PL[dB]')
    ax5.set_ylabel("Probabilidad")
    
    
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.savefig('Piso_3_4.svg')
    fig.clear()
    plt.close(fig)

cdf1 = CDF(np.mean(s1), np.std(s1), y1)   
cdf2 = CDF(np.mean(s2), np.std(s2), y2)   
cdf3 = CDF(np.mean(s3), np.std(s3), y3)    

piso_3(x1,y1,s1,cdf1)
piso_4(x2,y2,s2,cdf2)
piso_3_4(x3,y3,s3,cdf3)

plt.title('CDFs de los 3 casos')
plt.scatter(y1,cdf1, color="blue",marker="+")
cdf1_l = mpatches.Patch(color='blue', linestyle='-' ,label='Piso 3')
plt.scatter(y2,cdf2, color="red", marker=".", linewidths=0.1)
cdf2_l = mpatches.Patch(color='red', linestyle='-',label='Piso 4')
plt.scatter(y3,cdf3, color="green", marker="*", linewidths=0.001) 
cdf3_l = mpatches.Patch(color='green', linestyle='-',label='Piso 3 y 4')
plt.legend(handles=[cdf1_l, cdf2_l, cdf3_l])
plt.xlabel("PL[dB]")
plt.ylabel("Probabilidad")
plt.grid()
plt.show()
plt.savefig('CDF.svg')    

