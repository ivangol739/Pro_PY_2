import csv
import re


def new_contacts(contacts_list):

    pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    sub = r'+7(\2)-\3-\4-\5 \6\7'
    new_contacts_list = []
    for row in contacts_list:
        contact = f'{row[0].strip()} {row[1].strip()} {row[2].strip()}'.split()
        while len(contact) < 3:
            contact.extend([''])
        row[5] = re.sub(pattern, sub, row[5])
        contact.extend(row[3:])
        new_contacts_list.append(contact)

    for row in new_contacts_list:
        for i in new_contacts_list:
            if row != i and row[0] == i[0] and row[1] == i[1]:
                row[2] = i[2] if i[2] else row[2]
                row[3] = i[3] if i[3] else row[3]
                row[4] = i[4] if i[4] else row[4]
                row[5] = i[5] if i[5] else row[5]
                row[6] = i[6] if i[6] else row[6]
                new_contacts_list.remove(i)
    return new_contacts_list

if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts(contacts_list))