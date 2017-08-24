# BOFO
BOFO means bring old factories online. We try to use a series of imaging processing technologies to bring all the old gauges online.

## Hello there!
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