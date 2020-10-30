#level2

select name, COUNT(name) as COUNT from ANIMAL_INS where name is not null group by name having COUNT(name) > 1 order by name
