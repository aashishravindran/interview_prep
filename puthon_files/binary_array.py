# //Step 1: reverse the entire array.
#     //Step 2: reverse each word.
#     //time: O(2n) ... O(N)
#     //space: O(1) ... linear.


# public class ReverseWordsArray {
#   char[] reverseWords(char[] a) {

#     reverse(a, 0, a.length - 1); //step 1

#     int start = 0,  end = 0;
#     while (end < a.length) { //step 2
#       if (a[end] == ' ') {
#         reverse(a, start, end - 1);
#         start = end + 1;
#       }
#       end++;
#     }
#     reverse(a, start, a.length - 1);    //edge case, last word
#     return a;
#   }


#   void reverse(char[] a, int l, int r) {
#     while (l < r) {
#       char temp = a[l];
#       a[l++] = a[r];
#       a[r--] = temp;
#     }
#   }
# }
text1 = "abcde"
text2 = "ace" 
dp_arr=[[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        