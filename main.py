from bs4 import BeautifulSoup
import requests
import time
import csv

# Asks budget
value_error = True
input_attempt = 1
while value_error:
    try:
        if input_attempt == 1:
            print("What is your budget?")
        else:
            print("Please input a number.")
        budget = float(input(">"))
        value_error = False
    except ValueError:
        input_attempt += 1
        continue
budget_format = "{:.2f}".format(budget)

# Asks what graphics card(s) the user wants
print("What graphics card(s) are you looking for? If you have no preference, do NOT input anything. (separate multiple graphics cards with commas)")
preferred_graphics_cards = input(">")
# Checks if user inputs multiple graphics cards
multiple = False
if ',' in preferred_graphics_cards:
    multiple = True
    preferred_graphics_cards = preferred_graphics_cards.split(',')

print(f"Searching for your preferred graphics card(s) cheaper than ${budget_format} including shipping.")


# Function that searches graphics cards and outputs results
def find_graphics_cards():
    file = open('graphicscards.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(['Graphics Card', 'Price', 'Shipping', 'More Info'])
    writer.writerow([])

    # Checks if any graphics cards have been found
    is_available = False

    for page in range(1, 100+1):
        if page == 1:
            html_text = requests.get('https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48').text
        else:
            html_text = requests.get(f'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-{page}').text

        soup = BeautifulSoup(html_text, 'lxml')

        graphics_cards = soup.find_all('div', class_='item-container')

        for graphics_card in graphics_cards:
            price = graphics_card.find('li', class_='price-current').text.split()
            if price:
                price = price[0]
            else:
                continue
            num_price = float(price.replace('$', '').replace(',', ''))

            shipping = graphics_card.find('li', class_='price-ship').text.split()
            if 'Free' in shipping or 'Special' in shipping:
                num_shipping = 0
                shipping = shipping[0]
            elif 'Est.' in shipping:
                num_shipping = float(shipping[len(shipping)-1].replace('$', ''))
                shipping = shipping[len(shipping)-1]
            else:
                num_shipping = float(shipping[0].replace('$', ''))
                shipping = shipping[0]

            total_cost = num_price + num_shipping
            if total_cost <= budget:
                graphics_card_name = graphics_card.find('a', class_='item-title').text
                more_info = graphics_card.a['href']

                if multiple:
                    for preferred_graphics_card in preferred_graphics_cards:
                        preferred_graphics_card = preferred_graphics_card.strip()
                        if preferred_graphics_card.upper() in graphics_card_name.upper():
                            is_available = True
                            print(f"Graphics Card: {graphics_card_name}")
                            print(f"Price: {price}")
                            print(f"Shipping: {shipping}")
                            print(f"More info: {more_info}")

                            print()
                            writer.writerow([graphics_card_name, price, shipping, more_info])
                else:
                    if preferred_graphics_cards.strip() == '':
                        is_available = True
                        print(f"Graphics Card: {graphics_card_name}")
                        print(f"Price: {price}")
                        print(f"Shipping: {shipping}")
                        print(f"More info: {more_info}")

                        print()
                        writer.writerow([graphics_card_name, price, shipping, more_info])
                    else:
                        if preferred_graphics_cards.upper() in graphics_card_name.upper():
                            is_available = True
                            print(f"Graphics Card: {graphics_card_name}")
                            print(f"Price: {price}")
                            print(f"Shipping: {shipping}")
                            print(f"More info: {more_info}")

                            print()
                            writer.writerow([graphics_card_name, price, shipping, more_info])

    if not is_available:
        print("There are no graphics cards available.")
        writer.writerow(["None available."])

    file.close()


if __name__ == "__main__":
    while True:
        find_graphics_cards()
        print('A CSV file containing the graphics cards has been created.')
        # wait time in hours
        wait_time = 24
        print(f'Graphics cards will update every {wait_time} hours.')
        time.sleep(wait_time * 3600)



