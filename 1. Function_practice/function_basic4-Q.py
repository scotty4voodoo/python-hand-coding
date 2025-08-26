letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

## Password generator 를 만들어보세요
## 조건 : 문자, 숫자, 특수문자를 원하는 수만큼 입력받습니다.
## 조건2: 입력받은 수만큼 위의 list 에서 각각 문자, 숫자, 특수문자를 선정하여 password 를 조합합니다.
## 조건3: 출력된 password 를 Shuffle 해보세요


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many LETTERs in password? \n"))
nr_symbols = int(input(f"How many SYMBOLs in password? \n"))
nr_numbers = int(input(f"How many NUMBERs in password?\n"))