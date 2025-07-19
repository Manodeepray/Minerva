import sys
import asyncio
from pyppeteer import launch
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import os

# === PyQt GUI Setup ===
class ScreenshotViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label = QLabel()
        self.label.setStyleSheet("border: 4px solid #333; background-color: white;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.resize(1024, 768)
        self.show()

    def update_image(self, path):
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

# === Pyppeteer Agent ===
async def run_browser_and_capture(viewer):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({"width": 1024, "height": 768})
    await page.goto("https://example.com")

    screenshot_path = "screenshot.png"
    await page.screenshot({'path': screenshot_path})
    viewer.update_image(screenshot_path)
    await asyncio.sleep(2)

    await page.type("body", "Hello from Pyppeteer!")
    await page.screenshot({'path': screenshot_path})
    viewer.update_image(screenshot_path)
    await asyncio.sleep(2)

    await browser.close()

# === Combine PyQt + Pyppeteer ===
def run_app():
    app = QApplication(sys.argv)
    viewer = ScreenshotViewer()

    # Run asyncio loop after UI starts
    loop = asyncio.get_event_loop()

    def run_async_code():
        loop.create_task(run_browser_and_capture(viewer))

    # Slight delay to let GUI render before launching browser
    QTimer.singleShot(100, run_async_code)
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
