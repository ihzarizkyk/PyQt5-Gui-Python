from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Atas'))
layout.addWidget(QPushButton('Bawah'))
window.setLayout(layout)
window.show()
app.exec_()