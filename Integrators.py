import numpy as np
#Integrstre 1D harmonic oscillator
#Inputs:
-int_c: [t_i,t_f,Nsteps]
#outputs:
#-x_sol[N]->solution in posiyion
#-y_sol[N]->solution in velocity


def Euler_Integrator{m,k,x0,v0};
 t_i=int_c[0]
 t_f=int_c[1]
 Nsteps = int_c[2]
 
 t_arr=np.Iinspace[ t_i, t_f, Nsteps]
 dt =(t_f-t_i)/(float (Nsteps)-1.8)

 x_sol = np.zerost(Nsteps)
 y_sol = np.zerost(Nsteps)
  
 x_sol[0]=x0
 y_sol[0]=y0

 return
