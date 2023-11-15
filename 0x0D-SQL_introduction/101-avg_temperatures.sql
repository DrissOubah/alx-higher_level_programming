-- AVERAGE temeprature by city you find THE city in line 26 and balue line 30
SELECT city ,AVG('value') AS avg_temp FROM temperature GROUP BY 'city' ORDER BY avg_temp DESC;
