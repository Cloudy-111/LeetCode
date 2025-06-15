public class Solution {
    public int MaxDiff(int num) {
        string strNum = num.ToString();

        int maxNum = turnMax(strNum);
        int minNum = turnMin(strNum);
        return maxNum - minNum;
    }

    public int turnMax(string strNum){
        for(int i = 0; i < strNum.Length; i++){
            if(strNum[i] != '9'){
                strNum = strNum.Replace(strNum[i], '9');
                break;
            }
        }
        int res = int.Parse(strNum);
        return res;
    }

    public int turnMin(string strNum){
        if(strNum[0] != '1') return int.Parse(strNum.Replace(strNum[0], '1'));
        else{
            for(int i = 1; i < strNum.Length; i++){
                if(strNum[i] != '0' && strNum[i] != '1'){
                    strNum = strNum.Replace(strNum[i], '0');
                    break;
                }
            }
            int res = int.Parse(strNum);
            return res;
        }
    }
}