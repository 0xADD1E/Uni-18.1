#include "Transaction.hh"
void Transaction::AddItem(TransactionItem i)
{
    Items.push_back(i);
}
int Transaction::TotalCost() const
{
    int total = 0;
    for (auto i : Items)
    {
        total += i.TotalCost();
    }
    return total;
}
int Transaction::TotalPoints() const
{
    int total = 0;
    for (auto i : Items)
    {
        total += i.RewardPoints();
    }
    return total;
}
std::ostream &operator<<(std::ostream &stream, const Transaction &self)
{
    stream << "START OF TRANSACTION" << std::endl;
    for (auto i : self.Items)
    {
        stream << i << std::endl;
    }
    int dollars = self.TotalCost() / 100;
    int cents = self.TotalCost() % 100;
    stream << "==================" << std::endl
           << "Total spent for transaction: $" << dollars << "." << cents << std::endl
           << "END OF TRANSACTION " << std::endl;
    return stream;
}