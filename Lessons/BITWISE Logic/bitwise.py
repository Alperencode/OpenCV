import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("image_1.png")

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# === BITWISE Logic === #

# The Logic And
# 0 and 0 = 0
# 1 and 0 = 0
# 0 and 1 = 0
# 1 and 1 = 1

# The Logic Or
# 0 or 0 = 0
# 1 or 0 = 1
# 0 or 1 = 1
# 1 or 1 = 1

# The Logic XOR
# 0 xor 0 = 0
# 1 xor 0 = 1
# 0 xor 1 = 1
# 1 xor 1 = 0

# The Logic Not
# 1 not = 0
# 0 not = 1
# Opposite

# === BITWISE Logic === #

# === Quick Tips === #

# And
# If it has 0 result will be 0

# Or
# If it has 1 result will be 1

# Xor
# If it has same number result will be 0 - If its not same result will be 1

# Not
# Its always opposite and taking 1 argument --- Taking zeros and result = 1 --- Taking ones and result = 0
