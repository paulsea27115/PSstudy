select p.member_name, r.review_text, date_format(r.review_date, "%Y-%m-%d") as review_date
from (
    select r.member_id, r.review_text, r.review_date
    from rest_review r
    inner join (
        select member_id
        from rest_review r
        group by member_id
        order by count(member_id) desc
        limit 1
    ) f using(member_id)
    where f.member_id is not null
) r inner join member_profile p using(member_id)
order by r.review_date asc, r.review_text asc