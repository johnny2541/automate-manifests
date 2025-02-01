from bs4 import BeautifulSoup
from html_content import *

soup = BeautifulSoup(html_picklist_content, "html.parser")

# Extract body element class "picking-list multiple" from html element
body_El = soup.find("body", class_="picking-list multiple")

# From method find_all() extract div element class "picking-list-item" from bodyEl in pickings_Arr
pickinglist_Arr = body_El.find_all("div", class_="picking-list-item")

# From pickinglist_Arr extract each div element to pickinglist

for pickinglist in pickinglist_Arr : 

    # From pickinglist we are travel in it and extract data from it
    div_row_El = pickinglist.find_all("div", class_="row")
    orderNumber = div_row_El[0].find("div", class_="barcode col s4").find("div", class_="order-number").string.strip()
    order_product_list = div_row_El[1].find("tbody").find_all("tr")

    for product in order_product_list:
        product_detail_Arr = product.find_all("td") 

        #product location
        product_location_not_strip = product_detail_Arr[0].contents[0].string + product_detail_Arr[0].contents[1]
        product_location = product_location_not_strip.replace("|","").replace(" ","")
        product_name = product_detail_Arr[1]
        product_qualtity = product_detail_Arr[2]
        product_barcode_number = product_detail_Arr[4]
        product_detail = product_detail_Arr[5]
        print(f"name is {product_name}, ")
    
    break # test breack
    




