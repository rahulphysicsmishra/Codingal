prob_st = 0.2

prob_st_pos = 0.2*0.85
prob_nst_pos = 0.8*0.02
prob_positive = prob_st_pos + prob_nst_pos 

prob_pos_given_st = 0.85

prob_result = (prob_st*prob_pos_given_st)/prob_positive

print("Probability of person testing positive having step throat is :", round((prob_result),3))