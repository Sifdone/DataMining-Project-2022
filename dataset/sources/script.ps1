Get-Childitem 'D:\Documents\UNIVERSITY\project_mining_2022\DataMining-Project-2022\dataset\sources\*.csv' -Recurse | ForEach {
	(Get-Content $_ | ForEach { $_ -replace 'Large hydro', 'Large Hydro'}) |
	Set-Content $_
}