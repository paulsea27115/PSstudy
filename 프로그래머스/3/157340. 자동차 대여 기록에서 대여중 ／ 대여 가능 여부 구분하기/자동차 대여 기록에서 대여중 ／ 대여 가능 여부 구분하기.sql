select distinct c.car_id, if(f.end_date_final is null , "대여 가능", "대여중") as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c
left outer join  (
    select car_id, max(date_format(end_date, "%Y-%m-%d")) as end_date_final
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(start_date, "%Y-%m-%d") <= '2022-10-16'
    group by car_id
    having end_date_final >= '2022-10-16'
) f on c.car_id = f.car_id
order by c.car_id desc