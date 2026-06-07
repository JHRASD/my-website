# LC滤波和振荡

  日期：25/6/7
  分类：模电

---
#### 低通滤波

**计算截止频率**：
\[
f_c = \frac{1}{2\pi\sqrt{LC}}
\]

**设计实例**：截止频率 1kHz

先选电容 C = 16nF（0.000000016F）  
计算对应的电感 L：

\[
L = \frac{1}{(2\pi f_c)^2 C} = \frac{1}{(2 \times 3.14 \times 1000)^2 \times 16 \times 10^{-9}} \approx 1.59 \text{H}
\]

<img src="/articles/Analog Devices/img/LC低通.png" alt="LC低通" style="max-width:100%; height:auto;">


L 串联，C 并联到地，输出取 C 两端
输出端接入的电阻频率就是1khz衰减的0.07倍

#### LC 升压谐振
输出端不负载，能量在 L 和 C 之间来回交换,电压变大，波形变尖

<img src="/articles/Analog Devices/img/升压谐振电路.png" alt="谐振" style="max-width:100%; height:auto;">

#### LC振荡电路
<img src="/articles/Analog Devices/img/LC振荡.gif" alt="振荡" style="max-width:100%; height:auto;">

5v的电压中能达到560多的局部电压
原理：局5V电源产生560V局部电压，不是电阻分压或谐振升压，而是因为电感在开关断开瞬间，其存储的磁能（½LI²）需要释放。当开关断开速度极快时，产生极高的反电动势（V = -L·dI/dt），通过二极管给电容充电。电容电压逐渐累积，最终达到560V，远远超过电源电压。在这个过程中，电感和电容确实在振荡，但电压峰值的大小主要取决于开关断开的速度和电感储能

一般用于
- 无线电调谐
- 无线充电