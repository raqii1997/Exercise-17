class Kangaroo(object):
    def __init__(self):
        self.pouch_contents = []                          # [] is an empty list

    def put_in_pouch(self, anything):
        self.pouch_contents.append(anything)                # using append to add content to the pouch

    def __str__(self):                                     # using __str__ function to assign kangaroo pouch content
        return "Kangaroo object" + str(self.pouch_contents)


kanga = Kangaroo()                                         # assigning variable kangaa for the kangaroo first pouch
roo = Kangaroo()                                           # assigning variable roo for the the kangaroo second pouch

roo.put_in_pouch(raw_input('Enter anything you want: '))                # Enter anything you wan to add in kanga's pouch
print " kanga = ", roo
print " roo = ", kanga
