public class Solution {
    public string[] Spellchecker(string[] wordlist, string[] queries) {
        HashSet<string> words = new HashSet<string>(wordlist);

        Dictionary<string, string> lowerCase = new Dictionary<string, string>();
        Dictionary<string, string> vowelError = new Dictionary<string, string>();

        foreach(string word in wordlist){
            string lower = word.ToLower();
            if(!lowerCase.ContainsKey(lower)){
                lowerCase[lower] = word;
            }

            string pattern = pattern_word(word.ToLower());
            if(!vowelError.ContainsKey(pattern)){
                vowelError[pattern] = word;
            }
        }

        List<string> res = new List<string>();
        foreach(string query in queries){
            if(words.Contains(query)){
                res.Add(query);
            } else if(lowerCase.ContainsKey(query.ToLower())){
                res.Add(lowerCase[query.ToLower()]);
            } else {
                string pattern = pattern_word(query.ToLower());
                if(vowelError.ContainsKey(pattern)){
                    res.Add(vowelError[pattern]);
                } else {
                    res.Add("");
                }
            }
        }

        return res.ToArray();
    }

    public string pattern_word(string word){
        char[] arr = word.ToCharArray();
        for(int i = 0; i < arr.Length; i++){
            if("aeiou".Contains(arr[i])){
                arr[i] = '_';
            }
        }
        return new string(arr);
    }
}