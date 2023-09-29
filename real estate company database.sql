SELECT last_name FROM client
INNER JOIN view ON client.id = view.client_id
WHERE apartment_id IN (SELECT id FROM apartment WHERE rooms = 3)
GROUP BY view.client_id
HAVING COUNT(view.client_id) > 1;
