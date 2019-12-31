# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class FlipkartscrappingPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        hostname = 'localhost'
        username = 'postgres'
        password = 'qwerty'
        database = 'filpkart_scrap'
        portnumber = "5432"
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=portnumber)
        self.curr = self.connection.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS flipkart_data1""")
        self.curr.execute(""" CREATE TABLE flipkart_data1(
                        productname VARCHAR,
                        price VARCHAR,
                        imagelink VARCHAR
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO flipkart_data1 (productname, price, imagelink) VALUES (%s,%s,%s)""",
                          (
                              item['product_name'],
                              item['product_price'],
                              item['product_image_link']

                          ))
        self.connection.commit()




