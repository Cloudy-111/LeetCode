# Problem:

Alice and Bob are playing a game on a string.

You are given a string s, Alice and Bob will take turns playing the following game where Alice starts first:

- On Alice's turn, she has to remove any non-empty substring from s that contains an odd number of vowels.
- On Bob's turn, he has to remove any non-empty substring from s that contains an even number of vowels.

The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play optimally.

Return true if Alice wins the game, and false otherwise.

The English vowels are: a, e, i, o, and u.

# Solution:

Alice always goes first, with strings without vowels, Alice will lose

With strings with vowels, we will divide them into 2 types of strings, strings with even vowels and strings with odd vowels:

- With strings with odd vowels, Alice will take the whole string and win
- With strings with even vowels (assuming the number of vowels is n), Alice goes first and takes the string containing n - 1 vowels. The remaining part of the string will only have 1 vowel and x consonants.

- With x equal to 0, Bob will not be able to take any more strings with even vowels and Alice wins.
- With x different from 0, Bob will take all the consonants and leave 1 vowel, Alice will take more and Bob cannot take any more, Alice wins

### So in summary, strings without vowels, Alice loses, strings with vowels, Alice will always win
