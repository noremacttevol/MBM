import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  await page.goto('http://localhost:8080');
  await page.waitForSelector('.hook-screen', { timeout: 10000 }).catch(() => console.log('Hook screen not found'));
  
  await page.screenshot({ path: 'screenshots/hook-screen.png', fullPage: true });
  console.log('Hook screen captured');
  
  await browser.close();
})();
