public class Solution {
    public int MaxFreqSum(string s) {
        int[] characters = new int[26];
        int max_vowel = 0;
        int max_consonant = 0;

        for(int i = 0; i < s.Length; i++){
            characters[s[i] - 'a'] += 1;
            if("aiueo".Contains(s[i])){
                max_vowel = Math.Max(max_vowel, characters[s[i] - 'a']);
            } else {
                max_consonant = Math.Max(max_consonant, characters[s[i] - 'a']);
            }
        }

        return max_consonant + max_vowel;
    }
}