def save_contact_names(file_name):
    contact_numbers = []
    with open(file_name, 'r') as file:
        for row in file:
            number = row.split(',')[1]
            contact_numbers.append(number)
    #contact_numbers.pop(0)
    return contact_numbers

print(save_contact_names('contatos.csv'))
