->Threads are a way for a program to split itself into two or more simultaneously (or pseudo- simultaneously) running tasks.
  Threads and processes differ from one operating system to another, but in general, the way that a thread is created and
  shares its resources is different from the way a process does.



  #Thread in Operating System

'What is a Thread?'
A thread is a path of execution within a process. A process can contain multiple threads.

'Why Multithreading?'
A thread is also known as lightweight process.
The idea is to achieve parallelism by dividing a process into multiple threads.
For example, in a browser, multiple tabs can be different threads.
MS Word uses multiple threads: one thread to format the text, another thread to process inputs, etc.
More advantages of multithreading are discussed below

'Process vs Thread?'
->The primary difference is that threads within the same process run in a shared memory space,
  while processes run in separate memory spaces.


Threads are not independent of one another like processes are, and as a result threads share with other threads their code section,
data section, and OS resources (like open files and signals). But, like process, a thread has its own program counter (PC),
register set, and stack space.

'Advantages of Thread over Process'

1. 'Responsiveness':  If the process is divided into multiple threads,
                    if one thread completes its execution, then its output can be immediately returned.

2. 'Faster context switch': Context switch time between threads is lower compared to process context switch.
                            Process context switching requires more overhead from the CPU.

3. 'Effective utilization of multiprocessor system': If we have multiple threads in a single process, then we can schedule
                                                     multiple threads on multiple processor. This will make process execution faster.
