'''
Problem:Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row =  [0]*len(matrix)
        col = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j]=0
'''
Java Solution:

    public class Solution {
        public void setZeroes(int[][] matrix) {
            boolean[] row = new boolean[matrix.length];
            boolean[] col = new boolean[matrix[0].length];
            
            for(int i=0;i<matrix.length;i++){
                for(int j=0;j<matrix[0].length;j++){
                    if (matrix[i][j]==0){
                        row[i]= true;
                        col[j]= true;
                    }
                }
            }
            
            for(int i=0;i<matrix.length;i++){
                for(int j=0;j<matrix[0].length;j++){
                    if(row[i]||col[j]){
                        matrix[i][j]=0;
                    }
                }
            }
        }
    }
'''

'''
Test Case:
'''
if __name__ == '__main__':
    