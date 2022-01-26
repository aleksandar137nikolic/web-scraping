


def store_data(item_list,file_name, delimiter = ';'):
    # Storing 
    wd = '/Users/anikolic/Documents/Data/Web Scraping/'
    file_path = wd + file_name

    file = open(file_path, 'w')

    # Process products and store them as csv. 
    d = delimiter
    # create table headers
    headers = ''
    for i in item_list[0].keys():
        if headers == '':
                headers = headers + str(i)
        else:
                headers = headers + d + str(i)
        print(i)
    headers = headers + '\n'
    file.write(headers)
    print(headers)
    for item in item_list:
        print('product name: ',item['first_name'])
    # create an entry
        entry = ''
        for key in item.keys():
            if entry == '':
                entry = entry + str(item[key])
            else:
                entry = entry + d + str(item[key])
        print(entry)
        entry = entry + '\n'
        file.write(entry)

    file.close()