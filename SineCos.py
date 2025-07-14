# Write a Python program to use the math module to calculate the sine, cosine, and tangent of a given angle.


from math import sin, cos, tan, radians

def calculate_trigonometric_ratios(angle):
    rad = radians(angle)

    sine = sin(rad)
    cosine = cos(rad)

    if angle == 90 or angle == 270:
        tangent = "undefined"
    else:
        tangent = tan(rad)

    return sine, cosine, tangent

def main():
    angle = int(input("Enter angle in degrees: "))

    sine, cosine, tangent = calculate_trigonometric_ratios(angle)

    print(f"Sin({angle}°): {sine:.4f}" if isinstance(sine, float) else f"Sin({angle}°): {sine}")
    print(f"Cos({angle}°): {cosine:.4f}" if isinstance(cosine, float) else f"Cos({angle}°): {cosine}")
    print(f"Tan({angle}°): {tangent:.4f}" if isinstance(tangent, float) else f"Tan({angle}°): {tangent}")

if __name__ == "__main__":
    main()
