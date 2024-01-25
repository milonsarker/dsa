--https://leetcode.com/problems/find-cutoff-score-for-each-school/

/* Write your PL/SQL query statement below */
select school_id ,
       nvl((select min(score)
            from exam
            where student_count <= capacity), -1) score
    from schools