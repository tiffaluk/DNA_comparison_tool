def get_rand_parts(self):
	rand_parts = []
	n = 100

	for i in range(0, len(self.name), n):
        rand_parts.append(self.name[i:i+n])

    # if len(rand_parts) > 


	self.assembly_cost[0] = cost_penalty