# Steamdeck 使用感受
![..\image\blog2_steamdeck.png](..\image\blog2_steamdeck.png)
Steamdeck使用独特的SteamOS，基于ArchLinux改版得出的(个人猜测，未经验证)。
这个掌机的使用者对象应该是具有以下特征的:
- 对便携性高性能设备有需求的用户
- Steam库拥有较多游戏容量的用户
#### 1.steamdeck兼容问题 
SteamOS使用proton兼容层调用windowsAPI来进行.exe游戏文件运行。
所以SteamOS大部分支持有Value社认证标志的游戏，这里我会推荐protonDB，这是一个致力于让Windows游戏运行在linux上的社区，它的认证游戏多于Value社认证的游戏，我们使用proton就能兼容更多的游戏。
![..\\image\blog2_protondb.jpg](..\\image\blog2_protondb.png)
那么应该如何使用protonDB呢，有两种方法:
- 1.proton_QT+protontricks(红酒杯)
- 2.portproton:这个似乎是steam最近添加进来的，可以直接通过proton或者wine进行.exe游戏的驱动，安装如下图(portproton官网找的图，找的是俄语版本)
![..\\image\blog2_protononsteamdeck.png](..\\image\blog2_protononsteamdeck.png)
#### 2.steamdeck运行非linux下的游戏 
从B站上面搜索一些steamdeck移植游戏视频，可以看出，大部分steam游戏只需要导入steam即可启动，但是大部分导入都是通过steam调用兼容层来运行，对于使用其他启动器(EA,EPIC,R星)的游戏可能会导致使用困难。
例如:[SteamDeck运行最终幻想14](https://ottercorp.github.io/faq/steamdeck)
#### 3.steamdeck性能使用体验评测
Steamdeck已经被部分中国用户评测为"黄油启动利器"，那么我们不难根据这一项进行使用proton对于模拟结果的运行评测。
<!-- ![../image/blog2_userthoughts.jpg](../image/blog2_userthoughts.jpg) -->
SD内自带的discover商店搜索portproton进行下载后运行上述视频提供的游戏的结果:
|     名称      |     兼容层     | CPU-GPU  | 电源功率 |
| :-----------: | :------------: | :------: | :------: |
|  AIdealRays   | PROTON_LG_9-4  | 68%-100% |  23.2W   |
| AliceInCradle | WINE-PROTON-GE | 42%-50%  |  16.1W   |
|   DonaDona    | PROTON_LG_9-4  |   没测   |   没测   |

功率大概上下飘动26W左右。
# 我们使用的链接:
[Github一份教程](https://github.com/dzianismaroz/sd-port-proton)
[Linux下flathub下载](https://flathub.org/apps/ru.linux_gaming.PortProton)
[一些相似的评测](https://alancorn.github.io/blogs/2022/GamingWithWine.html)
[portproton官网.ru](https://linux-gaming.ru/)