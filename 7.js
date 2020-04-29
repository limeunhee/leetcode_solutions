var reverse = function(x) {
    var x_char = x.toString().split("")
    var output = []
    var out=""
    
    if (x_char.length===1){
        return x
    }   
    
    for (i=1; i<x_char.length-1; i++){
            output.unshift(x_char[i])
    }

    if (x_char[x_char.length-1]!=='0'){
        output.unshift(x_char[x_char.length-1])
    }
    
    
    if (x_char[0]==='-'){
        output.unshift('-')
    }else{
        output.push(x_char[0])
    }
    
    out = output.join("")
        
    if (out<=-1*Math.pow(2,31) || out>(Math.pow(2,31))){
        return 0
    }
    return out
    }
};
