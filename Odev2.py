import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)

# HSV renk aralığını ayarla
lower_red = (0, 100, 100)
upper_red = (10, 255, 255)

while True:
    # Görüntü yakala
    ret, frame = cap.read()

    # Görüntüyü hsv formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Maske oluştur
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Maskelenmiş görüntüyü göster
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    # Çıkmak için q ya bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()