# ESP32 GPIO 基础教程

 发布日期：2026-02-22  
 分类：ESP32

---

## 一、什么是 GPIO？

GPIO（通用输入输出引脚）是 ESP32 上最常用的功能之一。

它可以用来：

- 输出高低电平
- 读取按钮状态
- 控制 LED
- 连接传感器

---

## 二、GPIO 的四种模式

- OUTPUT（输出）
- INPUT（输入）
- INPUT_PULLUP（上拉输入）
- INPUT_PULLDOWN（下拉输入）

---

## 三、示例代码：点亮 LED

```cpp
int LED = 2;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);
}
