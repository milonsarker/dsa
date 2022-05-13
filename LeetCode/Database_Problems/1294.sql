/* Write your PL/SQL query statement below */
with avg_weather as
(
    select country_id , avg(weather_state) avg_weather_state
        from weather
        where to_char(day,'yyyymm') = '201911'
        group by country_id
)
select b.country_name,
        case
            when a.avg_weather_state <= 15 then 'Cold'
            when a.avg_weather_state >= 25 then 'Hot'
            else 'Warm'
        end weather_type
    from avg_weather a
    join
         countries b
    on (a.country_id = b.country_id)