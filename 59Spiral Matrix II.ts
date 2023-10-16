function generateMatrix(n: number): number[][] {
    const array_s: number[][] = [];
    for (let i = 0; i < n; i++) {
        const row: number[] = [];
        for (let j = 0; j < n; j++) {
            // 在这里可以设置每个元素的初始值
            row.push(0); // 这里将所有元素初始化为0
        }
        array_s.push(row);
    }
    if(n == 1){
        return [[1]]
    }
    if(n == 2){
        return [[1,2],[3,4]]
    }
    let index = 0;
    for(let j = 0;j < Math.ceil(n/2);j++){
        for(let i = j;i < n - j;i++){
            if(n/2 == j + 0.5){
                array_s[j][j] = n*n
                break;
            }
            array_s[i][n - 1 - j] = i - j + n - 2* j + index;
            array_s[n - 1 - j][i] = 3 * n - 6 * j - 2 - (i - j) + index;
            array_s[i][j] = 4 * n - 8 * j - 3 - (i - j) + index;
            array_s[j][i] = i - j + 1 + index;
        }
        index = 4 * n - 4 * j - 4 + index;
    }
    return array_s;
};

console.log(generateMatrix(4))