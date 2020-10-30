#level3 

SELECT O.animal_id, O.animal_type, O.name from ANIMAL_OUTS O, ANIMAL_INS I where I.animal_id = O.animal_id 
and I.sex_upon_intake != O.sex_upon_outcome
order by I.animal_id

