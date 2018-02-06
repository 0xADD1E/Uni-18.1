# Chapter 3 & 4 Homework
## 2 - Address Space
A proc's address space consists of bytecode (.CODE), global variables (.DATA), stack, and heap
On X86, the stack grows upward, in that order {INSERT PICTURE HERE}
## 6 - Context switching
Context switching is the act of the CPU moving from executing one process to another. Context switches happen whenever a process moves from running to another state. Information about suspended processes is stored in the process control block / PCB
## 8 - Queues
The jobs queue contains processes that have been requested to run, but not initialized in any way. The ready queue contains processes that have been loaded from disk, and are ready to be executed. Device queues contain processes that are requesting IOs from that device. 

In practice these queues are fantastic works of engineering with all sorts of speculation and profiling magic to keep the system running smoothly. In this class, we're representing them as simple FIFO lists / queues
## 9 - Schedulers
The long term scheduler picks processes to be run (IE handling the jobs queue). It runs on a rather long period (several hundred milliseconds), and aims for a mix of IO and CPU bound tasks.

The short term scheduler runs on a very short period, and takes processes from the ready queue and allows them to execute.
## 10 - Degree of multiprogramming
The number of tasks that are being executed at a time -- controlled by the jobs queue / long term scheduler
## 13 - Child process modes
(assuming a linux-style process creation api)

Simply remove the `wait(2)` and continue about your business

```
...
    x = fork();
    if (x == 0)
        execve(command, parameters, 0);
}
```
## 14 - Process tree
## 19 - Thread resources
## 22 - 