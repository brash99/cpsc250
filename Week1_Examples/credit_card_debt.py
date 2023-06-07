import csv
def read_customer_data(filename):
    """Read and return data from filename as a list of lists (name, state, debt)"""
    names_list = []
    states_list = []
    debts_list = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            names_list.append(row[0])
            states_list.append(row[1])
            debts_list.append(float(row[2]))
    return names_list, states_list, debts_list


# Main portion of the program
if __name__ == '__main__':

    # Step 1:  Get the data from CSV file
    names, states, debts = read_customer_data("CustomerData.csv")

    # Step 2: Input debt limit, search phrase, and state
    debt_limit = float(input('Enter the debt limit: '))
    search_phrase = input('Enter the last name phrase: ')
    st = input('Enter the state to search for: ')

    # Step 3: Find highest debt among customers
    print("U.S. Credit Card Debt Report - E.J. Brash - 6/7/2023")

    index_max = 0
    for n in range(1,len(names)):
        if debts[n] > debts[index_max]:
            index_max = n
    print(f"Highest debt: {names[index_max]} with debt = {debts[index_max]}")
    print()

    # Step 4: Find number of customers with name starting with specified phrase
    count = 0
    for n in range(len(names)):
        if names[n].startswith(search_phrase):
            count += 1
    print(f'Customer names that start with "{search_phrase}": {count}')
    print()

    # Step 5: Find customers with no debt and number with debt above specified amount
    count = 0
    no_debt = 0
    for n in range(len(names)):
        if debts[n] == 0:
            no_debt += 1
        elif debts[n] > debt_limit:
            count += 1

    print(f"Customers with debt over ${debt_limit}: {count}")
    print(f"Customers debt free: {no_debt}")
    print()

    # Step 6: State Report: count and highest debt of customers in the requested state
    count = 0
    highest_debt_index = 0
    for n in range(len(names)):
        if states[n] == st:
            count += 1
            if count == 1:
                highest_debt_index = n
            if debts[n] > debts[highest_debt_index]:
                highest_debt_index = n
    print(f"\n{st} Report")
    print(f"Customers: {count}")
    print(f"Highest debt: {names[highest_debt_index]}")
    print()

    # Step 7: Find customers with name starting with specified phrase for requested state
    count = 0
    for n in range(len(names)):
        if states[n] == st and names[n].startswith(search_phrase):
            count += 1
    print(f'Customer names that start with "{search_phrase}": {count}')
    print()

    # Step 8: Find customers with no debt and number with debt above specified amount for requested state
    count = 0
    no_debt = 0
    for n in range(len(names)):
        if states[n] == st:
            if debts[n] == 0:
                no_debt += 1
            elif debts[n] > debt_limit:
                count += 1
    print(f"Customers with debt over ${debt_limit}: {count}")
    print(f"Customers debt free: {no_debt}")
