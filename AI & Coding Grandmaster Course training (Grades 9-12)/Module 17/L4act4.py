import scipy.stats as stats

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print("Probability of getting 3 heads")
print(prob_1)

prob_2 = 1-stats.binom.pmf(0, n=10, p=.5)-stats.binom.pmf(1, n=10, p=.5)-stats.binom.pmf(2, n=10, p=.5)
print("Probability of getting more than 2 heads")
print(prob_2)