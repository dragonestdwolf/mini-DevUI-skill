const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080 });
    const fileUrl = 'file://' + path.resolve('HistoryRender/component/header/v4.html');
    await page.goto(fileUrl, {waitUntil: 'networkidle0'});
    await page.screenshot({path: '/Users/renyuqing/.gemini/antigravity/brain/7a8a3977-59c6-47a9-8009-38388b1ee7ab/media__1772183900.png', fullPage: true});
    await browser.close();
})();
