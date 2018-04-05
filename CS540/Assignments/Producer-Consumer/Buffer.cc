#include "Buffer.hh"

Buffer::Buffer()
{
    /* Story Time: Apple MacOS
     * Once upon a time, there was a poor developer that worked on a Macbook.
     * She tired over her code, for the better part of two ******* hours, before
     * realizing that pthreads semaphores on MacOS are basically just stubs!
     * 
     * This prevents you from even trying to debug the issue. Such efforts
     * will only end in pain and suffering.
     * **** you Apple
     * 
     * With Love,
     * Addie
     */
    int i = 0;
    do{
        sem_init(&empty, 0, SIZE);
        sem_getvalue(&empty, &i);
    } while(!i);

    do {
        sem_init(&full, 0, 0);
        sem_getvalue(&full, &i);
    } while(i);
}
void Buffer::insertItem(int item){
    sem_wait(&empty);
    bufferAccess.lock();

    store.push_back(item);

    bufferAccess.unlock();
    sem_post(&full);
}
int Buffer::removeItem(){
    sem_wait(&full);
    bufferAccess.lock();

    int toReturn = store.back();
    store.pop_back();

    bufferAccess.unlock();
    sem_post(&empty);

    return toReturn;
}
Buffer::~Buffer(){
    sem_destroy(&empty);
    sem_destroy(&full);
}