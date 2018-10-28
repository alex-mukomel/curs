import numpy as np 
import matplotlib.pyplot as plt
from time import time

tic = time()
data1 = np.loadtxt("1.txt", delimiter='\n', dtype=np.float)
data2 = np.loadtxt("3.txt", delimiter='\n', dtype=np.float)
toc = time()
print ("Время откр.: ", toc - tic, "c")

#Служит для уравнивания размерности массивов с наборами значений
if(len(data1) > len(data2)):
    d1 = data1[0:len(data2):1]
    d2 = data2
else:
    d2 = data2[0:len(data1):1]
    d1 = data1

#функция, вычисляющая коэффициент корреляции Пирсона
def custom_corrcoef(data1, data2):
  M_d1 = np.sum(data1) / len(data1)
  M_d2 = np.sum(data2) / len(data2)


  tic = time()
  d1 = (data1 - M_d1) #отклонение от среднего значения (1 поток)
  d2 = (data2 - M_d1) #отклонение от среднего значения (2 поток)
  toc = time()
  print ("Время вып.1: ", toc - tic, "c")

  tic = time()
  dd1 = d1 ** 2 #квадрат отклонения (1 поток)
  dd2 = d2 ** 2 #квадрат отклонения (2 поток)
  toc = time()
  print ("Время вып.2: ", toc - tic, "c")

  tic = time()
  d3 = d1 * d2 #произведение отклонений
  toc = time()
  print ("Время вып.3: ", toc - tic, "c")

  tic = time()
  res_res = np.sum(d3)/((np.sum(dd1) * np.sum(dd2)) ** .5)
  toc = time()
  print ("Время вып.4: ", toc - tic, "c")

  return res_res

#Вспомогательная функция, выч. корреляции с учетом сдвига
def custom_corr(data1, data2):
  return [custom_corrcoef(np.hstack([data1[(j - 1000) * 10:], data1[:(j - 1000) * 10]]), data2) for j in range(2000)]

print ("Коэффициент корреляции Пирсона для двух совокупностей данных:", custom_corrcoef(d1, d2))
tic = time()
data_res = custom_corr(d1, d2)
toc = time()
print ("Время выполнения5: ", toc - tic, "c")

tic = time()
#[custom_corr(d1, d2) for j in range(10)]
toc = time()
print ("Время выполнения6: ", toc - tic, "c")
print ("Максимальная корреляция с учетом сдвигов: ", max(data_res))

t = np.linspace(-40, 40, 2000)
plt.plot(t, data_res)
plt.title(u'Коэффициент корреляции в зависимости от сдвига')
plt.xlabel(u'Сдвиг')
plt.grid()
plt.ylabel(u'Коэффициент корреляции')
plt.show()

