class DBConnection:
    hostname = 'ec2-34-206-124-133.compute-1.amazonaws.com'
    databasename =  'db5g29u2cel02j'
    username =  'u61gjpmvjt5prl'
    passwordname =  'p6a67b3b89c0babe7005c17bd8e2af98551fcbdde9aae7f26fd80d45ad0d73024'

    def creden(self):
        return self.hostname, self.databasename, self.username, self.passwordname
# p = DBConnection()
# tpl = list(p.creden())
# print(tpl[1])