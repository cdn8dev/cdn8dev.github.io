$Interface = Get-NetAdapter | Where-Object { $_.Status -eq "Up" }
Set-DnsClientServerAddress -InterfaceIndex $Interface.ifIndex -ServerAddresses ("192.168.178.88", "1.1.1.1")
echo DNS Sucessfully set!