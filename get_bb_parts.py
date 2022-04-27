def get_bb_parts(self):

	ecori_site = "AATTC"
	xbal_site = "CTAGA"
	spel_site = "CTAGT"
	pstl_site = "CTGCA"

	res_sites = [ecori_site,xbal_site,spel_site,pstl_site]


	if any(res_site in self.name for res_site in res_sites):
		cost_penalty = float('inf')
	else
		cost_penalty = 0

	self.assembly_cost[1] = cost_penalty