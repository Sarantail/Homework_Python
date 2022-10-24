import menu
import jf
import add_key as ak
import print_base


def data_comm():
    data = jf.read_file()
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            print_base.get_выводить_базу(data)
        elif what == 2:
            ak.get_add_key(data)
        else:
            jf.write_in_file(data)
            exit = False
