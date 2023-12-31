def repl(string: str):
    x = string.split()
    x = list(map(int, x))
    if len(x) > 2:
        ans = []
        d = []
        for i in x:
            d.append(i)
            if len(d) >= 2:
                ans.append(d)
                d = []
        return ans
    else:
        return [x]


class Melodis:
    """ piano 0 = first
        piano 1 = greate \n

        ПРИМЕР
        [[0, 16], [1, 14]] - это 2 аккорда: Номер 16 на первой клавиатуре и 14 на второй клавиатуре.\n
        [-1] - это пауза (кривая)
    """
    mario_list = [
        [[1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],
        [[0, 12], [1, 14]],
        [[0, 16], [1, 14]],
        [[1, 14]],

        [[0, 19], [1, 19]],
        [[1, 19]],
        [[1, 19]],
        [[1, 19]],

        [[1, 7]],
        [[1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 4], [1, 12]],
        [[1, 12]],

        [[1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],
        [[0, 11], [1, 5]],
        [[1, 5]],
        [[0, 10], [1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],

        [[0, 7], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],
        [[0, 19], [1, 12]],

        [[0, 21], [1, 5]],
        [[1, 5]],
        [[0, 17], [1, 5]],
        [[0, 19], [1, 5]],

        [[1, 12]],
        [[0, 16], [1, 12]],
        [[1, 12]],
        [[0, 12], [1, 12]],

        [[0, 14], [1, 7]],
        [[0, 11], [1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[0, 4], [1, 12]],
        [[1, 12]],

        [[1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],
        [[0, 11], [1, 5]],
        [[1, 5]],
        [[0, 10], [1, 5]],
        [[0, 9], [1, 5]],
        [[1, 5]],

        [[0, 7], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],
        [[0, 19], [1, 12]],

        [[0, 21], [1, 5]],
        [[1, 5]],
        [[0, 17], [1, 5]],
        [[0, 19], [1, 5]],

        [[1, 12]],
        [[0, 16], [1, 12]],
        [[1, 12]],
        [[0, 12], [1, 12]],

        [[0, 14], [1, 7]],
        [[0, 11], [1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[0, 24], [1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[1, 5]],
        [[1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 8]],
        [[1, 8]],
        [[0, 15], [1, 8]],
        [[1, 8]],

        [[1, 10]],
        [[0, 14], [1, 10]],
        [[1, 10]],
        [[1, 10]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[0, 24], [1, 5]],
        [[0, 24], [1, 5]],
        [[1, 5]],
        [[1, 5]],
        [[1, 5]],

        [[1, 12]],
        [[1, 12]],
        [[0, 19], [1, 12]],
        [[0, 18], [1, 12]],
        [[0, 17], [1, 12]],
        [[0, 15], [1, 12]],
        [[1, 12]],
        [[0, 16], [1, 12]],

        [[1, 5]],
        [[0, 8], [1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[1, 5]],
        [[0, 9], [1, 5]],
        [[0, 12], [1, 5]],
        [[0, 14], [1, 5]],

        [[1, 8]],
        [[1, 8]],
        [[0, 15], [1, 8]],
        [[1, 8]],

        [[1, 10]],
        [[0, 14], [1, 10]],
        [[1, 10]],
        [[1, 10]],

        [[0, 12], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[0, 12], [1, 12]],
        [[1, 12]],
        [[0, 9], [1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 12], [1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],
        [[1, 8]],
        [[0, 12], [1, 8]],

        [[0, 14], [1, 10]],
        [[1, 10]],

        [[0, 16], [1, 12]],
        [[0, 12], [1, 12]],
        [[1, 12]],
        [[0, 9], [1, 12]],
        [[0, 7], [1, 12]],
        [[1, 12]],
        [[1, 12]],
        [[1, 12]],

        [[0, 14], [1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],
        [[0, 12], [1, 14]],
        [[0, 14], [1, 14]],
        [[1, 14]],

        [[0, 19], [1, 7]],
        [[1, 7]],
        [[1, 7]],
        [[1, 7]],

        [[1, 19]],
        [[1, 19]],
        [[1, 19]],
        [[1, 19]],
    ]

    rammstein_list = [
        [[0, 29]],
        [[0, 31]],
        [[0, 19]],
        [[0, 7]],
        [[0, 14]],
        [[0, 19]],
        [[0, 12]],
        [[0, 33]],
        [[0, 34]],
        [[0, 22]],
        [[0, 10]],
        [[0, 17]],
        [[0, 22]],
        [[0, 17]],
        [[1, 2]],
        [[0, 21]],
        [[0, 26]],
        [[0, 21]],
        [[0, 33]],
        [[0, 16]],
        [[0, 21]],
        [[0, 16]],
        [[0, 34]],
        [[0, 33]],
        [[0, 31]],
        [[0, 29]],
        [[0, 31]],
        [[0, 14]],
        [[0, 19]],
        [[0, 14]],
    ]

    new_list = []
    with open('new_melody.txt', "r") as f:
        text = f.read()
    new_list = [text.split('\n')][0]
    while '' in new_list:
        new_list.remove('')
    new_list = list(map(repl, new_list))


    def __init__(self):
        self.lists = [Melodis.mario_list, Melodis.rammstein_list, Melodis.new_list]
        self.this_list = Melodis.mario_list

    def change_song(self):
        self.this_list = self.lists[(self.lists.index(self.this_list) + 1) % len(self.lists)]
