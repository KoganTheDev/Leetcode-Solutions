#define MIN(x, y) (x > y ? y : x)
#define MY_INFINITY (999999)

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        auto min_distances_to_last_row = min_distances_to_row(triangle);
        int min_all = MY_INFINITY;
        for (int path_distance : min_distances_to_last_row)
        {
            min_all = MIN(min_all, path_distance);
        }

        return min_all;
    }

    vector<int> min_distances_to_row(vector<vector<int>>& triangle)
    {
        if (triangle.size() == 1)
        {
            return triangle[0];
        }

        vector<vector<int>> triangle_without_last_row = vector<vector<int>>(triangle.begin(), triangle.end() - 1);
        vector<int> all_min_paths_prev = min_distances_to_row(triangle_without_last_row);

        vector<int> min_paths_last_row;

        vector<int> last_row = *(triangle.end() - 1);

        for (int i = 0; i < last_row.size(); i++)
        {
            int option1 = i >= 1 ? all_min_paths_prev[i - 1] : MY_INFINITY;
            int option2 = i < last_row.size() - 1 ? all_min_paths_prev[i] : MY_INFINITY;

            min_paths_last_row.push_back(MIN(option1, option2) + last_row[i]);
        }

        return min_paths_last_row;
    }
};