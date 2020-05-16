import pandas as pd
import numpy as np

class remuestreo:
    def __init__(self,X,T):
        self.X = X
        self.T = T
        self.n = len(X)
    def bootstrap(self,a=0.05,B=300):
        T_star = []
        for i in range(B):
            X_star = np.random.choice(self.X,self.n)
            T_star.append(self.T(X_star))
        self.VarBoot = np.var(T_star)
        self.StdBoot = self.VarBoot**(1/2)
        self.IntBoot = (2*self.T(self.X)-np.quantile(T_star,1-a/2),2*self.T(self.X)-np.quantile(T_star,a/2))
    def jack(self):
        T_i = []
        for i in range(self.n):
            T_i.append(self.T(list(self.X[0:i]) + list(self.X[i+1:])))
        self.SesgoJack = (self.n-1)*(np.mean(T_i)-self.T(self.X))
        T_pseudo = [self.n*self.T(self.X)-(self.n-1)*T_i[i] for i in range(self.n)]
        self.StdJack = np.sqrt(((np.var(T_pseudo)*self.n)/(self.n-1))/self.n)