#include <iostream>
#include <mutex> //for cout_sync
#include "Buffer.hh"

//For sleep durations in a C++11 manner
#include <chrono>
#include <thread>
#include <random>

//Mersenne Twister RNG
static std::mt19937 rng;

static Buffer buffs[2];

static std::mutex cout_sync;

void producer(int id)
{
    while (true)
    {
        int sleep_for = rng() % 500;
        std::this_thread::sleep_for(std::chrono::milliseconds(sleep_for));

        int item = rng() % 100;
        int i = rng() % 2;
        buffs[i].insertItem(item);

        cout_sync.lock();
        std::cout << "Producer " << id << " inserted " << item << " to buffer " << i << std::endl;
        cout_sync.unlock();
    }
}
void consumer(int id)
{
    while (true)
    {
        int sleep_for = rng() % 500;
        std::this_thread::sleep_for(std::chrono::milliseconds(sleep_for));

        int i = rng() % 2;
        int item = buffs[i].removeItem();

        cout_sync.lock();
        std::cout << "Consumer " << id << " consumed " << item << " from buffer " << i << std::endl;
        cout_sync.unlock();
    }
}

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        std::cout << "Usage: prodCons runningTime nProducers nConsumers" << std::endl;
        return 1;
    }

    int runTime = atoi(argv[1]);
    int nProducers = atoi(argv[2]);
    int nConsumers = atoi(argv[3]);

    for (int i = 1; i <= nProducers; i++)
    {
        std::thread t(producer, i);
        t.detach();
    }

    for (int i = 1; i <= nConsumers; i++)
    {
        std::thread t(consumer, i);
        t.detach();
    }

    std::this_thread::sleep_for(std::chrono::seconds(runTime));
}