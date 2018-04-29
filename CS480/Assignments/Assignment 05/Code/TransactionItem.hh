#include <ostream>
#include "RentalItem.hh"
class TransactionItem
{
public:
  RentalItem Item;
  int Nights;

  int TotalCost() const;
  int RewardPoints() const;
  TransactionItem(RentalItem, int);
  friend std::ostream &operator<<(std::ostream &, const TransactionItem &);
};