#level2

select animal_type, COUNT(animal_type) as count from ANIMAL_INS group by animal_type order by animal_type
