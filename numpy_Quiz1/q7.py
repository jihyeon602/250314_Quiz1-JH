import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    x = np.arange(10)
    
    # 초기 figure와 축을 설정합니다.
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    # y = x 그래프를 그립니다. 따라서 x 데이터는 x, y 데이터도 x로 설정합니다.
    # label은 'y=x'로 설정하고, 마커는 'o', 마커 색깔은 'blue', 그래프의 선 스타일은 ':'로 설정합니다.
    ax.plot(x, 'o:b', label = 'y=x')
    
    # y = x^2 그래프를 그립니다. 따라서 x 데이터는 x, y 데이터는 x**2으로 설정합니다.
    # label은 'y=x^2'로 설정하고, 마커는 '^', 마커 색깔은 'red', 그래프의 선 스타일은 '--'로 설정합니다.
    ax.plot(x**2, '^--r', label = 'y=x^2')
    
    # 그래프 제목을 'Graph'로 설정합니다.
    ax.set_title("Graph")
    
    # x label은 'x', y label은 'y'로 설정합니다.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # x 범위는 0부터 10까지, y 범위는 0부터 100까지로 설정합니다.
    ax.axis([0, 10, 0, 100])
    
    # 범례의 위치는 'upper left'로 하고, 그림자 효과는 넣고, 테두리는 둥글게 합니다.
    ax.legend(loc='upper left', shadow = True, fancybox = True)
    
    # figure를 "plot.png"라는 이름으로 저장하세요.
    plt.savefig("plot.png")
    
    plt.show()

if __name__ == "__main__":
    main()

