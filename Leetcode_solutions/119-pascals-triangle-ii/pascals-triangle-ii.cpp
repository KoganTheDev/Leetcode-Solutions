class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0)
            return vector<int> {1};

        vector<int> last_row = this->getRow(rowIndex - 1);
        vector<int> next_row = {1};

        for (int i = 0; i < last_row.size() - 1; i++)
        {
            next_row.push_back(last_row[i] + last_row[i + 1]);
        }

        next_row.push_back(1);

        return next_row;
    }
};