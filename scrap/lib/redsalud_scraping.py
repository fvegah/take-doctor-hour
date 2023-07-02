import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    print('launch')

    page = await browser.newPage()
    print('page')

    url = 'https://agenda.redsalud.cl/#/patientPortal/identifyPatientls'
    await page.goto(url)
    print('Cambio de Pagina')

    await page.screenshot({"path": "python.png"})
    print('Logo de prueba')

    await browser.close()
