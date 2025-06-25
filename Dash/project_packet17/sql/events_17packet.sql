WITH events AS (
SELECT  
        edrpou,     
		report_month,
		COUNT(DISTINCT patient_id) FILTER (WHERE age_years < 18) AS count_before_18,
		COUNT(DISTINCT patient_id) FILTER (WHERE age_years >= 18 AND class = 'AMB') AS count_amb,
		COUNT(DISTINCT patient_id) FILTER (WHERE age_years >= 18 AND class = 'INPATIENT') AS count_inpat
 FROM 
	   analytics.rds_pmg_events_2025 AS e
	   INNER JOIN analytics.rds_pmg_events_checks_2025 AS eh USING(id)
 WHERE 
	   eh.is_correct
   AND eh.packet_number = '17'
 GROUP BY edrpou, report_month)

SELECT residence_area,
       e.edrpou,
       kwd_name,	
	   lat,
	   lng,
	   report_month, count_before_18, count_amb, count_inpat 
  FROM events e
 	   LEFT JOIN analytics.dwh_legal_entities_edrpou_view AS v ON e.edrpou = v.edrpou 	
                 AND v.is_active