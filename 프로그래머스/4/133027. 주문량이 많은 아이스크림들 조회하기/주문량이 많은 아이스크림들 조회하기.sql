select f.flavor
from first_half f
right outer join (
    select shipment_id, flavor, sum(total_order) as total_order
    from july
    group by flavor
) j on f.shipment_id = j.shipment_id
order by f.total_order + j.total_order desc
limit 3