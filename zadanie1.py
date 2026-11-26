import urllib.request
import cv2
import matplotlib.pyplot as plt

url = "https://upload.wikimedia.org/wikipedia/commons/e/e3/Oranges_-_whole-halved-segment.jpg"

zapytanie = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(zapytanie) as odpowiedz, open("orange.jpg", "wb") as plik:
    plik.write(odpowiedz.read())

obraz = cv2.imread("orange.jpg")
obraz_rgb = cv2.cvtColor(obraz, cv2.COLOR_BGR2RGB)

plt.imshow(obraz_rgb)
plt.axis("off")
plt.savefig("01_oryginal.png")
print("Obraz pobrany i zapisany jako 01_oryginal.png")

wysokosc, szerokosc, _ = obraz.shape

nowa_szerokosc = int(szerokosc / 2)
nowa_wysokosc = int(wysokosc / 2)

obraz_maly = cv2.resize(obraz, (nowa_szerokosc, nowa_wysokosc))

obraz_szary = cv2.cvtColor(obraz_maly, cv2.COLOR_BGR2GRAY)

obraz_obrocony = cv2.rotate(obraz_szary, cv2.ROTATE_90_CLOCKWISE)

plt.figure()
plt.imshow(obraz_obrocony, cmap="gray")
plt.axis("off")
plt.savefig("01_szary_obrot_zmniejszenie.png")

print("Zapisano 01_szary_obrot_zmniejszenie.png")

print("Macierz obrazu (siatka pikseli):")
print(obraz_obrocony)