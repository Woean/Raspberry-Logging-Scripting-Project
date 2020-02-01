#!/usr/bin/expect -f

spawn ssh pi@10.0.0.16
expect "?assword:"
send "Scripting\r"
expect "pi@raspberrypi:~ $ "
send "python3 plotgraph.py\r"
expect "pi@raspberrypi:~ $ "
send "exit\r"
interact
spawn scp pi@raspberrypi:temp-plot.html .
expect "?assword:"
send "Scripting\r"
interact
spawn open temp-plot.html
interact
