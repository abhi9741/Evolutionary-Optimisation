import numpy as np
import matplotlib.pyplot as plt

def fobj(x,y):
	# return np.sin(np.sqrt(x**2+y**2))
	a=y+47
	b=abs((x/2)+a)
	c=np.sin(np.sqrt(b))
	d=-a*c
	e=abs(x-(a))
	f=x*(np.sin(np.sqrt(e)))
	# print( d-f)
	return d-f

def generate_initial_population(population_size,dimentions):
	initial_population=np.random.rand(population_size,dimentions)

	# print(initial_population)
	return initial_population

def denormalise(population,bounds):
	l=len(population)
	denormalised_population=[]
	for candidate in population:
		denormalised_candidate=[]
		i=0
		while i<len(candidate):
			left_bound=bounds[i][0]
			right_bound=bounds[i][1]
			diff=right_bound-left_bound
			ans=left_bound+candidate[i]*diff # mapping from domain [0,1] to its actual domain,in this case [-520,520] for x and [-410,410] for y
			denormalised_candidate.append(ans)
			i=i+1
		denormalised_population.append(denormalised_candidate)
	return denormalised_population

def calculate_fitness(population,fobj):
	l=len(population)
	fitness=[]
	for candidate in population :
		fitness.append(fobj(candidate[0],candidate[1]))
	return(fitness)

def calculate_average(list_):
	sum_=0
	l=len(list_)
	for elem in list_:
		sum_=sum_+elem
	average=sum_/l
	return(average)

def sub(b,c):
	l=len(b)
	i=0
	res=[]
	while i<l:
		res.append(b[i]-c[i])
		i=i+1
	return res

def multiply(mut,sub_res):
	l=len(sub_res)
	i=0
	res=[]
	while i<l:
		res.append(sub_res[i]*mut)
		i=i+1
	return res

def add(b,c):
	l=len(b)
	i=0
	res=[]
	while i<l:
		res.append(b[i]+c[i])
		i=i+1
	return res

def adjust(mutant,bounds):
	i=0
	l=len(mutant)
	res=[]
	while i<l:
		temp=mutant[i]
		left_bound=bounds[i][0]
		right_bound=bounds[i][1]

		if temp<left_bound:
			# print(temp,left_bound)
			temp=left_bound
		if temp>right_bound:
			# print(temp,right_bound)
			temp=right_bound
		res.append(temp)
		i=i+1
	return res

if __name__ == '__main__':
	bounds=[[-520,520],[-410,410]]
	dimentions=2 #number of variables x,y
	population_size=500
	max_generations=100
	generation=0
	initial_population=generate_initial_population(population_size,dimentions)
	# print("initial population",initial_population)
	denorm_initial_population=denormalise(initial_population,bounds)
	# print("denormalised initial population",denorm_initial_population)
	current_gen_fitness=calculate_fitness(denorm_initial_population,fobj)
	# print("fitness of initialised population",current_gen_fitness)
	fittest=current_gen_fitness[0]
	for fit in current_gen_fitness:
		if fit<fittest:
			fittest=fit
	average=calculate_average(current_gen_fitness)
	best_fitness_history=[]
	average_fitness_history=[]
	print("------------------------------------------------------------------------------------------------------------------------------------------------------")
	print("generation number : \t\t\t",generation)
	dummy=fittest
	dummy1=average
	print("fittest one in current generation : \t",denorm_initial_population[current_gen_fitness.index(fittest)]," with fitness : ",fittest)
	
	print("average fitness in this generation : \t",average)
	print("------------------------------------------------------------------------------------------------------------------------------------------------------")
	best_fitness_history.append(fittest)
	average_fitness_history.append(average)
	generation=generation+1

	current_gen_population=denorm_initial_population
	

	while generation<max_generations and fittest!=0 :
		print("------------------------------------------------------------------------------------------------------------------------------------------------------")
		print('generation number : \t\t\t',generation)
		mutants=[]
		
		# list1_=[]
		# while i <population_size:
		# 	list1_.append(i)
		# 	i=i+1
		# # list2_=list1_
		#select targets
		#generate mutants
			#generate a list without current index
		f=np.random.uniform(-2,2,1)[0]
		k=0.5
		mut=0.8
		for candidate in current_gen_population :
			i=0
			list1_=[]
			while i <population_size:
				list1_.append(i)
				i=i+1
			j=current_gen_population.index(candidate)	
			del(list1_[list1_.index(j)])
			# print(j,list1_,s)			
			#select 3 random indices from above list
			s=np.random.choice(list1_,3,replace=False)
			a=current_gen_population[s[0]]
			b=current_gen_population[s[0]]
			c=current_gen_population[s[0]]
			#apply mutation between target and select
			# mutant=candidate+k*(a-candidate)+f*(b-c)
			# aa=sub(a,candidate)
			# bb=sub(b,c)
			# aaa=multiply(k,aa)
			# bbb=multiply(f,bb)
			# a4=add(aaa,bbb)
			# mutant_=add(candidate,a4)
			a1=sub(b,c)
			a2=multiply(mut,a1)
			mutant_=add(a,a2)
			mutant_=adjust(mutant_,bounds)
			# mutant_=candidate+multiply(k,sub(a,candidate))+multiply(f,sub(b,c))
			# print("candidate",candidate,"mutant",mutant_)
			mutants.append(mutant_)
		#generate trial vectors
		crossp=0.5050
		l=len(current_gen_population)
		i=0
		trialcandidates=[]
		while i<l:
			target=current_gen_population[i]
			mutant=mutants[i]
			cps=np.random.rand(dimentions)
			trial=[]
			j=0
			l1=len(cps)
			while j<l1:
				if cps[j]<=crossp:
					# print(i,j,cps[j],candidate,mutant)
					trial.append(candidate[j])
				else :
					trial.append(mutant[j])
					# print(i,j,cps[j],candidate,mutant)
				j=j+1
			# print(trial)
			trialcandidates.append(trial)
			i=i+1
		trial_fitness=[]
		for trial in trialcandidates:
			trial_fitness.append(fobj(trial[0],trial[1]))
		# print("trial candidates",trialcandidates)
		# print(current_gen_population)
		# print(mutants)


		
		#selection using elitism
		#generate next generation
		gen_next=[]
		i=0
		l=len(current_gen_population)
		while i<l:
			if current_gen_fitness[i]>=trial_fitness[i]:
				gen_next.append(trialcandidates[i])
			else :
				gen_next.append(current_gen_population[i])
			i=i+1

		gen_next_fitness=[]
		for temp in gen_next:
			gen_next_fitness.append(fobj(temp[0],temp[1]))
		fittest=gen_next_fitness[0]
		for fit in gen_next_fitness:
			if fit<=fittest:
				fittest=fit
		current_gen_population=gen_next
		# print(current_gen_fitness)
		current_gen_fitness=gen_next_fitness
		# print(current_gen_fitness)
		z=gen_next_fitness.index(fittest)
		print("best fitness in this generation : ",fittest)

		global_optimum=gen_next[z]
		best_fitness_history.append(fittest)
		average_=calculate_average(gen_next_fitness)
		average_fitness_history.append(average_)
		print("average fitness in this generation : ",average_)
		# print("--")
		#store fittest,average fitness in the current generation
		generation=generation+1
	# print(dummy)
	# print(dummy1)
	print("Global Optimum : ",global_optimum)
	xaxis=[]
	i=0
	while i <generation:
		xaxis.append(i)
		i=i+1
	plt.plot(xaxis,best_fitness_history)
	plt.plot(xaxis,average_fitness_history)
	plt.xlabel("Generations")
	plt.ylabel("Best fitness in blue ,Avg fitness in orange")
	plt.title("Convergence of Solutions")
	# print("best",best_fitness_history)
	# print("avg",average_fitness_history)
	plt.show()














































































































































































































































































































































































































































































































































