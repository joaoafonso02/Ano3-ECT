#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <errno.h>
#include <stdint.h>

#include "fifo.h"
#include "delays.h"
#include "thread.h"
#include "dbc.h"

void *myThreadFunc(void *arg) {
    for(int i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
    return NULL;
}

int main(){
    pthread_t thread_id;
    printf("Before thread");
    thread_create(&thread_id, NULL, myThreadFunc, NULL);
    thread_join(thread_id, NULL);
    printf("After thread");
    exit(0);
}

