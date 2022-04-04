$TaskName = 'reverse'
$User = 'domain\user'
$ScriptPath = "reverse.ps1"
$Trigger = New-ScheduledTaskTrigger -At 11:30 -Daily 
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-executionpolicy bypass -noprofile -file $ScriptPath"
Register-ScheduledTask -TaskName $TaskName -Trigger $Trigger -User $User -Action $Action -RunLevel Highest -Force
