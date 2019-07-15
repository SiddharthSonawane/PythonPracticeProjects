# List project on inviting guest for dinner
# If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

#

guest = ['raj', 'dhruv', 'mahesh', 'sonali', 'teju']

print('Hi ' + guest[0].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')

print('Hi ' + guest[1].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print('Hi ' + guest[2].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print('Hi ' + guest[3].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print('Hi ' + guest[4].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')

print('looks like ' + guest[0] + ' is not coming')
notComing_guest = guest.pop(0)
print(guest)

print(notComing_guest + ' will be not coming.Just got confirmation')
guest.append('Vishal')
print(guest)

print("we' got bigger table!")
guest.insert(0,'amol')
guest.insert(3,'yash')
guest.append('rahul')

print('Hi ' + guest[0].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print('Hi ' + guest[3].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print('Hi ' + guest[-1].title() + ' i would like you to invite'
                                 ' for dinner at my place.\nIt will be great if you can join us.')
print(guest)

print('sorry to inform you that we only have space for two members')

notComing_guest = guest.pop()
print(notComing_guest)
notComing_guest = guest.pop()
print(notComing_guest)
print(guest)
notComing_guest = guest.pop()
print(notComing_guest)

guest.pop()
print(guest)
guest.pop()
guest.pop()
print(guest)

print(guest[0] + ' you are invited to dinner')
print(guest[1] + ' you are invited to dinner')


del guest[0]
del guest[0]

print(guest)

print("list is empty")

