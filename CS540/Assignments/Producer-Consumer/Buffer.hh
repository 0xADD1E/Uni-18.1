/* Producer-Consumer Project
 * Addie Morrison
 * Q688R999
 * akmorrison@shockers.wichita.edu
 * 0xADD1E@gmail.com
 */
#include <vector>
#include <mutex>
#include <semaphore.h>
#include <iostream>

#define SIZE 5
class Buffer{
    std::vector<int> store;
    std::mutex bufferAccess;
    sem_t empty, full;
public:
  Buffer();
  ~Buffer();
  void insertItem(int);
  int removeItem();
};