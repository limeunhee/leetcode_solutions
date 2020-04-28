var majorityElement = function(nums) {
    var obj={};
    for (var i=0; i<nums.length;i++){
        if (obj[nums[i]]===undefined){
            obj[nums[i]] = 1
        } else{
            obj[nums[i]] +=1
        }
    }
    
    var max;
    var max_count=0
    for (var key in obj){
        if (obj[key]>=max_count){
            max = key
            max_count = obj[key]
        }
    }
    return max
};
