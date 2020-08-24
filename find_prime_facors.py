def get_prime_factors(N):
	""" function to find all prime factors """
	factors = []
	divisor = 2
	while(divisor <= N):
	# if the current divisor divides into N without ramaining
		if (N % divisor) == 0:
			factors.append(divisor)
            #set a new value for N for the next loop iteration
			N = N/divisor
		else:
			divisor += 1
	return factors
    