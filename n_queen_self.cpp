#include<bits/stdc++.h>
using namespace std;

bool isSafe(vector<string> board, int row, int col, int n) {
    for(int i = row, j = col; i >= 0 and j >= 0; i--, j--) {
        if(board[i][j] == 'q') {
            return false;
        }
    }

    for(int i = 0; i < row; i++) {
        if(board[i][col] == 'q') {
            return false;
        }
    }

    for(int i = row, j = col; i >= 0 and j < n; i--, j++) {
        if(board[i][j] == 'q') {
            return false;
        }
    }
    return true;
}

void solveNQueens(int row, int n, vector<string> &board, vector<vector<string>> &res) {
    if(row == n) {
        res.push_back(board);
        return;
    }

    for(int col = 0; col < n; col++) {
        if(isSafe(board, row, col, n)) {
            board[row][col] = 'q';
            solveNQueens(row + 1, n, board, res);
            board[row][col] = '.';
        }
    }
}

void solveNQueensBnB(int row, int n, vector<string> &board, vector<vector<string>> &res, vector<int> cols, vector<int> diag1, vector<int> diag2) {
    if(row == n) {
        res.push_back(board);
        return;
    }

    for(int col = 0; col < n; col++) {
        if(cols[col] == 0 and diag1[row + col] == 0 and diag2[row - col + n-1] == 0) {
            board[row][col] = 'q';
            cols[col] = diag1[row + col] = diag2[row - col + n-1] = 1;
            solveNQueensBnB(row+1, n, board, res, cols, diag1, diag2);
            board[row][col] = '.';
            cols[col] = diag1[row + col] = diag2[row - col + n-1] = 0;
        }
    }
}

void printBoard(vector<string> &board) {
    for (string row : board) {
        cout << row << endl;
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter value of n:";
    cin >> n;

    vector<string> board(n, string(n, '.'));
    vector<vector<string>> res;

    vector<int> cols(n,0);
    vector<int> diag1(2 * n-1, 0);
    vector<int> diag2(2 * n-1, 0);

    // solveNQueens(0, n, board, res);
    solveNQueensBnB(0, n, board, res, cols, diag1, diag2);
    cout << "All possible solutions for N-Queens problem are: " << endl;

    for (vector<string> board : res) {
        printBoard(board);
    }
    return 0;
}