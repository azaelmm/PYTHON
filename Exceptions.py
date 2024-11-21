numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
except TypeError:
    print("FATAL ERROR")
except TimeoutError:
    print("que hicistes¿?")
except Exception as error: 
    print(error)
else:
    print("se ejecuto correctamente la orden.")
finally:
    print("Chao")