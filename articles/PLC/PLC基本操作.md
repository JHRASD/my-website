# PLC基本操作

发布日期：2026/3/24
分类：PLC

---

## 前言

  事情是这样的，上次寒假不是去参加了一个赛项吗？就在临前的那一个月学plc,力控（组态软件），结果比赛完过了一个年，就全部忘光了（ 现在老师又要我负责去学这部分内容，估计是带新人或继续参加比赛，又得重新捡起来了

## 博图V17的基本使用：
一、创建项目
在主页面，点击创建新项目，无脑下一步，然后在新的页面打开项目视图

添加新设备：选1215C AC/DC/Rly (版本需要大于4,不然无法仿真)
<details>
   <summary>点击查看图片</summary>
   <img src="articles/PLC/img/234104.png" style="width:100%; max-width:600px; margin-top:10px;">
</details>

弹出来的安全设置需要关闭保护，plc访问保护改为完全访问
<details>
   <summary>点击查看图片</summary>
   <img src="articles/PLC/img/235058.png" style="width:100%; max-width:600px; margin-top:10px;">
</details>

然后双击PLC，找到防护和安全，关闭保护机密的plc组态数据,基本就设置完了

## 画梯形图，仿真的流程

在main入口，拖入


