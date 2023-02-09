import csv


def save_data_avito_file(time, name, price, image, about, rules, address, description, home, data, _link):
    with open('Avito.csv', 'a', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                time,
                name,
                price,
                image,
                about,
                rules,
                address,
                description,
                home,
                data,
                _link
            ]
        )
