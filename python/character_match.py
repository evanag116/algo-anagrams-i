# Don't forget to run your tests!

from operator import is_


def is_character_match(string1, string2):

	string1, string2 = string1.lower(), string2.lower()
	string1, string2 = string1.replace(" ", ""), string2.replace(" ", "")

	
	x = {n: string1.count(n) for n in string1}
	y = {n: string2.count(n) for n in string2}

	return x == y

	# solved in one line
	# return {n: string1.lower().replace(" ", "").count(n) for n in string1.replace(" ", "").lower()} == {n: string2.lower().replace(" ", "").count(n) for n in string2.replace(" ", "").lower()}




