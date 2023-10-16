function minSubArrayLen(target: number, nums: number[]): number {
    let left_index = 0;
    let right_index = 0;
    let total = 0;
    let result = Infinity;

    while (right_index < nums.length || total >= target) {
        if(total < target){
            total += nums[right_index++];
        }
        else{
            result = Math.min(result, right_index - left_index);
            total -= nums[left_index];
            ++left_index;
        }
    }
    if(result != Infinity){
        return result;
    }
    return 0;
};

var num = [1, 4, 4];
var target = 4;
console.log(minSubArrayLen(target, num));
