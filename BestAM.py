def BestAM(self):
	am_list = ["Random", "BioBrick", "Gibson", "GoldenGate"]

	indexes = [i for i, x in enumerate(self.assembly_cost) if x == min(self.assembly_cost)]

return am_list[indexes]