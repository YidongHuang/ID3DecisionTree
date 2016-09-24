class Tree_node:
    def __init__(self):
        self._name = ""
        self._available_attr_index = []
        self._entropy = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def available_attr(self):
        return self._available_attr_index

    @available_attr.setter
    def available_attr(self, new_list):
        self._available_attr_index = new_list

    @property
    def entropy(self):
        return self._entropy

    @entropy.setter
    def entropy(self, new_entropy):
        self._entropy = new_entropy