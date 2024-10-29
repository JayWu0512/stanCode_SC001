"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	: param temperature : int, the int, the temperature to be compared whether it's highest or lowest temperature.
	: param summary : int, the summary of all temperature
	: param count : int, to count how many temperature data we typed
	"""
	print('stanCode "Weather Master 4.0"! ')
	temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	count = 1
	# count start from boundary condition (including boundary condition)
	summary = 0
	summary += temperature
	if temperature == EXIT:
		print('No temperatures were entered.')
	# boundary condition
	else:
		highest = temperature
		lowest = temperature
		if temperature < 16:
			cold = 1
		else:
			cold = 0
		# discriminate cold day in boundary condition
		while True:
			temperature = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temperature == EXIT:
				break
			elif temperature > highest:
				highest = temperature
				summary += temperature
				count += 1
			elif temperature < lowest:
				lowest = temperature
				summary += temperature
				count += 1
			elif temperature == temperature:
				summary += temperature
				count += 1
			# discriminate highest, lowest and how many data we typed in while loop
			if temperature < 16:
				cold += 1
			# discriminate cold days in while loop
		average = summary / count
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
