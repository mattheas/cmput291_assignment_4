import sqlite3
import csv
import random

# code used and modified from link below to read in UPC's from CSV file, starting at "with open..."
#https://realpython.com/python-csv/


def extract_data(list_countries, list_part_ids):

    # open file contaning part #'s and extract data into list
    with open('upc_corpus.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:

            if line_count == 0:
                # ignore first row because it is col name
                line_count += 1
                
            else:
                # add UPC to list if its value is not null
                if row[0] != "null":
                    line_count += 1
                    list_part_ids.append(row[0])
                
    print("length of list = {}".format(len(list_part_ids)))
    
    # remove duplicate part numbers because of primary key constraint
    list_part_ids = list(dict.fromkeys(list_part_ids))
    print("length of list with duplicates removed = {}".format(len(list_part_ids)))

    
    # now remove country name abbreviations from second file
    with open('data_csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:

            if line_count == 0:
                # ignore first row because it is col name
                line_count += 1
                
            else:
                # add country to list if its value is not null
                line_count += 1
                list_countries.append(row[1])

    print("length of list = {}".format(len(list_countries)))  

    return list_countries, list_part_ids

def populate_db(list_countries, list_part_ids):

    counter_100, counter_1k, counter_10k, counter_100k, counter_1M = 0, 0, 0, 0, 0

    # define INSERT query
    sql_select_query = """INSERT INTO Parts (partNumber, partPrice, needsPart, madeIn)
    VALUES(?,?,?,?);"""


    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    temp_part_num_list = list_part_ids.copy()

    x = 99

    # 0 to 99
    while x>=0:
        print(x)
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index = random.randint(0,(len(temp_part_num_list)-1))
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        # save random partNumber from list
        temp_partNumber = temp_part_num_list[rand_index]

        # remove selected partNumber from templist so its not selected againx
        temp_part_num_list.remove(temp_partNumber)

        try:
            c1.execute(sql_select_query, (int(temp_partNumber), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]) ))
            x-=1
        except:
            print("error")


    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    temp_part_num_list = list_part_ids.copy()

    x = 999

    # 0 to 999
    while x>=0:
        
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index = random.randint(0,(len(temp_part_num_list)-1))
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        # save random partNumber from list
        temp_partNumber = temp_part_num_list[rand_index]

        # remove selected partNumber from templist so its not selected againx
        temp_part_num_list.remove(temp_partNumber)

        try:
            c2.execute(sql_select_query, (int(temp_partNumber), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]) ))
            x-=1
        except:
            print("error")
        


    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    temp_part_num_list = list_part_ids.copy()

    x = 9999

    # 0 to 9999
    while x>=0:
        
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index = random.randint(0,(len(temp_part_num_list)-1))
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        # save random partNumber from list
        temp_partNumber = temp_part_num_list[rand_index]

        # remove selected partNumber from templist so its not selected againx
        temp_part_num_list.remove(temp_partNumber)

        try:
            c3.execute(sql_select_query, (int(temp_partNumber), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]) ))
            x-=1
        except:
            print("error")




    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    temp_part_num_list = list_part_ids.copy()

    x = 99999

    # 0 to 999
    while x>=0:
        
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index = random.randint(0,(len(temp_part_num_list)-1))
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        # save random partNumber from list
        temp_partNumber = temp_part_num_list[rand_index]

        # remove selected partNumber from templist so its not selected againx
        temp_part_num_list.remove(temp_partNumber)

        try:
            c4.execute(sql_select_query, (int(temp_partNumber), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]) ))
            x-=1
        except:
            print("error")




    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    temp_part_num_list = list_part_ids.copy()

    x = 999999

    # 0 to 999
    while x>=0:
        print(x)
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index = random.randint(0,(len(temp_part_num_list)-1))
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        # save random partNumber from list
        temp_partNumber = temp_part_num_list[rand_index]

        # remove selected partNumber from templist so its not selected againx
        temp_part_num_list.remove(temp_partNumber)

        try:
            c5.execute(sql_select_query, (int(temp_partNumber), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]) ))
            x-=1
        except:
            print("error")


if __name__ == "__main__":
    # connect with databases
    conn1 = sqlite3.connect("A4v100.db")
    c1 = conn1.cursor()
    conn2 = sqlite3.connect("A4v1k.db")
    c2 = conn2.cursor()
    conn3 = sqlite3.connect("A4v10k.db")
    c3 = conn3.cursor()
    conn4 = sqlite3.connect("A4v100k.db")
    c4 = conn4.cursor()
    conn5 = sqlite3.connect("A4v1M.db")
    c5 = conn5.cursor()

    # lists to hold part number ID's and country abbreviations
    country_list = []
    part_id_list = []

    # extract data and store in lists
    country_list, part_id_list = extract_data(country_list, part_id_list)

    # now populate DB's
    populate_db(country_list, part_id_list)


