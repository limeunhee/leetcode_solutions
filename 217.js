var containsDuplicate = function(nums) {
    var obj={}
    for (var i=0; i<nums.length; i++){
        if (obj[nums[i]]===undefined){
            obj[nums[i]]=1
        }
        else{
            return true
        }
    }
    return false
};
