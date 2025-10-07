param([string]$Summary)
$ts=Get-Date -Format o
Write-Host "[JIRA] Would create ticket: $Summary at $ts"
