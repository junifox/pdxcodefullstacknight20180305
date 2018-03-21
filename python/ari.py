import math

file_name = 'dickens.txt'
with open(file_name, 'r') as f:
    text = f.read()

    sen_count = 0
    for char in text:
        if char in ['.','!','?']:
            sen_count += 1

    words = text.lower().split()
    words_count = len(words)

    character_count = 0
    for word in words:
        character_count += len(words)

    ari = 4.71 * (character_count/words_count) + 0.5 * (words_count/sen_count) - 21.43
    ari = math.ceil(ari)


    if ari > 14:
        ari = 14

    ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

grade_level = ari_scale[ari]
output = '-'*80
output += 'The ARI for ' + file_name + 'is ' + str(ari) + '\n'
output += 'This corresponds to a ' + grade_level['grade_level'] + ' level of difficulty\n'
output += 'that is suitable for the average person' + grade_level['ages'] + ' years old\n'
output += '-'*80
print(output)
