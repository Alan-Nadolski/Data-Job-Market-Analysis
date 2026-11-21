select
    country as Country,
    cast(postalCode as integer) as Postal_Code,
    postalDistrictName as District_Name,
    hiringOrgName as Company,
    occupation as Occupation,
    workHourPartTime as Part_Time,
    jobAdId as Job_ID,
    workPlaceAddress as Address,
    cvr as CVR,
    title as Title,
    description as Description,
    cast(left(applicationDeadline, 10) as date) as Deadline,
    cast(left(publicationDate, 10) as date) as Publication_Date,
    municipality as Municipality
from {{ source('external_source', 'ads') }}