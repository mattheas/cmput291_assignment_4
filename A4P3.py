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

    # now remove floats and integers BIGGER than 8 bytes(2^63 -1) 
    list_part_ids_int=[]
    for num in list_part_ids:
        try:
            int_test=int(num)
            if int_test <= 9223372036854775807:
                list_part_ids_int.append(num)
        except ValueError:
            pass
    
    print("length of list with floats/ and not integers removed = {}".format(len(list_part_ids_int)))

    
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

    print("length of list of countries = {}".format(len(list_countries)))  

    return list_countries, list_part_ids_int




def populate_db(list_countries, list_part_ids):

    #counter_100, counter_1k, counter_10k, counter_100k, counter_1M = 0, 0, 0, 0, 0

    # define INSERT query
    sql_insert_query = """INSERT INTO Parts (partNumber, partPrice, needsPart, madeIn)
    VALUES(?,?,?,?);"""

    # copy partNumber list so we can remove partNumbers from it after they're inserted into DB
    #temp_part_num_list = list_part_ids.copy()

    


    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # loop variables/ list
    error_count = 0
    x = 0
    list_of_rows =[]

    while x<=99:
        #print(x)

        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        temp_tuple = ()

        try:
            temp_tuple = (int(list_part_ids[x]), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]))
            list_of_rows.append(temp_tuple)
            x+=1

        except:
            print("error")
            error_count+=1


    print('error count is', error_count)

    #insert multiple rows in a single query
    c1.executemany(sql_insert_query, list_of_rows)

    print('We have inserted', c1.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c1.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c1.fetchone()[0]
    print (rowcount)




    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # loop variables/ list
    error_count = 0
    x = 0
    list_of_rows =[]

    while x<=999:
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        temp_tuple = ()

        try:
            temp_tuple = (int(list_part_ids[x]), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]))
            list_of_rows.append(temp_tuple)
            x+=1

        except:
            print("error")
            error_count+=1


    print('error count is', error_count)

    #insert multiple rows in a single query
    c2.executemany(sql_insert_query, list_of_rows)

    print('We have inserted', c2.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c2.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c2.fetchone()[0]
    print (rowcount)







    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # loop variables/ list
    error_count = 0
    x = 0
    list_of_rows =[]

    while x<=9999:
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        temp_tuple = ()

        try:
            temp_tuple = (int(list_part_ids[x]), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]))
            list_of_rows.append(temp_tuple)
            x+=1

        except:
            print("error")
            error_count+=1


    print('error count is', error_count)

    #insert multiple rows in a single query
    c3.executemany(sql_insert_query, list_of_rows)

    print('We have inserted', c3.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c3.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c3.fetchone()[0]
    print (rowcount)





    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # loop variables/ list
    error_count = 0
    x = 0
    list_of_rows =[]

    while x<=99999:
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        temp_tuple = ()

        try:
            temp_tuple = (int(list_part_ids[x]), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]))
            list_of_rows.append(temp_tuple)
            x+=1

        except:
            print("error")
            error_count+=1


    print('error count is', error_count)

    #insert multiple rows in a single query
    c4.executemany(sql_insert_query, list_of_rows)

    print('We have inserted', c4.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c4.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c4.fetchone()[0]
    print (rowcount)



    '''


    #shuffle all part #'s/ countries once for DB
    random.shuffle(list_countries)
    random.shuffle(list_part_ids)

    # loop variables/ list
    error_count = 0
    x = 0
    list_of_rows =[]

    while x<=999999:
        # generate random int for price for each part
        rand_price = random.randint(1,100)

        # generate random num to index list of partNumbers, partNeeds and madeIn
        rand_index2 = random.randint(0,(len(list_part_ids)-1))
        rand_index3 = random.randint(0,(len(list_countries)-1))

        temp_tuple = ()

        try:
            temp_tuple = (int(list_part_ids[x]), int(rand_price), int(list_part_ids[rand_index2]), str(list_countries[rand_index3]))
            list_of_rows.append(temp_tuple)
            x+=1

        except:
            print("error")
            error_count+=1


    print('error count is', error_count)

    #insert multiple rows in a single query
    c5.executemany(sql_insert_query, list_of_rows)

    print('We have inserted', c5.rowcount, 'records to the table.')

    #commit the changes to db	  		
    #conn1.commit()

    c5.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c5.fetchone()[0]
    print (rowcount)
    '''


def part3_query(list_countries, list_part_ids):

    # define part3 query
    sql_select_query = """SELECT p.partNumber, MAX(p.partPrice)
    FROM Parts p
    WHERE p.madeIn = ?
    GROUP BY p.partNumber;"""

    # generate radom country code 
    rand_country_index = random.randint(0,(len(list_countries)-1))
    rand_country = list_countries[rand_country_index]

    # execute query to find most expensive part in country code
    c1.execute(sql_select_query, (str(rand_country),) )

    records = c1.fetchall()

    print(" partNumber   MAX(part price)")

    for row in records:
        print("{}   {}".format(row[0], row[1]))






    # query used to check if ACTUAL query is correct
    sql_select_query1 = """SELECT p.partNumber, p.madeIn
    FROM Parts p
    WHERE p.madeIn = ?;"""

    c1.execute(sql_select_query1, (str(rand_country),) )

    records = c1.fetchall()

    print(" partNumber   madeIn")

    for row in records:
        print("{}   {}".format(row[0], row[1]))








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

    # used to clear all rows in table if needed
    '''
    sql_update_query = """DELETE from Parts """
    c1.execute(sql_update_query)
    conn1.commit()
    '''

    # lists to hold part number ID's and country abbreviations
    country_list = []
    part_id_list = []

    # extract data and store in lists
    country_list, part_id_list = extract_data(country_list, part_id_list)

    # now populate DB's randomly
    #populate_db(country_list, part_id_list)

    # Run part 3
    part3_query(country_list, part_id_list)



