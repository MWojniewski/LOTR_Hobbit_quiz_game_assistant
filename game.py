import sys
import csv
import os

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QGraphicsOpacityEffect,
)

from PyQt6.QtGui import QPixmap, QShortcut, QKeySequence, QFont, QFontDatabase, QCursor
from PyQt6.QtCore import Qt, QPropertyAnimation
import random


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def endapp():
    sys.exit()


def choose_action_with_esc():
    if window.current_screen_number == window.starting_screen_number:
        endapp()
    elif window.current_screen_number == window.question_screen_number:
        window.set_all_categories_layout()


def choose_action_with_space():
    if window.current_screen_number == window.question_screen_number:
        window.switch_choice()
    else:
        pass


def do_nothing():
    pass


def move_to_question_screen(color_number, category_number):
    if window.current_screen_number == window.all_categories_screen_number:
        window.set_question_layout(color_number, category_number)


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.choice = "Q"
        self.photo = QLabel()
        self.photo.setPixmap(QPixmap(resource_path("images/background1.jpg")))
        self.photo.setScaledContents(True)
        self.setCentralWidget(self.photo)
        self.set_cursors()
        self.upload_font()
        self.init_layouts()
        self.photo.setLayout(self.main_layout)

        self.starting_screen_number = 0
        self.all_categories_screen_number = 1
        self.question_screen_number = 2
        self.current_screen_number = 0

        self.current_question_number = 0
        self.question_indexes = []
        self.films_indexes = 0

        self.init_shortcuts()

    def change_img(self, img_index):
        self.current_screen_number = img_index
        self.main_layout.setCurrentIndex(img_index)
        self.photo.setPixmap(QPixmap(resource_path("images/background2.jpg")))
        self.photo.setScaledContents(True)
        window.showFullScreen()

    def init_shortcuts(self):
        self.escape = QShortcut(QKeySequence("Esc"), self)
        self.escape.activated.connect(choose_action_with_esc)
        self.Key_Space = QShortcut(QKeySequence("Space"), self)
        self.Key_Space.activated.connect(choose_action_with_space)

        self.category1_shortcut = QShortcut(QKeySequence("1"), self)
        self.category1_shortcut.activated.connect(
            lambda: move_to_question_screen("A10CA1", 1)
        )
        self.category2_shortcut = QShortcut(QKeySequence("2"), self)
        self.category2_shortcut.activated.connect(
            lambda: move_to_question_screen("05A1D1", 2)
        )
        self.category3_shortcut = QShortcut(QKeySequence("3"), self)
        self.category3_shortcut.activated.connect(
            lambda: move_to_question_screen("D10578", 3)
        )
        self.category4_shortcut = QShortcut(QKeySequence("4"), self)
        self.category4_shortcut.activated.connect(
            lambda: move_to_question_screen("E26B03", 4)
        )
        self.category5_shortcut = QShortcut(QKeySequence("5"), self)
        self.category5_shortcut.activated.connect(
            lambda: move_to_question_screen("E2D408", 5)
        )
        self.category6_shortcut = QShortcut(QKeySequence("6"), self)
        self.category6_shortcut.activated.connect(
            lambda: move_to_question_screen("21C61B", 6)
        )

        # useless
        self.Key_Up = QShortcut(QKeySequence("Up"), self)
        self.Key_Up.activated.connect(do_nothing)
        self.Key_Right = QShortcut(QKeySequence("Right"), self)
        self.Key_Right.activated.connect(do_nothing)
        self.Key_Down = QShortcut(QKeySequence("Down"), self)
        self.Key_Down.activated.connect(do_nothing)
        self.Key_Left = QShortcut(QKeySequence("Left"), self)
        self.Key_Left.activated.connect(do_nothing)
        self.Key_Tab = QShortcut(QKeySequence("Tab"), self)
        self.Key_Tab.activated.connect(do_nothing)

    def init_layouts(self):
        self.main_layout = QStackedLayout()

        self.starting_layout = QVBoxLayout()
        self.starting_widget = QWidget()
        self.starting_widget.setLayout(self.starting_layout)
        self.main_layout.addWidget(self.starting_widget)
        self.init_starting_layout()

        self.all_categories_layout = QGridLayout()
        self.all_categories_widget = QWidget()
        self.all_categories_widget.setLayout(self.all_categories_layout)
        self.main_layout.addWidget(self.all_categories_widget)
        self.init_all_categories_layout()

        self.question_layout = QVBoxLayout()
        self.question_widget = QWidget()
        self.question_widget.setLayout(self.question_layout)
        self.main_layout.addWidget(self.question_widget)
        self.init_question_layout()

    def init_starting_layout(self):

        self.new_title_img = QLabel()
        self.new_title_img.setText("")
        self.new_title_img.setPixmap(QPixmap(resource_path("images/title.png")))
        self.new_title_img.setFixedWidth(1100)
        self.new_title_img.setScaledContents(True)

        self.start_button = QPushButton("Start", clicked=self.start_game)
        self.start_button.setCursor(QCursor(self.pointing_cursor_img))
        self.start_button.setFont(QFont(self.font_family[0], 30))
        self.start_button.setFixedSize(400, 70)
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(205, 206, 178, 150); 
                color: #FFC300; 
                border: 2px solid;
                border-color: #FFC300;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(205, 206, 178, 190); 
            }
            QPushButton:pressed {
                background-color: rgba(205, 206, 178, 220); 
            }
            """
        )

        self.quit_button1 = QPushButton("Wyjście", clicked=endapp)
        self.quit_button1.setCursor(QCursor(self.pointing_cursor_img))
        self.quit_button1.setFont(QFont(self.font_family[0], 30))
        self.quit_button1.setFixedSize(400, 70)
        self.quit_button1.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(205, 206, 178, 150); 
                color: #FFC300; 
                border: 2px solid;
                border-color: #FFC300;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(205, 206, 178, 190); 
            }
            QPushButton:pressed {
                background-color: rgba(205, 206, 178, 220); 
            }
            """
        )

        self.starting_layout.addSpacing(150)
        self.starting_layout.addWidget(
            self.new_title_img, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.starting_layout.addWidget(
            self.start_button, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.starting_layout.addWidget(
            self.quit_button1, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.starting_layout.addSpacing(150)

    def init_all_categories_layout(self):
        self.all_categories_layout.setVerticalSpacing(40)
        self.all_categories_layout.setHorizontalSpacing(150)

        self.category1_button = QPushButton("Drużyna Pierścienia")
        self.category1_button.clicked.connect(
            lambda: self.set_question_layout("A10CA1", 1)
        )
        self.category1_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category1_button.setFont(QFont(self.font_family[0], 20))
        self.category1_button.setFixedSize(400, 70)
        self.category1_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #A10CA1; 
                border: 4px solid;
                border-color: #A10CA1;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02;
                border: 7px solid;
                border-color: #A10CA1;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.category2_button = QPushButton("Dwie wieże")
        self.category2_button.clicked.connect(
            lambda: self.set_question_layout("05A1D1", 2)
        )
        self.category2_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category2_button.setFont(QFont(self.font_family[0], 20))
        self.category2_button.setFixedSize(400, 70)
        self.category2_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #05A1D1; 
                border: 4px solid;
                border-color: #05A1D1;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 7px solid;
                border-color: #05A1D1;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.category3_button = QPushButton("Powrót króla")
        self.category3_button.clicked.connect(
            lambda: self.set_question_layout("D10578", 3)
        )
        self.category3_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category3_button.setFont(QFont(self.font_family[0], 20))
        self.category3_button.setFixedSize(400, 70)
        self.category3_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #D10578; 
                border: 4px solid;
                border-color: #D10578;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 7px solid;
                border-color: #D10578;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.category4_button = QPushButton("Niezwykła podróż")
        self.category4_button.clicked.connect(
            lambda: self.set_question_layout("E26B03", 4)
        )
        self.category4_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category4_button.setFont(QFont(self.font_family[0], 20))
        self.category4_button.setFixedSize(400, 70)
        self.category4_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #E26B03; 
                border: 4px solid;
                border-color: #E26B03;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 7px solid;
                border-color: #E26B03;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.category5_button = QPushButton("Pustkowie Smauga")
        self.category5_button.clicked.connect(
            lambda: self.set_question_layout("E2D408", 5)
        )
        self.category5_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category5_button.setFont(QFont(self.font_family[0], 20))
        self.category5_button.setFixedSize(400, 70)
        self.category5_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #E2D408; 
                border: 4px solid;
                border-color: #E2D408;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02;
                border: 7px solid;
                border-color: #E2D408; 
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.category6_button = QPushButton("Bitwa Pięciu Armii")
        self.category6_button.clicked.connect(
            lambda: self.set_question_layout("21C61B", 6)
        )
        self.category6_button.setCursor(QCursor(self.pointing_cursor_img))
        self.category6_button.setFont(QFont(self.font_family[0], 20))
        self.category6_button.setFixedSize(400, 70)
        self.category6_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E;
                color: #21C61B; 
                border: 4px solid;
                border-color: #21C61B;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 7px solid;
                border-color: #21C61B; 
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.quit_button2 = QPushButton("Wyjście", clicked=endapp)
        self.quit_button2.setCursor(QCursor(self.pointing_cursor_img))
        self.quit_button2.setFont(QFont(self.font_family[0], 20))
        self.quit_button2.setFixedSize(300, 60)
        self.quit_button2.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E; 
                color: #797978; 
                border: 2px solid;
                border-color: #797978;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 4px solid;
                border-color: #797978;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.all_categories_layout.addWidget(
            self.category1_button, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.category2_button, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.category3_button, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.category4_button, 0, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.category5_button, 1, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.category6_button, 2, 2, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.all_categories_layout.addWidget(
            self.quit_button2, 3, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter
        )

    def init_question_layout(self):
        self.question_text = QLabel()
        self.question_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_text.setWordWrap(True)
        self.question_text.setFont(QFont(self.font_family[0], 25))
        self.question_text.setFixedSize(900, 300)

        self.get_back_button = QPushButton(
            "Powrót", clicked=self.set_all_categories_layout
        )
        self.get_back_button.setCursor(QCursor(self.pointing_cursor_img))
        self.get_back_button.setFont(QFont(self.font_family[0], 15))
        self.get_back_button.setFixedSize(200, 45)
        self.get_back_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2A2B0E; 
                color: #797978; 
                border: 2px solid;
                border-color: #797978;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1A1B02; 
                border: 4px solid;
                border-color: #797978;
            }
            QPushButton:pressed {
                background-color: #0F1001; 
            }
            """
        )

        self.change_text_type_button = QPushButton(clicked=self.switch_choice)
        self.change_text_type_button.setFont(QFont(self.font_family[0], 20))
        self.change_text_type_button.setFixedSize(400, 100)

        self.question_layout.addWidget(
            self.get_back_button, alignment=Qt.AlignmentFlag.AlignTop
        )
        self.question_layout.addWidget(
            self.question_text, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.question_layout.addWidget(
            self.change_text_type_button, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.question_layout.addSpacing(150)

    def init_questions(self):
        self.questions = [[], [], [], [], [], [], []]

        with open(
            resource_path("questions/lotr_q.csv"), newline="", encoding="utf-8"
        ) as question_file:
            reader = csv.DictReader(question_file)
            for row in reader:
                self.questions[int(row["Category"])].append(
                    {
                        "Q": row["Question"],
                        "A": row["Answer"],
                    }
                )

        with open(
            resource_path("questions/hobbit_q.csv"), newline="", encoding="utf-8"
        ) as question_file:
            reader = csv.DictReader(question_file)
            for row in reader:
                self.questions[int(row["Category"])].append(
                    {
                        "Q": row["Question"],
                        "A": row["Answer"],
                    }
                )

        for i in self.questions:
            self.question_indexes.append(-1)
            question_set = i
            random.shuffle(question_set)

    def prepare_question_or_answer(self):

        self.question_text.setStyleSheet(
            """
            QLabel {
                background-color: #1A1B02;
                color: #"""
            + self.text_color
            + """; 
                border: 2px solid;
                border-color: #"""
            + self.text_color
            + """;
                border-radius: 10px;
                padding: 10px;
            }
            """
        )

        self.change_text_type_button.setStyleSheet(
            """
            QPushButton {
                background-color: #1A1B02;
                color: #"""
            + self.text_color
            + """; 
                border: 2px solid;
                border-color: #"""
            + self.text_color
            + """;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0F1001;
                border: 2px solid;
                border-color: #"""
            + self.text_color
            + """;
            }
            QPushButton:pressed {
                border: 4px solid;
                border-color: #"""
            + self.text_color
            + """;
                background-color: #0B0001; 
            }
            """
        )

        if self.choice == "Q":
            self.question_text.setText(
                self.questions[self.current_question_number][
                    self.question_indexes[self.current_question_number]
                ]["Q"]
            )
            self.change_text_type_button.setText("Zobacz Odpowiedź")
        elif self.choice == "A":
            self.question_text.setText(
                self.questions[self.current_question_number][
                    self.question_indexes[self.current_question_number]
                ]["A"]
            )
            self.change_text_type_button.setText("Zobacz Pytanie")

    def set_cursors(self):
        self.normal_cursor_img = QPixmap(
            resource_path("cursors/normal_cursor.png")
        ).scaled(
            32,
            32,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.setCursor(QCursor(self.normal_cursor_img))
        self.pointing_cursor_img = QPixmap(
            resource_path("cursors/pointing_cursor.png")
        ).scaled(
            32,
            32,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def set_all_categories_layout(self):
        self.main_layout.setCurrentIndex(self.all_categories_screen_number)
        self.current_screen_number = self.all_categories_screen_number
        self.choice = "Q"

    def set_question_layout(self, text_color, category_number):
        if self.current_screen_number != self.question_screen_number:
            self.text_color = text_color
            self.main_layout.setCurrentIndex(self.question_screen_number)
            self.current_screen_number = self.question_screen_number
            self.current_question_number = category_number
            self.question_indexes[self.current_question_number] += 1
            if self.question_indexes[self.current_question_number] >= len(
                self.questions[self.current_question_number]
            ):
                self.question_indexes[self.current_question_number] = 0
                random.shuffle(self.questions[self.current_question_number])
        self.prepare_question_or_answer()
        self.start_animation()

    def set_selected_films(self, films_indexes):
        self.films_indexes = films_indexes

    def start_game(self):
        self.init_questions()
        self.change_img(self.all_categories_screen_number)

    def start_animation(self):
        self.opacity_effect = QGraphicsOpacityEffect()
        self.question_text.setGraphicsEffect(self.opacity_effect)

        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()

    def switch_choice(self):
        if self.choice == "Q":
            self.choice = "A"
        else:
            self.choice = "Q"
        self.prepare_question_or_answer()
        self.start_animation()

    def upload_font(self):
        self.font_id = QFontDatabase.addApplicationFont(
            resource_path("fonts/Beryliumbolditalic.ttf")
        )
        self.font_family = QFontDatabase.applicationFontFamilies(self.font_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.showFullScreen()
    window.show()
    sys.exit(app.exec())
