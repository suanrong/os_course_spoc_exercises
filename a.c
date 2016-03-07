#include "stdio.h"
#include "assert.h"
const int LENGTH = 10000;
const int inf = 123456789;
typedef struct {
	int start;
	int length;
}Mem;
typedef struct {
	int num_used;
	int num_free;
	Mem used[10000];
	Mem free[10000];
}Mem_list;
Mem_list mylist;
void init()
{
	mylist.num_free = 1;
	mylist.free[0].start = 0;
	mylist.free[0].length = LENGTH;
	mylist.num_used = 0;
}
int my_malloc(int size_request)
{
	if (size_request==0) return -1;
	int i;
	int ret = -1;
	int size_find = inf;
	for(i=0;i<mylist.num_free;++i)
		if (mylist.free[i].length>=size_request && mylist.free[i].length<size_find)
		{
			size_find=mylist.free[i].length;
			ret = i;
		}
	if (ret!=-1)
	{
		i = mylist.num_used++;
		mylist.used[i].start = mylist.free[ret].start;
		mylist.used[i].length = size_request;
		mylist.free[ret].length -= size_request;
		mylist.free[ret].start += size_request;
		if (mylist.free[ret].length==0)
		{
			i = (--mylist.num_free);
			mylist.free[ret].start = mylist.free[i].start;
			mylist.free[ret].length = mylist.free[i].length;
		}
	}
	return ret;
}
void get_free(int start,int length)
{
	int i,j;
	for (i=0;i<mylist.num_free;++i)
		if(mylist.free[i].start == start + length)
		{
			length += mylist.free[i].length;
			j = --mylist.num_free;
			mylist.free[i].start = mylist.free[j].start;
			mylist.free[i].length = mylist.free[j].length;
			--i;
		}
		else if(mylist.free[i].start + mylist.free[i].length == start)
		{
			start += mylist.free[i].start;
			j = --mylist.num_free;
			mylist.free[i].start = mylist.free[j].start;
			mylist.free[i].length = mylist.free[j].length;
			--i;
		}
	i = mylist.num_free++;
	mylist.free[i].start = start;
	mylist.free[i].length = length;
}
int my_free(int start)
{
	int ret = -1;
	int i;
	for(i=0;i<mylist.num_used;++i)
		if (mylist.used[i].start == start)
		{
			ret = i;
			break;
		}
	if(ret!=-1)
	{
		get_free(mylist.used[ret].start,mylist.used[ret].length);
		i = (--mylist.num_used);
		mylist.used[ret].start = mylist.used[i].start;
		mylist.used[ret].length = mylist.used[i].length;
	}
}
void my_print()
{
	int i=0;
	printf("free:");
	for(i=0;i<mylist.num_free;++i)
	{
		printf("\ts_%d\tL_%d\n",mylist.free[i].start,mylist.free[i].length);
	}
	printf("used:");
	for(i=0;i<mylist.num_used;++i)
	{
		printf("\ts_%d\tL_%d\n",mylist.used[i].start,mylist.used[i].length);
	}
}
int main()
{
	init();
	int a = my_malloc(120);
	my_malloc(480);
	my_malloc(240);
	my_malloc(960);
	my_malloc(240);
	my_free(120);
	my_free(840);
	my_malloc(950);
	my_malloc(5);
	my_print();
	return 0;
}