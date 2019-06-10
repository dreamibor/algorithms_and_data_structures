def hash_function(key_str, size):
    return sum([ord(i) for i in key_str]) % size

class HashTable():
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self._keys = []
        self.data = [[] for _ in range(capacity)]

    def get(self, key):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.data[index]
        for item in hash_table_cell:
            if item[0] == key:
                return item[1]
                break
        else:
            raise ValueError("Key Not Found!")

    def set(self, key, value):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.data[index]
        for item in hash_table_cell:
            if item[0] == key:
                item[1] = value
                break
        else:
            hash_table_cell.append([key, value])
            self.size += 1
            self._keys.append(key)

    def __setitem__(self, key, value):
        self.set(key, value)
    def __getitem__(self, key):
        return self.get(key)

my_dict = HashTable()
my_dict["def"] = 34
my_dict["sa"] = 45
print(my_dict["sa"])
# my_dict["cd"]

def char_count(string):
    char_list = [0] * 26
    for i in string:
        char_list[ord(i) - ord('a')] += 1
    return char_list

def get_delta(char_list_1, char_list_2):
    delta = 0
    for i in range(0, 26):
        delta += abs(char_list_1[i] - char_list_2[i])
    return delta

def anagram_problem(string_one, string_two):
    string_one_count = char_count(string_one)
    string_two_count = char_count(string_two)
    return get_delta(string_two_count, string_one_count)

print(anagram_problem('hello', 'billion'))