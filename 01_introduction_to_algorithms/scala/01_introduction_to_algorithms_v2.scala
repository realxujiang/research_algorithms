def binarySearch(list: List[Int], item: Int): Int = {
    if(list.isEmpty) { println("item not found."); return 0 }
    val guessIndex = (list.length)/2
    val guess = list(guessIndex)
    if(guess == item) guessIndex
    else if(guess > item) {
        val halfList = list.take(list.length/2)
        binarySearch(halfList, item)
    } 
    else {
        val halfList = list.drop((list.length/2) + 1)
        binarySearch(halfList, item)
    }
}

val myList = List(1,3,5,7,9)
println(binarySearch(myList, 3))
println(binarySearch(myList, -1))
