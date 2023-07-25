from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Create a new instance of the Firefox driver
# driver = webdriver.Chrome()


# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Go to the page that we want to scrape
driver.get("https://set.loud.red/play")

# Wait for the page to load
time.sleep(1)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the tiles
tiles = soup.find_all('div', {'class': 'svelte-ttp4q4'})

# Print the tiles
# for tile in tiles:
#     print(tile)

# Close the browser
# driver.quit()

print("Done")
print(tiles[0])


class Tile:
    def __init__(self, number, shape, color, shading):
        self.number = number
        self.shape = shape
        self.color = color
        self.shading = shading
    def compareColor(self, other): 
        return self.color == other.color
    def compareShape(self, other):
        return self.shape == other.shape
    def compareShading(self, other):
        return self.shading == other.shading
    def compareNumber(self, other):
        return self.number == other.number

def extract_tile_info(tile):
    info = {}

    # Extract number
    shapes_div = tile.select_one('div.shapes.svelte-1ojzx2w')
    if shapes_div and 'two' in shapes_div['class']:
        info['number'] = 2
    elif shapes_div and 'three' in shapes_div['class']:
        info['number'] = 3
    else:
        info['number'] = 1

    # Extract color
    color_div = tile.select_one('div.color-indicator.svelte-ttp4q4')
    info['color'] = color_div['class'][-1] if color_div else None

    # Extract shape
    svg = tile.select_one('svg')
    if svg:
        if svg.select_one('rect'):
            info['shape'] = 'square'
        elif svg.select_one('circle'):
            info['shape'] = 'circle'
        elif svg.select_one('path'):
            info['shape'] = 'triangle'

    # Extract shading
    shape_div = tile.select_one('div.shape.svelte-krderl')
    info['shading'] = shape_div['class'][-1] if shape_div else None

    return info

tile_info = [extract_tile_info(tile) for tile in tiles]

for tile in tile_info:
    # if the tile has a "None" value, it's not a valid tile, and throw it out of the list
    if None in tile.values():
        tile_info.remove(tile)

print(tile_info)

print(tile_info[0]['number'])

tile_list = []

for tile in tile_info:
    tile_list.append(Tile(tile['number'], tile['shape'], tile['color'], tile['shading']))


class Game: 
    def __init__(self, tileList):
        self.tileList = tileList


    # def findWin(self):
    #     for i in range(len(self.tileList)):
    #         for j in range(i+1, len(self.tileList)):
    #             for k in range(j+1, len(self.tileList)):
    #                 a, b, c = self.tileList[i], self.tileList[j], self.tileList[k]
    #                 colorMatch = (a.compareColor(b) and a.compareColor(c) and b.compareColor(c)) or (not a.compareColor(b) and not a.compareColor(c) and not b.compareColor(c))
    #                 numberMatch = (a.compareNumber(b) and a.compareNumber(c) and b.compareNumber(c)) or (not a.compareNumber(b) and not a.compareNumber(c) and not b.compareNumber(c))
    #                 shapeMatch = (a.compareShape(b) and a.compareShape(c) and b.compareShape(c)) or (not a.compareShape(b) and not a.compareShape(c) and not b.compareShape(c))
    #                 shadeMatch = (a.compareShading(b) and a.compareShading(c) and b.compareShading(c)) or (not a.compareShading(b) and not a.compareShading(c) and not b.compareShading(c))
    #                 if(colorMatch and numberMatch and shapeMatch and shadeMatch): 
    #                     print(i,j,k)
    #                     buttons[i].click()
    #                     buttons[j].click()
    #                     buttons[k].click() 
    #     return None
    def findWin(self):
        for i in range(len(self.tileList)):
            for j in range(i+1, len(self.tileList)):
                for k in range(j+1, len(self.tileList)):
                    a, b, c = self.tileList[i], self.tileList[j], self.tileList[k]
                    colorMatch = (a.compareColor(b) and a.compareColor(c) and b.compareColor(c)) or (not a.compareColor(b) and not a.compareColor(c) and not b.compareColor(c))
                    numberMatch = (a.compareNumber(b) and a.compareNumber(c) and b.compareNumber(c)) or (not a.compareNumber(b) and not a.compareNumber(c) and not b.compareNumber(c))
                    shapeMatch = (a.compareShape(b) and a.compareShape(c) and b.compareShape(c)) or (not a.compareShape(b) and not a.compareShape(c) and not b.compareShape(c))
                    shadeMatch = (a.compareShading(b) and a.compareShading(c) and b.compareShading(c)) or (not a.compareShading(b) and not a.compareShading(c) and not b.compareShading(c))
                    if(colorMatch and numberMatch and shapeMatch and shadeMatch): 
                        buttons = grid_div.find_elements(By.CSS_SELECTOR, 'button.svelte-t8ucx0')  # Fetch the buttons afresh
                        # buttons[i] = driver.find_element(By.CSS_SELECTOR, 'button.svelte-t8ucx0:nth-child({})'.format(i+1))
                        # buttons[j] = driver.find_element(By.CSS_SELECTOR, 'button.svelte-t8ucx0:nth-child({})'.format(j+1))
                        # buttons[k] = driver.find_element(By.CSS_SELECTOR, 'button.svelte-t8ucx0:nth-child({})'.format(k+1))
                        # time.sleep(.1)
                        buttons[i].click()
                        # time.sleep(.1)
                        buttons[j].click()
                        # time.sleep(.1)
                        buttons[k].click()
                        print(i,j,k)
                        return None
        return None



# Go to the page that we want to scrape
# driver.get("https://set.loud.red/play")

# print("helloooooooooo")

# Wait for the page to load
# time.sleep(1)

# Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the tiles
# tiles = soup.find_all('div', {'class': 'svelte-2fu5i7'})

# Print the tiles
# for tile in tiles:
#     print(tile)

# Close the browser

    # Wait for the grid div to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.grid.svelte-2fu5i7')))

# Find the grid div
grid_div = driver.find_element(By.CSS_SELECTOR, 'div.grid.svelte-2fu5i7')

# Find all buttons within the grid div
buttons = grid_div.find_elements(By.CSS_SELECTOR, 'button.svelte-t8ucx0')

# Click the first, second, third, ..., ninth button
# Remember, indexing starts at 0 in Python, so subtract 1 from each number
# for i in range(9):
#     buttons[i].click()
#     print(i)
#     time.sleep(3)
#     print("i clicked a tile")

# buttons[0].click()
# time.sleep(1)
# buttons[4].click()
# time.sleep(1)
# buttons[7].click()

# for tile in tile_info:
#     if tile['color'] == 'green':
#         buttons[]
# for i in range(3):
#     # if tile_info[i]['color'] == 'green':
#     buttons[i].click()
#     time.sleep(1)
# time.sleep(2)
attempt = Game(tile_list)
attempt.findWin()
time.sleep(1)

# while(True):
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     print("WTFFFFF")
#     tiles = soup.find_all('div', {'class': 'svelte-ttp4q4'})
#     tile_info = [extract_tile_info(tile) for tile in tiles]

#     for tile in tile_info:
#         # if the tile has a "Non" value, it's not a valid tile, and throw it out of the list
#         if None in tile.values():
#             tile_info.remove(tile)

#     tile_list = []
    
#     for tile in tile_info:
#         tile_list.append(Tile(tile['number'], tile['shape'], tile['color'], tile['shading']))

#     print(tile_list)
    
#     # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.  grid.svelte-2fu5i7')))


#     grid_div = driver.find_element(By.CSS_SELECTOR, 'div.grid.svelte-2fu5i7')


#     buttons = grid_div.find_elements(By.CSS_SELECTOR, 'button.svelte-t8ucx0')
#     attempt = Game(tile_list)
#     attempt.findWin()
#     time.sleep(2)
# time.sleep(10)
while(True):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print("WTFFFFF")
    tiles = soup.find_all('div', {'class': 'svelte-ttp4q4'})
    tile_info = [extract_tile_info(tile) for tile in tiles]

    for tile in tile_info:
        # if the tile has a "None" value, it's not a valid tile, and throw it out of the list
        if None in tile.values():
            tile_info.remove(tile)

    tile_list = []
    
    for tile in tile_info:
        tile_list.append(Tile(tile['number'], tile['shape'], tile['color'], tile['shading']))
    if len(tile_list)==0:
        break
    print(tile_list)
    
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.grid.svelte-2fu5i7')))

    # Refresh the buttons element references
    grid_div = driver.find_element(By.CSS_SELECTOR, 'div.grid.svelte-2fu5i7')
    buttons = grid_div.find_elements(By.CSS_SELECTOR, 'button.svelte-t8ucx0')

    attempt = Game(tile_list)
    attempt.findWin()
    time.sleep(.5)

time.sleep(10)




# driver.quit()