import numpy as np
sizes=[10,100,1000,10000]
for n in sizes:
    tosses=np.random.randint(0,2,size=n)
    head_count=np.count_nonzero(tosses==0)
    tail_count=np.count_nonzero(tosses==1)
    exp_prob_head=np.mean(tosses==0)
    print("Tosses",n)
    print("Number of heads",head_count)
    print("Number of tails",tail_count)
    print("experimental probability of head:",exp_prob_head)
    error=abs(exp_prob_head-0.5)
    print("Error:",error)