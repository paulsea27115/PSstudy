select p.product_id, p.product_name, (o.amount * p.price) as total_sales
from (
    select product_id, sum(amount) as amount, date_format(produce_date,'%Y-%m-%d') as produce_date
    from food_order
    where produce_date like '2022-05%'
    group by product_id
) o inner join food_product p using(product_id)
order by total_sales desc, o.product_id asc

# select product_id, sum(amount) as amount, date_format(produce_date,'%Y-%m-%d') as produce_date
# from food_order
# where out_date is not null
# group by product_id
# having produce_date between '2022-05-01' and '2022-06-01'

# select *
# from food_order