# Graphics Card Finder

This repository contains a python script that parses the Newegg site for graphics cards.

## Setup Instructions

1. Make sure to have Python installed. If you don't have it installed, visit [this link](https://www.python.org/downloads/)
2. Open your terminal
3. Have *BeautifulSoup4* installed by running `pip install bs4` which is the library used for scraping
4. Ensure *lxml* is installed by running `pip install lxml`. This is the library that is used to parse HTML and XML 
5. Clone this repository by running `git clone https://github.com/HubertTheodore/graphics-card-finder.git` in the terminal. Make sure you cd into the directory where you want to clone it before running the command
6. Change directory to `...\graphics-cards-finder>`
7. Have the *requests* library installed by running `pip install requests` which is the library used to send a request to a website

## Running the Script

1. Make sure you are in the directory `...\graphics-cards-finder>`
2. Run `python main.py` then follow the prompts
3. You will see that graphics cards that fit the requirements are printed to the console
4. After all graphics cards have been parsed, the program will re-run every 24 hours assuming you do not terminate the script
5. If you are satisfied, terminate the script with `Ctrl+C`
6. A csv file called *graphicscards.csv* contains all of the desired graphics cards from the results that have been previously ran by the script
7. Open the file by running `.\graphicscards.csv` (assuming you are in the `...\graphics-cards-finder>` directory)
