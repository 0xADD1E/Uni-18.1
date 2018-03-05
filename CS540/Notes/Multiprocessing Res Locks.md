# Critical Section
Mutual exclusion: more than one proc should not be accessing critical section at the same time

## Solutions

```
//General proc structure
while(true){
    entry section
    critical section
    exit section
    rs
}
```
- Peterson's: Software based, only works for two procs
- HW Based: Test-and-set-lock (TSL), atomic insert's provided by hardware -- Typically limited to OS functionality, not apps
- Mutex: Software based, OS provided, available to apps. only one permission available. Uses `acquire()` and `release()` as entry and exit sections respectively

```
acquire(){ //this method must be executed atomically
    while(!available); //block until avail
    available = false
}  
release(){
    available = true; //give lock back
}
```
- Semaphores: Integer value, counts number of things using a resource at a time. `wait()` and `signal()` are entry and exit sections

```
wait(){
    while(s<=0);
    s--
}
signal(){
    s++
}
```
### Limitations
- Mutexes and semaphores: The scheduler needs to be aware of these, otherwise there's potential for considerable resource wasting (IE: proc with the lock uses up time share, scheduler switch to process that just busy-waits)
### A better solution
What if we could get a process that's trying for the lock to be placed in waiting until it's available...

Semaphore structure

```
struct semaphore {
    //Semaphore counter
    int value; 
    
    //Procs that were suspended while waiting on resource
    proc *lst;
}

wait(){
 value--;
 if(value<0){
     //add this to lst
     block();
 }
}

signal(){
    value++;
    if(value<=0){
        //wake up a process from lst
    }
}
```

## Deadlock
Process A is waiting for resource x, and is holding resource y

Process B is waiting for resource y, and is holding resource x