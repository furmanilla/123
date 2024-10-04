# оформление (в обучении таблицы стилей - необязательный материал, 
# можно оставить на ознакомление особо заинтересованными):

       



QSS = '''
QWidget{
    background-color: rgb(255, 254, 204)
}
QPushButton { 
    background-color: rgb(0, 255, 255); 
    border-width: 1px;
    border-radius: 10px;
    border-color: red;
    font: 11px "Courier New";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: jade;
    border-style: inset;
}
QGroupBox {
    color: gray;
    font: 14px;
    border-radius: 15px;
    border: 2px solid jade;
    margin-top: 2ex;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}

QRadioButton {
    font: bold 14px;
}
QRadioButton::indicator {
    width: 14px;
    height: 14px;
    border-radius: 7px;
}
QRadioButton::indicator::unchecked {
    border: 2px solid; 
    border-color: red;
    background-color: white;
    border-radius: 7px;
}

QRadioButton::indicator:unchecked:hover {
    border-color: red;
    background-color: white;
    border-radius: 7px;
}

QRadioButton::indicator::checked {
    border: 15px; 
    border-color: red;
    background-color: red;
    border-radius: 7px;
}

QLabel { 
    font: 11px "Montserrat";
}
'''

QSS_OK = '''
QPushButton { background-color: rgb(204, 229, 255); 
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 18px "Montserrat";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: gray;
    border-style: inset;
}
'''

QSS_TextCardQuestion = '''QLabel { 
    font: bold 26px "Courier New";
}'''

QSS_TextResult = '''QLabel {
    font: italic 22px "Courier New";
}'''

QSS_TextHeader = '''QLabel {
    font: 18px ;
}'''

QSS_menu = '''
QPushButton { background-color: rgb(204, 229, 255); 
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 18px "Courier New";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: gray;
    border-style: inset;
}'''

