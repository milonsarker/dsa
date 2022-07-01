//https://leetcode.com/problems/reshape-the-matrix/

class Solution
{
    public:
        vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c)
        {
            int m = mat.size();
            int n = mat[0].size();
            if ( m * n != r * c)
            {
                return mat;
            }
            vector < vector <int>> result_mat;
            vector <int> row;
            int k = m * n;
            int one_d[k];
            int cntr = 0;
            for (int i = 0; i < m; i++)
            {
                for ( int j = 0; j < n; j++ )
                {
                    one_d[cntr] = mat[i][j];
                    cntr++;
                }
            }
            cntr = 0;
            for (int i = 0; i < r; i++)
            {
                for ( int j = 0; j < c; j++ )
                {
                    row.push_back(one_d[cntr]);
                    if (j == c -1)
                    {
                        result_mat.push_back(row);
                        row.clear();
                    }

                    cntr++;
                }
            }
            return result_mat;
        }
};