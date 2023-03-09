import csv
import random
import numpy
from datetime import date
from datetime import datetime

#region classes
#üst sınıflar olan pizza ve decorator ve alt sınıflarını fiyatlariyla belirliyoruz
class pizza:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost
    def title(self):
       return self.component.title() + \
         pizza.title(self)
    def cost(self):
       return self.component.cost() + \
         ' ' + pizza.cost(self)
    def show(self):
        print(pizza.title, pizza.cost)

klasik = pizza("Klasik Pizza", 20)
margarita = pizza("Margarita Pizza", 18)
sade = pizza("Sade Pizza", 15)
turk = pizza("Turk Pizza", 22)

class decorator:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost
    def cost(self):
       return self.component.cost() + \
         pizza.cost(self)


    def title(self):
       return self.component.title() + \
         ' ' + pizza.title(self)
    
zeytin = decorator("Zeytin", 3)
mantar = decorator("Mantar", 5)
kecipeyniri = decorator("Keci Peyniri", 6)
meat = decorator("Et", 10)
sogan = decorator("Sogan", 4)
misir = decorator("Misir", 4)



#endregion

#region Generating a random Order ID when starting a new order
#her bir siparis icin siparis kimligi olusturan fonk karismasin diye
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region main
#menu.txt yazdirip kullanicidan secimleri yapmasini istiyoruz
f = open('menu.txt', 'r')
file_contents = f.read()
print (file_contents)
f.close()
x = input('pizza tabani seciniz (menude yazdigi seklinde yaziniz)')
y = eval(x)
print('Fiyati: ' + str(y.cost))

toppingnumber = input('Kac tane malzeme olacak?(en az 1 seciniz)')

z = [str(z) for z in input("Birer boslukla malzemeleri yazın: ").split()]

#z strsi toppinglerimizin liste seklinde alindigi bir list
#asagidaki ile split ediyoruz
split_items = numpy.array_split(z, int(toppingnumber))
order_total1 = 0
#asagıda splitted seklinde yazdırıyoruz
# splitted olan listeleri önce strye sonra eval ile objeye ceviricez 
for array in split_items:
    #print(list(array)) 
    string = ''.join(list(array)) 
    b = eval(string)  
    print(str(b.title) + '....' + str(b.cost))
    order_total1 += b.cost
order_total = order_total1 + y.cost
print('Toplam ....' + str(order_total) + '$')


class user:
    def __init__(self, name, surname, tc, kkno, cvv):
        self.name = name
        self.tc = tc
        self.kkno = kkno
        self.cvv = cvv
name =  input('Isminiz?: ')
tc = int(input('TC kimlik no?: '))
kkno = int(input('Kredi karti numaraniz?: '))
cvv = int(input('cvv?: '))

 #endregion   

#region dosyaya yazdırma
#siparis verilen tarihleri kaydediyoruz
order_day = date.today()
order_time = datetime.now()
with open("orders_database.csv", 'a') as file:
        file.write("________________________________________________________")
        file.write("\n")
        file.write(ORDER_ID())
        file.write("\n")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        file.write(y.title)
        file.write("\n\n")
        file.write("Toppings: \n")
        for item in z:
            file.write(item + "\n")
        file.write("\n\n")
        file.write("TOTAL: " + str(order_total))
        file.write("\n\n")
        file.write("NAME: " + name)
        file.write("\n\n")
        file.write("TC: " + str(tc))
        file.write("\n\n")
        file.write("CREDIT CARD NO: " + str(kkno))
        file.write("\n\n")
        file.write("CVV: " + str(cvv))
        file.write("\n")
        file.write("________________________________________________________")

#endregion