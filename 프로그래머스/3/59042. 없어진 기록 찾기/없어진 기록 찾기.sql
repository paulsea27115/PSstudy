select a_o.animal_id, a_o.name
from ANIMAL_INS a_i
right outer join ANIMAL_OUTS a_o on a_o.animal_id = a_i.animal_id
where a_i.animal_id is null