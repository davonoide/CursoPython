import cv2


# Cargar el clasificador Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen de la máscara con transparencia
mask = cv2.imread('filtro_sencillo/spidy.png', cv2.IMREAD_UNCHANGED)

# Función para superponer una imagen sobre otra
def overlay_image_alpha(img, img_overlay, x, y, alpha_mask):
    """Overlay img_overlay on top of img at (x, y) and blend using alpha_mask."""
    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if there is no overlap
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    # Blend overlay within the determined ranges
    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o, None] / 255.0

    img_crop[:] = (1.0 - alpha) * img_crop + alpha * img_overlay_crop

# Capturar el video de la cámara
cap = cv2.VideoCapture(0)

# Variable para ajustar el tamaño de la imagen de la máscara
scale = 1.8  # Ajusta esta variable para cambiar el tamaño de la máscara

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Ajustar el tamaño de la máscara con la variable scale
        new_w = int(w * scale)
        new_h = int(h * scale)
        mask_resized = cv2.resize(mask, (new_w, new_h), interpolation=cv2.INTER_AREA)

        # Calcular las nuevas coordenadas para centrar la máscara sobre el rostro
        x_offset = x - (new_w - w) // 2
        y_offset = y - (new_h - h) // 2

        # Superponer la máscara en la posición detectada del rostro
        overlay_image_alpha(frame, mask_resized[:, :, :3], x_offset, y_offset, mask_resized[:, :, 3])

    cv2.imshow('Mask Overlay', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()