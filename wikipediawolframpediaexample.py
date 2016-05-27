import wikipedia
import wolframalpha

while True :
	input = raw_input("Question: ")

	try :
		#wolframalpha
		app_id = "Q9Y82R-3EPW3WQKHP"
		client = wolframalpha.Client(app_id)
		res = client.query(input)
		answer = next(res.results).text
		print answer
	except :
		#wikipedia
		print wikipedia.summary(input)


