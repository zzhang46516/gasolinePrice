import psycopg2


class GasolinePricePipeline(object):

    def __init__(self):
        hostname = 'localhost'
        database = 'rgp'
        self.connection = psycopg2.connect(host=hostname, dbname=database)
        self.cur = self.connection.cursor()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):

        # check if the state exist in the table
        if not self.cur.execute('''SELECT EXISTS (SELECT 1 FROM "gasolinePrice_states" WHERE states = %s)''', (item['State'],
        )):
            try:
                self.cur.execute('''INSERT INTO "gasolinePrice_states"(states) VALUES(%s)''', (item['State'],))
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                raise
        # check if the release date is exist in the table
        if self.cur.execute('''SELECT EXISTS(SELECT 1 FROM "gasolinePrice_updateprice" WHERE release_date = %s)''', (item['Released_Date'],)):
            print("data is latest")
        else:
            try:
                self.cur.execute('''INSERT INTO "gasolinePrice_updateprice"(release_date, price, state_id) VALUES (%s, %s, (SELECT id from "gasolinePrice_states" WHERE states = %s))''', (item['Released_Date'], item['Price'], item['State'],))
                self.connection.commit()

            except Exception as e:
                self.connection.rollback()
                raise

        return item
