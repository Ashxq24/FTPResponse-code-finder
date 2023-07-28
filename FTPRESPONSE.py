import FTPSERVERRETURNCODES
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

description1=str(input("Enter the description you want to find FTP response code for : "))
choices = ["Restart marker replay","Service ready in nnn minutes","Data connection already open; transfer starting","File status okay; about to open data connection","Command not implemented, superfluous at this site","System status, or system help reply","Directory status","File status","Help message","NAME system type. Where NAME is an official system name from the registry kept by IANA", "Service ready for new user","Service closing control connection","Data connection open; no transfer in progress",
"Closing data connection. Requested file action successful",
"Entering Passive Mode",
"Entering Long Passive Mode",
"Entering Extended Passive Mode",
"User logged in, proceed. Logged out if appropriate",
"User logged out; service terminated",
"Logout command noted, will complete when transfer done",
"Specifies that the server accepts the authentication mechanism specified by the client, and the exchange of security data is complete. A higher level nonstandard code created by Microsoft",
"Requested file action okay, completed",
"PATHNAME created",
"User name okay, need password",
"Need account for login",
"Requested file action pending further information",
"Service not available, closing control connection. This may be a reply to any command if the service knows it must shut down",
"Can't open data connection",
"Connection closed; transfer aborted",
"Invalid username or password",
"Requested host unavailable",
"Requested file action not taken",
"Requested action aborted. Local error in processing",
"Requested action not taken. Insufficient storage space in system.File unavailable",
"Syntax error in parameters or arguments",
"Command not implemented",
"Bad sequence of commands",
"Command not implemented for that parameter",
"Not logged in",
"Need account for storing files",
"Could Not Connect to Server - Policy Requires SSL",
"Requested action not taken. File unavailable",
"Requested action aborted. Page type unknown",
"Requested file action aborted. Exceeded storage allocation",
"Requested action not taken. File name not allowed",
"Integrity protected reply",
"Confidentiality and integrity protected reply",
"Confidentiality protected reply",
"Connection reset by peer. The connection was forcibly closed by the remote host",
"Cannot connect to remote server",
"Cannot connect to remote server. The connection is actively refused by the server",
"Directory not empty",
"Too many users, server is full"]
print("Choose the correct description to find its FTP response code from below ")
print (process.extract(description1, choices))

description2=input("enter the correct description of the method you want to use (CASE SENSITIVE) : ")
if description2 in FTPSERVERRETURNCODES.codes:
      print ("FTP RESPONSE CODE :  ", FTPSERVERRETURNCODES.codes[description2])
else:
      print("description incorrect! NOTE:the correct description method you want to use is CASE SENSITIVE")


   
