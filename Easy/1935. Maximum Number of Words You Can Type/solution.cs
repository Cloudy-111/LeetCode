public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        int counter = 0;
        
        string[] words = text.Split(" ");
        foreach(string word in words){
            foreach(char c in word){
                if(brokenLetters.Contains(c)){
                    counter += 1;
                    break;
                }
            }
        }

        return words.Length - counter;
    }
}