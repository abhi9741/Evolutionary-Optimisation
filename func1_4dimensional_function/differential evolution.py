import numpy as np
import matplotlib.pyplot as plt
#initial population

#fora generation g 

#for a candidate p 
#generate mutant vector
#generate trial vector
#evaluate constraints
#if no generate mutant again
#if yes evaluate fitness
#selection using elitism
#travesre all p
#complete all gen or if solution converged 
#identify best pool member ##the end


#initialisation
#mutation
#recombination
#replacement
#evaluation

# def differential_evolution()

# if __name__ == '__main__':
# 	differential_evolution(function,x,y,number_of_iterations)


def fobj(x):
	l=len(x)
	sum=0
	for xx in x:
		sum=sum+(xx**2)/l
	return sum
# print(fobj([1,2,3,4]))

dimensions=4

bounds=[[-5,5],[-5,5],[-5,5],[-5,5]]
population_size=10

#initialisation
initial_population=np.random.rand(10,4)
# print('normalised initial population',initial_population)
#for evaluating fitness we will denormalise  the values using fobj else we can directly generate random numbers between the bounds for each x
def denormalise(initial_population,bounds):
	denormalised_population=[]
	for candidate in initial_population:
		i=0
		denormalised_candidate=[]
		while i<len(candidate):
			min_bound=bounds[i][0]
			max_bound=bounds[i][1]
			diff=max_bound-min_bound
			# print(diff)
			# print(candidate[i])
			# print(candidate[i]*diff)
			ans=min_bound+candidate[i]*diff
			# print(ans)
			denormalised_candidate.append(ans)
			# print(candidate[i])
			# print(bounds[i][0],bounds[i][1])
			# print(bounds[i][1]-bounds[i][0])
			# print((bounds[i][1]-bounds[i][0])*candidate[i])
			# print(denormalised_candidate)
			i=i+1
		denormalised_population.append(denormalised_candidate)
	return denormalised_population

denorm_initial_population=denormalise(initial_population,bounds)
# print('denormalised population : ',denorm_initial_population)
# print('________________________________________________________________________________\n')
# i=0
# while i<len(initial_population):
# 	print(initial_population[i])
# 	print(denorm_initial_population[i])
# 	i=i+1
fittest=fobj(denorm_initial_population[0])
fitness=[]
for candidate in denorm_initial_population:
	# print(candidate,fobj(candidate))
	if (fobj(candidate)<fittest):
		fittest=fobj(candidate)
	fitness.append(fobj(candidate))
# print('fittest : ',denorm_initial_population[fitness.index(fittest)],' has ',fittest)
# print('________________________________________________________________________________\n')
# print(denorm_initial_population)
print('initising population')
print('initial fitness',fittest)
#mutation
# denorm_initial_population=[]
# for candidate in initial_population:
# 	cand=[]
# 	for elem in candidate:
# 		cand.append(elem)
# 	denorm_initial_population.append(cand)
l=len(denorm_initial_population)

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
generations=1
fitness_history=[]
fitness_history.append(fittest)
while generations<10000 and fittest!=0:
		print('generation : ',generations)

		mutants=[]
		for target in denorm_initial_population:
			j=denorm_initial_population.index(target)
			l2=[]
			i=0
			while i<l:
				l2.append(i)
				# print(i)
				i=i+1
			
			del(l2[l2.index(j)])
			s=np.random.choice(l2,3,replace=False)
			a=denorm_initial_population[s[0]]
			b=denorm_initial_population[s[1]]
			c=denorm_initial_population[s[2]]
			mut=0.478 #mut are usually chosen between
			mutant=multiply(mut,sub(b,c))
			# print(mutant)
			# print(len(bounds))
			# print(denorm_initial_population.index(target))
			bounds2=[[0,1],[0,1],[0,1],[0,1]]
			
			# print("___________________")
			
			# print(mutant) 
			# print(a)
			# print(add(a,mutant))
			mutant=adjust(mutant,bounds)
			# print(mutant)
			mutants.append(mutant)
			# print(a,b,c)
			# print(b,c,sub(b,c))
			# print(s)
			# print(j,l2)

		# print(denorm_initial_population)
		# print("________________________________________________________________________________")
		# print(mutants)
		# print("________________________________________________________________________________")
		# print(fitness)
		# print("________________________________________________________________________________")
		# print(len(fitness),len(mutants),len(denorm_initial_population))
		k=0
		l=len(denorm_initial_population)
		while k<l:
			# print('target vector : ',denorm_initial_population[k],'mutant vector : ',mutants[k],'target fitness : ',fitness[k])
			k=k+1
		# print("________________________________________CROSSOVER________________________________________")
		#recombination
		crossp=0.5050
		l=len(denorm_initial_population)
		i=0
		trialcandidates=[]
		while i<l:
			target=denorm_initial_population[i]
			mutant=mutants[i]
			cps=np.random.rand(dimensions)
			trial=[]
			j=0
			ll=len(cps)
			# print(cps)
			while j<ll:
				if cps[j]>=crossp:
					trial.append(candidate[j])
				else :
					trial.append(mutant[j])
				j=j+1
			trialcandidates.append(trial)
			# print('target',candidate)
			# print('trial',trial)
			i=i+1
		trial_fitness=[]
		for trial in trialcandidates:
			trial_fitness.append(fobj(trial))
		# print('target fitness',fitness)
		# print("trial_fitness",trial_fitness)

		gen_next=[]
		i=0
		l=len(denorm_initial_population)
		while i<l:
			if fitness[i]>=trial_fitness[i]:
				gen_next.append(trialcandidates[i])
			else :
				gen_next.append(denorm_initial_population[i])
			i=i+1
		# print("next gen",gen_next)
		# print("old gen",denorm_initial_population)
		gen_next_fitness=[]
		for temp in gen_next:
			gen_next_fitness.append(fobj(temp))
		# print(gen_next_fitness)
		fittest=gen_next_fitness[0]
		for fit in gen_next_fitness:
			if fit<=fittest:
				fittest=fit
		# print(fittest)
		# print(fittest)
		denorm_initial_population=gen_next
		fitness=gen_next_fitness
		z=gen_next_fitness.index(fittest)
		print('best fitness in this generation : ',fittest)
		global_optimum=gen_next[z]
		fitness_history.append(fittest)
		generations=generations+1
# print(fitness_history)
# print(generations)
gen_axis=[]
i=0
g=generations
while i<g:
	gen_axis.append(i)
	i=i+1
print("________________________________________________________________________________")
print("Global Optimum : ",global_optimum)
print("________________________________________________________________________________")
plt.plot(gen_axis,fitness_history)
plt.title("Optimising 4 Dimensional Function Using Differential Evolution")
plt.xlabel('Generations->')
plt.ylabel('Best Fitness in current generation')
plt.show()






















