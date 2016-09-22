class Attribute:
    def __init__(self, name):
        self._name = name
        self._value = [];
        self._nominal = True

    def append_val(self, new_val):
        self._value.append(new_val)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val

    @property
    def nominal(self):
        return self._nominal

    def not_nominal(self):
        self._nominal = False

class ARFF:
    def __init__(self, attributes, data):
        self._attributes = []
        self._data = []
        self._relation = ""

    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, value):
        self._relation = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def read_file(self, fname):
        file = open(fname)

        stage = 0
        try:
            for line in file:
                if stage == 0 and line[0:9].lower() == "@relation":
                    self.relation = line[9:].strip()
                    stage = 1
                    continue

                elif stage == 1 and line[0:10].lower() == "@attribute":
                    spaced_line = line[10:].replace("\t", " ").strip()
                    splited_attr = spaced_line.split(" ")
                    attr = Attribute(splited_attr[0])
                    attrs = spaced_line.replace(splited_attr[0], "").strip()
                    attrs = attrs.replace("{","").strip()
                    attrs = attrs.replace("}", "").strip()
                    attrs = attrs.replace(" ","").strip()
                    attr_vals = attrs.split(",")
                    if attr_vals.count() > 1 :
                        attr.value = attr_vals
                    else:
                        attr.value = []
                        attr.not_nominal()
                    self._attributes.append(attr)
                    continue

                elif stage == 1 and line[0:5].lower() == "@data":
                    stage = 2
                    continue

                elif stage == 2:



        except:
            print "something went wrong when reading {}".format(fname)
            exit()





