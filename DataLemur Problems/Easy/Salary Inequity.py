def min_inequity(salaries, n):

	return (max(sorted(salaries)[:n]) - min(sorted(salaries)[:n]))
