#include <iostream>
#include "Customer.hh"

std::vector<Customer> customers;
std::vector<RentalItem> catalog;

Customer *GetCustomer(std::string name)
{
    return &std::find_if(customers.begin(), customers.end(),
                         [name](const Customer &o) -> bool { return o.Name == name; })[0];
}
RentalItem *GetItem(std::string name)
{
    return &std::find_if(catalog.begin(), catalog.end(),
                         [name](const RentalItem &o) -> bool { return o.Name == name; })[0];
}
std::string PromptAndGetValue(std::string prompt)
{
    std::cout << prompt;
    std::string val;
    std::getline(std::cin, val);
    return val;
}
int main()
{
    //TODO: Load from files if avail?
    while (true)
    {
        std::cout << "Select a number for an action" << std::endl
                  << "1: Add a customer" << std::endl
                  << "2: Add a transaction to a customer" << std::endl
                  << "3: Print a customer's summary" << std::endl
                  << "4: Add an item to the catalog" << std::endl
                  << "5: Print the current catalog" << std::endl;
        int sel = atoi(PromptAndGetValue("Choice: ").c_str());
        switch (sel)
        {
        case 1:
        {
            auto name = PromptAndGetValue("New Customer's Name: ");
            customers.push_back(Customer(name));
        }
        break;
        case 2:
        {
            auto name = PromptAndGetValue("Customer's Name: ");
            auto cust = GetCustomer(name);

            Transaction transaction;
            std::cout << "Enter Items (blank name to end)" << std::endl;
            auto itemName = PromptAndGetValue("Item Name: ");
            while (itemName.find_first_not_of(' ') != std::string::npos)
            {
                auto item = GetItem(itemName);
                auto nights = atoi(PromptAndGetValue("Number of nights: ").c_str());
                transaction.AddItem(TransactionItem(*item, nights));

                itemName = PromptAndGetValue("Item Name: ");
            }
            cust->AddTransaction(transaction);
        }
        break;
        case 3:
        {
            auto customer = GetCustomer(PromptAndGetValue("Customer's Name: "));
            std::cout << *customer << std::endl;
        }
        break;
        case 4:
        {
            auto name = PromptAndGetValue("Item Name: ");
            auto categoryCandidate = PromptAndGetValue("Item Category (Regular, NewRelease, Childrens): ");
            std::transform(categoryCandidate.begin(), categoryCandidate.end(), categoryCandidate.begin(), ::tolower);
            auto category = Category::Regular;
            if (categoryCandidate == "new release" || categoryCandidate == "newrelease")
            {
                category = Category::NewRelease;
            }
            if (categoryCandidate == "childrens")
            {
                category = Category::Childrens;
            }
            catalog.push_back(RentalItem(name, category));
        }
        break;
        case 5:
        {
            for (auto i : catalog)
            {
                std::cout << i << std::endl;
            }
        }
        break;
        default:
            std::cout << "Invalid" << std::endl;
            break;
        }
    }
}