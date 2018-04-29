#include "Customer.hh"
Customer::Customer(std::string name) : Name(name){};

void Customer::AddTransaction(Transaction t)
{
    Transactions.push_back(t);
    RewardPoints += t.TotalPoints();
}

std::ostream &operator<<(std::ostream &stream, const Customer &self)
{
    stream << self.Name << ": " << self.RewardPoints << " points" << std::endl;
    int runningTotal = 0;
    for (auto i : self.Transactions)
    {
        runningTotal += i.TotalCost();
        stream << i;
    }
    int dollars = runningTotal / 100;
    int cents = runningTotal % 100;
    stream << "--------------------" << std::endl
           << "Total spent for customer: $" << dollars << "." << cents;
    return stream;
}