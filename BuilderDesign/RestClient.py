# Builder design pattern is used to create a complex instance or object by using same construction process
# Builder design pattern is concrete Design Pattern used for validation check

# Product, Builder Interface, Concrete Builder, Director, Client

from abc import ABC, abstractmethod

class RestClient:
    def __init__(self, base_url, header, auth, timeout):
        self.base_url=base_url
        self.header=header
        self.auth=auth
        self.timeout=timeout

    def __repr__(self) -> str:
        return (f"RestClient(base_url={self.base_url}, header={self.header})")
    

class RestClientBuilder(ABC):
    def __init__(self):
        self.base_url=None
        self.header=None
        self.auth=None
        self.timeout=None

    def set_base_url(self, base_url):
        self.base_url=base_url
        return self

    def set_header(self, header):
        self.header=header
        return self
    
    def set_auth(self, auth):
        self.auth=auth
        return self
    
    def set_timeout(self, timeout):
        self.timeout=timeout
        return self


    def validate(self):
        if not self.timeout:
            raise ValueError("Timeout")
        if not self.header:
            raise ValueError("Header must be set")
        if not self.base_url:
            raise ValueError("Base URL should be set")
    @abstractmethod
    def build(self):
        pass

class ConcreteRestClientBuilder(RestClientBuilder):
    def build(self):
        self.validate()
        return RestClient(self.base_url,self.header,self.auth,self.timeout)

class Director:
    def __init__(self, builder:ConcreteRestClientBuilder):
        self.builder=builder

    def construct(self, base_url, auth, header, timeout):
        return self.builder.set_auth(auth).set_base_url(base_url).set_timeout(timeout).set_header(header).build()

if __name__=="__main__":
    builder=ConcreteRestClientBuilder()
    director=Director(builder)
    client=director.construct("https.hello",("username","password"),"Content-Type:Application-json",30)
    print(client)