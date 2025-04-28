import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from scipy.special import legendre

def task1():
    # X Axis
    x = np.linspace(-1, 1, 400)

    # Graph
    plt.figure(figsize=(10, 6))

    # Colors for graph
    colors = plt.cm.viridis(np.linspace(0, 1, 7))

    # Const x_annotate
    x_annotate = (0.8, 0.9)

    for n in range(1, 8):
        Pn = legendre(n)  # Polynomial from 1 to 8
        y = Pn(x)  # Y Axis
        y_annotate = Pn(x_annotate[n % 2]) # Flux y_annotate

        plt.plot(x, y, color=colors[n - 1])  # Draw polynomial
        # Create annotation
        plt.annotate(f"- n = {n}", xy=(x_annotate[n % 2], y_annotate),
                     xytext=(x_annotate[n % 2] + 0.05, y_annotate + 0.1),
                     arrowprops=dict(arrowstyle="->", color=colors[n - 1]),
                     color=colors[n - 1], fontsize=10)


    # Graph decoration
    plt.title("Полиномы Лежандра")
    plt.xlabel("x")
    plt.ylabel("Pₙ(x)")
    plt.grid(True)
    plt.tight_layout()

    plt.show()


def task2():
    # Time (parameter t)
    t = np.linspace(0, 2 * np.pi, 1000)

    # Ratios
    ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

    # Graph 2x2
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Phase rift
    delta = np.pi / 2

    for ax, (a, b) in zip(axs.flat, ratios):
        x = np.sin(a * t + delta)
        y = np.sin(b * t)

        ax.plot(x, y)
        ax.set_title(f'Частоты: {a}:{b}')
        ax.set_aspect('equal')
        ax.grid(True)

    plt.suptitle('Фигуры Лиссажу', fontsize=14)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    plt.show()


def task3():
    # Parameters
    t = np.linspace(0, 2 * np.pi, 1000)
    b = 1  # Y-frequency
    delta = 0

    # Shape and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_title('Анимация фигуры Лиссажу')
    ax.grid(True)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        a = frame / 100  # 0 < a < 1
        x = np.sin(a * t + delta)
        y = np.sin(b * t)
        line.set_data(x, y)
        return line,

    # Create animation
    anim = FuncAnimation(fig, update, frames=101, init_func=init, blit=True, interval=50)

    plt.show()


def task4():
    # Time, X_Axis
    x = np.linspace(0, 2 * np.pi, 1000)

    # Beginning parameters
    amp1_init, freq1_init = 1, 1
    amp2_init, freq2_init = 1, 1

    # Create graphs
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))
    plt.subplots_adjust(left=0.1, bottom=0.35, hspace=0.5)

    # Draw beggining graphs
    line1, = axs[0].plot(x, amp1_init * np.sin(freq1_init * x), label="Волна 1")
    axs[0].set_title("Волна 1")

    line2, = axs[1].plot(x, amp2_init * np.sin(freq2_init * x), label="Волна 2")
    axs[1].set_title("Волна 2")

    line_sum, = axs[2].plot(x, amp1_init * np.sin(freq1_init * x) + amp2_init * np.sin(freq2_init * x),
                            label="Сумма волн")
    axs[2].set_title("Сумма волн")

    for ax in axs:
        ax.grid(True)
        ax.set_ylim(-3, 3)

    # Create sliders
    axcolor = 'lightgoldenrodyellow'
    ax_amp1 = plt.axes((0.08, 0.25, 0.35, 0.03), facecolor=axcolor)
    ax_freq1 = plt.axes((0.08, 0.2, 0.35, 0.03), facecolor=axcolor)

    ax_amp2 = plt.axes((0.57, 0.25, 0.35, 0.03), facecolor=axcolor)
    ax_freq2 = plt.axes((0.57, 0.2, 0.35, 0.03), facecolor=axcolor)

    s_amp1 = Slider(ax_amp1, 'Amp 1', 0, 2, valinit=amp1_init)
    s_freq1 = Slider(ax_freq1, 'Freq 1', 0.1, 5, valinit=freq1_init)

    s_amp2 = Slider(ax_amp2, 'Amp 2', 0, 2, valinit=amp2_init)
    s_freq2 = Slider(ax_freq2, 'Freq 2', 0.1, 5, valinit=freq2_init)

    # Update the graphs function
    def update(val):
        a1 = s_amp1.val
        f1 = s_freq1.val
        a2 = s_amp2.val
        f2 = s_freq2.val

        y1 = a1 * np.sin(f1 * x)
        y2 = a2 * np.sin(f2 * x)
        y_sum = y1 + y2

        line1.set_ydata(y1)
        line2.set_ydata(y2)
        line_sum.set_ydata(y_sum)

        fig.canvas.draw_idle()

    # Link update function
    s_amp1.on_changed(update)
    s_freq1.on_changed(update)
    s_amp2.on_changed(update)
    s_freq2.on_changed(update)

    plt.show()


def task5():
    # Parameters generation
    w1 = np.linspace(-3, 3, 100)
    w2 = np.linspace(-3, 3, 100)
    W1, W2 = np.meshgrid(w1, w2)

    # Random model func MSE
    Z = (W1 ** 2 + W2 ** 2 + 0.5)  # +0.5, so no log(0)

    # Create shape and two 3-D graphs
    fig = plt.figure(figsize=(16, 6))

    # First graph - normal
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    surf1 = ax1.plot_surface(W1, W2, Z, cmap='viridis')
    ax1.set_title('MSE: линейная шкала Z')
    ax1.set_xlabel('w1')
    ax1.set_ylabel('w2')
    ax1.set_zlabel('MSE')
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

    # Second graph — log_10 - Z-Axis
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    logZ = np.log10(Z)
    surf2 = ax2.plot_surface(W1, W2, logZ, cmap='plasma')
    ax2.set_title('MSE: логарифмическая шкала Z (log_10)')
    ax2.set_xlabel('w1')
    ax2.set_ylabel('w2')
    ax2.set_zlabel('log(MSE)')
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

    plt.tight_layout()
    plt.show()


task1()