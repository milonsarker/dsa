//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution
{
    public:
        int maxProfit(vector<int>& prices)
        {
            int min_price = INT_MAX;
            int max_profit = 0;
            for ( int i = 0; i < prices.size(); i++ )
            {
                if ( min_price > prices[i] )
                {
                    min_price = prices[i];
                }
                if ( prices[i] - min_price  > max_profit )
                {
                    max_profit = prices[i] - min_price;
                }
            }
            return max_profit;
        }
};