$headers = @{
    "Content-Type" = "application/json"
}

$body = @'
{
    "Store": [1],
    "DayOfWeek": [5],
    "Customers": [555],
    "Open": [1],
    "Promo": [1],
    "SchoolHoliday": [0]
}
'@

Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Headers $headers -Body $body
