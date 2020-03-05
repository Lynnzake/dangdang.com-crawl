# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Dangdang25Pipeline(object):
    def process_item(self, grocery, spider):
        conn=pymysql.connect(host="localhost",user="root",passwd="qwezxc8520963?",db="dangdang",charset="utf8")
        cur=conn.cursor()#return the cursor of the database
        for i in range(0,len(grocery["titl"])):
            titl= grocery["titl"][i]
            link=grocery["link"][i]
            comment=grocery["comment"][i]
            sql="insert into books(title,link,comments) values (%s,%s,%s)"#to insert values got by the crawler
            values=(titl,link,comment)#pass the data
            cur.execute(sql,values)#execute insertion
            conn.commit()#commit the order
            #Tips:once you change the tables'content,you commit()
        '''the former statements went like this:
            sql="insert into books(title,link,comments) values ('"+titl+"',"+titl+"',"+titl+"')"
            conn.query(sql)
            without the cursor,but the program didn't return error msg.if anyone knows it,plese help me corect it.thanks.
        '''
        conn.close()
        return grocery
