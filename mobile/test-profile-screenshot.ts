// Simple Playwright script to screenshot ProfileScreen
import { chromium } from 'playwright';

async function main() {
  console.log('Starting browser...');
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Wait for Expo web server
  console.log('Waiting for Expo web server on http://localhost:19006...');
  
  try {
    await page.goto('http://localhost:19006', { 
      waitUntil: 'networkidle',
      timeout: 30000 
    });
    
    // Wait for app to load
    await page.waitForTimeout(3000);
    
    // Click Profile tab in bottom nav
    const profileTab = await page.$('[href="/profile"]', () => 
      document.querySelector('a[href="/profile"]') || 
      document.querySelector('button[aria-label*="Profile"]') ||
      Array.from(document.querySelectorAll('*')).find(el => 
        el.textContent?.includes('Profile') || 
        el.textContent?.includes('Journey')
      )
    );
    
    console.log('Profile tab element:', profileTab ? 'FOUND' : 'NOT FOUND');
    
    // Try to navigate directly
    console.log('Navigating to /profile...');
    await page.goto('http://localhost:19006/profile', { 
      waitUntil: 'networkidle',
      timeout: 30000 
    });
    
    await page.waitForTimeout(2000);
    
    // Screenshot
    await page.screenshot({ 
      path: '/tmp/mbm-profile-screenshot.png',
      fullPage: true,
      type: 'png'
    });
    
    console.log('✓ Screenshot saved to /tmp/mbm-profile-screenshot.png');
  } catch (err: any) {
    console.error('Error:', err.message);
    
    // Try alternative port
    try {
      console.log('Trying port 8081...');
      await page.goto('http://localhost:8081', { 
        waitUntil: 'networkidle',
        timeout: 30000 
      });
      await page.waitForTimeout(3000);
      await page.screenshot({ 
        path: '/tmp/mbm-profile-screenshot.png',
        fullPage: true
      });
      console.log('✓ Screenshot saved to /tmp/mbm-profile-screenshot.png');
    } catch (err2: any) {
      console.error('Alternative port also failed:', err2.message);
    }
  }
  
  await browser.close();
}

main().catch(console.error);
