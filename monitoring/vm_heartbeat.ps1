param([string[]]$Hosts=@('127.0.0.1','8.8.8.8'))
foreach($h in $Hosts){$ok=Test-Connection -ComputerName $h -Count 1 -Quiet; "$h " + ($ok?'up':'down')}
