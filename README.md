# BOFO
BOFO means _**bring old factories online**_. We try to use a series of imaging processing technologies to bring all the old gauges online.

## 个人简介
赵之，一个能读懂科研文献的工程师。供职于某企业的研发中心，在一堆科学家中工作。个人的使命是为众多的科学家服务，把他们研究的各项技术集成成产品。

## 开源声明与免责声明
从最开始有BOFO这个想法的时候，就下定决心要将整个项目开源。在工业互联网和人工智能上，我和很多人一样只是一个初学者，希望我的工作能给更多的初学者带来灵感。由于本人现在就职于某公司，因此会在此开源部分屏蔽掉所有取之于公司的东西。
>"取之开源，用之开源"。

## 这里有什么？
BOFO是一个基于python开发的项目，整个项目包含了：
- 一个基于嵌入式系统的传感器集群（目前基于树莓派）
- 一个图像识别和配置终端
- 一系列的人工智能图像识别的尝试

以及，更为重要的，整个项目从0到1的点滴细节。

## 目前
BOFO目前正在开发之中。各项模块都在逐步搭建之中。大家[开发日志][https://github.com/AppliedAIGroup/BOFO/blob/master/Devlog/Devlog.md]见。



Hi,everone. The BOFO project relies on a smart gauge containting camera, ARM and WIFI moduels,so some codes in this repository need this hardwears. But we also have some fleet management & algorithm configuration you can use.


### What's now (Untill 2017.8.23)
We've finshed the Demo of BOFO in June. And now we are heading for the pilot test.

### What's next. Target of Pilot test
Now, we are heading for the pilot test. 
对于软件部分，当Pilot test开始的时候，我们需要一个fleet management的主机,监视所有Pi的运行。同时需要一个算法的远程配置窗口，用于更新和配置算法，运行在workstation上。而对于Pi内部来说，需要两部分的软件，一部分是算法，另一部分是configuration部分。
The BOFO software should have 4 parts: two parts inside raspiberry Pi :image processing, gauge configuration. and two parts on 
fleet management, remote configuration.

#### todo 
1.powertest with 10000 mhA batteries and 60,600 seconds sleep time.