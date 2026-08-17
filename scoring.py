import numpy as np
DIMS=("U","K","P","R","E","C","X","H")
def css(scores):
    v=np.array([scores[d] for d in DIMS],dtype=float)
    if np.any((v<0)|(v>4)): raise ValueError("scores must be 0..4")
    return float(v.mean()/4)
def paired_bootstrap(diff,n=10000,seed=230047):
    d=np.asarray(diff,dtype=float); rng=np.random.default_rng(seed)
    b=np.array([np.mean(rng.choice(d,size=len(d),replace=True)) for _ in range(n)])
    return np.quantile(b,[.025,.975])
