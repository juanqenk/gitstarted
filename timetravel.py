
# coding: utf-8

# In[1]:

import time


# In[7]:

print('Estimado viajero en el tiempo, gracias por confiar en TimeTraveler para deshacer sus errores del pasado.')
print('Actualmente usted está en', time.asctime())


# In[19]:

party_time = time.struct_time((2009, 6, 28, 
                 10, 10, 1, 6, 179, 1))

# El valor devuelto es un objeto struct_time con
# los siguientes atributos:

# - tm_year: año 
# - tm_mon: mes 
# - tm_mday: día del mes 
# - tm_hour: hora 
# - tm_min: minutos
# - tm_sec: segundos 
# - tm_wday: día de la semana [0, 6] 
# - tm_yday: día del año [1, 366] 
# - tm_isdst: horario de verano: 0 (no vigente), 
#                                1 (vigente) y 
#                               -1 (desconocido)

print('Abrochense los cinturones. Usted va a viajar al día', party_time.tm_mday,'-', party_time.tm_mon,'-', party_time.tm_year)
print('Done!')
print('Bienvenido al pasado, esperamos que pase un buen rato. ')


# In[ ]:



