from mysql.connector import connect, Error

class InsertData:

    def InsTableClient(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="Mdk10mkK1984!",
                database="autoservice",
            ) as connection:
                a = input('Введите фамилию: ')
                b = input('Введите имя: ')
                c = input('Введите отчество: ')
                d = input('Введите номер телефона: ')
                f = input('Введите адрес: ')
                var1 = (a, b, c, d, f)
                var = []
                var.append(var1)
                insert_data_client = """
                INSERT client(LastName, FirstName, MiddleName, Phone, Adress)
                VALUES (%s, %s, %s, %s, %s)
                """
                with connection.cursor() as cursor:
                    cursor.executemany(insert_data_client, var)
                    print("Запись добавлена!")
                    connection.commit()
        except Error as e:
            print(e)

    def InTableAuto(self):
        try:
            with connect(
                host="localhost",
                user="root",
                password="Mdk10mkK1984!",
                database="autoservice",
            ) as connection:
                a = input('Введите госномер автомобиля: ')
                b = input('Введите марку автомобиля: ')
                c = input('Ведите модель автомобиля: ')
                d = input("Введите ВИН номер автомобиля: ")
                val = (a, b, c, d)
                var = []
                var.append(val)
                incert_data_auto = """
                        INSERT auto (Number, Marka, Model, VIN)
                        VALUES (%s, %s, %s, %s)
                        """
                with connection.cursor() as cursor:
                    cursor.executemany(incert_data_auto, var)
                    connection.commit()
        except Error as e:
            print(e)


