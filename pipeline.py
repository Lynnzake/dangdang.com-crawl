
class Dangdang25Pipeline(object):
    def process_item(self, grocery, spider):
        for i in range(0,len(grocery["titl"])):
            titl= grocery["titl"]
            link=grocery["link"]
            comment=grocery["comment"]
            print(titl)
            print(link)
            print(comment)
        return grocery
        #when i chose to "yield grocery",the terminator display <generator object Dangdang25Pipeline.process_item at 0x000002B28A3E89C8>
        #so there dose exit some differences betwenn "return" and "yield" in python 
