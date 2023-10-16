function sortedSquares(nums: number[]): number[] {
    let len = nums.length;
    let result: number[] = new Array(len).fill(0);

    let left_index = 0;
    let right_index = len - 1;
    let index = right_index;
    
    let left_square = -1;
    let right_square = -1;
    
    while (index >= 0) {
        left_square = nums[left_index] ** 2;
        right_square = nums[right_index] ** 2;
        if(left_square < right_square){
            result[index] = right_square;
            --right_index;
        }
        else{
            result[index] = left_square;
            ++left_index;
        }
        --index;
    }
    return result;
};
/*function sortedSquares(nums: number[]): number[] {
    let right_index = nums.length - 1;
    if(right_index == 0){
        nums[right_index] = nums[right_index] ** 2;
        return nums;
    }
    while (right_index > 0 && nums[right_index - 1] ** 2 <= nums[right_index] ** 2) {
        let left_square = nums[0] ** 2;
        let right_square = nums[right_index] ** 2;
        if(left_square > right_square){ 
            nums[0] = nums[right_index];
            nums[right_index] = left_square;
            --right_index;
        }
        else{
            nums[right_index] = nums[right_index] ** 2;
            --right_index
        }
    }
    let i = 0;
    let middle = Math.floor((right_index + 1) / 2)
    for (i;i < middle; ++i) {
        let temp = nums[i] ** 2;
        nums[i] = nums[right_index - i] ** 2 ;
        nums[right_index - i] = temp;
    };
    if (right_index % 2 == 0) {
        nums[middle] = nums[middle] ** 2;
    }
    return nums;
};
*/
let nums: number[] = [-7,-3,2,3,11]
console.log(sortedSquares(nums));
