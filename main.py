import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("K_Mean Cluster App")
        self.setFixedSize(QSize(800, 500))

        spliter = QSplitter(Qt.Horizontal)

        # Left widget
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_label = QLabel("Left Panel")
        left_layout.addWidget(left_label)
        left_widget.setLayout(left_layout)

        # Right widget
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_label = QLabel("Right Panel")
        right_layout.addWidget(right_label)

        start_button = QPushButton("Start")
        right_layout.addWidget(start_button)
        
        right_widget.setLayout(right_layout)
        
        spliter.addWidget(left_widget)
        spliter.addWidget(right_widget)
        spliter.setSizes([500, 300])
        spliter.setHandleWidth(5)

        self.setCentralWidget(spliter)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()