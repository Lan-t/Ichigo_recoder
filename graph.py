# coding: UTF-8

import urllib.request
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def graph(res):

# テキストデコード
    text = res.decode('UTF-8')
    resList = [i for i in text.split('\n') if i != '' ]
    for i in range(resList.__len__()):
        resList[i] = resList[i].split(' ')

# list整理
    t = [[]]
    h = [[]]
    x = [[]]
    dates = [resList[0][0]]
    a = 0
    for i, date in enumerate(resList):
        if i != 0 and date[0] != resList[i-1][0]:
            x.append([])
            t.append([])
            h.append([])
            dates.append(date[0])
            a = a+1
        l = [ int(i) for i in date[1].split(':')]
    #x[a].append(l[0]*3600 + l[1]*60 + l[2])
        x[a].append(date[1].split(':')[0])
        t[a].append(int(date[2]))
        h[a].append(int(date[3]))



    c = 0
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    for i in range(len(x)):
        plt.subplot(2,len(x),i+1)
        plt.plot(x[i],t[i], label='t')
        plt.title('temperature / '+dates[i])
        plt.subplot(2,len(x),i+1+len(x))
        plt.plot(x[i],h[i], label='h', linestyle='--')
        plt.title('humidity / '+dates[i])

    plt.show()
    plt.savefig('resoureces/fig.png')




    print('exit')
