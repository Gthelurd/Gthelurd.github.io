# C语言中的数组

### 定义与性质

> 「数组是存放在连续内存空间上的相同类型数据的集合。」

性质有二:
-    「数组下表都是从0开始的。」
-    「数组内存空间的地址是连续的」
所以在增加或者删除的时候总避免不了移动改变量附近的下标。

### 声明
数组可以声明成多种类型，但是要注意长度以及初始化。
```c
//type arrayName [ arraySize ];
double float_array[] = {1000.0, 2.0, 3.4, 7.0, 50.0};
int int_array[3] = {1, 2, 3};
char ch_array[6] = {'H','E','L','L','O','\0'};
char str[]="Hello,world!";//结尾会自动添加'\0'
```
我们可以快速获取长度,使用下面的语句:
```c
//int length = sizeof(Array) / sizeof(Array[0]);
#define LENGTH(array) (sizeof(array) / sizeof(array[0]))
```
其实数组类型的$\text{Array}\text{[index]}$是一种语法糖:
```c
int array[] = {1, 2, 3, 4, 5, 6};
int *a =array; //*a指向array[0]，如果直接赋值*a，那么后面的丢失。
printf("%d,%d,%d",a[3],3[a],*(a+3));
//4,4,4
```
### 初始化

全部初始化为0：
```c
    int a[10]={0};
    char str[10]="\0";    //等价于char str[10]={0};
```

初始化为其他值：
```c
    int a[10]={0,1,2,3,4,5,6,7,8,9};
    char str[10]="Hello";    //也可以写成char str[10]={'H','e','l','l','o','\0'}
```

如果初始化列表包含数组a的所有元素，可以省略数组的长度：
```c
int a[]={0,1,2,3,4,5,6,7,8,9};
```

多维数组在计算机中也是线性存储的，因此下面两种写法等价：
```c
    int a[2][5]={{0,1,2,3,4},{5,6,7,8,9}};
    //int a[2][5]={0,1,2,3,4,5,6,7,8,9};
```
当然，你也可以使用memset来初始化，推荐用来初始化字符串数组，初始化整形数组一般为0或-1:
```c
void *memset(void *s, int c, unsigned long n);
//将s内存后的长度为n个字节的空间初始化为c
```
比如:
```c
    char str[10];
    memset(str,0,sizeof(str));
    int a[10];
    memset(a,-1,sizeof(a));
```

### 操作

数组的操作主要包括访问、修改、插入和删除元素。由于数组在内存中是连续存储的，因此在插入和删除元素时需要移动其他元素，这可能会导致性能开销。

#### 访问元素

访问数组元素非常简单，只需使用数组名和下标即可。

```c
int array[] = {1, 2, 3, 4, 5};
int value = array[2];  // value 现在是 3
```

#### 修改元素

修改数组元素同样简单，只需对指定下标的元素进行赋值。

```c
array[2] = 10;  // 现在 array 是 {1, 2, 10, 4, 5}
```

#### 插入元素

在数组中插入元素通常需要移动其他元素，以保持数组的连续性。假设我们要在数组的第 `i` 个位置插入一个元素 `x`，我们需要将 `i` 位置及其后面的所有元素向后移动一位。

```c
void insertElement(int array[], int *size, int element, int position) {
    // 确保数组有足够的空间
    if (position < 0 || position > *size) {
        printf("Invalid position\n");
        return;
    }

    // 移动元素
    for (int i = *size; i > position; i--) {
        array[i] = array[i - 1];
    }

    // 插入新元素
    array[position] = element;
    (*size)++;
}
```

#### 删除元素

删除数组中的元素也需要移动其他元素。假设我们要删除数组中第 `i` 个位置的元素，我们需要将 `i` 位置后面的所有元素向前移动一位。

```c
void deleteElement(int array[], int *size, int position) {
    // 确保位置有效
    if (position < 0 || position >= *size) {
        printf("Invalid position\n");
        return;
    }

    // 移动元素
    for (int i = position; i < *size - 1; i++) {
        array[i] = array[i + 1];
    }

    (*size)--;
}
```

### DP数组

动态规划（Dynamic Programming, DP）是一种通过将问题分解为子问题来解决复杂问题的方法。DP通常使用数组来存储子问题的解，以便在后续计算中重复使用这些解。

#### 示例：斐波那契数列

斐波那契数列是一个经典的DP问题。我们可以使用一个数组来存储每个斐波那契数，从而避免重复计算。

```c
#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) return n;

    int dp[n + 1];
    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}
```

### 矩阵

矩阵是二维数组的常见应用。矩阵操作包括矩阵加法、矩阵乘法、转置等。

#### 矩阵加法

矩阵加法要求两个矩阵的维度相同，对应位置的元素相加。

```c
void matrixAddition(int A[M][N], int B[M][N], int C[M][N], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}
```

#### 矩阵乘法

矩阵乘法要求第一个矩阵的列数等于第二个矩阵的行数。结果矩阵的维度为第一个矩阵的行数和第二个矩阵的列数。

```c
void matrixMultiplication(int A[M][N], int B[N][M], int C[M][M], int rowsA, int colsA, int colsB) {
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            C[i][j] = 0;
            for (int k = 0; k < colsA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}
```