class TargetHost:
    """Collected info on target"""
    hostname = "Unknown"
    os = "Unknown"
    open_ports = []

    def info(self):
        print("Hostname: {verdi}".format(verdi=self.hostname))
        print("OS:", self.os)
        print("Open ports: %s" % ", ".join(self.open_ports))
