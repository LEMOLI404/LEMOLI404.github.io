# -*- coding: UTF-8 -*-（python3默认的编码格式是utf-8格式）
#coding=utf-8

#调用matplotlib以及numpy函数库
import matplotlib.pyplot as plt 
import numpy as np 

plt.rcParams['font.sans-serif'] = ['SimHei']  #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False  #用来正常显示负号

#设置阶跃函数的自定义函数：当x>=0时返回1
def JY (x):
    return np.array(x>=0,dtype=np.int_)
#设置冲击函数的自定义函数：当x==0时返回1
def CJ (x):
    return np.array(x==0,dtype=np.int_)
#设置锯齿函数的自定义函数：返回1-x%1
def JC (x):
    return 1-x%1

#arange()函数 : np.arange(start,stop,step,dtype=None),括号内分别为(起点值 默认0,终点值,步长 默认1,数据类型 默认None)
#linspace()函数 : linspace(x1,x2,N),括号内分别为(起点值,结束值,样本数 默认50)
#plt.subplot(n,m,p) : m表示m行，n表示n列，p表示图的位置(先上后下，先左后右)
#plt.title(' ') : 图表标题
#plt.plot(x,y) : 绘制连续图像
#plt.stem(x, y) : 绘制茎叶图


#阶跃——连续信号
t1 = np.arange(-10,10,0.01) 
plt.subplot(2,1,1)
plt.title('阶跃_连续') 
y1 = JY (t1)
plt.plot(t1,y1)

#阶跃——离散信号
t2 = np.arange(-10,10,1) 
plt.subplot(2,1,2)
plt.title('阶跃_离散') 
y2 = JY (t2)
plt.stem(t2, y2)
plt.show()

#冲击连续做不出来
#冲击——离散信号
t3 = np.arange(-10,10,1) 
plt.subplot(2,1,2)
plt.title('冲击_离散') 
y3 = CJ (t3)
plt.stem(t3, y3)
plt.show()

#余弦——连续信号
t4 = np.linspace(0,3*np.pi,100)
y4 = np.cos(t4)

plt.subplot(2,1,1)
plt.title(r'$f(x)=cos(x)$') 
plt.plot(t4, y4)

#余弦——离散信号
t5 = np.arange(0,10,0.5) 
y5 = np.cos(t5)
plt.subplot(2,1,2)
plt.title(r'$f[x]=cos[x]$') 
plt.stem(t5, y5)
plt.show()

#锯齿——连续信号
t6 = np.arange(-10,10,0.01) 
plt.subplot(2,1,1)
plt.title('锯齿_连续') 
y6 = JC (t6)
plt.plot(t6,y6)

#锯齿——离散信号
t7 = np.arange(-10,10,0.05) 
plt.subplot(2,1,2)
plt.title('锯齿_连续') 
y7 = JC (t7)
plt.stem(t7,y7)
plt.show()