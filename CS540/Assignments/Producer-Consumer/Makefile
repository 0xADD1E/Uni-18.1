CXX = g++
CXXFLAGS = -std=c++11 -Wno-c++11-extensions -g3

all: bin
bin: main buffer
	$(CXX) $(CXXFLAGS) -lpthread -o prodCons main.o buffer.o
main: main.cc
	$(CXX) $(CXXFLAGS) -o main.o -c main.cc
buffer: Buffer.cc Buffer.hh
	$(CXX) $(CXXFLAGS) -o buffer.o -c Buffer.cc
run: bin
	./prodCons 6 2 3
clean:
	rm -f $(wildcard *.o)
	rm -f prodCons
transfer:
	scp $(wildcard *.hpp) $(wildcard *.hh) kira:~/tmp/
	scp $(wildcard *.cpp) $(wildcard *.cc) kira:~/tmp/
	scp Makefile kira:~/tmp/
handin: all clean transfer
		# Set of tasks for handing things in automagically
		ssh kira "cd ~/tmp/ &&\
			make all &&\
			make clean &&\
			~cs540/bin/handin -y 1 * &&\
			rm -f * ;\
			true"
