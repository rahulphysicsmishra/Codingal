import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

type = [blood_sugar_men, blood_sugar_women]
colors = ['g', 'r']
label = ['men', 'women']
bins = [80, 100, 125, 150]
plt.xlabel("Blood Sugar Range")
plt.ylabel("Total no. of patients")
# Diabetic blood_sugar range
#
# 80 - 100 = normal
# 100 - 125 = pre-diabetic
# above 125 = diabetic

plt.hist(type, bins=bins, width=0.95, color=colors,
    label=label, orientation="horizontal")

plt.title("Blood Sugar Level Chart")
plt.legend()
plt.show()