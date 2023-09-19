Write-Output "TIME INFO:"
Get-Date
Write-Output "SYSTEM INFORMATION"
systeminfo
Write-Output "CPU INFORMATION"
Get-WmiObject Win32_Processor
Write-Output "DRIVE INFORMATION"
Get-PSDrive *
Write-Output "COMPUTER FQDN/HOSTNAME"
[System.Net.Dns]::GetHostByName($env:computerName)
Write-Output "INTERFACE INFORMATION"
ipconfig /all
Get-NetAdapter | Format-List -Property PromiscuousMode
Write-Output "CURRENT CONNECTIONS"
Get-NetTCPConnection
Write-Output "LOGGED IN USERS"
query user /server:$SERVER
Write-Output "ALL USERS"
Get-LocalUser
Write-Output "ADMINISTRATORS"
Get-LocalGroupMember -Group "Administrators"
Write-Output "RUNNING PROCESSES"
Get-Process
Write-Output "FILES MODIFIED WITHIN 24 HOURS"
Get-ChildItem -Path C:\Users\asdf\ -Recurse | Foreach {
$lastupdatetime=$_.LastWriteTime
$nowtime = get-date
if (($nowtime - $lastupdatetime).totalhours -le 24)
{
Write-Host "Folder/File modified in the last 24 hours: "$_.Name
}
else
{
}
}
Write-Output "SCHEDULED TASKS"
Get-ScheduledTask
Write-Output "POWERSHELL HISTORY"
Get-History
Write-Output "POWERSHELL VERSION"
$PSVersionTable.PSVersion
