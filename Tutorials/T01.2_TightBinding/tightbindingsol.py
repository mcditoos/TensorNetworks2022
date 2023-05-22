import numpy as np



def tightbindinghamiltonian(t):
    H=np.diag(-t,-1)+np.conjugate(np.diag(-t,-1).T)
    return H
def eigvals(t):
    H=tightbindinghamiltonian(t)
    vals=np.linalg.eigvals(H)
    vals=[0 if np.isclose(vals[i],0) else np.real(vals[i]) for i in range(len(vals)) ]
    return np.sort(vals)


def groundstate(t):
    eig=eigvals(t)
    return eig[eig<0].sum() # I need to understand why the negative values are summed I thought ut was just the minimum 
def degeneracies(t):
    eig=eigvals(t)
    return 2**(np.isclose(eig,0)).sum() # Why the number of zeros instead of repetitions


# Homework cases 

L=9
t=np.ones(L)
print(f"for {L} and tl=1 we have {groundstate(t).round(2)} as a ground state and it is {degeneracies(t)} fold degenerated")


L=10
t=np.ones(L)
print(f"for {L} and tl=1 we have {groundstate(t).round(2)} as a ground state and it is {degeneracies(t)} fold degenerated")

L=10
t=np.linspace(1,L,L)
t1=np.exp(1j*t)
print(f"for {L} and tl=e**il we have {groundstate(t1).round(2)} as a ground state and it is {degeneracies(t1)} fold degenerated")


