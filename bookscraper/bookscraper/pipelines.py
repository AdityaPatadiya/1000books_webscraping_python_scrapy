# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# pipelines.py

from itemadapter import ItemAdapter
import logging
import sqlite3

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)  # create an instance


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        logger.info(f"Processing item: {item}")

        # strip all the white spaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "Description":
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()
        logger.info("strips done!")

        # category & product type --> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()
        logger.info("lowercase done!")

        # price --> convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            if value:
                # Remove currency symbol and convert to float
                clean_value = value.replace('£', '').strip()
                if clean_value:
                    adapter[price_key] = float(clean_value)
                else:
                    logger.warning(f"Empty value for {price_key}")
        logger.info("float conversion done!")

        # availability --> extract number of books in stock
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        logger.info("extraction done!")

        # reviews --> convert string to number
        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)
        logger.info("num_reviews done!")

        # stars --> convert text to number
        stars_rating = adapter.get('stars')
        split_stars_array = stars_rating.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == "zero":
            adapter['stars'] = 0
        elif stars_text_value == "one":
            adapter['stars'] = 1
        elif stars_text_value == "two":
            adapter['stars'] = 2
        elif stars_text_value == "three":
            adapter['stars'] = 3
        elif stars_text_value == "four":
            adapter['stars'] = 4
        elif stars_text_value == "five":
            adapter['stars'] = 5

        logger.info("calculation of stars done!")

        # items = adapter.field_names()
        # for item in items:
        #     print(type(item))

        return item
    logger.info("BookscraperPipeline code is executed.")


class SaveToMySqlPipeline:
    def __init__(self):
        self.conn = sqlite3.connect('booksdata.db')  # it will create a database if it does not exist.
        logger.info("database is connected!")

        # create cursor, used to execute commands
        self.cur = self.conn.cursor()

        # create books table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url VARCHAR(255),
            title TEXT,
            upc VARCHAR(255),
            product_type VARCHAR(255),
            price_excl_tax DECIMAL,
            price_incl_tax DECIMAL,
            tax DECIMAL,
            availability INTEGER,
            num_reviews INTEGER,
            stars INTEGER,
            category VARCHAR(255),
            description TEXT,
            price VARCHAR(255)
        )
        """)
        # REAL is a floating point value
        logger.info("Table is created.")
        self.conn.commit()

    def process_item(self, item, spider):

        self.cur.execute("""
                    insert into books (url, title, upc, product_type, price_excl_tax, price_incl_tax, 
                    tax, availability, num_reviews, stars, category, description, price) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
            item["url"], item["title"], item["upc"], item["product_type"], item["price_excl_tax"], item["price_incl_tax"],
            item["tax"], item["availability"], item["num_reviews"],
            item["stars"], item["category"], item["description"], item["price"]))

        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
        logger.info("SQLite connection closed")
