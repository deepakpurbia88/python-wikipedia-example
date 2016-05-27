import wikipedia

while True :
	input = raw_input("Question: ")
	wikipedia.set_lang("hi")
	print wikipedia.summary(input)

	