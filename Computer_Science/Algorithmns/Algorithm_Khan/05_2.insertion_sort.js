var insert = function(array, rightIndex, value) {
    for(var j = rightIndex;
        j >= 0 && array[j] > value;
        j--) {
        array[j + 1] = array[j];
    }   
    array[j + 1] = value; 
};

var insertionSort = function(array) {
    for(var flag = 1;
        flag < array.length;
        flag++){
        insert(array, flag-1, array[flag]);
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [7, 9, 11, 22, 42, 88, 99]);


var array = [22, 11, 99, 88, 9, -1, 0];
insertionSort(array);
println("Array after sorting:  " + array);
Program.assertEqual(array, [-1,0, 9, 11, 22, 88, 99]);
