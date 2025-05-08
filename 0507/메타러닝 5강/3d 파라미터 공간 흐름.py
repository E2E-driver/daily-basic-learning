# Re-import after reset
import numpy as np
import matplotlib.pyplot as plt


# 초기 파라미터
theta = np.array([0.0, 0.0])

# 가상의 태스크 최적 파라미터
phi_stars = np.array([
    [1.5, 1.0],
    [-1.2, 1.5],
    [0.5, -1.5]
])

# learning rate
alpha = 0.5

# 태스크 손실 함수
def task_loss(w, phi_star):
    return np.exp(-0.5 * ((w[0] - phi_star[0])**2 + (w[1] - phi_star[1])**2))

# 그라디언트 계산
def task_grad(w, phi_star):
    return -(w - phi_star) * task_loss(w, phi_star)

# 시각화용 그리드
X = np.linspace(-2, 2, 100)
Y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X)

for phi in phi_stars:
    Z += np.exp(-0.5 * ((X - phi[0])**2 + (Y - phi[1])**2))

# 3D 시각화
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

# 메타 초기화 위치
ax.scatter(theta[0], theta[1], sum(task_loss(theta, phi) for phi in phi_stars),
           color='red', s=80, label='meta-init θ')

# 각 태스크에 대한 업데이트 경로
for i, phi_star in enumerate(phi_stars):
    grad = task_grad(theta, phi_star)
    phi_i = theta - alpha * grad
    ax.plot([theta[0], phi_i[0]], [theta[1], phi_i[1]],
            [task_loss(theta, phi_star), task_loss(phi_i, phi_star)],
            color='black', linestyle='--', label='adaptation' if i == 0 else "")
    ax.scatter(phi_star[0], phi_star[1], task_loss(phi_star, phi_star),
               color='blue', s=60, label='φ* (task optimum)' if i == 0 else "")

ax.set_xlabel('w1')
ax.set_ylabel('w2')
ax.set_zlabel('Loss')
ax.set_title('3D Visualization of Meta-learning and Adaptation')
ax.legend()
plt.tight_layout()
plt.show()
