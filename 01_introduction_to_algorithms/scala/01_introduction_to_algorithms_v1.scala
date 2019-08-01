def binarySearch(list: List[Int], item: Int): Int = {
    if(list.isEmpty) { println("Item not found."); return 0 }
    var low = 0
    var high = list.length
    while(low <= high) {
        val mid = (low + high)/2
        val guess = list(mid)
        if (guess == item) { 
            return mid 
        }
        if (guess > item) {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    println("Item not found."); return 0
}

val myList = List(1,3,5,7,9)

println(binarySearch(myList, 3)) // => 1
println(binarySearch(myList, -1)) // => None
