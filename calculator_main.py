import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.number_ui = QLineEdit("")
        layout_equation_solution.addRow(self.number_ui)

        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 추가 연산 버튼 생성
        button_remainder = QPushButton("%")
        button_square= QPushButton("x^2")
        button_reciprocal = QPushButton("1/x")
        button_squareroot= QPushButton("√x")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 추가 연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "^2": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(lambda state, operation = "^(-1)": self.button_operation_clicked(operation))
        button_squareroot.clicked.connect(lambda state, operation = "√": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus, 4,3)
        layout_operation.addWidget(button_minus, 3,3)
        layout_operation.addWidget(button_product, 2,3)
        layout_operation.addWidget(button_division, 1,3)

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_remainder, 0,0)
        layout_operation.addWidget(button_square, 1,1)
        layout_operation.addWidget(button_reciprocal, 1,0)
        layout_operation.addWidget(button_squareroot, 1,2)

        ### =, C/CE(clear), backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("CE")
        button_backspace = QPushButton("Backspace")
        button_C = QPushButton("C")

        ### =, C/CE(clear), backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)
        button_C.clicked.connect(self.button_C_clicked)

        ### =, C/CE(clear), backspace 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_clear, 0,1)
        layout_operation.addWidget(button_backspace, 0,3)
        layout_operation.addWidget(button_equal, 5,3)
        layout_operation.addWidget(button_C, 0,2)

        ### 숫자 버튼 생성하고, layout_operation 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_operation.addWidget(number_button_dict[number], x, y,4,1)
            elif number==0:
                layout_operation.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_operation.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_operation.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.number_ui.text()
        equation += str(num)
        self.number_ui.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.number_ui.text()
        equation += operation
        self.number_ui.setText(equation)

    def button_C_clicked(self):
        self.number_ui.setText("")
        self.number_ui.setText("")

    def button_equal_clicked(self):
        equation = self.number_ui.text()
        solution = eval(equation)
        self.number_ui.setText(str(solution))

    def button_clear_clicked(self):
        self.number_ui.setText("")
        self.number_ui.setText("")

    def button_backspace_clicked(self):
        equation = self.number_ui.text()
        equation = equation[:-1]
        self.number_ui.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
