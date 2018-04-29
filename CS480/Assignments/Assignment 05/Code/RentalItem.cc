#include "RentalItem.hh"
RentalItem::RentalItem(std::string name, Category type)
{
    Name = name;
    Type = type;
}
int RentalItem::PricePerNight() const
{
    switch (Type)
    {
    case Category::Regular:
        return 100;
    case Category::Childrens:
        return 75;
    case Category::NewRelease:
        return 150;
    }
}
std::ostream &operator<<(std::ostream &stream, const RentalItem &self)
{
    int ppn = self.PricePerNight();
    int dollars = ppn / 100;
    int cents = ppn % 100;
    std::string type;
    switch (self.Type)
    {
    case Category::Regular:
        type = "Regular";
        break;
    case Category::Childrens:
        type = "Childrens";
        break;
    case Category::NewRelease:
        type = "New Release";
    }
    stream << self.Name << " (" << type << "): $" << dollars << "." << cents << "/day";
    return stream;
}