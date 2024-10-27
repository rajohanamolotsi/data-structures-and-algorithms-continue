from linkedlist import Linkedlist

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_at(1, "blueberry")
    ll.print()
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.print()
    ll.insert_at_end(67)
    ll.print()
    ll.print_backwards()