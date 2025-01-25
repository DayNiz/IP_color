# IP_color
See your internet in color!
---
The programm work as following:
Your IPv4 address (ex: 192.168.1.32) is stored in 4 octets, right?
But what can also be represented by four octets? 
Yeah, colors! (alpha, red, green, blue)...
So it simply does the following:
  - Check your IP address (both locale and public)
  - Take each octet and turn it into its hexadecimal reppresentation (ex: 0xc0.0xa8.0x01.0x20)
  - Display the corresponding color (first octet isn't used, was planned for transparency)
  - Check every second if the address changed (eg internet lost)

---
I did my best to handle most usecases, but if any bugs are found, please feel a bug request or a pull request and I'll do my best :)
