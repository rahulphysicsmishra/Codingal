import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob1 = 1-stats.poisson.cdf(20, 15)

# print prob_more_than_20
print(prob1)

## Checkpoint 2
# calculate prob_17_to_21
prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

# print prob_17_to_21
print(prob2)