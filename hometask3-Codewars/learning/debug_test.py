import logging
logging.basicConfig(level=logging.ERROR)  #opredelyaet, s kakogo urovnya pokazivat soobscheniya

def test(a, b):
    logging.info("Function enter")
    c = a + b
    logging.warning("Don't use name c with value={}".format(c))
    s = "Demo"
    logging.error("ERROR!")
    print(s)
    logging.info("Function exit")
    return c, s

class Test():
    def my(self):
        print("gui")

mmm = Test()
mmm.my()

if __name__ == "__main__":
    test(3, 5)
