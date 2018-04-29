#include <string>
#include <ostream>
#include "Category.hh"
class RentalItem
{
public:
  std::string Name;
  Category Type;

  RentalItem(std::string, Category);
  int PricePerNight() const;

  friend std::ostream &operator<<(std::ostream &, const RentalItem &);
};