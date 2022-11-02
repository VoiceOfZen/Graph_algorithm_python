class Graph(object):
    def __init__(self, B, one, two, three,
                 four, five, six, seven,
                 eight, nine, ten, nodes_dict):
        self.B = B
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.nodes_dict = nodes_dict


Graph.B = ['B', 'Not processed', 'Not final']
Graph.one = ['1', 'Not processed', 'Not final']
Graph.two = ['2', 'Not processed', 'Not final']
Graph.three = ['3', 'Not processed', 'Not final']
Graph.four = ['4', 'Not processed', 'Not final']
Graph.five = ['5', 'Not processed', 'Not final']
Graph.six = ['6', 'Not processed', 'Not final']
Graph.seven = ['7', 'Not processed', 'Not final']
Graph.eight = ['8', 'Not processed', 'Not final']
Graph.nine = ['9', 'Not processed', 'Not final']
Graph.ten = ['10', 'Not processed', 'Not final']

Graph.B.append([Graph.one[0], 35])
Graph.B.append([Graph.two[0], 20])
Graph.B.append([Graph.three[0], 20])
Graph.B.append([Graph.four[0], 30])

Graph.one.append([Graph.seven[0], 70])
Graph.one.append([Graph.B[0], 35])
Graph.one.append([Graph.two[0], 20])

Graph.two.append([Graph.one[0], 20])
Graph.two.append([Graph.B[0], 20])
Graph.two.append([Graph.three[0], 10])
Graph.two.append([Graph.five[0], 40])

Graph.three.append([Graph.B[0], 20])
Graph.three.append([Graph.six[0], 30])
Graph.three.append([Graph.eight[0], 60])
Graph.three.append([Graph.five[0], 35])
Graph.three.append([Graph.two[0], 10])

Graph.four.append([Graph.B[0], 30])
Graph.four.append([Graph.ten[0], 40])
Graph.four.append([Graph.nine[0], 60])
Graph.four.append([Graph.six[0], 40])

Graph.five.append([Graph.two[0], 40])
Graph.five.append([Graph.three[0], 35])
Graph.five.append([Graph.eight[0], 30])
Graph.five.append([Graph.seven[0], 70])

Graph.six.append([Graph.three[0], 30])
Graph.six.append([Graph.four[0], 40])
Graph.six.append([Graph.nine[0], 40])
Graph.six.append([Graph.eight[0], 50])

Graph.seven.append([Graph.one[0], 70])
Graph.seven.append([Graph.five[0], 70])
Graph.seven.append([Graph.eight[0], 20])

Graph.eight.append([Graph.seven[0], 20])
Graph.eight.append([Graph.five[0], 30])
Graph.eight.append([Graph.three[0], 60])
Graph.eight.append([Graph.six[0], 50])
Graph.eight.append([Graph.nine[0], 10])

Graph.nine.append([Graph.eight[0], 10])
Graph.nine.append([Graph.six[0], 40])
Graph.nine.append([Graph.four[0], 60])
Graph.nine.append([Graph.ten[0], 15])

Graph.ten.append([Graph.nine[0], 15])
Graph.ten.append([Graph.four[0], 40])

Graph.nodes_dict = {'B': 'B', 'one': '1', 'two': '2',
                    'three': '3', 'four': '4',
                    'five': '5', 'six': '6',
                    'seven': '7', 'eight': '8',
                    'nine': '9', 'ten': '10'}


def init_first_node(first_node):
    print(first_node)
    print(len(first_node))

    first_node[1] = [0, 'S']
    first_node[2] = 'Final'

    find_shortest_way(first_node)


def find_shortest_way(first_node):
    count = 3
    for n in first_node[3:]:
        for k, v in Graph.nodes_dict.items():
            if v == n[0]:
                getattr(Graph, k)[1] = [first_node[count][1] + first_node[1][0], first_node[0]]
                print('node neighbour: ', getattr(Graph, k))
        count += 1


init_first_node(Graph.B)

print('\n', Graph.B)
