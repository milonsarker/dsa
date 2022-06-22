--https://leetcode.com/problems/tasks-count-in-the-weekend/

/* Write your PL/SQL query statement below */
select sum(
            case when to_char(submit_date,'DY') in ('SAT', 'SUN')
                then 1
                else 0
            end
          ) weekend_cnt,
        sum(
            case when to_char(submit_date,'DY') not in ('SAT', 'SUN')
                then 1
                else 0
            end
          ) working_cnt
    from tasks;