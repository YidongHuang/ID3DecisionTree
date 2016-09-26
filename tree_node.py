class Tree_node:
    def __init__(self):
        self._name = ""
        self._available_attr_index = []
        self._entropy = 1
        self._threshold = "nominal"
        self._children = []
        self._parent_common_class = ""
        self._result = ""
        self._condition = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, new_result):
        self._result = new_result

    @property
    def available_attr_index(self):
        return self._available_attr_index

    @available_attr_index.setter
    def available_attr_index(self, new_list):
        self._available_attr_index = new_list

    @property
    def entropy(self):
        return self._entropy

    @entropy.setter
    def entropy(self, new_entropy):
        self._entropy = new_entropy

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, new_threshold):
        self._threshold = new_threshold

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, new_children):
        self._children = new_children

    @property
    def parent_common_class(self):
        return self._parent_common_class

    @parent_common_class.setter
    def name(self, new_val):
        self._parent_common_class = new_val

    @property
    def condition(self):
        self._condition

    def append_condition(self, addition):
        self._condition.join([addition])


    def print_tree(self, blank):
        print "{}{} {}".format(blank, self.name, self.result)
        for child in self.children:
            child.print_tree("    {}".format(blank))