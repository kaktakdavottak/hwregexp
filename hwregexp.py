from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_pattern = "(\+7|8)(\s?)(\(?)([0-9]{3})(\)?)(\s?)(\-?)([0-9]{3})" \
                "(\-?)([0-9]{2})(\-?)([0-9]{2})(\s?)(\(?)([а-яё]*)(\.?)" \
                "(\s?)([0-9]*)(\)?)"
lfs_names_pattern = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"
lfs_names_pattern2 = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"

for contact in contacts_list:
    new_phone = re.sub(phone_pattern, r"+7(\4)\8-\10-\12\13\15\16\18",
                       contact[5])
    contact[5] = new_phone

    if re.match(lfs_names_pattern, contact[0]):
        result = re.match(lfs_names_pattern, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)
        contact[2] = result.group(5)

    if re.match(lfs_names_pattern2, contact[0]):
        result = re.match(lfs_names_pattern2, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)

    if re.match(lfs_names_pattern2, contact[1]):
        result = re.match(lfs_names_pattern2, contact[1])
        contact[1] = result.group(1)
        contact[2] = result.group(3)

with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)


