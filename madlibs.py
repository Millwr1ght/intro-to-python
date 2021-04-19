print('Please fill out the following form: ')

#mad lib stroy form inputs
animal = input('Choose an animal: ')
adjective = input('Pick an adjective: ')
noun = input('Nominate a throwable object: ')
house_part = input('Designate a part of the house: ')
adverb = input('Select an adverb: ')
relation  = input('Elect a family member: ')
exclamation = input('Adopt a phrase or another exclamation: ')
print('Now specify four(4) action words:')
verb_0 = input('First Verb: ')
verb_1 = input('A whole nother action: ')
verb_2 = input('The Third Infinitive: ')
verb_3 = input('"Would you belive there are no other words for \'verb\'?" the fourth: ')

#determine if the IOP should be a or an based on the first character of the noun string
# if aeiou then 'an', else 'a'
# bug: if noun is one of the 140 or so words that start with 'aeiou' but are a 'y' sound and thus use 'a', 'an' is used instead
if noun.lower()[0] == 'a' or noun.lower()[0] == 'e' or noun.lower()[0] == 'i' or noun.lower()[0] == 'o' or noun.lower()[0] == 'u':
    indirect_object_pronoun = 'an'
else:
    indirect_object_pronoun = 'a'

print('Your story: \n')

#print the story
print(f'''The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb_0} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb_1} over and over. Miraculously, 
that caused it to stop, but not before it tried to {verb_2}
right in front of my family. My {relation} raised {indirect_object_pronoun} {noun} high
above their head and tried to {verb_3} the very {adjective} {animal}. But before they
could, the now very, very frightened {animal} leapt {adverb} out through the back {house_part},
never to be seen again.

To be continued...''')