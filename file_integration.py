import csv

# print(csv.list_dialects())


class CsvWriter():
    ''' Singleton CSV Handler '''

    def save(data, header=None, file_name=None):

        # my data rows as dictionary objects
        mydict = [{header: data}]

        # field names
        fields = [header]

        # writing to csv file
        with open(file_name, 'w', newline='') as csvfile:

            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            writer.writeheader()

            # writing data rows
            writer.writerows(mydict)


if __name__ == '__main__':
     
     serial_number = '240711BM070001'
     CsvWriter.save(serial_number)