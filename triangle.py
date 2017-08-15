def max_path_sum(triangle, row=0, col=0):
    # Base case
    if row == len(triangle)-1:
        return triangle[row][col]
    # Recursive case
    max_left = max_path_sum(triangle, row+1, col)
    max_right = max_path_sum(triangle, row+1, col+1)
    return triangle[row][col] + max(max_left, max_right)


def load_triangle(filename='test_triangle.txt'):
    triangle = []
    with open(filename, 'r') as f:
        for line in f:
            triangle.append([int(item) for item in line.split()])
    return triangle


def main():
    triangle = load_triangle()
    print(max_path_sum(triangle))

if __name__ == "__main__":
    main()
