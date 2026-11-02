
# -*- coding: utf-8 -*-
"""
OpenCV:
1. Contours
2. Contour Approximation
3. Convex Hull
4. Convexity Defects
5. Extreme Points
"""

import cv2
import numpy as np


# --------------------------------
# 1. READ IMAGE
# --------------------------------

img = cv2.imread("hand.jpg")

if img is None:
    raise FileNotFoundError("hand.jpg not found!")

img = cv2.resize(img, (600, 700))

# Convert to grayscale
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# --------------------------------
# 2. IMAGE PREPROCESSING
# --------------------------------

blur = cv2.medianBlur(img1, 11)

ret, thresh = cv2.threshold(
    blur,
    240,
    255,
    cv2.THRESH_BINARY_INV
)

# --------------------------------
# 3. FIND CONTOURS
# --------------------------------

cnts, hier = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


if len(cnts) == 0:

    print("No contours found!")

else:

    # Find largest contour
    c_max = max(cnts, key=cv2.contourArea)

    print("Largest contour area:", cv2.contourArea(c_max))


    # --------------------------------
    # 4. CONTOUR APPROXIMATION + HULL
    # --------------------------------

    for c in cnts:

        epsilon = 0.0001 * cv2.arcLength(c, True)

        data = cv2.approxPolyDP(
            c,
            epsilon,
            True
        )

        hull = cv2.convexHull(data)

        # Draw original contour
        cv2.drawContours(
            img,
            [c],
            -1,
            (50, 50, 150),
            2
        )

        # Draw convex hull
        cv2.drawContours(
            img,
            [hull],
            -1,
            (0, 255, 0),
            2
        )


    # --------------------------------
    # 5. CONVEXITY DEFECTS
    # --------------------------------

    # Get hull indices, not coordinates
    hull2 = cv2.convexHull(
        c_max,
        returnPoints=False
    )

    if hull2 is not None and len(hull2) >= 3:

        defect = cv2.convexityDefects(
            c_max,
            hull2
        )

        if defect is not None:

            print("\nDefect shape:", defect.shape)
            print("Defect ndim:", defect.ndim)

            # Each defect must contain:
            # start, end, farthest point, distance

            defects = np.asarray(defect).reshape(-1, 4)

            for i, (s, e, f, d) in enumerate(defects):

                s = int(s)
                e = int(e)
                f = int(f)
                d = int(d)

                print(
                    f"Defect {i}: "
                    f"Start={s}, "
                    f"End={e}, "
                    f"Far={f}, "
                    f"Distance={d / 256.0:.2f}px"
                )

                # Get contour coordinates
                start = tuple(c_max[s][0])
                end = tuple(c_max[e][0])
                far = tuple(c_max[f][0])

                # Draw line between start and end
                cv2.line(
                    img,
                    start,
                    end,
                    (255, 0, 0),
                    2
                )

                # Draw farthest point
                cv2.circle(
                    img,
                    far,
                    5,
                    (0, 0, 255),
                    -1
                )

        else:

            print("No convexity defects found!")

    else:

        print("Not enough convex hull points!")


    # --------------------------------
    # 6. EXTREME POINTS
    # --------------------------------

    # Leftmost point
    extLeft = tuple(
        c_max[c_max[:, :, 0].argmin()][0]
    )

    # Rightmost point
    extRight = tuple(
        c_max[c_max[:, :, 0].argmax()][0]
    )

    # Topmost point
    extTop = tuple(
        c_max[c_max[:, :, 1].argmin()][0]
    )

    # Bottommost point
    extBot = tuple(
        c_max[c_max[:, :, 1].argmax()][0]
    )


    # --------------------------------
    # 7. DRAW EXTREME POINTS
    # --------------------------------

    cv2.circle(img, extLeft, 8, (255, 0, 255), -1)

    cv2.circle(img, extRight, 8, (0, 125, 255), -1)

    cv2.circle(img, extTop, 8, (255, 10, 0), -1)

    cv2.circle(img, extBot, 8, (19, 152, 152), -1)


# --------------------------------
# 8. DISPLAY RESULTS
# --------------------------------

cv2.imshow("Original + Contours + Hull + Defects", img)

cv2.imshow("Grayscale", img1)

cv2.imshow("Threshold", thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()
