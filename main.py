import numpy as np
import matplotlib.pyplot as plt

# Fonction pour créer un radar chart
def radar_chart(name, stats, labels):
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    stats += stats[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='b', alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(name, size=20, color='blue', y=1.1)
    plt.show()

# Exemple d'utilisation
name = "Compétences du personnage"
stats = [80, 60, 75, 90, 85, 50, 70]  # Remplacez ces valeurs par les compétences de votre personnage
labels = ['Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5', 'Comp6', 'Comp7']  # Remplacez ces libellés par les noms de vos compétences

radar_chart(name, stats, labels)
