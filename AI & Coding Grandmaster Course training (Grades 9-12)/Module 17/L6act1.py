import numpy as np

#Below is an array that represents the puppies we have in our sample, where 1 
#represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes.

np.random.seed(42)

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

#Finding the proportion of puppies with blue eyes in the above array. 
#Storing this value in a variable p

p=puppies.mean()
print("Mean", p)
print("Standard Deviation", puppies.std())
print("Variance", puppies.var())

#Using numpy's random.choice to simulate 5 draws from the puppies array.
np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

#Proportion of sample with blue eyes in 0.8

#Repeating the above to obtain 10,000 additional proportions, where 
#each sample was of size 5. Storing these in a variable called sample_props
print("\nSampling Distribution with size 5 \n")
sample_props= []
for i in range(10000):
    sample = np.random.choice(puppies, 5, replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

#The mean of the sampling distribution
sm = sample_props.mean()
print("Mean", sample_props.mean())
print("Standard Deviation", sample_props.std())
print("Variance", sample_props.var())

print("\nSampling Distribution with size 20 \n")

#Let's repeat all these steps with a new sample, this time size 20.
twenty_sample_props= []
for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

print("New Mean", twenty_sample_props.mean())
print("New Standard Deviation", twenty_sample_props.std())
print("New Variance", twenty_sample_props.var())
