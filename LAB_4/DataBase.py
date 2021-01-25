

class DataBase:
    def __init__(self):
        self.data_dict = {}
    
    def add_by_key(self, key, value):
        if key not in self.data_dict:
            self.data_dict[key] = value

    def remove_by_key(self, key):
        result = key in self.data_dict
        try:
            del self.data_dict[key]
        except KeyError:
            pass
        return result

    def print_all(self):
        print("<data>")
        for k, v in self.data_dict.items():
            print(k + " : " + str(v))
        print("</data>")

    def find_by_value(self, value, comparator):
        result_set = []
        for item in self.data_dict.values():
            if comparator(value, item):
                result_set.append(item)
        return result_set

    def find_by_key(self, key):
        return self.data_dict.get(key)