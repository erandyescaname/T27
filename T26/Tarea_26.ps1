# Obtener información de los servicios y transformarlo a CSV
Get-Service | Select-Object DisplayName, Status, ServiceType | ConvertTo-Csv -NoTypeInformation
