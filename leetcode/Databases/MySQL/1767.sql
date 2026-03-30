#https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/description/

# Write your MySQL query statement below
with recursive cte_gen as
(
    select task_id, 1 subtask_id, subtasks_count
        from tasks
        union all
    select task_id, 1 + subtask_id, subtasks_count
        from cte_gen
        where subtask_id < subtasks_count
)
select a.task_id, a.subtask_id
    from cte_gen a
    left join
         executed b
    on (a.task_id = b.task_id and a.subtask_id = b.subtask_id)
    where b.subtask_id is null
