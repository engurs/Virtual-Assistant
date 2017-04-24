import wikipedia
import wolframalpha

while True:
	input = raw_input("Q: ")

	try:
		#wolframalpha
		app_id = "RKLL27-5HG3AP6AUP"
		client  = wolframalpha.Client(app_id)

		result = client.query(input)
		answer = next(result.results).text

		print answer	
	except :
		#wikipedia
		wikipedia.set_lang("en")
		print (wikipedia.summary(input, sentences=2)).encode("utf-8")