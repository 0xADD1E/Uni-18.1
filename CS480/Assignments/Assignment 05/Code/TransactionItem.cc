#include "TransactionItem.hh"

TransactionItem::TransactionItem(RentalItem item, int nights) : Item(item), Nights(nights){};

int TransactionItem::TotalCost() const
{
    return Item.PricePerNight() * Nights;
}
int TransactionItem::RewardPoints() const
{
    if (Item.Type == Category::NewRelease)
    {
        return 20;
    }
    return 10;
}

std::ostream &operator<<(std::ostream &stream, const TransactionItem &self)
{
    int total = self.Item.PricePerNight() * self.Nights;
    int dollars = total / 100;
    int cents = total % 100;
    stream << self.Item << " x " << self.Nights << " = $" << dollars << "." << cents;
    return stream;
}