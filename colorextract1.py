import cv2


img = cv2.imread('strip_images/image1.jpg', cv2.IMREAD_UNCHANGED)

height, width, channel = img.shape
cx = int(width / 2 + 30)
cy = int(height / 2 + 40)

response = {}
strip_para = ['leukocytes', 'nitrite', 'urobilinogen', 'protein', 'pH', 'Haemoglobin', 'specific_gravity', 'ketone', 'bilirubin', 'glucose']
for i in range(10):
    pixel_center = img[cy, cx]
    r, g, b = pixel_center[0], pixel_center[1], pixel_center[2]
    
    response.update({f'{strip_para[i]}':[r, g, b]})
    cv2.circle(img, (cx, cy), 5, (255, 0, 0), 3)
    cy -= 73

print(response)
cv2.destroyAllWindows()