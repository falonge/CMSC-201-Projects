if __name__ == '__main__':
    numbers = [75, 635, 274, 353, 534, 684, 381, 67, 968, 155, 502, 149, 10, 789, 757, 379, 732, 386, 692, 473, 797,
               272, 538, 703, 629, 179, 197, 521, 411, 590, 818, 892, 896, 951, 365, 800, 767, 651, 584, 220, 584, 221,
               23, 819, 794, 957, 74, 985, 395, 544, 324, 464, 980, 293, 980, 208, 560, 651, 710, 21, 322, 968, 610,
               947, 622, 369, 504, 113, 785, 119, 46, 332, 137, 865, 127, 333, 83, 403, 696, 771, 733, 811, 220, 451,
               559, 446, 895, 90, 591, 257, 506, 208, 432, 197, 16, 344, 261, 830, 115, 924, 288, 442, 464, 213, 409,
               815, 495, 205, -123, 147, 930, 69, 188, 419, 880, 815, 291, 646, 464, 888, 310, 228, 529, 218, 565, 642,
               315, 328, 288, 374, 208, 830, 834, 879, 75, 983, 112, 556, 736, 211, 582, 437, 717, 833, 719, 684, 518,
               517, 744, 350]
    
    #setting up variables for my 3 ending values
    average = 0
    largest_value = numbers[0]
    smallest_value = numbers[0]
    for number in numbers:
            average +=  number
            if largest_value < number:
                largest_value = number
            elif smallest_value > number:
                smallest_value = number
    average /= (len(numbers))
    print("The average is", average)
    print("The largest value is", largest_value)
    print("The smallest value is", smallest_value)
