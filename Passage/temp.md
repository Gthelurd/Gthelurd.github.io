## C语言中的排序
#### "stdlib.h"中自带的qsort
qsort函数定义如下
```c
void qsort(void *base, // nums
           size_t nitems, // sizeof(nums)/sizeof(nums[0])
           size_t size,   // sizeof(nums[0])
           int (*compar)(const void *, const void *));
```
如果你要使用他，那么你大概需要自己写一个cmp函数，输出应该为-1,0,1来告知qsort怎么排序。(1:升序,-1:降序)
```c
int cmp_int(const void*_a,const void*_b)
{
    return *(int*)_a - *(int*)_b;
}
int cmp_char(const void*_a,const void*_b)
{
   return *(char*)_a - *(char*)_b;
}
int cmp_dob(const void*_a,const void*_b)
{
    return *(double*)_a > *(double*)_b ? 1 : -1;
}
// 或者一劳永逸版本
struct node{
	int i;
	double d;
	char c;
};
int cmp(const void *a,const void *b) {
	return (*(node*)a).i-(*(node*)b).i;
}

```
具体实例：
```c
// nums:[1,1,1,3,3,4,3,2,4,2]->[1,1,1,2,2,3,3,3,4,4]
qsort(nums,NumSizes,sizeof(int),cmp_int);
```
#### C语言中实现swap()函数
C是没有自己的swap函数的，只能靠自己实现。
```c
void swap(int *a,int *b)
{
    a ^= b ^= a ^= b; //仅限int型
}

void swap1(int &a,int &b)
{
    a = a + b;
    b = a - b;
    a = a - b;
}

void swap2(int &a,int &b) //创建临时变量，较为常用
{
    int tmp = b;
    b = a;
    a = tmp;
}
```

#### 冒泡
常见的算法，小元素上浮，大元素下沉，当一次排序中没有交换时说明数组已经排序完全。
```c
void bubble_sort(int *nums,int numsSize)
{
    for(int i=0;i<numsSize;i++)
    {
        for(int j=numsSize-1;j>i;j--)
        {
            if(nums[j-1]>nums[j])
            {
                swap(nums[j-1],nums[j]);
            }
        }
    }
}
```
#### 插入
逐个处理待排序的记录，每个记录与前面已排序已排序的子序列进行比较，将它插入子序列中正确位置。
```c
void insert_sort(int *nums,int numsSize)
{
    for(int i=0;i<numsSize;i++)
    {
        for(int j=i;j>1;j--)
        {
            if(nums[j-1]>nums[j])
            {
                swap(nums[j-1],nums[j]);
            }
        }
    }
}
```
#### 选择
次从未排序的序列中找到最小元素，放到未排序数组的最前面。
```c
void select_sort(int *nums,int numsSize)
{
    for(int i=0;i<numsSize;i++)
    {
        for(int j=i+1;j<numsSize>;j++)
        {
            if(nums[i]>nums[j])
            {
                swap(nums[i],nums[j]);
            }
        }
    }
}
```

#### 快排
这个推荐直接使用qsort，$O(n\log{n})$复杂度都不用自己手搓。

#### 归并
```cpp
template<class Elem>
void mergesortcore(Elem A[],Elem temp[],int i,int j)
{
    if(i == j)  return;
    int mid = (i + j)/2;

    mergesortcore(A,temp,i,mid);
    mergesortcore(A,temp,mid + 1,j);

    /*归并*/
    int i1 = i,i2 = mid + 1,curr = i;
    while(i1 <= mid && i2 <= j){
        if(A[i1] < A[i2])
            temp[curr++] = A[i1++];
        else
            temp[curr++] = A[i2++];
    }
    while(i1 <= mid)
        temp[curr++] = A[i1++];
    while(i2 <= j)
        temp[curr++] = A[i2++];
    for(curr = i;curr <= j;curr++)
        A[curr] = temp[curr];
}

template<class Elem>
void mergesort(Elem A[],int sz)
{
    Elem *temp = new Elem[sz]();
    int i = 0,j = sz - 1;
    mergesortcore(A,temp,i,j);
    delete [] temp;
}
```


#### 堆
```cpp
/********************************************
 * 向堆中插入元素
 *  hole：新元素所在的位置
 ********************************************/
template <class value>
void _push_heap(vector<value> &arr,int hole){
    value v = arr[hole];//取出新元素，从而产生一个空洞
    int parent = (hole - 1) / 2;
    //建最大堆，如果建最小堆换成 arr[parent] > value
    while(hole > 0 && arr[parent] < v){
        arr[hole] = arr[parent];
        hole = parent;
        parent = (hole - 1) / 2;
    }
    arr[hole] = v;
}

/********************************************
 * 删除堆顶元素
 ********************************************/
template <class value>
void _pop_heap(vector<value> &arr,int sz)
{
    value v = arr[sz - 1];
    arr[sz - 1] = arr[0];
    --sz;
    int hole = 0;
    int child = 2 * (hole + 1); //右孩子
    while(child < sz){
        if(arr[child] < arr[child - 1])
            --child;
        arr[hole] = arr[child];
        hole = child;
        child = 2 * (hole + 1);
    }
    if(child == sz){
        arr[hole] = arr[child - 1];
        hole = child - 1;
    }
    arr[hole] = v;
    _push_heap(arr,hole);
}

/********************************************
 * 建堆
 *  sz：删除堆顶元素后的大小
 *  v： 被堆顶元素占据的位置原来的元素的值
 ********************************************/
template <class value>
void _make_heap(vector<value> &arr)
{
    int sz = arr.size();
    int parent = (sz - 2) / 2;
    while(parent >= 0){
        int hole = parent;
        int child = 2 * (hole + 1); //右孩子
        value v = arr[hole];
        while(child < sz){
            if(arr[child] < arr[child - 1])
                --child;
            arr[hole] = arr[child];
            hole = child;
            child = 2 * (hole + 1);
        }
        if(child == sz){
            arr[hole] = arr[child - 1];
            hole = child - 1;
        }
        arr[hole] = v;
        _push_heap(arr,hole);
        --parent;
    }
}

template <class value>
void heap_sort(vector<value> &arr)
{
    _make_heap(arr);
    for(int sz = arr.size();sz > 1;sz--)
        _pop_heap(arr,sz);
}
```