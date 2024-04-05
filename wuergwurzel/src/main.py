from common.log import protokolliere as protokolliere
from common.parallel import multiPool as pool

def start():
    print("i: Starting start() ...")
    hi(test_highorderfunction)
    #hi(pool.demo_multi_processing)

def hi(func_to_be_called):
    protokolliere.als().info('Betrete '+str(func_to_be_called))
    func_to_be_called()
    protokolliere.als().info('Verlasse '+str(func_to_be_called))

def test_highorderfunction():
    print('i: Hi order!')

if __name__ == "__main__":
    try:
        print("i: ok ...geht los mit main.main()")
        start()

    except Exception as e:
        protokolliere.ok("Schöne Ausnahme: " + str(e))