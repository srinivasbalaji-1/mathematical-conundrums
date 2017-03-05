def simulate_monty_hall(num_of_doors,num_of_iterations):
	doors = [i for i in range(1,num_of_doors+1)]
	import random
	prize_door = random.choice(doors)
	no_variable_change_win_count, variable_change_win_count = 0,0
	same_choice, not_same_choice = True, True	
	print prize_door
	for i in range(num_of_iterations):
		paricipant_choice = random.choice(doors)
		#Now the host opens up one of the other non-prize doors
		#and prods the participant to making a choice again.
		door_opened = random.choice(list(set(doors)-set([paricipant_choice])-
						  set([prize_door])))
		#If the participant goes for variable change there
		#is an additional probability of success in an attempt
		#to make an informed choice now.		
		if same_choice and prize_door == paricipant_choice:
			no_variable_change_win_count += 1
		if not_same_choice:
			changed_choice = random.choice(list(set(doors)-set([paricipant_choice])-set([door_opened])))
			if changed_choice == prize_door:
				variable_change_win_count += 1
	print "Change of choice sample probability of a win=", float(no_variable_change_win_count)/num_of_iterations
	print "Staying with the initial choice sample probability of a win", float(variable_change_win_count)/num_of_iterations

if __name__ == "__main__":
        simulate_monty_hall(3,1000)
