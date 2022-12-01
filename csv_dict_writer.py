import csv

# This program gets user input: company name, symbol, and transfer agent.
# It then creates a dictionary of the input into a file named ("transfer_agent.csv") per line 10.

company_name = input("What is the company name? ")
symbol = input("What is the stock symbol? ")
transfer_agent = input("Who is the transfer agent? ")

with open("transfer_agent.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["company_name", "symbol", "transfer_agent"])
    writer.writerow({"company_name": company_name, "symbol": symbol, "transfer_agent": transfer_agent})