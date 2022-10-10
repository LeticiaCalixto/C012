import threading

def razor():
    x = 0
    while x < 20:
        print("Razor Crest")
        x += 1
        if(x == 20):
            print("Razor Crest chegou!!!!")

def millennium():
    y = 0
    while y < 20:
        print("Millennium Falcon")
        y += 1
        if(y == 20):
            print("Millennium Falcon chegou!!!!")

def executor():
    z = 0
    while z < 20:
        print("Executor")
        z += 1
        if(z == 20):
            print("Executor chegou!!!!")

def onibus():
    m = 0
    while m < 20:
        print("Ônibus imperial")
        m += 1
        if(m == 20):
            print("Ônibus imperial chegou!!!!")

def slave():
    n = 0
    while n < 20:
        print("Slave I")
        n += 1
        if(n == 20):
            print("Slave I chegou!!!!")

threading.Thread(target=razor).start()
threading.Thread(target=millennium).start()
threading.Thread(target=executor).start()
threading.Thread(target=onibus).start()
threading.Thread(target=slave).start()