def compute_n_moment(stream, n):
    if n <= 0:
        return None  # Invalid input for n

    num_values = 0
    sum_of_powers = 0

    for value in stream:
        num_values += 1
        sum_of_powers += value ** n

    if num_values == 0:
        return None  # Empty stream

    nth_moment = sum_of_powers / num_values

    return nth_moment

def main():
    # Example: Compute the 2nd moment for a stream of numbers
    stream = [1, 2, 3, 4, 5]
    n = 3

    nth_moment = compute_n_moment(stream, n)

    if nth_moment is not None:
        print(f"{n}-th Moment: {nth_moment}")
    else:
        print("Invalid input or empty stream.")

if __name__ == "__main__":
    main()
