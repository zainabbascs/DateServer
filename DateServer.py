
class DateServer :
    def main(self, args) :
        try :
            sock =  java.net.ServerSocket(6013)
            # now listen for connections
            while (True) :
                client = sock.accept()
                pout =  java.io.PrintWriter(client.getOutputStream(), True)
                # write the Date to the socket 
                pout.println( java.util.Date().toString())
                # close the socket and resume 
                # listening for connections 
                client.close()
        except java.lang.Exception as ioe :
            print(ioe)


if __name__=="__main__":
    DateServer().main([])