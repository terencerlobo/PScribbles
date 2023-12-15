import matplotlib.pyplot as plt

plt.axis([0,5,0,5])
plt.title("My First Plot")
plt.xlabel("This is X axis")
plt.ylabel("This is y axis")

plt.plot([1,2,3,4],[1,2,3,4], color = 'k',linestyle='--',linewidth=5)
