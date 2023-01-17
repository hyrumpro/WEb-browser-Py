#Documentation
------------------------------------------------------------------------


QtPy is a Python binding for the Qt library, which is a cross-platform application development framework that can
 be used to create desktop applications, including web browsers. To build a web browser using Python and QtPy, you 
will need to use the QWebView or QWebEngine classes from the QtWebKit or QtWebEngine modules respectively. 
These classes provide a web view widget that can be used to display web pages, and you can interact with them using
 Python to create a functional web browser.


This browser defines a Browser class that inherits from QMainWindow. The __init__ method sets up the basic layout 
of the browser window, including a QWebEngineView widget for displaying web pages and a QLineEdit widget for 
entering URLs. The navigate_to_url method is connected to the returnPressed signal of the URL bar, so that it is 
called when the user presses the Enter key after entering a URL.
You can run this code by saving it to a file with a .py extension and running it using python.
It is a basic example and you can add more functionality and improve the UI as you want.
Here's an example that shows how to add "back", "forward", "refresh" buttons and a url bar functionality to the
 browser:
This example adds three QAction instances to the toolbar, one for each of the "back", "forward", and "refresh" 
buttons. Each action is connected to the corresponding method of the QWebEngineView, "back", "forward", "reload".
Additionally, this example also connects the urlChanged signal of the QWebEngineView to update_urlbar method, which
 updates the urlbar with the current url of the page.

It also adds the urlbar to the toolbar, so that the user can type a URL and press Enter to navigate to a new page.

You can run this code by saving it to a file with a .py extension and running it using python.

You can further customize the appearance and functionality of the browser by modifying the code.




##How to use this app

###Go to the app directory 
cd /yourappdirectory

###Execute this code
python web-browser.py



