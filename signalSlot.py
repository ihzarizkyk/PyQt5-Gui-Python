'''
Author : Mochammad Ihza Rizky Karim
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

# buat class contoh 
class contoh(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

# move() berfungsi untuk mengatur tata letak tombol
		button1 = QPushButton("Tombol 1",self)
		button1.move(50,40)

		button2 = QPushButton("Tombol 2",self)
		button2.move(50,100)

# fungsi connect untuk menghubungkan button dengan fungsi button clicked
		button1.clicked.connect(self.buttonClicked)
		button2.clicked.connect(self.buttonClicked)

		self.statusBar()
		self.setGeometry(300, 300, 450, 350)
		self.setWindowTitle("PYQT5 SIGNAL-SLOT(EVENT)")
		self.show()
	'''
	buat fungsi buttonClicked(self) yang berfungsi untuk memberikan 
	pemberitahuan ketika tombol diklik dan akan mengirimkan teks dibawah

	-fungsi showMessage() untuk menampilkan status atau pesan ketika teks diklik
	-fungsi sender untuk mengirimkan respon klik
	'''
	def buttonClicked(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text() + " Telah diklik ")

# fungsi main() untuk menampilkan GUI aplikasi beserta fungsi contoh
def main():
	app = QApplication(sys.argv)
	ex = contoh()
	sys.exit(app.exec_())

if(__name__ == "__main__"):
	main()
