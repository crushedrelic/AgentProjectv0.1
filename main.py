# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from MasterHttpServer import MasterHttpServer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hostIP = "192.168.1.19"
    port = 8080
    https = False
    httpserver = MasterHttpServer(hostIP, port, https)
    httpserver.executeServer()




