def count_characters(start, end, arr):
    cnt = 0
    for i in range(start, end + 1):
        cnt += len(arr[i])
    return cnt


# function to fill the end of str with spaces
def pad_line(s, W):
    len_s = len(s)
    return s + ' ' * (W - len_s)


# function to form a line using all the words in range [start, end]
# and justify the line to push it to the result
def justify(start, end, arr, W):
    justified_line = ""
    words_cnt = end - start + 1

    # If the line has only 1 word, then pad it with spaces and return it
    if words_cnt == 1:
        return pad_line(arr[start], W)

    space_cnt = W - count_characters(start, end, arr)
    space = " "
    extra_spaces = 0

    # If the line is not the last line, then all words should have
    # even spaces between them and all the extra spaces will be
    # added to the spaces to the left
    if end != len(arr) - 1:
        space = ' ' * (space_cnt // (words_cnt - 1))
        extra_spaces = space_cnt % (words_cnt - 1)

    for i in range(start, end + 1):
      
        # Add the word to the justified line
        justified_line += arr[i]

        # add spaces to the justified line
        if i < end:
            justified_line += space

            # If there are extra spaces, add it to the spaces to the left
            if extra_spaces > 0:
                justified_line += ' '
                extra_spaces -= 1

    # Remove extra spaces from the right end
    justified_line = justified_line[:W]

    # Pad line with spaces if we have empty space to the right
    return pad_line(justified_line, W)


# function to get the end index such that all the words from
# start to end can be placed in one line
def get_end(start, arr, W):
    end = start + 1
    len_words = len(arr[start])
    while end < len(arr) and (len_words + 1 + len(arr[end])) <= W:
        len_words += len(arr[end]) + 1
        end += 1
    return end - 1

# function to combine the words to each line and justify the line
# from both sides
def justify_text(arr, W):
    start = 0
    justified_text = []

    while start < len(arr):
        # find the ending index such that words in the range
        # [start, end] can be put in a single line
        end = get_end(start, arr, W)

        # Form a line using words from start to end and justify it
        justified_line = justify(start, end, arr, W)

        # Push the justified line to the result
        justified_text.append(justified_line)
        start = end + 1

    return justified_text

if __name__ == "__main__":
    arr = ["GfG", "is", "the", "best", "computer",
           	"science", "portal", "for", "geeks."]
    W = 16

    ans = justify_text(arr, W)
    for line in ans:
        print(line)
