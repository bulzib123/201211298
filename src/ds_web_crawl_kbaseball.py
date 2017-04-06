# coding: utf-8
import requests
import lxml.etree

def getkb():
    r = requests.get('http://www.kbreport.com/main')
    _htmlTree = lxml.etree.HTML(r.text)
    nodes = _htmlTree.xpath("//div[@class='main-stats-box']//div[@class='ms-1']//tr")
    print "table cooooooools: ", len(nodes)
    counter=0
    for teams in nodes:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            else:
                print cols.text.strip(),
        print
        
    print "---"
    nodes2 = _htmlTree.xpath("//div[@class='main-stats-box']//div[@class='ms-2']//tr")
    print "table cooooooools: ", len(nodes2)
    counter=0
    for teams in nodes2:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            else:
                print cols.text.strip(),
        print

def main():
    getkb()

if __name__ == "__main__":
    main()