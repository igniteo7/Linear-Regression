S = 50
def main():

    x = [0] * (S + 1)
    y = [0] * (S + 1)
    sumX = 0
    sumX2 = 0
    sumY = 0
    sumXY = 0

    n = int(input("How many data points? "))

    print("Enter data:")

    for i in range(1, n + 1):
        x[i] = float(input(f"x[{i}] = "))
        y[i] = float(input(f"y[{i}] = "))

    for i in range(1, n + 1):
        sumX += x[i]
        sumX2 += x[i] * x[i]
        sumY += y[i]
        sumXY += x[i] * y[i]

    b = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX)
    a = (sumY - b * sumX) / n
    rounded_b = round(b,4)
    rounded_a = round(a,4)
    print(f"Calculated value of a is {rounded_a} and b is {rounded_b}")
    print(f"Equation of best fit is: y = {rounded_a} + {rounded_b}x")

if __name__ == "__main__":
    main()

