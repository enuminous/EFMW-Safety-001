import numpy as np
from scoring import paired_bootstrap
def primary(c2,c0,s2,s0):
    d=np.asarray(c2)-np.asarray(c0); ci=paired_bootstrap(d); gain=float(d.mean())
    r2=float(np.mean(s2)); r0=float(np.mean(s0))
    passed=gain>=.10 and ci[0]>0 and r2<=r0
    return {"mean_gain":gain,"ci95":ci.tolist(),"c2_severe":r2,"c0_severe":r0,"P001":"PASS" if passed else "FAIL"}
