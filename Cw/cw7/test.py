owners = [item for item in input('enter :').split()]
names = ['ali', 'saeed', 'hosein']
print(owners)
counter = 0

for i in owners:
    if i in names:
        counter += 1
        print(i)
if counter == len(owners):
    print('true')
else:
    print('false')

 self.owners = [item for item in input('enter the owners :').split()]

self.owners = [item for item in input('enter the owners :').split()]
if Document.is_valid(self.owners):
    pass
else:
    print('the Owners entered is not valid')
    self.owners = [item for item in input('please enter the valid owners: ').split()]

    [[{'Book': {}}, {'Poem': {}}, {'Article': {}}],
     [{'Writer': {}}, {'Researcher': {}}, {'Poet': {}}]]

    [{'Writer': {},
      'Poet': {},
      'Researcher': {}
      }, {
         'Book': {},
         'Poem': {},
         'Article': {}
     }]