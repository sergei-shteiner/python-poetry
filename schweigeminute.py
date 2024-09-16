import time
import numpy as np
import matplotlib.pyplot as plt
import moviepy.editor as mpy

# Funktion zum Erstellen eines Frames mit der gewünschten Anzahl von Wörtern
def make_frame(t):
    plt.figure(figsize=(8, 8), facecolor='black')
    
    # Erzeugen eines Kreises
    circle = plt.Circle((0.5, 0.5), 0.4, color='black', fill=False, edgecolor='white')
    plt.gca().add_artist(circle)
    plt.gca().set_facecolor('black')
    
    # Anzahl der Wörter, die zu einem bestimmten Zeitpunkt angezeigt werden sollen (ein Wort pro Sekunde)
    num_words = int(t)
    
    # Platzieren der Wörter "schweigen" im Kreis
    for i in range(num_words):
        angle = -2 * np.pi * i / 60 + np.pi / 2  # Verschieben des Winkels um -90 Grad, um oben zu beginnen
        x = 0.5 + 0.4 * np.cos(angle)
        y = 0.5 + 0.4 * np.sin(angle)
        plt.text(x, y, 'schweigen', fontsize=8, rotation=np.degrees(angle), ha='center', va='center', color='white')
    # Achsen ausblenden
    plt.axis('off')
    
    # Frame als Bild speichern
    plt.savefig('frame_{:02d}.png'.format(num_words), dpi=300, facecolor='black')
    plt.close()
    time.sleep(1)

# Video erstellen
duration = 60  # Dauer des Videos in Sekunden
fps = 1  # 1 Frame pro Sekunde (da jede Sekunde ein neues Wort hinzugefügt wird)

# Frames generieren
for t in range(1, duration + 1):
    make_frame(t)

# Liste von Bildern für das Video erstellen
frames = ['frame_{:02d}.png'.format(i) for i in range(1, duration + 1)]

# Moviepy verwenden, um das Video zu erstellen
video = mpy.ImageSequenceClip(frames, fps=fps)

# Video speichern
video.write_videofile("schweigeminute.mp4", fps=fps)
