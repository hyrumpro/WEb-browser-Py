import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QAction, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Browser")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        self.urlbar = QLineEdit(self)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        self.back_button = QAction("Back", self)
        self.back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction("Forward", self)
        self.forward_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(self.forward_button)

        self.refresh_button = QAction("Refresh", self)
        self.refresh_button.triggered.connect(self.browser.reload)
        self.toolbar.addAction(self.refresh_button)

        self.toolbar.addWidget(self.urlbar)

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)
        self.browser.urlChanged.connect(self.update_urlbar)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())