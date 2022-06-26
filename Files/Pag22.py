line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
a=line.split(":")


# when unpacking an throwingaway some values using "_"

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record



items = [1, 10, 7, 4, 5, 9]
head, *tail = items


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
    sum(items)
    
    