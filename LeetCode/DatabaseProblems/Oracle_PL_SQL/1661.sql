--https://leetcode.com/problems/average-time-of-process-per-machine/

/* Write your PL/SQL query statement below */

select a.machine_id, round(avg(b.timestamp - a.timestamp),3) processing_time
    from
        (select * from activity where activity_type = 'start') a
        join
        (select * from activity where activity_type = 'end') b
    on (a.machine_id = b.machine_id and a.process_id = b.process_id)
    group by a.machine_id;