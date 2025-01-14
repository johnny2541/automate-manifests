from bs4 import BeautifulSoup
from html_content import *

# soup = BeautifulSoup(html_picklist_content, "html.parser")

# pickinglists = soup.find_all("div", class_="picking-list-item")

# for pickinglist in pickinglists:
#     order_number = pickinglist.find("div", class_="order-number")
#     if order_number:
#         print(order_number.text)
    
#     line_items = pickinglist.find_all("table", class_="line-items-table")
#     print(line_items)

soup = BeautifulSoup(html_picklist_content, "html.parser")

pickinglists = soup.find("div", class_="picking-list-item")
item_table = pickinglists.find("table", class_="line-items-table")

if item_table :
    for tr in item_table.find_all("tr"):
        if tr.find("td",class_="nowrap"):
            # location = tr.find("td",class_="nowrap").contents
            locationBin = (tr.find("td",class_="nowrap").text)
            brand = tr.find_all("td")[1].text
            quantity = tr.find_all("td")[2].text
            bacodeNumber = tr.find_all("td")[4].text
            print(f"brand is {brand} location {locationBin} quantity {quantity} bacode {bacodeNumber}")

        
        
            
            
            

