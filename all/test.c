#include <cstdio>
#include <algorithm>
using namespace std;

int num;
struct Mem{
    int start;
    int size;
    int next;
    int prev;
    bool free;
}memory[10000];


void split(int index, int size){
    memory[index].free = 0;
    if (size == memory[index].size) return;
    memory[num].start = memory[index].start + size;
    memory[num].size = memory[index].size - size;
    memory[num].free = 1;
    memory[index].size = size;
    
    
    memory[num].next = memory[index].next;
    memory[index].next = num;
    num++;
}

void merge(int index){
    int cur = index;
    while(memory[cur].next && memory[memory[cur].next].free){
        cur = memory[cur].next;
        memory[index].size += memory[cur].size;
    }
    memory[index].next = memory[cur].next;
}

int myMalloc(int size){
    int ans = -1;
    for(int k = 1; k; k = memory[k].next){
        if (memory[k].free) merge(k);
        if (memory[k].free && memory[k].size >= size && 
            (ans == -1 || memory[k].size >= memory[ans].size)){
            ans = k;
        }
    }
    split(ans, size);
    return memory[ans].start;
}



void myFree(int start){
    for(int k = 1; k; k = memory[k].next){
        if (memory[k].start == start){
            memory[k].free = 1;
            break;
        }
    }
}

int main(){
    //init;
    num = 1;
    memory[num].start = 0;
    memory[num].free = 1;
    memory[num++].size = 10000;
    
    
    int a = myMalloc(10);
    printf("malloc 10 : %d\n", a);
    int b = myMalloc(20);
    printf("malloc 20 : %d\n", b);
    int c = myMalloc(30);
    printf("malloc 30 : %d\n", c);
    myFree(a);
    myFree(b);
    int d = myMalloc(30);
    printf("malloc 30 : %d\n", d);
    
}