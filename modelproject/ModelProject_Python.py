#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'modelproject'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # Model Project 
#%% [markdown]
# We start by importing necessary packages:

#%%
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import ipywidgets as widgets
import time
from scipy import linalg
from scipy import optimize
import sympy as sm

#%% [markdown]
# # Solow model with climate change 
#%% [markdown]
# Consider the standard Solow-model with an indicator for climate change where:
# 
# $K_t$ is capital
#     $L_t$ is labor (growing with a constant rate of $n$)
#     $A_t$ is technology (growing with a constant rate of $g$)
#     $D_t$ is the damage function (growing with a constant rate of $n$)
#     $Y_t = F(K_t,A_t,L_t,D_t)$ is GDP
# 
#     
# The Damage-function depends on temperature T
# 
# $$ D_t = 1-\frac{1}{1+\theta_1T_t^{\theta_2}} =< 1 $$
# 
# $T_t^{\theta_2}$ is the global mean temperature change at time t. $\theta_1$ is the damage parameter.
#     
# Cobb-Douglas production-function
# 
# 
# $$ F(K_{t},A_{t}L_{t},D_{t})=  (1-D_{t})A_{t}K_{t}^{\alpha}L_{t}^{1-\alpha}$$
# 
# It is convenient to express all variables of interest in terms of per effective worker, as this can we used as a measure of welfare of sociely. We use small letters to denote per effective worker, so $y=Y/AL$ and $k=K/AL $, which gives: 
# 
# $$ f({k}_{t})=(1-D){k}_{t}^{\alpha} $$
# 
# 
# Saving is a constant fraction of GDP
# 
# $$ S_t = sY_t,\,s\in(0,1) $$
# 
# 
#  **Capital accumulates** according to
# 
# \\[ K_{t+1}=S_{t}+(1-\delta)K_{t}=sF(K_{t},A_{t}L_{t})+(1-\delta)K_{t}, \delta \in (0,1) \\]
# 
# The economy is growing over time (due to exogenous technological progress and population growth), which makes it useful to focus on the behavior of capital stock per unit of effective labor. The transition in the model can be decribed by
# 
# 
# \\[ \tilde{k}_{t+1}= \frac{1}{(1+n)(1+g)}[sf(\tilde{k}_{t})+(1-\delta)\tilde{k}_{t}] \\]
# 
# 
# 
#%% [markdown]
# # Behavior of capital stock per unit of effective labor over time
#%% [markdown]
# ## Model including climate change 

#%%
k = sm.symbols('k')
alpha = sm.symbols('alpha')
delta = sm.symbols('delta')
s = sm.symbols('s')
A = sm.symbols('A')
D = sm.symbols('D')
n = sm.symbols('n')
g = sm.symbols('g')

sm.init_printing(use_unicode=True)

#%% [markdown]
# Equation of capital stock per unit of effective labour

#%%
ss1 = sm.Eq(k,(s*((1-D)*((k)**alpha))+(1-delta)*k)/((1+n)*(1+g)))
ss1

#%% [markdown]
# Create a vector for time, t 

#%%
x_vec = np.zeros((100,1))


#%%
x_vec[0] = 1

#%% [markdown]
# Then we select some parameter values, Let
# $$s=0.2 $$
# $$ g=0.02 $$ 
# $$ n=0.01 $$
# $$ delta=0.1$$
# $$ alpha=1/3 $$
# $$ D=0,1 $$

#%%
s = 0.2
g = 0.02
n = 0.01
delta = 0.1
alpha = (1/3)
D = 0.1

#%% [markdown]
# Now, plug vector x_vec into the capital transition equation: 

#%%
for i in range(1, 100):
    x_vec[i] = (s*(1-D)*x_vec[i-1]**alpha+(1-delta)*x_vec[i-1])/((1+g)*(1+n))

#%% [markdown]
# Now we can check whether the x_vec [steady state capital] converges to a steady state.

#%%
x_vec

#%% [markdown]
# ## Model ignoring climate change

#%%
ss2 = sm.Eq(k,(s*(((k)**alpha))+(1-delta)*k)/((1+n)*(1+g)))
ss2

#%% [markdown]
# Create a vector to plug in for time, t

#%%
y_vec = np.zeros((100,1))


#%%
y_vec[0] = 1

#%% [markdown]
# plug vector y_vec in the equation for behavior of capital stock per unit of effective labour.

#%%
for i in range(1, 100):
    y_vec[i] = (s*y_vec[i-1]**alpha+(1-delta)*y_vec[i-1])/((1+g)*(1+n))

#%% [markdown]
# ### Plot both functions in the same graph

#%%
fid, ax = plt.subplots()
ax.plot(x_vec, label="model including climate change")
ax.plot(y_vec, label="model ignoring climate change")
ax.set(xlabel = 'time, t', ylabel ='k(t)')
plt.title('capital stock per unit of effective labour over time')
plt.legend()
plt.show()

#%% [markdown]
# Both equations converge to a steady state over time. The model including climate change has a lower steady state because it implements climate change as a external cost.
#%% [markdown]
# # Steady state calculations 
#%% [markdown]
# We now want to find an **analytic an analytical** expression for the steady state, that is: where $ k_{t+1} = k_{t} =k_{ss}$

#%%

k = sm.symbols('k')
alpha = sm.symbols('alpha')
delta = sm.symbols('delta')
s = sm.symbols('s')
A = sm.symbols('A')
D = sm.symbols('D')
n = sm.symbols('n')
g = sm.symbols('g')


#%%
sm.init_printing(use_unicode=True)

f = (1-D)*((k)**alpha)
ss = sm.Eq(k,(s*f+(1-delta)*k)/((1+n)*(1+g)))
kss = sm.solve(ss,k)[0]
kss

#%% [markdown]
# In the standard Solow model, **without the damage-function**, the steady state capital is given by: 

#%%
f1= (k)**alpha
ss1 = sm.Eq(k,(s*f1+(1-delta)*k)/((1+n)*(1+g)))
kss1 = sm.solve(ss1,k)[0]
kss1

#%% [markdown]
# From these equations it becomes clear that, with D≤1, the steady state capital growth is reduced by including the damage-function, compared to the the model without
#%% [markdown]
# We can also find the **specific numerical value** for steady state capital. Usning the same parameter values as before, we have 
# 
# $$s=0.2 $$
# $$ g=0.02 $$ 
# $$ n=0.01 $$
# $$ delta=0.1$$
# $$ alpha=1/3 $$
# $$ D=0,1 $$

#%%
ss_func = sm.lambdify((s,g,n,delta,alpha,D),kss)

#%% [markdown]
# Steady state capital, including the damage function, is then given by:

#%%
ss_func(0.2,0.02,0.01,0.1,1/3, 0.1)

#%% [markdown]
# By comparison, excluding the damage function, the steady state is given by:

#%%
ss_func(0.2,0.02,0.01,0.1,1/3, 0)

#%% [markdown]
# Notice how these values corresponds to steady state levels the figure. 
#%% [markdown]
# It becomes clear that the steady state capital excluding the damage function (representing climate change) is higher than the steady state capital in case of climate damage. Climate change is a negative externality for the society. For example, increased temperature causes sea level to rise and drought periods. This again, can increase human conflicts. Today's generation benefits from the use of fossil fuels, which releases greenhouse gases into the atmosphere and in turn causes climate change. But the benefit from using fossil fuels, does not internalize these external costs of climate change. 
#%% [markdown]
# # Impact of damage on steady state capital 
#%% [markdown]
# In order to visualize the impact of damage due to climate change (ceteris paribus), we plot the steady state as a dependent variable of D.
#%% [markdown]
# First, create a list that contains all values we want D to take

#%%
Ds = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#%% [markdown]
# Define the function that returns the steady state only dependent on D.
# 

#%%
def calc_ss(D):
    return ss_func(0.2,0.02,0.01,0.1,1/3, D)

#%% [markdown]
# Create a while loop so that a new list (nDs)is generated that contains all steady states for the respective D.
# 

#%%
index = 0
while index <= len(Ds)-1:
    Ds[index] = calc_ss(Ds[index])
    index = index +1

print(Ds)


#%%
Damage = [0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#%% [markdown]
# ## Plot: 

#%%
fid, ax = plt.subplots()
ax.plot(Damage, Ds)
ax.set(xlabel = 'Damage', ylabel ='Steady state')
plt.show()

#%% [markdown]
# From the plot we can see that as damage increases, the steady state capital decreases. This could be due to higher expenses in order to compensate for i.e. agricultural damage.

#%%



