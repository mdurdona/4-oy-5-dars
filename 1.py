# --------------------------UYGA VAZIFA 5 ----------------
# -----------MISOL- 1 ------
# import random
# from PyQt5.QtWidgets import ( 
#     QApplication, QWidget  , QLabel, QPushButton
# )
# app = QApplication([])

# oyna = QWidget()
# oyna.setWindowTitle("No 1")
# oyna.setGeometry(1350,200,500,700)
# oyna.setStyleSheet("background-color: white;")

# label1 = QLabel(oyna)
# label1.setText("0")
# label1.setStyleSheet("font-size:100px;")
# label1.setGeometry(200,150,200,180)

# def random_son():
#     a = random.randint(1,100) 
#     label1.setText(str(a))

# botton = QPushButton(oyna)
# botton.setText("Start")
# botton.setStyleSheet("font-size:70px;")
# botton.move(200,300)
# botton.clicked.connect(random_son)

# oyna.show()
# app.exec_()

# -----------MISOL- 2 ------
# from PyQt5.QtWidgets import(
#     QApplication,QWidget,QLabel,QPushButton
# )
# app = QApplication([])

# bottoms_style   = """
#     background-color: #ffffff;
#     color: #5b229c;
#     font-size:20px;
#     border-radius:20px;
#     border: 4px solid yellow;
# """

# oyna = QWidget()
# oyna.setWindowTitle("No 2")
# oyna.setGeometry(1000,200,500,700)
# oyna.setStyleSheet("background-color:#5b229c;")

# label1 = QLabel(oyna)
# label1.setText("Hello")
# label1.setGeometry(100,150,300,100)
# label1.setStyleSheet("font-size: 50px;color: white;  border: 5px solid yellow;")

# def ism():
#     label1.setText("Durdona")

# def familiya():
#     label1.setText("Meliyeva")

# def sana():
#     label1.setText("13.06.2005")

# botton1 = QPushButton(oyna)
# botton1.setText("Ism")
# botton1.clicked.connect(ism)
# botton1.setGeometry(150,300,200,60)
# botton1.setStyleSheet(bottoms_style)


# botton2 = QPushButton(oyna)
# botton2.setText("Familiya")
# botton2.clicked.connect(familiya)
# botton2.setGeometry(150,380,200,60)
# botton2.setStyleSheet(bottoms_style)

# botton3 = QPushButton(oyna)
# botton3.setText("Tug`ilgan sana")
# botton3.clicked.connect(sana)
# botton3.setGeometry(150,460,200,60) 
# botton3.setStyleSheet(bottoms_style)

# oyna.show()
# app.exec_()


# -----------MISOL- 3 ------
# from PyQt5.QtWidgets import(
#     QApplication , QWidget , QLabel , QPushButton , QLineEdit

# )
# app = QApplication([])
# line_style = """
#     font-size:20px;
#     background-color: white;
#     border: 3px solid black;

# """

# oyna = QWidget()
# oyna.setGeometry(1000,200,600,700)
# oyna.setWindowTitle("No 3")

# line1 = QLineEdit(oyna)
# line1.setStyleSheet(line_style)
# line1.setGeometry(200,150, 200, 50)
# line1.setPlaceholderText("Son kiriting:")

# line2 = QLineEdit(oyna)
# line2.setStyleSheet(line_style)
# line2.setGeometry(200,230, 200, 50)
# line2.setPlaceholderText("Son kiriting:")

# label = QLabel(oyna)
# label.setGeometry(200,300,300,50)
# label.setStyleSheet("font-size: 25px; color: blue;")


# def qushish():
#     try:
#         s1 = float(line1.text())
#         s2 = float(line2.text())
#         c= s1 + s2
#         label.setText("Natija: "+ str(c))
#     except:
#         label.setText("Xato ! Son kiriting ")    

# def ayirish():
#     try:
#         s1 = float(line1.text())
#         s2 = float(line2.text())
#         c= s1 - s2
#         label.setText("Natija: "+ str(c))
#     except:
#         label.setText("Xato ! Son kiriting ")  

# def kupaytirish():
#     try:
#         s1 = float(line1.text())
#         s2 = float(line2.text())
#         c= s1 * s2
#         label.setText("Natija: "+ str(c))
#     except:
#         label.setText("Xato ! Son kiriting ")      

# def bulish():
#     try:
#         s1 = float(line1.text())
#         s2 = float(line2.text())
#         c= s1 / s2
#         label.setText("Natija: "+ str(c))
#     except:
#         label.setText("Xato ! Son kiriting ")          


# b1 = QPushButton(oyna)
# b1.setText("Qo'shish:")
# b1.setGeometry(200,380,200,50)
# b1.clicked.connect(qushish)

# b2 = QPushButton(oyna)
# b2.setText("Ayirish:")
# b2.setGeometry(200,440,200,50)
# b2.clicked.connect(ayirish)


# b3 = QPushButton(oyna)
# b3.setText("Ko'paytirish:")
# b3.setGeometry(200,500,200,50)
# b3.clicked.connect(kupaytirish)


# b4 = QPushButton(oyna)
# b4.setText("Bo'lish:")
# b4.setGeometry(200,560,200,50)
# b4.clicked.connect(bulish)


# oyna.show()
# app.exec_()

# -----------MISOL- 4 ------
# import random
# from PyQt5.QtWidgets import(
#     QApplication,QWidget,QLabel,QPushButton
# )
# app = QApplication([])
# bottoms_style   = """
#     background-color: #ffffff;
#     color: black;
#     font-size:20px;
#     border-radius:20px;
#     border: 4px solid yellow;

# """
# label_style = """
#     color: black;
#     font-size:20px;
#     border-radius:20px;
#     border: 4px solid black;

# """
# oyna = QWidget()
# oyna.setGeometry(1000,200,600,700)
# oyna.setWindowTitle("No 4")


# label = QLabel(oyna)
# label.setGeometry(200,150, 200, 50)
# label.setText("Hello")
# label.setStyleSheet(label_style)

# ranglar = ["red", "blue", "green", "yellow"]
# def rang():
#     new = random.choice(ranglar)
#     label.setStyleSheet(f"color: {new} ; font-size:20px; border-radius:20px; border: 4px solid black ;")
    

# button = QPushButton(oyna)
# button.setText("Start")
# button.setGeometry(200,230, 200, 50)
# button.setStyleSheet(bottoms_style)
# button.clicked.connect(rang)


# oyna.show()
# app.exec_()

# -----------MISOL- 5 ------

# from PyQt5.QtWidgets import (
#     QApplication,QWidget,QLabel,QLineEdit,QPushButton
# )
# app = QApplication([])

# oyna = QWidget()
# oyna.setGeometry(1000,200,500,400)
# oyna.setWindowTitle("No 5")


# line = QLineEdit(oyna)
# line.setGeometry(150,50,200,40)
# line.setPlaceholderText("Parol kiriting")


# label = QLabel(oyna)
# label.setText("...")
# label.setGeometry(150,120,300,40)
# label.setStyleSheet("font-size:18px; color: green;")


# def tekshir():
#     if line.text() == "12345":
#         label.setText("Parol to'g'ri")
#     else:
#         label.setText("Noto'g'ri parol")

# button = QPushButton( oyna)
# button.setText("Tekshir")
# button.setGeometry(150,180,200,40)
# button.clicked.connect(tekshir)        

# oyna.show()
# app.exec_()

# -----------MISOL- 6 ------

# from PyQt5.QtWidgets import (
#     QApplication,QWidget,QLabel,QPushButton
# )
# app = QApplication([])

# oyna = QWidget()
# oyna.setGeometry(1000,200,500,400)
# oyna.setWindowTitle("No 6")

# qiymat = 0

# label = QLabel(str(qiymat), oyna)
# label.setGeometry(180,50,100,50)
# label.setStyleSheet("font-size:30px; color: black; border: 2px solid blue;")


# def plus():
#     global qiymat
#     qiymat += 1
#     label.setText(str(qiymat))

# def minus():
#     global qiymat
#     qiymat -= 1
#     label.setText(str(qiymat))

# b_plus = QPushButton("+1", oyna)
# b_plus.setGeometry(100,150,80,50)
# b_plus.clicked.connect(plus)

# b_minus = QPushButton("-1", oyna)
# b_minus.setGeometry(220,150,80,50)
# b_minus.clicked.connect(minus)

# oyna.show()
# app.exec_()