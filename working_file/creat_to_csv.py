import csv


def creat_avito_csv():
    with open(f'Avito.csv', 'w', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "Data, Time of adding to the board",
                "Name",
                "Price",
                "Image",
                "About",
                "Rules",
                "Address",
                "Description",
                "About the house",
                "Data, Time of addition to the database, table",
                "Link"
            ]
        )
    print("\nCreat Avit.csv")
