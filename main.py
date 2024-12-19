import sys

from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QDialog, QApplication, QLabel

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.ui.pushButton.clicked.connect(self.play_song)

        layout = self.ui.horizontalLayout
        self.animation = QLabel(self)
        self.animation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.animation.hide()
        layout.addWidget(self.animation)

    def play_song(self):
        self.ui.pushButton.deleteLater()
        song_path= 'Wham! - Last Christmas (Official Video).mp3'
        self.media_player.setSource(QUrl.fromLocalFile(song_path))
        self.media_player.play()
        movie = QMovie('pies.gif')
        self.animation.setMovie(movie)
        self.animation.show()
        movie.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())