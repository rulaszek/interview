def send_async(task):
    return task


def wait_on(tasks):
    return tasks

h = send_async("H")
d = send_async("D")
f = send_async("F")

wait_on([d, f])

g = send_async("G")
b = send_async("B")
c = send_async("C")

wait_on([b, c])

a = send_async("A")

wait_on([a])

e = send_async("E")

wait_on([e])

wait_on([h, g])

