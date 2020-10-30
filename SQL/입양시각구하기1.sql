#level2

select hour(datetime) as HOUR, COUNT(*) as COUNT from ANIMAL_OUTS group by hour having hour >= 9 and hour < 20 order by hour
