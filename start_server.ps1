Set-Location "C:\Users\EYU\Documents\worktest\minilife"
$log = "$env:TEMP\server.log"
python -m http.server 8000 > $log 2>&1
