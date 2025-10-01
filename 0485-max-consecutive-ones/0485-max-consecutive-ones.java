class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int len=nums.length,max=0,temp=0;
        for(int i=0;i<len;i++){
            if (nums[i]==1){
                temp+=1;
            }
            else{
                if(temp>max){
                    max=temp;
                }
                temp=0;
            }
        }
        if(temp>max){
            max=temp;}
        return max;
    }
}