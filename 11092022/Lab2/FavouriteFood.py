import numpy as np

existing_points = np.array(((170, 60), (172,60), (173,61), (173,64),(175,67),(175,66)))

x1 = np.array((170,172,173,173,175,175))
y1 = np.array((60,60,61,64,67,66))

x_new = np.array((173))
y_new = np.array((62))

new_points = np.array((173, 62))

print(np.linalg.norm(x1 - x_new, 2, axis=0))
print(np.linalg.norm(existing_points - new_points, 2, axis=0))

existing_points = np.array(((170, 60), (172,60), (173,61), (173,64),(175,67),(175,66)))

new_points = np.array((173, 62))

print(np.linalg.norm(existing_points - new_points, 2, axis=0))

mean = np.mean(existing_points, axis = 1)
cov = np.cov(mean, rowvar=False)
print(cov)

evals, evecs = np.linalg.eig(cov)

print(evals)
print(evecs)
pc = evecs[:, np.argsort(-np.abs(evals))]