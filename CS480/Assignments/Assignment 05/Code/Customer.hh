#include <string>
#include <vector>
#include "Transaction.hh"
class Customer
{
public:
  std::string Name;
  int RewardPoints;
  std::vector<Transaction> Transactions;

  void AddTransaction(Transaction);

  Customer(std::string);
  friend std::ostream &operator<<(std::ostream &, const Customer &);
};