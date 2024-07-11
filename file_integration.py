import csv

# print(csv.list_dialects())

# Name of csv file
FILENAME = 'C:\Data\scan\data.csv'
HEADERNAME = 'SerialNumber'


class CsvWriter():
    ''' Singleton CSV Handler '''

    def save(data):

        # my data rows as dictionary objects
        mydict = [{HEADERNAME: data}]

        # field names
        fields = [HEADERNAME]

        # writing to csv file
        with open(FILENAME, 'w', newline='') as csvfile:

            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            writer.writeheader()

            # writing data rows
            writer.writerows(mydict)


if __name__ == '__main__':
     
     serial_number = '240711BM070001'
     CsvWriter.save(serial_number)