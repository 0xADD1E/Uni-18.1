#include <string>
#include <vector>
#include "TransactionItem.hh"
class Transaction
{
public:
  std::vector<TransactionItem> Items;

  void AddItem(TransactionItem);
  int TotalCost() const;
  int TotalPoints() const;

  friend std::ostream &operator<<(std::ostream &, const Transaction &);
};