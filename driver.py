from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://set.loud.red/play')
    
    # Wait for the first tile to load
    await page.waitForSelector('.svelte-2fu5i7')
    
    content = await page.content()
    await browser.close()
    return content

html_content = asyncio.get_event_loop().run_until_complete(main())

soup = BeautifulSoup(html_content, 'html.parser')
print(html_content)
tiles = soup.find_all('div', {'class': 'svelte-2fu5i7'})
for tile in tiles:
    print(tile)