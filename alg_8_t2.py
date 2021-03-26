from collections import Counter, deque


class HuffmanCoding:
    def __init__(self, str_obj):
        self.str_obj = str_obj
        self.character_code = dict()

    def getting_frequencies(self):
        cnt = Counter(self.str_obj)
        return deque(sorted(cnt.items(), key=lambda el: el[1]))

    def binary_tree(self):
        res_tree = HuffmanCoding.getting_frequencies(self)
        for _ in range(len(res_tree) - 1):
            sum_frequency = res_tree[0][1] + res_tree[1][1]
            res = {0: res_tree.popleft()[0],
                   1: res_tree.popleft()[0]}
            for i, cnt in enumerate(res_tree):
                if sum_frequency > cnt[1]:
                    continue
                else:
                    res_tree.insert(i, (res, sum_frequency))
                    break
            else:
                res_tree.append((res, sum_frequency))
        return res_tree[0][0]

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.character_code[tree] = path
        else:
            HuffmanCoding.haffman_code(self, tree[0], path=f'{path}0')
            HuffmanCoding.haffman_code(self, tree[1], path=f'{path}1')
        return self.character_code

    def result_str(self, table_dict):
        res = ''
        for el in self.str_obj:
            res += table_dict[el] + ' '
        return res


s = 'beep boop beer!'
HC = HuffmanCoding(s)
table = HC.haffman_code(HC.binary_tree())
print(HC.result_str(table))
