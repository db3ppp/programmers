#level3

SELECT O.animal_id, O.name from ANIMAL_OUTS O, ANIMAL_INS I
where I.animal_id = O.animal_id
order by O.datetime - I.datetime desc
limit 2
