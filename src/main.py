import numpy as np
import matplotlib.pyplot as plt

def recover_angle(normalized_angle):
    recovered_angle = [0]
    offset = [0]
    for x in normalized_angle[1:]:
        offset.append(np.floor_divide(recovered_angle[-1] - x + np.pi, 2 * np.pi))
        recovered_angle.append(x + offset[-1] * 2 * np.pi)
    return np.asarray(recovered_angle)


if __name__ == "__main__":
    t = np.arange(0, 10, 0.01)
    real_angle = 3*np.pi*np.sin(t)
    normalized_angle = (real_angle - np.pi) % (2*np.pi) - np.pi
    recovered_angle = recover_angle(normalized_angle)

    fig, ax = plt.subplots(ncols=1, nrows=2)
    fig.suptitle("Angle Tracking")
    
    ax[0].plot(t, real_angle, label="Angle réel")
    ax[0].plot(t, normalized_angle, label="Angle normalisé")
    ax[0].legend(loc="best")
    ax[0].grid(True)
    ax[0].axis([np.min(t), np.max(t), 1.2*np.min(real_angle), 1.2*np.max(real_angle)])
    ax[0].fill_between(t, -np.pi, np.pi, color="gold", alpha=0.3)
    ax[0].set_xlabel("Temps (en $s$)")
    ax[0].set_ylabel("Angle (en $rad$)")

    ax[1].plot(t, recovered_angle, label="Angle récupéré")
    ax[1].grid(True)
    ax[1].legend(loc="best")
    ax[1].axis([np.min(t), np.max(t), 1.2*np.min(recovered_angle), 1.2*np.max(recovered_angle)])
    ax[1].set_xlabel("Temps (en $s$)")
    ax[1].set_ylabel("Angle (en $rad$)")
    
    plt.tight_layout()
    plt.show()