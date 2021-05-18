import requests
import clientui
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.temp=[]

        self.urls = {'btc': 'https://yobit.net/api/2/btc_usd/ticker',
                     'yo': 'https://yobit.net/api/2/yo_usd/ticker',
                     'ltc': 'https://yobit.net/api/2/ltc_usd/ticker',
                     'doge': 'https://yobit.net/api/2/doge_usd/ticker',
                     'dash': 'https://yobit.net/api/2/dash_usd/ticker', }
        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(partial(self.get_rate_usd, self.urls['btc']))
        #self.timer.start(1000)
        self.btc.pressed.connect(partial(self.get_rate_usd, self.urls['btc']))
        self.yo.pressed.connect(partial(self.get_rate_usd, self.urls['yo']))
        self.ltc.pressed.connect(partial(self.get_rate_usd, self.urls['ltc']))
        self.doge.pressed.connect(partial(self.get_rate_usd, self.urls['doge']))
        self.dash.pressed.connect(partial(self.get_rate_usd, self.urls['dash']))






    def get_rate_usd(self,url):
        try:
            self.temp = requests.get(url).json()
            self.text.clear()
            self.text.append(str(self.temp['ticker']['last']))
            self.text.repaint()
        except:
            self.text.clear()
            self.text.append("Ошибка соединения")
            self.text.repaint()
            return


app=QtWidgets.QApplication([])
window=MyWindow()
window.show()
app.exec_()