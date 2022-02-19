from aiogram import Bot, Dispatcher
from configparser import ConfigParser
from database.products import Products
from database.users import Users
from database.store_connection import StoreConnection
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = ConfigParser() 
config.read("config.ini")

bot = Bot(token=config["TELEGRAM"]["token"])

dispatcher = Dispatcher(bot, storage=MemoryStorage())

connection = StoreConnection.get_connection(
    config["DATABASE"]["username"],
    config["DATABASE"]["password"]
)

database = connection[config["DATABASE"]["name"]]

products = Products(database)
users = Users(database)

