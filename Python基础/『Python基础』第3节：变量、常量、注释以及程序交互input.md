---
title: 『Python基础』第3节：变量、常量、注释以及程序交互input
keywords: 变量、常量、注释以及程序交互input
description: 变量、常量、注释以及程序交互input
categories: Python全栈之路
tags:
  - Python基础
avatar: 'https://wx1.sinaimg.cn/large/006bYVyvgy1ftand2qurdj303c03cdfv.jpg'
photos: >-
  https://static.2heng.xin/wp-content/uploads//2019/02/wallhaven-672007-1-1024x576.png
author: 李培冠
authorLink: 'https://lipeiguan.top'
authorAbout: 一个好奇的人
authorDesc: 一个好奇的人
comments: true
abbrlink: 993123629
date: 2019-06-30 12:24:26
---

## 一. 变量

### 1. 变量是什么？

变量，是指把程序运行的中间结果临时的存在内存里，以便后续的代码调用，其值可以修改。

在python中，当变量被使用时，在内存里将产生两个动作，一是开辟指定地址的空间，二是赋予指定的变量值。

在python语言中，变量在指定的同时，必须强制赋初值，否则解释器报错。

```python
name        # name变量未赋值，解释器认为非法，报未定义错误
name = 'kidd'        # name变量赋予初值'kidd'，解释器执行通过
```

这里的name为变量名，其值为'kidd'。Python变量赋值通过等号(`=`)来实现。

变量建立的结果，往往被其他代码所使用。例如：

```python
x = 1 + 2 + 3 + 4
print(x)        # print函数打印变量x的结果，输出10
```

### 2. 多个变量赋值

Python允许同时为多个变量赋值。

```python
one = two = three = 1
print(one, two, three)        # print函数允许多值打印输出，用逗号分隔变量
注：one, two, three三个变量在内存中指向同一个地址。也可以按照下面的格式，给不同的变量名赋值：
one, two, three = 1, 1, 1
print(one, two, three)        # print输出值也为三个连续的1
```

### 3. 变量值类型

所有编程语言的变量值都是分类型的，Python语言变量值的类型在赋值后才被隐性确定。

例如x = 0，那么0就是整数类型的值；x = 'ok'，那么ok就是字符串类型的值；x = True，那么True就是布尔类型的值。

Python语言的基本变量类型包括字符串、数字、列表、元组、字典五大类。


> 变量命名规则
> （1）变量只能由字母、数字、下划线组成。
> （2）不能以数字开头。
> （3）不能是python中的关键字
> （4）大小写区分，a = 1和A = 1是两个变量。

以上要求是必须满足的，下面的要求要尽量做到

> （5）变量名要有描述性，要简洁、易读，不宜过长。
> （6）变量名不能使用中文以及拼音。
> （7）官方推荐使用的变量名：
>     	- 下划线：my_name = 'kidd'
>     	- 驼峰体：MyName = 'kidd'

看个例题:

```python
age1 = 18
age2 = age1
age3 = age2
age2 = 23
print(age1, age2, age3)
```

![](https://i.loli.net/2019/07/19/5d30b520bc21199387.png)

> 变量只能指向数据, 不能指向变量;
> 变量在内存中是唯一命名的.

## 二. 常量

常量，即不能变的数据对象。

> 在Python中, 没有真正的常量. 为了迎合其他语言, Python定义全部大写的变量为常量, 且放在文件的最上面。
> 虽然在Python中常量也可以改变, 但一般约定俗成不能改变. 


```python
NAME = ‘kidd’
```

注意: 下面的代码虽然把常量的值改了也没有报错, 但是请不要这样做.

```python
NAME = 'kidd'
print(NAME)  # kidd
NAME = 'Conan'
print(NAME)  # Conan
```

## 三. 注释

> 注释是对一些比较晦涩难懂的代码进行解释说明, 便于理解. 

```
单行注释: #
多行注释: """被注释的内容""" 或者 '''被注释的内容'''
```

## 四. 程序交互input

input() 以字符串的方式获取用户的输入内容

```python
a = input('>>>')
# 如果用户输入123
print(type(a))  # <class 'str'>
```


