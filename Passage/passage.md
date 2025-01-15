> 非商业转载于
[《数字图像处理(第四版)》阅读随笔 ch4 (频率域滤波)](https://zhuanlan.zhihu.com/p/360557063)

# 频率域滤波基础
#### 频率域的其他特性

由二维DFT公式：

$$F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}f(x,y)e^{-j2\pi(ux/M+vy/N)}$$

可知，式中 $F(u,v)$ 的每一项都包含用指数项修改过的 $f(x,y)$ 的所有值。于是，将一幅图像的某些规定分量与其变换直接联系起来通常是不可能的。然而，对于傅里叶变换的频率分量与图像的空间特征之间的关系，我们可以做一些一般性的说明。例如，由于频率与空间变化率直接相关，因此直观的将傅里叶变换中的频率与图像中的灰度变化模式关联起来并不困难。

变化最慢的频率分量$（ u=v=0 ）$与图像的平均灰度成正比。远离变换的原点时，低频对应于图像中变化缓慢的灰度分量。例如，在一幅房间图像中，低频可能对应于墙壁和地板的平滑灰度变化。更加远离原点时，较高的频率开始对应于图像中越来越快的灰度变化。它们是图像中由灰度急剧变化表征的物体边缘或其他分量。

#### 频率域滤波基础知识

频率域滤波的步骤是，首先修改一幅图像的傅里叶变换，然后计算其反变换，得到处理后的结果的空间域表示。因此，若已知大小为 $P\times Q$ 像素的一幅（经过填充的）数字图像 $f(x,y) $,则我们感兴趣的基本滤波公式为：

$$ g(x,y)=Real\left\{ \Im^{-1}[H(u,v)F(u,v)] \right\}$$

式中， $\Im^{-1}$ 是IDFT， $F(u,v)$ 是输入图像 $f(x,y)$ 的DFT， $H(u,v)$ 是滤波器传递函数（更常称为滤波器或滤波器函数）， g(x,y) 是滤波后的（输出）图像。函数 $F,H,g$ 是大小为 $P\times Q$ 的阵列，即填充过的输入图像的大小。乘积 $H(u,v)F(u,v)$ 是由对应元素相乘得到的。滤波器传递函数修改输入图像的变换，得到处理后的输出 $g(x,y)$ 。使用中心对称的函数，可大大简化规定 $H(u,v)$ 的任务，这一任务要求 $F(u,v)$ 也中心化，这是在计算变换之前，用 $(-1)^{x+y}$ 乘以输入图像来完成的。

具体而言，我们在本章中采用的方法是将图像零填充到 $P\times Q$ 大小，并在频率域直接构建相同维数的滤波器传递函数。

最后分析滤波后的图像的相角。DFT可以表示为实部和虚部，即 $F(u,v)=R(u,v)+jI(u,v)$ 。于是，频率域滤波的公式变为：

$$g(x,y)=\Im^{-1}[H(u,v)R(u,v)+jH(u,v)I(u,v)]$$

相角计算为复数的实部与虚部之比的反正切。因为 $H(u,v)$ 同时乘以 $R$ 和 $I$ ，所以当这个比率形成后，它会被抵消。对实部和虚部的影响相同且对相角无影响的滤波器，被恰当地称为零相移滤波器。本章中仅考虑这类滤波器。

#### 频率域滤波步骤小结

频率域中的滤波过程小结如下：

Step 1：已知一幅大小为 $M\times N$ 的输入图像 $f(x,y)$ ，计算填充后的尺寸为 $P\times Q$ ，这里 $P=2M$ ， $Q=2N$ ；

Step 2：使用零填充，镜像填充或复制填充，形成大小为 $P\times Q$ 的填充后的图像 $f_p(x,y)$；

Step 3： 将 $f_p(x,y)$ 乘以 $(-1)^{x+y}$ ，使傅里叶变换位于 $P\times Q$ 大小的频率矩阵的中心；

Step 4：计算步骤3得到的图像的DFT，即 $F(u,v)$ ;

Step 5：构建一个实对称的滤波器传递函数 $H(u,v)$ ，其大小为 $P\times Q$ ，中心在 $(P/2,Q/2)$ 处；

Step 6：采用对应像素相乘得到 $G(u,v)=H(u,v)F(u,v)$ ，即 $G(i,k)=H(i,k)F(i,k)$ ， $i=0,1,2,...,P-1$ ， $k=0,1,2,...,Q-1$ 。

Step 7：计算 $G(u,v)$ 的IDFT得到滤波后的图像（大小为 $P\times Q$ ）：

$$g_p(x,y)=\left\{ real[\Im^{-1}[G(u,v)]] \right\}(-1)^{x+y}$$

Step 8：最后，从 $g_p(x,y)$ 的左上象限提取一个大小为 $M\times N$ 的区域，得到与输入图像大小相同的滤波后的结果 $g(x,y)$ 。

#### 空间域和频率域滤波之间的对应关系

空间域滤波和频率域滤波之间的纽带是卷积定理。本节前面将频率域滤波定义为滤波器传递函数 $H(u,v)$ 与输入图像的傅里叶变换 $F(u,v)$ 的对应像素相乘。已知 $H(u,v)$ 时，假设我们想要求其空间域中的等效核，则计算 $\Im^{-1}\left\{ H(u,v) \right\}$ ，它是空间域中的对应核。相反，由类似的分析和卷积定理可知，若已知一个空间域滤波核，则可用这个核的傅里叶正变换得到其频率域中的表达式。因此，两个滤波器形成了一个傅里叶变换对：

$$h(x,y)\Leftrightarrow H(u,v)$$

上式中， $h(x,y)$ 是空间核。因为这个核可由一个频率域滤波器对一个冲激的相应得到（ 若$f(x,y)=\delta(x,y)$，则$F(u,v)=1$ ），因此有时，我们称 $h(x,y)$ 是 $H(u,v)$ 的冲激响应。由于离散实现中的所有数据都是有限的，因此这样的滤波器称为有限冲激响应（FIR）滤波器。这些滤波器是本书中唯一考虑的线性空间滤波器。

空间卷积运算非常适合采用硬件和/或固件的小型核。但在使用普通计算机时，使用快速傅里叶变换（FFT）算法计算DFT的频率域方法，要比空间卷积运算的速度快几百倍，具体取决于所用核的大小。

频率域中的滤波概念更加直观，且频率域中的滤波器设计也更容易。充分利用频率域和空间域性质的一种方法是，在频率域中规定一个滤波器，计算其IDFT，然后利用生成的全尺寸空间核的性质，指导构建较小的核。

我们对于基于高斯函数的滤波器非常感兴趣，因为高斯函数的傅里叶正，反变换都是实高斯函数。为了便于说明基本原理，我们将讨论限制在一维情况。二维高斯传递函数将在本章后面讨论。

令 $H(u)$ 表示一维频率域高斯传递函数：

$$H(u)=Ae^{-u^2/2\sigma^2}$$

式中， $\sigma$ 是高斯曲线的标准差。空间域中的核由 $H(u)$ 的傅里叶反变换得到：

$$h(x)=\sqrt{2\pi}\sigma Ae^{-2\pi^2\sigma^2x^2}$$

这两个公式很重要，原因有二：

（1）它们是一个傅里叶变换对，两者都是高斯函数和实函数。由于不涉及复数，因此方便了分析。另外，高斯曲线非常直观，并且易于操作；

（2）两个函数的表现相反。例如， $H(u)$ 的外形较宽时（ $\sigma$ 值较大）时， $h(x)$ 的外形较窄，反之亦然。事实上，当 $\sigma$ 趋近于无限时， $H(u)$ 趋近于一个常数函数，而 $h(x)$ 趋近于一个冲激，这意味着在频率域和空间域都不进行滤波运算。

使用系数全部为正的一个核就可用在空间域实现低通滤波。频率域函数越窄，其衰减的低频越多，导致的模糊越大。在空间域中，这意味着必须使用较大的核来增大模糊。

一个常量减去低通函数，就可以由一个低通滤波器构建一个高通滤波器。由于我们正在使用高斯函数，因此使用所谓的高斯差（涉及两个低通函数），就可以更好地控制滤波函数的形状。在频率域中，这变为：

$$H(u)=Ae^{-u^2/2\sigma_1^2}-Be^{-u^2/2\sigma_2^2}$$

上式中， $A\geq B$ ， $\sigma_1>\sigma_2$ 。空间域中的对应函数是：

$$h(x)=\sqrt{2\pi}\sigma_1Ae^{-2\pi^2\sigma_1^2x^2}-\sqrt{2\pi}\sigma_2Be^{-2\pi^2\sigma_2^2x^2}$$

$h(x)$ 有一个重要的特性，即它的中心是一个正项，中心两侧有许多负项（空间域高通滤波核的特征）。

有些在空间域中非常难以处理的任务，就可以在频率域中使用FFT直接实现这个滤波器，也可取这个传递函数的IDFT得到等价的空间域函数。

#### 由空间核得到频率域传递函数

通常，当滤波器较小时，在计算上空间滤波器要比频率域滤波更有效率。Brigham[1988]曾使用一维函数对此进行了比较，结果表明，当滤波器有大约32个或更多元素时，使用FFT算法的滤波处理要比空间实现快，所以所讨论问题中的这个数字并不大。

下面这个函数用于填充图像，代码来源于《数字图像处理（Matlab版）（第二版）》。

```matlab
function PQ = paddedsize(AB, CD, PARAM)
%使用基于FFT滤波器时的填充大小计算
if nargin == 1
    PQ = 2 * AB;
elseif nargin == 2 && ~ischar(CD)
    PQ = AB + CD -1;
    PQ = 2 * ceil(PQ / 2);
elseif nargin == 2
    m = max(AB); %Maximun dimension
    
    %Find power-of-2 at least twice m.
    P = 2^nextpow2(2*m);
    PQ = [P,P];
elseif (nargin == 3) && strcmpi(PARAM,'pwr2')
    m = max([AB CD]);%Maximum dimension.
    P = 2^nextpow2(2*m);
    PQ = [P,P];
else
    error('Wrong number of inputs.')
end
end
```

于是，我们可以根据空间域的核（以垂直Sobel为例），绘制出其对应的频率域滤波器的图像。

```matlab
clear all;
cover = double(imread('1.pgm'));%读入图像
F = fft2(cover);%对图像进行DFT变换
S = fftshift(log(1+abs(F))); %得到傅里叶频谱
h = [1 0 -1; 2 0 -2; 1 0 -1];%给定空间域滤波器，也可以通过h = fspecial('sobel')'获取
PQ = paddedsize(size(cover));
H = freqz2(h,PQ(1),PQ(2));
H1 = ifftshift(H);%ifftshift用于重排数据，以便使得原点位于频率域矩阵的左上角
figure;
subplot(2,3,1);imshow(cover,[]);title('源图像');
subplot(2,3,4);imshow(S,[]);title('傅里叶频谱');
subplot(2,3,2);imshow(abs(H),[]);title('Sobel滤波器频率域绝对值');
subplot(2,3,5);mesh(abs(H));title('Sobel滤波器频率域绝对值(三维视图)');
subplot(2,3,3);imshow(abs(H1),[]);title('ifftshift后的频率域Sobel滤波器');
subplot(2,3,6);mesh(abs(H1));title('ifftshift后的频率域Sobel滤波器(三维视图)');
```

从空间滤波器获取频率域滤波器

图像转化为浮点数函数：

```matlab
function [out, revertclass] = tofloat(in)
%将一幅图像转化为浮点数（floating point）
identity = @(x) x;
tosingle = @im2single;

table = {'uint8',  tosingle, @im2uint8
         'uint16', tosingle, @im2uint16
         'int16', tosingle, @im2int16
         'logical', tosingle, @logical
         'double', identity, identity
         'singel', identity, identity};
     
classIndex = find(strcmp(class(in), table(:,1)));
if isempty(classIndex)
    error('Unsupported input image class');
end

out = table{classIndex, 2}(in);
revertclass = table{classIndex, 3};
end
```

频率域滤波的函数：

```matlab
function g = dftfilt(f, H, classout)
%用于频率域滤波的函数

% Convert the input to floating point.
[f, revertClass] = tofloat(f);

% Obtain the FFT of the padded input.
F = fft2(f, size(H,1), size(H,2));

% Perform filtering.
g = ifft2(H.*F);

% Crop to original size.
g = g(1:size(f,1),1:size(f,2)); % g is of class single here.

% Convert the output to the same class as the input if so specified.
if nargin == 2 || strcmp(classout, 'original')
    g = revertClass(g);
elseif strcmp(classout, 'fltpoint')
    return
else
    error('Undefined class for the output image.')
end
end
```

获得填充大小的函数:

```matlab
function PQ = paddedsize(AB, CD, PARAM)
%使用基于FFT滤波器时的填充大小计算
if nargin == 1
    PQ = 2 * AB;
elseif nargin == 2 && ~ischar(CD)
    PQ = AB + CD -1;
    PQ = 2 * ceil(PQ / 2);
elseif nargin == 2
    m = max(AB); %Maximun dimension
    
    %Find power-of-2 at least twice m.
    P = 2^nextpow2(2*m);
    PQ = [P,P];
elseif (nargin == 3) && strcmpi(PARAM,'pwr2')
    m = max([AB CD]);%Maximum dimension.
    P = 2^nextpow2(2*m);
    PQ = [P,P];
else
    error('Wrong number of inputs.')
end
end
```

对比空域滤波和频率域滤波的效果：

```matlab
clear all;
cover = double(imread('1.pgm'));%读入图像
F = fft2(cover);%对图像进行DFT变换
S = fftshift(log(1+abs(F))); %得到傅里叶频谱
h = [-1 -1 -1; -1 8 -1; -1 -1 -1];%给定空间域滤波器，也可以通过h = fspecial('sobel')'获取
PQ = paddedsize(size(cover));
H = freqz2(h,PQ(1),PQ(2));
H1 = ifftshift(H);%ifftshift用于重排数据，以便使得原点位于频率域矩阵的左上角

gs = imfilter(cover,h);%空间域滤波，默认情况下使用0
```