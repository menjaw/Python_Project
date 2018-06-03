from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Scraper(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance
        print('Hi {} your current balance is: {}'.format(self.name, self.balance))

    def setChromeDriver(self, path):
        return webdriver.Chrome('{}').format(path)


    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        print('Your new balance is: {}'.format(self.balance))
        return self.balance

    def showBalance(self):
        print(self.balance)
