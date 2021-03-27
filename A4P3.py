import sqlite3
import csv
import random
import time

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
                
    #print("length of list = {}".format(len(list_part_ids)))
    
    # remove duplicate part numbers because of primary key constraint
    list_part_ids = list(dict.fromkeys(list_part_ids))
    #print("length of list with duplicates removed = {}".format(len(list_part_ids)))

    # now remove floats and integers BIGGER than 8 bytes(2^63 -1) 
    list_part_ids_int=[]
    for num in list_part_ids:
        try:
            int_test=int(num)
            if int_test <= 9223372036854775807:
                list_part_ids_int.append(num)
        except ValueError:
            pass
    
    #print("length of list with floats/ and not integers removed = {}".format(len(list_part_ids_int)))

    
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

    #print("length of list of countries = {}".format(len(list_countries)))  

    return list_countries, list_part_ids_int




def populate_db(list_countries, list_part_ids):

    #counter_100, counter_1k, counter_10k, counter_100k, counter_1M = 0, 0, 0, 0, 0

    # define INSERT query
    sql_insert_query = """INSERT INTO Parts (partNumber, partPrice, needsPart, madeIn)
    VALUES(?,?,?,?);"""


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


    #print('error count is', error_count)

    #insert multiple rows in a single query
    c1.executemany(sql_insert_query, list_of_rows)

    #print('We have inserted', c1.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c1.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c1.fetchone()[0]
    #print (rowcount)




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


    #print('error count is', error_count)

    #insert multiple rows in a single query
    c2.executemany(sql_insert_query, list_of_rows)

    #print('We have inserted', c2.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c2.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c2.fetchone()[0]
    #print (rowcount)






    
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


    #print('error count is', error_count)

    #insert multiple rows in a single query
    c3.executemany(sql_insert_query, list_of_rows)

    #print('We have inserted', c3.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c3.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c3.fetchone()[0]
    #print (rowcount)





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


    #print('error count is', error_count)

    #insert multiple rows in a single query
    c4.executemany(sql_insert_query, list_of_rows)

    #print('We have inserted', c4.rowcount, 'records to the table.')

    #commit the changes to db			
    #conn1.commit()

    c4.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c4.fetchone()[0]
    #print (rowcount)



    


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


    #print('error count is', error_count)

    #insert multiple rows in a single query
    c5.executemany(sql_insert_query, list_of_rows)

    #print('We have inserted', c5.rowcount, 'records to the table.')

    #commit the changes to db	  		
    #conn1.commit()

    c5.execute("SELECT COUNT (*) FROM Parts")
    rowcount = c5.fetchone()[0]
    #print (rowcount)
    
    


def part3_query():

    print("Executing Part 3")
    print()
    print("Executing Task I")

    # define part3 query
    sql_select_query = """SELECT p.partNumber, p.madeIn, p.partPrice
    FROM Parts p
    WHERE p.madeIn = ? AND p.partPrice >= (SELECT MAX(p1.partPrice) FROM Parts p1 WHERE p1.madeIn = ?);"""
    
    # define query for generating list of countries in db
    sql_select_countries = """SELECT p.madeIn
    FROM Parts p;"""



    # generate list of all countries in A4v100.db
    c1.execute(sql_select_countries)
    list_countries = []
    records = c1.fetchall()
    for row in records:
        list_countries.append(row[0])   

    query_time_100 = []
    # values 0 to 49 for DB A4v100.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c1.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_100.append(end - start)
      
    print('Average query time of A4v100 in seconds without index = ',sum(query_time_100) / len(query_time_100))



    # generate list of all countries in A4v1k.db
    c2.execute(sql_select_countries)
    list_countries = []
    records = c2.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_1k = []
    # values 0 to 49 for DB A4v1k.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c2.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_1k.append(end - start)
      
    print('Average query time of A4v1k in seconds without index = ',sum(query_time_1k) / len(query_time_1k))
    
    

    # generate list of all countries in A4v10k.db
    c3.execute(sql_select_countries)
    list_countries = []
    records = c3.fetchall()
    for row in records:
        list_countries.append(row[0]) 
    
    query_time_10k = []
    # values 0 to 49 for DB A4v10k.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c3.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_10k.append(end - start)
       
    print('Average query time of A4v10k in seconds without index = ',sum(query_time_10k) / len(query_time_10k))



    # generate list of all countries in A4v100.db
    c4.execute(sql_select_countries)
    list_countries = []
    records = c4.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_100k = []
    # values 0 to 9 for DB A4v100k.db
    for x in range(10):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c4.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_100k.append(end - start)
      
    print('Average query time of A4v100k in seconds without index = ',sum(query_time_100k) / len(query_time_100k))



    # generate list of all countries in A4v100.db
    c5.execute(sql_select_countries)
    list_countries = []
    records = c5.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_1M = []
    # values 0 to 4 for DB A4v1M.db
    for x in range(5):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c5.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_1M.append(end - start)
      
    print('Average query time of A4v1M in seconds without index = ',sum(query_time_1M) / len(query_time_1M))
    


    # define and create index for all 5 db's
    sql_create_index = '''CREATE INDEX idx_parts_country ON Parts( partPrice ASC, madeIn );'''
    c1.execute(sql_create_index)
    c2.execute(sql_create_index)
    c3.execute(sql_create_index)
    c4.execute(sql_create_index)
    c5.execute(sql_create_index)
    
    print()
    print("Creating Index")
    print()
    print("Executing Task K")



    # generate list of all countries in A4v100.db
    c1.execute(sql_select_countries)
    list_countries = []
    records = c1.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_100_indexed = []
    # values 0 to 49 for DB A4v100.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c1.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_100_indexed.append(end - start)
      
    print('Average query time of A4v100 in seconds with index = ',sum(query_time_100_indexed) / len(query_time_100_indexed))



    # generate list of all countries in A4v1k.db
    c2.execute(sql_select_countries)
    list_countries = []
    records = c2.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_1k_indexed = []
    # values 0 to 49 for DB A4v1k.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c2.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_1k_indexed.append(end - start)
      
    print('Average query time of A4v1k in seconds with index = ',sum(query_time_1k_indexed) / len(query_time_1k_indexed))
    


    # generate list of all countries in A4v10k.db
    c3.execute(sql_select_countries)
    list_countries = []
    records = c3.fetchall()
    for row in records:
        list_countries.append(row[0]) 
    
    query_time_10k_indexed = []
    # values 0 to 49 for DB A4v10k.db
    for x in range(50):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c3.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_10k_indexed.append(end - start)
      
    print('Average query time of A4v10k in seconds with index = ',sum(query_time_10k_indexed) / len(query_time_10k_indexed))



    # generate list of all countries in A4v100k.db
    c4.execute(sql_select_countries)
    list_countries = []
    records = c4.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_100k_indexed = []
    # values 0 to 9 for DB A4v100k.db
    for x in range(10):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c4.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_100k_indexed.append(end - start)
      
    print('Average query time of A4v100k in seconds with index = ',sum(query_time_100k_indexed) / len(query_time_100k_indexed))



    # generate list of all countries in A4v1M.db
    c5.execute(sql_select_countries)
    list_countries = []
    records = c5.fetchall()
    for row in records:
        list_countries.append(row[0]) 

    query_time_1M_indexed = []
    # values 0 to 99 for DB A4v1M.db
    for x in range(5):
        # generate radom country code 
        rand_country_index = random.randint(0,(len(list_countries)-1))
        rand_country = list_countries[rand_country_index]

        # execute query to find most expensive part in random country code while timing it
        start = time.time()
        c5.execute(sql_select_query, (str(rand_country), str(rand_country)) )
        end = time.time()

        # add query time to list
        query_time_1M_indexed.append(end - start)
      
    print('Average query time of A4v1M in seconds with index = ',sum(query_time_1M_indexed) / len(query_time_1M_indexed))




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
    
    sql_update_query = """DELETE from Parts """
    c1.execute(sql_update_query)
    c2.execute(sql_update_query)
    c3.execute(sql_update_query)
    c4.execute(sql_update_query)
    c5.execute(sql_update_query)
    conn1.commit()
    

    # drop idxMadeIn index if it exists for all db's
    sql_drop_query = '''DROP INDEX IF EXISTS idxMadeIn;'''
    c1.execute(sql_drop_query)
    c2.execute(sql_drop_query)
    c3.execute(sql_drop_query)
    c4.execute(sql_drop_query)
    c5.execute(sql_drop_query)


    # drop idxMadeIn index if it exists for all db's
    sql_drop_query = '''DROP INDEX IF EXISTS idx_parts_country;'''
    c1.execute(sql_drop_query)
    c2.execute(sql_drop_query)
    c3.execute(sql_drop_query)
    c4.execute(sql_drop_query)
    c5.execute(sql_drop_query)



    # lists to hold part number ID's and country abbreviations
    country_list = []
    part_id_list = []

    # extract data and store in lists
    country_list, part_id_list = extract_data(country_list, part_id_list)

    # now populate DB's randomly
    populate_db(country_list, part_id_list)

    # Run part 3
    part3_query()



