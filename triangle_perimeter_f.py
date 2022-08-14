def triangle_perimetr(side_lengths):
    for i in range(len(side_lengths) - 2):
        if side_lengths[i] < side_lengths[i + 1] + side_lengths[i + 2]:
            return side_lengths[i] + side_lengths[i + 1] + side_lengths[i + 2]
        else:
            i += 1


if __name__ == "__main__":
    number_of_segments = input()
    side_lengths = sorted([int(x) for x in input().split()], reverse=True)
    print(triangle_perimetr(side_lengths))
