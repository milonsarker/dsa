# https://leetcode.com/problems/calculate-parking-fees-and-duration/
# Write your MySQL query statement below

with cte_lot as 
(
    select * , rank() over (partition by car_id order by tot_time desc) as rnk
        from (select car_id, lot_id, sum(TIMESTAMPDIFF(SECOND, entry_time, exit_time)/3600) tot_time
                from ParkingTransactions
                group by car_id, lot_id
             ) a
), 
cte_fee as
(
    select  car_id, 
            sum(fee_paid) total_fee_paid , 
            round(sum(fee_paid) / sum(TIMESTAMPDIFF(SECOND, entry_time, exit_time)/3600), 2) avg_hourly_fee
        from ParkingTransactions
        group by car_id
)
select a.car_id, a.total_fee_paid, a.avg_hourly_fee, b.lot_id most_time_lot
    from cte_fee a 
    join cte_lot b
    on (a.car_id = b.car_id)
    where b.rnk = 1
    order by car_id
    ;
