CXX = g++
CXXFLAGS = -std=c++11 -Wno-c++11-extensions -g3

.PHONY: run
all: bin
bin: main transaction rentalitem category customer
	$(CXX) $(CXXFLAGS) -o rental.bin main.o transaction.o rentalitem.o
main: Main.cc
	$(CXX) $(CXXFLAGS) -c -o main.o -c Main.cc
transaction: Transaction.cc Transaction.hh
	$(CXX) $(CXXFLAGS) -c -o transaction.o Transaction.cc
rentalitem: RentalItem.cc RentalItem.hh
	$(CXX) $(CXXFLAGS) -c -o rentalitem.o RentalItem.cc
category: Category.hh
customer: Customer.hh
run: bin
	./rental.bin
clean:
	rm -f $(wildcard *.o)
	rm -f rental.bin