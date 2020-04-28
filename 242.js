var isAnagram = function(s, t) {
    var s_char = s.split("")
    var t_char = t.split("")
    
    if (s_char.length ===0 && t_char.length ===0){
        return true
    }
    
    if (s_char.length !==t_char.length){
        return false
    }
    
    var obj={}
    
    for (var i=0; i<s_char.length; i++){
        if (obj[s_char[i]] === undefined){
                obj[s_char[i]]=1
        }
        else{
                obj[s_char[i]]+=1
            }
    }
    
    for (var j=0; j<t_char.length; j++){
        if (obj[t_char[j]] === undefined){
                obj[t_char[j]]=-1
        }
        else{
                obj[t_char[j]]-=1
            }
    }

    for (var key in obj){
        console.log(obj[key])
        if (obj[key]!==0){
            return false
        }
    }
    return true
};
