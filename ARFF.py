import sys, traceback

class Attribute:
    def __init__(self, name):
        self._name = name
        self._value = []
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

    def value_setter(self, new_val):
        self._value = new_val

    @property
    def nominal(self):
        return self._nominal

    def not_nominal(self):
        self._nominal = False

    def __str__(self):
        return "{} {}".format(self._name, self._value)

class ARFF:
    def __init__(self, fname):
        self._attributes = []
        self._data = []
        self._relation = ""
        self._read_file(fname)

    def __str__(self):
        for i in range(len(self._attributes)):
            print self._attributes[i]
        return '\n'.join( [ str(data) for data in self._data ])


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

    def _read_file(self, fname):
        file = open(fname)
        numeric = []
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
                    attr = Attribute(splited_attr[0].replace("'", ""))
                    attrs = spaced_line.replace(splited_attr[0], "").strip()
                    attrs = attrs.replace("{","").strip()
                    attrs = attrs.replace("}", "").strip()
                    attrs = attrs.replace(" ","").strip()
                    attr_vals = attrs.split(",")
                    if len(attr_vals) > 1 :
                        attr.value_setter(attr_vals)
                    else:
                        attr.value_setter([])
                        attr.not_nominal()
                    self._attributes.append(attr)
                    continue

                elif stage == 1 and line[0:5].lower() == "@data":
                    for i in range(len(self._attributes)):
                        if self._attributes[i].nominal is not True:
                            numeric.append(i)
                    stage = 2
                    continue

                elif stage == 2:
                    line = line.strip()
                    vals = line.split(",")
                    for i in range(len(numeric)):
                        self._attributes[numeric[i]].append_val(float(vals[numeric[i]]))
                        vals[numeric[i]] = float(vals[numeric[i]])
                    self._data.append(vals)
                    continue

                else:
                    raise Exception("Bad formed ARFF")


        except:
            print "something went wrong when reading {}".format(fname)
            traceback.print_exc(file=sys.stdout)
            exit()







