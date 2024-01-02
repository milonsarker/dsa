#https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/description/

#Very Difficult one


Create table If Not Exists CoffeeShop (id int, drink varchar(20))
Truncate table CoffeeShop
insert into CoffeeShop (id, drink) values ('9', 'Mezcal Margarita')
insert into CoffeeShop (id, drink) values ('6', 'None')
insert into CoffeeShop (id, drink) values ('7', 'None')
insert into CoffeeShop (id, drink) values ('3', 'Americano')
insert into CoffeeShop (id, drink) values ('1', 'Daiquiri')
insert into CoffeeShop (id, drink) values ('2', 'None')


# Write your MySQL query statement below
with cte_grp as
(
    select *, sum(if(drink is not null, 1, 0)) over win as grp
        from coffeeshop
        window win as
        (
            rows between unbounded preceding and current row
        )
)
select  id, first_value(drink) over(PARTITION by grp) AS drink
    from cte_grp;