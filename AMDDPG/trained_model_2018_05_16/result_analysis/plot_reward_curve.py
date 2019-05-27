# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt
import numpy as np



# 画图显示中文
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib.font_manager
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False



file_path = "reward_5500_episode_Aalborg.json"
reward_file = open(file_path, 'r')
Reward = json.load(reward_file)
num_steps = len(Reward[-1])

for reward in Reward:
    print(len(reward), reward[-1])
    reward += list( reward[-1] * np.ones(num_steps- len(reward)) )

#plt.figure(figsize=(9,6))
#plt.grid(linestyle = "--")      #设置背景网格线为虚线
ax = plt.gca()
#ax.spines['top'].set_visible(False)  #去掉上边框
#ax.spines['right'].set_visible(False) #去掉右边框

'''
plt.plot(Reward[3], color='red', label='aggregated-policy', linewidth=3)
plt.plot(Reward[0], '--', color='blue', label='sub-policy 1', linewidth=2)
plt.plot(Reward[1], ':', color='green', label='sub-policy 2', linewidth=2)
plt.plot(Reward[2], '-.', color='purple', label='sub-policy 3', linewidth=2)
'''
plt.plot(Reward[3], color='red', label='集成策略', linewidth=3)
plt.plot(Reward[0], '--', color='blue', label='子策略 1', linewidth=2)
plt.plot(Reward[1], ':', color='green', label='子策略 2', linewidth=2)
plt.plot(Reward[2], '-.', color='purple', label='子策略 3', linewidth=2)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# plt.xlabel('Step', fontsize=16)
# plt.ylabel('Cumulative Reward', fontsize=16)
plt.xlabel('汽车行驶步数', fontsize=16)
plt.ylabel('累积回报', fontsize=16)
plt.legend(loc=0, numpoints=1, fontsize=16)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.subplots_adjust(top = 0.98, bottom = 0.13, right = 0.98, left = 0.18, hspace = 0.20, wspace = 0.20)
plt.setp(ltext, fontsize=12)  #设置图例字体的大小和粗细
#plt.savefig(file_path[:-4] + 'svg', format='svg', bbox_inches = 'tight')
#plt.savefig(file_path[:-4] + 'svg', format='svg')
plt.savefig('集成策略与子策略的回报值对比.svg', format='svg')
plt.show()


"""
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial']  #如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False  #显示负号
 
x = np.array([3,5,7,9,11,13,15,17,19,21])
A = np.array([0.9708, 0.6429, 1, 0.8333, 0.8841, 0.5867, 0.9352, 0.8000, 0.9359, 0.9405])
B= np.array([0.9708, 0.6558, 1, 0.8095, 0.8913, 0.5950, 0.9352, 0.8000, 0.9359, 0.9419])
C=np.array([0.9657, 0.6688, 0.9855, 0.7881, 0.8667, 0.5952, 0.9361, 0.7848, 0.9244, 0.9221])
D=np.array([0.9664, 0.6701, 0.9884, 0.7929, 0.8790, 0.6072, 0.9352, 0.7920, 0.9170, 0.9254])
 
#label在图示(legend)中显示。若为数学公式，则最好在字符串前后添加"$"符号
#color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
#线型：-  --   -.  :    , 
#marker：.  ,   o   v    <    *    +    1
plt.figure(figsize=(10,5))
plt.grid(linestyle = "--")      #设置背景网格线为虚线
ax = plt.gca()
ax.spines['top'].set_visible(False)  #去掉上边框
ax.spines['right'].set_visible(False) #去掉右边框
 
plt.plot(x,A,color="black",label="A algorithm",linewidth=1.5)
plt.plot(x,B,"k--",label="B algorithm",linewidth=1.5)
plt.plot(x,C,color="red",label="C algorithm",linewidth=1.5)
plt.plot(x,D,"r--",label="D algorithm",linewidth=1.5)
 
group_labels=['dataset1','dataset2','dataset3','dataset4','dataset5',' dataset6','dataset7','dataset8','dataset9','dataset10'] #x轴刻度的标识
plt.xticks(x,group_labels,fontsize=12,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=12,fontweight='bold')
plt.title("example",fontsize=12,fontweight='bold')    #默认字体大小为12
plt.xlabel("Data sets",fontsize=13,fontweight='bold')
plt.ylabel("Accuracy",fontsize=13,fontweight='bold')
plt.xlim(3,21)         #设置x轴的范围
#plt.ylim(0.5,1)
 
#plt.legend()          #显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=12,fontweight='bold') #设置图例字体的大小和粗细
 
plt.savefig('D:\\filename.svg',format='svg')  #建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
plt.show()
"""
