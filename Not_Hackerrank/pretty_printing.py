def minimum_messiness(words, line_length):

    num_remaining_blanks = line_length - len(words[0])
    # min_messiness[i] is the minimum messiness when placing words[0:i + 1].
    min_messiness = ([num_remaining_blanks**2] + [float('inf')] *
                     (len(words) - 1))
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks**2
        # Try adding words[i - 1], words[i - 2], ...
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                # Not enough space to add more words.
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                   first_j_messiness + current_line_messiness)
    return min_messiness

word_arr = ['Pier', 'likes', 'to', 'code', 'and', 'play', 'the', 'guitar']
min_mess = minimum_messiness(word_arr, 10)
print(min_mess)

min_so_far = min_mess[0]
print(word_arr[0], end=' ')
for x in range(1, len(word_arr)):
    if min_mess[x] > min_so_far:
        min_so_far = min_mess[x] 
        print('') # newline printed
    print(word_arr[x], end=' ')
	
