from socket import *


def encode(s: str):
    table = [['A', 'B', 'C', 'D', 'E'],
             ['F', 'G', 'H', 'I', 'K'],
             ['L', 'M', 'N', 'O', 'P'],
             ['Q', 'R', 'S', 'T', 'U'],
             ['V', 'W', 'X', 'Y', 'Z']]

    s = s.replace('J', 'I')

    indexes_y = []
    indexes_x = []
    for c in s:
        for y in range(len(table)):
            for x in range(len(table[y])):
                if c == table[y][x]:
                    indexes_y.append(y)
                    indexes_x.append(x)

    indexes = indexes_x + indexes_y

    new_str = ""
    i = 0
    while i < len(indexes):
        new_str += table[indexes[i+1]][indexes[i]]
        i += 2

    return new_str


def decode(s: str):
    table = [['A', 'B', 'C', 'D', 'E'],
             ['F', 'G', 'H', 'I', 'K'],
             ['L', 'M', 'N', 'O', 'P'],
             ['Q', 'R', 'S', 'T', 'U'],
             ['V', 'W', 'X', 'Y', 'Z']]

    indexes = []
    for c in s:
        for y in range(len(table)):
            for x in range(len(table[y])):
                if c == table[y][x]:
                    indexes.append(x)
                    indexes.append(y)

    indexes_y = indexes[0: len(indexes) // 2]
    indexes_x = indexes[len(indexes) // 2: len(indexes)]

    new_str = ""
    for i in range(len(indexes_y)):
        new_str += table[indexes_x[i]][indexes_y[i]]

    return new_str

def send(s: socket, data: str):
    end_seq = "#"
    data += end_seq
    s.send(data.encode("utf-8"))


def get(s: socket):
    res_str = ""
    end_seq = "#"
    while(True):
        tmp_dt = s.recv(2048)
        tmp_str = tmp_dt.decode("utf-8")
        res_str += tmp_str
        if res_str.endswith(end_seq):
            return res_str[0:len(res_str)-len(end_seq)]


def main():
    server = socket()
    server.bind(('', 25565))
    server.listen(1024)
    print("Started")
    while(True):
        print("Accept")
        connection, address = server.accept()
        print("Accepted {0}".format(connection))

        data = get(connection)
        print(data)
        if data.endswith("+"):
            data = encode(data.replace('', '+'))

        if data.endswith("-"):
            data = decode(data.replace('', '-'))

        send(connection, data)

        connection.close()
        print("Disconnected")


main()