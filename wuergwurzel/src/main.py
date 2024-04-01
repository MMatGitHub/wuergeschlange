import common.log.protokolliere as protokolliere


def main():
    protokolliere.als().info('Betrete main()')
    protokolliere.als().info('Verlasse main()')
    # raise NameError('HiThere')
    raise Exception("test")


try:
    main()

except Exception as e:
    protokolliere.ok("Schöne Ausnahme: " + str(e))


