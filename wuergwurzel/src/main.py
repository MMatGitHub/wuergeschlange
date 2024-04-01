from .common.log import protokolliere as protokolliere


def main():
    print("i: main()")
    call(test_highorderfunction)
    # raise NameError('HiThere')
    # raise Exception("test")

def call(func_to_be_called):
    protokolliere.als().info('Betrete main()')
    func_to_be_called()
    protokolliere.als().info('Verlasse main()')

def test_highorderfunction():
    print('i: Hi order')

if __name__ == "__main__":
    try:
        print("i: ok ...geht los mit main.main()")
        main()

    except Exception as e:
        protokolliere.ok("Schöne Ausnahme: " + str(e))


