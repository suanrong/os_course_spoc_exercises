#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<pthread.h>
using namespace std;
const int N=5;
enum state{
	IDLE,
	WAITING,
	ACTIVE
};
state flags[N];
pthread_t id[N];
int turn;
void* mythread(void* args)
{
	int id = *(int*)args;
	while(true)
	{
		flags[id]=WAITING;
		int index = turn;
		while(index!=id)
		{
			if(flags[index]!=IDLE) index = turn;
			else index = (index+1)%N;
		}
		flags[id] = ACTIVE;
		index = 0;
		while ( index < N && (index == id || flags[index] != ACTIVE) ) index++;
		if(index >= N  && (turn == id || flags[turn] == IDLE) ) break;
	}
	turn = pid;
	index = (turn + 1) % N;
	while (flags[index] == IDLE)
		index = (index + 1) % MAX_THREADS;
	turn = index;
	flags[pid] = IDLE;		
	return NULL;
}
int main()
{
	for(int i=0;i<N;++i)
		flags[i] = IDLE,id[i]=i;
	for(int i=0;i<N;++i)
		pthread_create(&id[i],NULL,mythread,(void*)&id[i]);
	for(int i=0;i<N;++i)
		pthread_join(id[i],NULL);
	return 0;
}
