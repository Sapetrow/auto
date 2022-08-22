from mysql.connector import connect, Error

#create db
def DBAutoservise():
    try:
        with connect(
            host = "localhost",
            user = "root",
            password = "Mdk10mkK1984!",
        ) as connection:
            create_db = "CREATE DATABASE autoservice"
            with connection.cursor() as cursor:
                cursor.execute(create_db)
    except Error as e:
        print(e)

    #create table db
    try:
        with connect(
            host="localhost",
            user = "root",
            password = "Mdk10mkK1984!",
            database = "autoservice",
        ) as connection:
            print(connection)
            create_table_client="""
            CREATE TABLE Client(
                id INT AUTO_INCREMENT PRIMARY KEY,
                LastName VARCHAR(100) NOT NULL,
                FirstName VARCHAR(100) NOT NULL,
                MiddleName VARCHAR(100) NULL,
                Phone INT(9) UNIQUE NOT NULL,
                Adress VARCHAR(200) NULL
                )
                """

            create_table_auto="""
            CREATE TABLE Auto(
                id INT AUTO_INCREMENT PRIMARY KEY,
                Number VARCHAR(100),
                Marka VARCHAR(100),
                Model VARCHAR(100),
                VIN VARCHAR(17)
            )
            """

            create_table_work="""
            CREATE TABLE Work(
                id INT AUTO_INCREMENT PRIMARY KEY,
                CodWork INT,
                NameWork VARCHAR(30),
                PriceWork DECIMAL(6,2)
            )
            """

            create_table_product="""
            CREATE TABLE product(
                id INT AUTO_INCREMENT PRIMARY KEY,
                CodProduct INT,
                NameProduct VARCHAR(30),
                PriveProduct DECIMAL(6,2)
            )
            """
            create_table_zakaz="""
            CREATE TABLE zakaz(
                id INT AUTO_INCREMENT PRIMARY KEY,
                codMaster INT,
                ClientId INT,
                AutoId INT,
                DateZakaz DATETIME,
                DateClose DATETIME,
                FOREIGN KEY (ClientId) REFERENCES Client (id),
                FOREIGN KEY (AutoId) REFERENCES Auto (id)
            )
            """
            create_table_zakaz_info="""
            CREATE TABLE ZakazInfo(
                WorkId INT,
                ProductId INT,
                ZakazId INT,
                Price DECIMAL(6,2),
                Sale INT(2),
                FOREIGN KEY (WorkId) REFERENCES Work (id),
                FOREIGN KEY (ProductId) REFERENCES product (id),
                FOREIGN KEY (ZakazId) REFERENCES zakaz (id)
            )
            """
            with connection.cursor() as cursor:
                cursor.execute(create_table_client)
                cursor.execute(create_table_auto)
                cursor.execute(create_table_work)
                cursor.execute(create_table_product)
                cursor.execute(create_table_zakaz)
                cursor.execute(create_table_zakaz_info)
                connection.commit()


    except Error as e:
        print(e)
